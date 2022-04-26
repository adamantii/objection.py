from functools import cache, lru_cache
from dataclasses import dataclass, field
import re
from warnings import warn
from typing import Optional
from requests import post, get
from json import JSONDecodeError
from . import enums, _utils


class Asset:
    id: int
    exists: bool = True
    _loaded: bool = False
    _reprKeys: tuple = ('id', 'name')

    def __init__(self, id):
        self.id = id

    def __getattribute__(self, __name: str):
        if __name != '_assetKeys' and __name in self._assetKeys + ('exists',) and not self._loaded:
            self._loaded = True
            assetExists, characterData = type(self)._requestData(self.id)
            self.exists = assetExists
            if assetExists:
                for key, value in characterData.items():
                    setattr(self, key, value)
        return object.__getattribute__(self, __name)

    def __repr__(self) -> str:
        if self.exists:
            return _utils._reprFunc(self, self._reprKeys)
        else:
            return _utils._reprFunc(self, ('id', 'exists'))

    @classmethod
    def _requestData(cls, *_) -> tuple[bool, dict]:
        raise NotImplementedError(
            "_requestData must be implemented by " + cls.__name__ + " subclasses")


class GetAsset(Asset):
    _getUrl: str
    _tag: str
    name: str
    url: str

    @classmethod
    @cache
    def _requestData(cls, id):
        request = get(
            url=cls._getUrl + str(id)
        )
        return True, request.json()

    def __init__(self, id):
        super().__init__(id)
        self.tag = '[#' + self._tag + str(self.id) + ']'

    def __str__(self) -> str:
        return self.tag


class PostAsset(Asset):
    _postUrl: str
    name: str

    @classmethod
    @cache
    def _requestData(cls, id):
        request = post(
            url=cls._postUrl,
            json={
                "ids": [id]
            }
        )
        try:
            json = request.json()
            return True, json[0]
        except (JSONDecodeError, IndexError):
            AssetWarning.warn(id)
            return False, None


class Sound(GetAsset):
    _getUrl = 'https://api.objection.lol/assets/sound/get?id='
    _assetKeys = ('name', 'url', 'volume', 'fileSize')
    _tag = 'bgs'


class Music(GetAsset):
    _getUrl = 'https://api.objection.lol/assets/music/get?id='
    _assetKeys = ('name', 'url', 'volume', 'fileSize')
    _tag = 'bgm'


class Popup(PostAsset):
    _postUrl = 'https://api.objection.lol/assets/popup/getpopups'
    _assetKeys = ('name', 'url', 'alignment', 'center', 'posY', 'resize')


class Background(PostAsset):
    _postUrl = 'https://api.objection.lol/assets/background/getbackgrounds'
    _assetKeys = ('name', 'url', 'deskUrl', 'isWide')


class Character(PostAsset):
    _postUrl = 'https://api.objection.lol/character/getcharacters'
    _assetKeys = ('alignment', 'backgroundId', 'blipUrl', 'bubbles', 'galleryAJImageUrl', 'galleryImageUrl',
                  'iconUrl', 'limitWidth', 'name', 'namePlate', 'offsetX', 'offsetY', 'poses', 'side')

    id: Optional[int] = None
    alignment: Optional[list] = None
    backgroundId: int = 0
    blipUrl: str = '/Audio/blip.wav'
    bubbles: list
    galleryAJImageUrl: Optional[str] = None
    galleryImageUrl: Optional[str] = None
    iconUrl: Optional[str] = None
    limitWidth: bool = False
    name: str = 'None'
    namePlate: str = ''
    offsetX: int = 0
    offsetY: int = 0
    poses: list
    side: enums.CharacterLocation = enums.CharacterLocation.WITNESS
    _aj: bool = False

    def __init__(self, id, loaded=False):
        self.bubbles = []
        self.poses = []
        super().__init__(id)
        if loaded:
            self._loaded = True
            self.exists = True

    @property
    def background(self):
        if not hasattr(self, '_background'):
            self._background = Background(self.backgroundId)
        return self._background

    @property
    def isPreset(self):
        return self.id is None or self.id < 1000

    @classmethod
    def _poseLookupKey(cls, name: str) -> str:
        name = re.sub('[^a-zA-Z0-9]', '', name)
        name = name.lower()
        return name

    @property
    @lru_cache(1)
    def _poseLookupKeys(self) -> list:
        return list(map(lambda pose: self._poseLookupKey(pose['name']), self.poses))

    def lookupPoseSubstr(self, lookupSubstr: str) -> int:
        keyToFind = self._poseLookupKey(lookupSubstr)

        bestI = -1
        bestLengthDifference = 0
        for i, key in enumerate(self._poseLookupKeys):
            if keyToFind not in key:
                continue
            lengthDifference = len(key) - len(keyToFind)
            if bestI == -1 or lengthDifference < bestLengthDifference:
                bestI = i
                bestLengthDifference = lengthDifference

        return self.poses[bestI]['id']

    def getPose(
        self,
        name: Optional[str] = None,
        idleImageUrl: Optional[str] = None,
        speakImageUrl: Optional[str] = None,
        iconUrl: Optional[str] = None,
    ) -> int:
        for pose in self.poses:
            for key in ('name', 'idleImageUrl', 'speakImageUrl', 'iconUrl'):
                if key is None:
                    continue
                if pose[key] != eval(key):
                    continue
                return pose['id']
        return -1


class Evidence(Asset):
    _getUrl = 'https://api.objection.lol/assets/evidence/get?id='
    _assetKeys = ('url',)
    _reprKeys = ('id', 'url')

    @classmethod
    @cache
    def _requestData(cls, id):
        request = get(
            url=cls._getUrl + str(id)
        )
        if len(request.text) > 0:
            return True, {'url': request.text}
        else:
            AssetWarning.warn(id)
            return False, None

    def __init__(self, id):
        super().__init__(id)
        self.tag = '[#evd' + str(self.id) + ']'
        self.icon = '[#evdi' + str(self.id) + ']'


class AssetBank:
    characters: dict[str, Character]
    backgrounds: dict[str, Background]
    music: dict[str, Music]
    sounds: dict[str, Sound]
    popups: dict[str, Popup]
    evidence: dict[str, Evidence]

    def __init__(self, assetDict: dict[str, Asset] = {}) -> None:
        for key in self.__annotations__.keys():
            setattr(self, key, {})
        self.loadAssets(assetDict)

    def loadAssets(self, assetDict: dict[str, Asset]):
        for name, asset in assetDict.items():
            if type(asset) is Character:
                self.characters[name] = asset
            elif type(asset) is Background:
                self.backgrounds[name] = asset
            elif type(asset) is Music:
                self.music[name] = asset
            elif type(asset) is Sound:
                self.sounds[name] = asset
            elif type(asset) is Popup:
                self.popups[name] = asset
            elif type(asset) is Evidence:
                self.evidence[name] = asset
            else:
                raise TypeError('Unknown asset type ' + type(asset).__name__)

    def loadAssetIDs(self, assetType: type, ids: dict[str, int]):
        if assetType is Character:
            targetDict = self.characters
        elif assetType is Background:
            targetDict = self.backgrounds
        elif assetType is Music:
            targetDict = self.music
        elif assetType is Sound:
            targetDict = self.sounds
        elif assetType is Popup:
            targetDict = self.popups
        elif assetType is Evidence:
            targetDict = self.evidence
        else:
            raise TypeError('Unknown asset type ' + assetType.__name__)

        for name, id in ids.items():
            targetDict[name] = assetType(id)


class AssetWarning(Warning):
    @classmethod
    def warn(cls, id):
        warn('asset ' + str(id) + ' not found', AssetWarning)
