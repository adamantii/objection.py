from dataclasses import dataclass, field
from functools import _lru_cache_wrapper, cache
from json import dumps
from base64 import b64encode
from typing import Optional, Sized
from unicodedata import name
from warnings import warn
from objectionpy import enums, assets, frames, _utils


PACKAGE_VERSION = 'v0.0'
LATEST_OBJECTION_VERSION = 4

Frame = frames.Frame


@dataclass
class Group:
    name: str
    type: enums.GroupType
    tag: str = ''
    frames: list[Frame] = field(default_factory=list)
    _ceCounselFrames: list[Frame] = field(default_factory=list, init=False)
    _ceFailureFrames: list[Frame] = field(default_factory=list, init=False)

    def _exceptIfNotCEType(self):
        if self.type is not enums.GroupType.CROSS_EXAMINATION:
            raise TypeError(
                'counsel and failure frame sequences are only available in cross-examination groups')

    @property
    def ceCounselFrames(self):
        self._exceptIfNotCEType()
        return self._ceCounselFrames

    @ceCounselFrames.setter
    def ceCounselFrames(self, value):
        self._exceptIfNotCEType()
        self._ceCounselFrames = value

    @property
    def ceFailureFrames(self):
        self._exceptIfNotCEType()
        return self._ceFailureFrames

    @ceFailureFrames.setter
    def ceFailureFrames(self, value):
        self._exceptIfNotCEType()
        self._ceFailureFrames = value


class _ObjectionBase:
    type: enums.ObjectionType

    @dataclass
    class Options:
        dialogueBox: enums.PresetDialogueBox = enums.PresetDialogueBox.CLASSIC
        defaultTextSpeed: int = 28
        blipFrequency: int = 56
        autoplaySpeed: int = 500
        continueSoundUrl: str = "/Audio/Case/Continue_Trilogy.wav"

        MAX_PAIRS = 100
        MAX_GROUPS = 100
        MAX_ALIASES = 100
        MAX_GROUP_FRAMES = 1000
        MAX_FRAME_ACTIONS = 10
        MAX_EVIDENCE = 50
        MAX_PROFILES = 50
    options: Options

    aliases: dict[str, str]
    _groups: list[Group]
    _nextFrameIID: int

    def __init__(self, options: Optional[Options] = None) -> None:
        self.options = options if options is not None else self.Options()
        self.aliases = {}
        self._groups = []

    @classmethod
    def _verifyFrameChar(cls, char: Optional[frames.FrameCharacter]) -> frames.FrameCharacter:
        return char if char is not None else frames.noneCharacter

    def _compileFrame(self, frame: Frame, requestPair: _lru_cache_wrapper, frameList: list[Frame], frameTags: dict, groupTags: dict):
        chars = (
            self._verifyFrameChar(frame.char),
            self._verifyFrameChar(frame.pairChar),
        )
        activeIndex = _utils._maxIndex(
            [*map(lambda char: char._getIndividualValue(char.isActive), chars)])
        activeChar = chars[activeIndex]
        secondaryChar = chars[1 - activeIndex]
        frontChar = chars[_utils._maxIndex(
            [*map(lambda char: char._getIndividualValue(char.isFront) if not char.isNone else -2, chars)])]

        flip = (
            ('1' if frame.backgroundFlip else '0') +
            ('1' if activeChar.flip else '0') +
            ('1' if secondaryChar.flip else '0')
        )
        frameObject = {
            "id": -1,
            "iid": self._nextFrameIID,
            "text": frame.text,
            "characterId": activeChar.character.id if not activeChar.character.isPreset else None,
            "poseId": activeChar.poseId,
            "pairPoseId": secondaryChar.poseId,
            "bubbleType": frame.bubble if frame.bubble is not None else 0,
            "username": frame.customName if frame.customName is not None else "",
            "mergeNext": frame.properties.merge,
            "doNotTalk": not frame.properties.talk,
            "goNext": frame.properties.moveNext,
            "poseAnimation": frame.properties.poseAnim,
            "flipped": flip,
            "popupId": frame.popup if frame.popup is not None else None,
            "backgroundId": frame.background.id if frame.background is not None else activeChar.character.backgroundId,
            "transition": {},
            "filter": {},
            "frameFades": [],
            "frameActions": [],
            "caseAction": {},
            "pairId": None,
        }
        frameTags[frame.tag] = frameObject
        self._nextFrameIID += 1

        if frame.transition:
            frameObject['transition']['duration'] = frame.transition.duration
            frameObject['transition']['easing'] = frame.transition.easing.value
            frameObject['transition']['left'] = 0
        if frame.wideLeft is not None:
            frameObject['transition']['left'] = int(frame.wideLeft * 100)

        if frame.filter:
            frameObject['filter'] = {
                "id": 0,
                "type": frame.filter.type.value,
                "target": frame.filter.target.value,
                "amount": frame.filter.amount,
            }

        if frame.fade:
            frameObject['frameFades'].append({
                "id": 0,
                "fade": frame.fade.direction.value,
                "target": frame.fade.target.value,
                "easing": frame.fade.easing.value,
                "color": frame.fade.color,
                "duration": frame.fade.duration,
            })

        if frame.properties.offScreen:
            frameObject['frameActions'].append({
                'actionId': 6,
            })
        if frame.properties.centerText:
            frameObject['frameActions'].append({
                'actionId': 9,
            })

        presetPopup = frame.properties.presetPopup
        if presetPopup is not None:
            if presetPopup.value > 0:
                frameObject['frameActions'].append({
                    'actionId': 7,
                    'actionParam': str(presetPopup.value),
                })
            elif presetPopup == enums.PresetPopup.TESTIMONY_LABEL_HIDE:
                frameObject['frameActions'].append({
                    'actionId': 8,
                    'actionParam': '1',
                })

        presetBlip = frame.properties.presetBlip
        if presetBlip is not None:
            if presetBlip.value > 0:
                frameObject['frameActions'].append({
                    'actionId': 4,
                    'actionParam': str(presetBlip.value),
                })
            elif presetBlip == enums.PresetBlip.MUTE:
                frameObject['frameActions'].append({
                    'actionId': 5,
                })

        if frame.options.autoplaySpeed is not None:
            frameObject['frameActions'].append({
                'actionId': 15,
                'actionParam': str(frame.options.autoplaySpeed),
            })
        if frame.options.dialogueBox is not None:
            frameObject['frameActions'].append({
                'actionId': 12,
                'actionParam': str(frame.options.dialogueBox.value),
            })
        if frame.options.dialogueBoxVisible is not None:
            frameObject['frameActions'].append({
                'actionId': 1,
                'actionParam': str(int(frame.options.dialogueBoxVisible)),
            })
        if frame.options.defaultTextSpeed is not None:
            frameObject['frameActions'].append({
                'actionId': 13,
                'actionParam': str(frame.options.defaultTextSpeed),
            })
        if frame.options.blipFrequency is not None:
            frameObject['frameActions'].append({
                'actionId': 14,
                'actionParam': str(frame.options.blipFrequency),
            })
        if frame.options.frameSkip is not None:
            frameObject['frameActions'].append({
                'actionId': 16,
                'actionParam': str(int(frame.options.frameSkip)),
            })
        if frame.options.galleryRemove is not None:
            # TODO make it choose dynamically between action 3 (PW) and 11 (AJ) galleries
            for location in frame.options.galleryRemove:
                frameObject['frameActions'].append({
                    'actionId': 3,
                    'actionParam': location.value,
                })
                frameObject['frameActions'].append({
                    'actionId': 11,
                    'actionParam': location.value,
                })
        galleryModifier = frame.options.galleryAssign
        if galleryModifier is not None:
            for character in galleryModifier.__dict__.values():
                if character is None:
                    continue
                if character.isPreset:
                    actionId = 2 if not character._aj else 10
                    frameObject['frameActions'].append({
                        'actionId': actionId,
                        'actionParam': str(character.id),
                    })
                else:
                    pass  # TODO make it create new frames before current frame to set custom characters gallery sprites

        if not secondaryChar.isNone or activeChar.pairOffset != (0, 0):
            pairNeeded = True
        else:
            pairNeeded = False
        if pairNeeded:
            pairChars = [activeChar, secondaryChar]
            pairChars.sort(
                key=lambda char: char.character.id if char.character.id is not None else 0, reverse=True)
            pair = requestPair(pairChars[0].character.id, pairChars[1].character.id, pairChars[0].pairOffset,
                               pairChars[1].pairOffset, True if chars[0] is frontChar else False)
            frameObject['pairId'] = pair['pairId']

        if frame.onCompile is not None:
            frameObject = frame.onCompile(frameObject)

        LimitWarning.checkList(frameObject['frameActions'], self.options.MAX_FRAME_ACTIONS,
                               'frame actions (frame iid=' + str(frameObject['iid']) + ')')

        return frameObject

    def compile(self) -> dict:
        objectionObject = {
            'credit': 'made with objection.py ' + PACKAGE_VERSION,
            'version': LATEST_OBJECTION_VERSION,
            'pairs': [],
            'groups': [],
            'courtRecord': {
                'evidence': [],
                'profiles': [],
            },
            'aliases': [],
            'options': {},
            'type': 'scene' if self.type == enums.ObjectionType.SCENE else 'case' if self.type == enums.ObjectionType.CASE else 'unknown',
        }

        objectionObject['options']['chatbox'] = self.options.dialogueBox.value
        objectionObject['options']['textSpeed'] = self.options.defaultTextSpeed
        objectionObject['options']['textBlipFrequency'] = self.options.blipFrequency
        objectionObject['options']['autoplaySpeed'] = self.options.autoplaySpeed
        objectionObject['options']['continueSoundUrl'] = self.options.continueSoundUrl

        for i, alias in self.aliases.items():
            objectionObject['aliases'].append({
                "id": i,
                "from": alias[0],
                "to": alias[1],
            })
        LimitWarning.checkList(
            objectionObject['aliases'], self.options.MAX_ALIASES, 'aliases')

        nextPairID = 1

        @cache
        def requestPair(cid1: int, cid2: int, offset1: tuple[int, int], offset2: tuple[int, int], front: bool):
            nonlocal nextPairID
            pair = {
                'id': 0,
                'pairId': nextPairID,
                'name': 'Generated ' + str(nextPairID),
                'characterId': cid1,
                'characterId2': cid2,
                'offsetX': offset1[0],
                'offsetY': offset1[1],
                'offsetX2': offset2[0],
                'offsetY2': offset2[1],
                'front': front,
            }
            objectionObject['pairs'].append(pair)
            nextPairID += 1
            return pair

        self._nextFrameIID = 1
        groupMap = []
        frameMap = []
        groupTags = {}
        frameTags = {}
        for i, group in enumerate(self._groups):
            groupObject = {
                "iid": i + 1,
                "name": group.name,
                "type": group.type.value,
                "frames": [],
            }

            groupTags[group.tag] = groupObject

            for frame in group.frames:
                frameObject = self._compileFrame(
                    frame, requestPair=requestPair, frameList=groupObject['frames'], frameTags=frameTags, groupTags=groupTags)
                frameMap.append((frame, frameObject))
                groupObject['frames'].append(frameObject)

            groupMap.append((group, groupObject))
            objectionObject['groups'].append(groupObject)
            LimitWarning.checkList(groupObject['frames'], self.options.MAX_GROUP_FRAMES,
                                   'frames in a group (group iid=' + str(groupObject['iid']) + ')')
        LimitWarning.checkList(
            objectionObject['groups'], self.options.MAX_GROUPS, 'groups')
        LimitWarning.checkList(
            objectionObject['pairs'], self.options.MAX_PAIRS, 'pairs')

        return objectionObject

    @classmethod
    def makeObjectionFile(cls, objectionObject: dict) -> str:
        return str(b64encode(bytes(dumps(objectionObject), encoding='utf-8')))


class Scene(_ObjectionBase):
    type = enums.ObjectionType.SCENE

    def __init__(self, options: Optional[_ObjectionBase.Options] = None) -> None:
        super().__init__(options)
        mainGroup = Group(
            'Main',
            enums.GroupType.NORMAL,
        )
        self._groups.append(mainGroup)

    @property
    def frames(self) -> list[Frame]:
        return self._groups[0].frames


class Case(_ObjectionBase):
    type = enums.ObjectionType.CASE

    @dataclass
    class RecordItem:
        name: str
        iconUrl: str
        checkUrl: str = ''
        description: str = ''
        hidden: bool = False
    evidence: list[RecordItem]
    profiles: list[RecordItem]

    def __init__(self, options: Optional[_ObjectionBase.Options] = None) -> None:
        super().__init__(options)
        self.evidence = []
        self.profiles = []

    @property
    def groups(self) -> list[Group]:
        return self._groups

    def compile(self):
        objectionObject = super().compile()

        for items, recordName in (self.evidence, 'evidence'), (self.profiles, 'profiles'):
            for i, item in enumerate(items):
                targetRecord = objectionObject['courtRecord'][recordName]
                targetRecord.append({
                    "iid": i + 1,
                    "name": item.name,
                    "iconUrl": item.iconUrl,
                    "url": item.checkUrl,
                    "description": item.description,
                    "hide": item.hidden,
                })
        LimitWarning.checkList(
            objectionObject['courtRecord']['evidence'], self.options.MAX_EVIDENCE, 'evidence')
        LimitWarning.checkList(
            objectionObject['courtRecord']['profiles'], self.options.MAX_PROFILES, 'profiles')

        return objectionObject


class LimitWarning(Warning):
    @classmethod
    def warn(cls, limit: int, limitTarget: str):
        warn(
            f'exceeded limit of {limit} {limitTarget} - objection.lol support is not guaranteed', LimitWarning)

    @classmethod
    def checkList(cls, lst: Sized, limit: Optional[int], limitTarget: str):
        if limit is not None and len(lst) > limit:
            cls.warn(limit, limitTarget)
