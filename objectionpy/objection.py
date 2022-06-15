"""Main module containing everything related to objection exporting, importing, and structure (except for frame-related components)."""

from copy import deepcopy
from dataclasses import dataclass, field
from functools import cache
from json import loads, dumps
from base64 import b64decode, b64encode
from warnings import warn
from typing import Any, Optional, Sized, Union, TypeVar, TYPE_CHECKING
from . import enums, _utils, frames, assets, preset
from ._version import __version__
if TYPE_CHECKING:
    from enum import EnumMeta
    EnumT = TypeVar('EnumT')


LATEST_OBJECTION_VERSION = 4

Frame = frames.Frame


@dataclass
class Group:
    """
    Container for frames used in Cases.

    Attributes:
        - `objection : Optional[_ObjectionBase]`
            - The case to automatically append to on the group's initialization.
        - `name : str`
            - Group name.
        - `caseTag : str`
            - A unique tag used to identify the group in case actions. (A direct reference to the group object works too)
        - `frames : list[Frame]`
            - The group's frame list. May be of type Frame or CEFrame.
    """
    _type: enums.GroupType = field(default=enums.GroupType.NORMAL, init=False)
    objection: Optional['_ObjectionBase'] = None
    name: Optional[str] = None
    caseTag: Optional[str] = None
    frames: list[Frame] = field(default_factory=list)

    def __post_init__(self):
        try:
            self.objection.groups.append(self) # type: ignore
        except AttributeError:
            pass

@dataclass
class CEGroup(Group):
    """
    Special container for cross-examination sequences.

    Can contain both Frame and CEFrame.

    Attributes:
        - `objection : Optional[_ObjectionBase]`
            - The case to automatically append to on the group's initialization.
        - `name : str`
            - Group name.
        - `caseTag : str`
            - A unique tag used to identify the group in case actions. (A direct reference to the group object works too)
        - `frames : list[Frame]`
            - The group's frame list. May be of type Frame or CEFrame.
        - `counselSequence : list[Frame]`
            - A sequence of frames played after the last statement of the cross-examination, before looping back to the first.
        - `failureSequence : list[Frame]`
            - A sequence of frames played when failing to present a correct contradiction.
    """
    _type: enums.GroupType = field(
        default=enums.GroupType.CE, init=False)
    counselSequence: list[Frame] = field(default_factory=list, init=False)
    failureSequence: list[Frame] = field(default_factory=list, init=False)

class GameOverGroup(Group):
    """
    Special container whose frames are played when the player's health reaches 0.

    Attributes:
        - `objection : Optional[_ObjectionBase]`
            - The case to automatically append to on the group's initialization.
        - `name : str`
            - Group name.
        - `caseTag : str`
            - A unique tag used to identify the group in case actions. (A direct reference to the group object works too)
        - `frames : list[Frame]`
            - The group's frame list. May be of type Frame or CEFrame.
    """
    _type = enums.GroupType.GAME_OVER


@dataclass
class Options:
    """
    The default options of an objection.
    
    Most can be modified with OptionModifiers in Frames.
    """
    dialogueBox: enums.PresetDialogueBox = enums.PresetDialogueBox.CLASSIC
    defaultTextSpeed: int = 28
    blipFrequency: int = 56
    autoplaySpeed: int = 500
    continueSoundUrl: str = "/Audio/Case/Continue_Trilogy.wav"

    MAX_PAIRS: int = 100
    MAX_GROUPS: int = 100
    MAX_ALIASES: int = 100
    MAX_GROUP_FRAMES: int = 1000
    MAX_FRAME_ACTIONS: int = 10
    MAX_EVIDENCE: int = 50
    MAX_PROFILES: int = 50


class _ObjectionBase:
    """
    Base objection class.
    
    Should not be initialized. Use Scene or Case instead.

    Attributes:
        - `options : Options`
            - Default objection options.
        - `aliases : dict[str, str]`
            - Dictionary of aliases, mapping original name to alias.
    """
    _type: enums.ObjectionType

    options: Options

    aliases: dict[str, str]
    _groups: list[Group]
    _nextFrameIID: int

    def __init__(self, options: Optional[Options] = None) -> None:
        self.options = options if options is not None else Options()
        self.aliases = {}
        self._groups = []

    @classmethod
    def _verifyFrameChar(cls, char: Optional[frames.FrameCharacter]) -> frames.FrameCharacter:
        return char if char is not None else frames.noneCharacter

    def _compileFrame(self, frame: Frame, frameList: list[Frame]):
        try:
            _utils._tupleMapGet(self._frameMap, frame)
            frame = deepcopy(frame) # Makes a copy if map get didn't fail
        except KeyError:
            pass

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

        secondaryFlip = '1' if secondaryChar.flip else '0'
        activeFlip = '1' if activeChar.flip else '0'
        if frame.backgroundFlip is None:
            backgroundFlip = '0' if not secondaryChar.isNone else activeFlip
        else:
            backgroundFlip = '1' if frame.backgroundFlip else '0'
        flip = backgroundFlip + activeFlip + secondaryFlip

        frameDict = {
            "id": -1,
            "iid": self._nextFrameIID,
            "text": frame.text,
            "characterId": activeChar.character.id if not activeChar.character.isPreset else None,
            "poseId": activeChar.poseId,
            "pairPoseId": secondaryChar.poseId,
            "bubbleType": frame.bubble if frame.bubble is not None else 0,
            "username": frame.customName if frame.customName is not None else "",
            "mergeNext": frame.merge,
            "doNotTalk": not frame.talk,
            "goNext": frame.goNext,
            "poseAnimation": frame.poseAnim,
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
        if frame.hidden:
            frameDict['hide'] = True

        if frame.caseTag:
            if (frame.caseTag in self._frameTags):
                raise ObjectionError('Duplicate frame tag "' + frame.caseTag + '"')
            self._frameTags[frame.caseTag] = frameDict
        self._nextFrameIID += 1

        if frame.transition:
            frameDict['transition']['duration'] = frame.transition.duration
            frameDict['transition']['easing'] = frame.transition.easing.value
            frameDict['transition']['left'] = 0
        if frame.wideX is not None:
            frameDict['transition']['left'] = int(frame.wideX * 100)

        if frame.filter:
            frameDict['filter'] = {
                "id": 0,
                "type": frame.filter.type.value,
                "target": frame.filter.target.value,
                "amount": frame.filter.amount,
            }

        if frame.fade:
            frameDict['frameFades'].append({
                "id": 0,
                "fade": frame.fade.direction.value,
                "target": frame.fade.target.value,
                "easing": frame.fade.easing.value,
                "color": str(frame.fade.color),
                "duration": frame.fade.duration,
            })

        if frame.offScreen:
            frameDict['frameActions'].append({
                'actionId': 6,
            })
        if frame.centerText:
            frameDict['frameActions'].append({
                'actionId': 9,
            })

        presetPopup = frame.presetPopup
        if presetPopup is not None:
            if presetPopup.value > 0:
                frameDict['frameActions'].append({
                    'actionId': 7,
                    'actionParam': str(presetPopup.value),
                })
            elif presetPopup == enums.PresetPopup.TESTIMONY_LABEL_HIDE:
                frameDict['frameActions'].append({
                    'actionId': 8,
                    'actionParam': '1',
                })

        presetBlip = frame.presetBlip
        if presetBlip is not None:
            if presetBlip.value > 0:
                frameDict['frameActions'].append({
                    'actionId': 4,
                    'actionParam': str(presetBlip.value),
                })
            elif presetBlip == enums.PresetBlip.MUTE:
                frameDict['frameActions'].append({
                    'actionId': 5,
                })

        if frame.options.autoplaySpeed is not None:
            frameDict['frameActions'].append({
                'actionId': 15,
                'actionParam': str(frame.options.autoplaySpeed),
            })
        if frame.options.dialogueBox is not None:
            frameDict['frameActions'].append({
                'actionId': 12,
                'actionParam': str(frame.options.dialogueBox.value),
            })
        if frame.options.dialogueBoxVisible is not None:
            frameDict['frameActions'].append({
                'actionId': 1,
                'actionParam': str(int(frame.options.dialogueBoxVisible)),
            })
        if frame.options.defaultTextSpeed is not None:
            frameDict['frameActions'].append({
                'actionId': 13,
                'actionParam': str(frame.options.defaultTextSpeed),
            })
        if frame.options.blipFrequency is not None:
            frameDict['frameActions'].append({
                'actionId': 14,
                'actionParam': str(frame.options.blipFrequency),
            })
        if frame.options.frameSkip is not None:
            frameDict['frameActions'].append({
                'actionId': 16,
                'actionParam': str(int(frame.options.frameSkip)),
            })
        if frame.options.galleryRemove is not None:
            # TODO make it choose dynamically between action 3 (PW) and 11 (AJ) galleries
            for location in frame.options.galleryRemove:
                frameDict['frameActions'].append({
                    'actionId': 3,
                    'actionParam': location.value,
                })
                frameDict['frameActions'].append({
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
                    frameDict['frameActions'].append({
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
            pair = self._requestPair(pairChars[0].character.id, pairChars[1].character.id, pairChars[0].pairOffset,
                               pairChars[1].pairOffset, True if chars[0] is frontChar else False)
            frameDict['pairId'] = pair['pairId']

        self._frameMap.append((frame, frameDict))

        if frame.onCompile is not None:
            frameDict = frame.onCompile(frameDict)

        LimitWarning.checkList(frameDict['frameActions'], self.options.MAX_FRAME_ACTIONS,
                               'frame actions (frame iid=' + str(frameDict['iid']) + ')')

        return frameDict


    def compile(self) -> dict:
        """
        Compile objection.

        Raises:
            - `ObjectionError`
                - Duplicate case tag was found.
                - CEFrame was found in the wrong group.

        Returns:
            JSON-serializable dictionary in the .objection format.
        """
        objectionDict = {
            'credit': 'made with objection.py v' + __version__,
            'version': LATEST_OBJECTION_VERSION,
            'pairs': [],
            'groups': [],
            'courtRecord': {
                'evidence': [],
                'profiles': [],
            },
            'aliases': [],
            'options': {},
            'type': 'scene' if self._type is enums.ObjectionType.SCENE else 'case' if self._type is enums.ObjectionType.CASE else 'unknown',
        }

        objectionDict['options']['chatbox'] = self.options.dialogueBox.value
        objectionDict['options']['textSpeed'] = self.options.defaultTextSpeed
        objectionDict['options']['textBlipFrequency'] = self.options.blipFrequency
        objectionDict['options']['autoplaySpeed'] = self.options.autoplaySpeed
        objectionDict['options']['continueSoundUrl'] = self.options.continueSoundUrl

        for i, alias in enumerate(self.aliases.items()):
            objectionDict['aliases'].append({
                "id": i,
                "from": alias[0],
                "to": alias[1],
            })
        LimitWarning.checkList(
            objectionDict['aliases'], self.options.MAX_ALIASES, 'aliases')

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
            objectionDict['pairs'].append(pair)
            nextPairID += 1
            return pair
        
        self._requestPair = requestPair

        self._nextFrameIID = 1
        self._nextGeneratedGroupName = 1
        self._groupMap = []
        self._frameMap = []
        self._groupTags = {}
        self._frameTags = {}
        for i, group in enumerate(self._groups):
            name = group.name
            if not name:
                name = 'Generated ' + str(self._nextGeneratedGroupName)
                self._nextGeneratedGroupName += 1
            
            groupDict = {
                "iid": i + 1,
                "name": name,
                "type": group._type.value,
                "frames": [],
            }

            if (group.caseTag):
                if (group.caseTag in self._groupTags):
                    raise ObjectionError(
                        'Duplicate group tag "' + group.caseTag + '"')
                self._groupTags[group.caseTag] = groupDict

            for frame in group.frames:
                if isinstance(frame, frames.CEFrame) and not isinstance(group, CEGroup):
                    raise ObjectionError('CEFrame found in non-CE group')
                frameDict = self._compileFrame(frame, frameList=groupDict['frames'])
                groupDict['frames'].append(frameDict)

            if isinstance(group, CEGroup):
                if len(group.counselSequence) > 0:
                    groupDict["counselFrames"] = []
                    for frame in group.counselSequence:
                        if isinstance(frame, frames.CEFrame):
                            raise ObjectionError('CEFrame found within counsel sequence')
                        groupDict["counselFrames"].append(
                            self._compileFrame(frame, frameList=groupDict["counselFrames"])
                        )
                if len(group.failureSequence) > 0:
                    groupDict["failureFrames"] = []
                    for frame in group.failureSequence:
                        if isinstance(frame, frames.CEFrame):
                            raise ObjectionError('CEFrame found within failure sequence')
                        groupDict["failureFrames"].append(
                            self._compileFrame(frame, frameList=groupDict["failureFrames"])
                        )

            self._groupMap.append((group, groupDict))
            objectionDict['groups'].append(groupDict)
            LimitWarning.checkList(groupDict['frames'], self.options.MAX_GROUP_FRAMES,
                                   'frames in a group (group iid=' + str(groupDict['iid']) + ')')
        LimitWarning.checkList(
            objectionDict['groups'], self.options.MAX_GROUPS, 'groups')
        LimitWarning.checkList(
            objectionDict['pairs'], self.options.MAX_PAIRS, 'pairs')

        return objectionDict

    @classmethod
    def makeObjectionFile(cls, objectionDict: dict) -> str:
        return b64encode(bytes(dumps(objectionDict), encoding='utf-8')).decode('utf-8')


class Scene(_ObjectionBase):
    """
    Objection scene - a linear series of frames that can be recorded or played in a browser.
    
    Primarily modified by editing frames in Scene.frames.
    
    Attributes:
        - `options : Options`
            - Default objection options.
        - `aliases : dict[str, str]`
            - Dictionary of aliases, mapping original name to alias.
        - `frames : list[Frames]`
            - The scene's frame list. Primary way of modifying scenes.
    """

    type = enums.ObjectionType.SCENE

    def __init__(self, options: Optional[Options] = None) -> None:
        super().__init__(options)
        mainGroup = Group(name='Main')
        self._groups.append(mainGroup)

    @property
    def frames(self) -> list[Frame]:
        return self._groups[0].frames
    
    def compile(self) -> dict:
        objectionDict = super().compile()

        compiledFrames = self._groupMap[0][1]['frames']
        for frameDict in [*compiledFrames]:
            if frameDict.get('hide'):
                compiledFrames.remove(frameDict)

        return objectionDict


class Case(_ObjectionBase):
    """
    Objection case - interactive game playable only on a browser, with certain extra features.
    
    Attributes:
        - `options : Options`
            - Default objection options.
        - `aliases : dict[str, str]`
            - Dictionary of aliases, mapping original name to alias.
        - `evidence : list[RecordItem]`
        - `profiles : list[RecordItem]`
        - `groups : list[Group]`
            - The case's group list. Primary way of modifying cases.
    """
    type = enums.ObjectionType.CASE

    @dataclass
    class RecordItem:
        type: enums.RecordType
        name: str
        iconUrl: str
        checkUrl: str = ''
        description: str = ''
        hidden: bool = False

        def _getIid(self, objMap: list[tuple]) -> str:
            recordObject = _utils._tupleMapGet(objMap, self)
            prefix: str
            if (self.type is enums.RecordType.EVIDENCE):
                prefix = 'e-'
            elif (self.type is enums.RecordType.PROFILE):
                prefix = 'p-'
            else:
                raise TypeError('Unknown record item type ' + self.type.name)

            return prefix + str(recordObject["iid"])
    evidence: list[RecordItem]
    profiles: list[RecordItem]

    def __init__(self, options: Optional[Options] = None) -> None:
        super().__init__(options)
        self.evidence = []
        self.profiles = []

    @property
    def groups(self) -> list[Group]:
        return self._groups

    def _getByTagOrObj(
        self,
        identifier: Union[str, Any],
        objMap: list[tuple],
        tagMap: dict,
        errorText: str
    ) -> dict:
        if (type(identifier) is str):
            return tagMap[identifier]
        else:
            try:
                return _utils._tupleMapGet(objMap, identifier)
            except KeyError:
                raise KeyError(errorText)

    def _getFrameDict(self, frameParam: Union[str, Frame]) -> dict:
        return self._getByTagOrObj(frameParam, objMap=self._frameMap, tagMap=self._frameTags, errorText='Parsed frame object wasn\' found')

    def _getGroupDict(self, groupParam: Union[str, Group]) -> dict:
        return self._getByTagOrObj(groupParam, objMap=self._groupMap, tagMap=self._groupTags, errorText='Parsed group object wasn\' found')

    def _post_process_frame(self, processedList: list, frame: Frame, frameDict: dict):
        if frame in processedList:
            return
        processedList.append(frame)

        if isinstance(frame, frames.CEFrame):
            if len(frame.pressSequence) > 0:
                frameDict["pressFrames"] = []
                for pressFrame in frame.pressSequence:
                    if isinstance(pressFrame, frames.CEFrame):
                        raise ObjectionError('CEFrame found within press sequence')
                    frameDict["pressFrames"].append(
                        self._compileFrame(pressFrame, frameList=frameDict["pressFrames"])
                    )

            if len(frame.contradictions) > 0:
                frameDict["contradictions"] = []
                for recordItem, frameParam in frame.contradictions:
                    frameDict["contradictions"].append({
                        "eid": recordItem._getIid(self._recordMap),
                        "fid": str(self._getFrameDict(frameParam)["iid"]),
                    })
        
        action = frame.caseAction
        if action is None:
            return
        actionId: int = -1
        actionValue: Any = None

        if isinstance(action, frames.CaseActions.ToggleEvidence):
            actionId = 16
            actionValue = {
                "show": [],
                "hide": [],
            }
            item: Case.RecordItem
            for item in action.show:
                actionValue["show"].append(item._getIid(self._recordMap))
            for item in action.hide:
                actionValue["hide"].append(item._getIid(self._recordMap))

        elif isinstance(action, frames.CaseActions.ToggleFrames):
            actionId = 3
            actionValue = {
                "show": "",
                "hide": "",
            }
            for frameParam in action.show:
                targetframeDict: dict = self._getFrameDict(frameParam)
                actionValue["show"] += str(targetframeDict["iid"]) + ' '
            for frameParam in action.hide:
                targetframeDict: dict = self._getFrameDict(frameParam)
                actionValue["hide"] += str(targetframeDict["iid"]) + ' '
            for key in ("show", "hide"):
                if (len(actionValue[key]) > 0):
                    actionValue[key] = actionValue[key].strip()

        elif isinstance(action, frames.CaseActions.GoToFrame):
            actionId = 4
            actionValue = str(self._getFrameDict(action.frame)["iid"])

        elif isinstance(action, frames.CaseActions.SetGameOverGroup):
            actionId = 15
            actionValue = str(self._getGroupDict(action.group)["iid"])

        elif isinstance(action, frames.CaseActions.EndGame):
            actionId = 5

        elif isinstance(action, (frames.CaseActions.HealthSet, frames.CaseActions.HealthAdd, frames.CaseActions.HealthRemove)):
            actionId = 6
            actionValue = {
                "amount": int(action.amount * 100)
            }
            if isinstance(action, frames.CaseActions.HealthSet):
                actionValue["type"] = 0
            elif isinstance(action, frames.CaseActions.HealthAdd):
                actionValue["type"] = 1
            elif isinstance(action, frames.CaseActions.HealthRemove):
                actionValue["type"] = 2

        elif isinstance(action, frames.CaseActions.FlashingHealth):
            actionId = 7
            actionValue = str(int(action.amount * 100))

        elif isinstance(action, frames.CaseActions.PromptPresent):
            actionId = 8
            actionValue = {
                "evidence": action.presentEvidence,
                "profiles": action.presentProfiles,
                "falseFid": str(self._getFrameDict(action.failFrame)["iid"]),
                "items": [],
            }

            for recordItem, frameParam in action.choices:
                actionValue["items"].append({
                    "eid": recordItem._getIid(self._recordMap),
                    "fid": str(self._getFrameDict(frameParam)["iid"]),
                })

        elif isinstance(action, frames.CaseActions.PromptChoice):
            actionId = 9
            actionValue = []
            for choiceText, frameParam in action.choices:
                actionValue.append({
                    "text": choiceText,
                    "fid": str(self._getFrameDict(frameParam)["iid"]),
                })

        elif isinstance(action, (frames.CaseActions.PromptInt, frames.CaseActions.PromptStr)):
            actionId = 12
            actionValue = {
                "name": action.varName,
                "type": "int",
            }
            if isinstance(action, frames.CaseActions.PromptStr):
                actionValue["lowercase"] = action.toLower
                actionValue["type"] = "string"
                if not action.allowSpaces:
                    actionValue["type"] = "word"

        elif isinstance(action, frames.CaseActions.PromptCursor):
            actionId = 17
            actionValue = {
                "imageUrl": action.previewImageUrl,
                "prompt": action.prompt,
                "color": str(action.cursorColor),
                "falseFid": str(self._getFrameDict(action.failFrame)["iid"]),
                "areas": []
            }

            for cursorRect, frameParam in action.choices:
                actionValue["areas"].append({
                    "fid": str(self._getFrameDict(frameParam)["iid"]),
                    "shape": {
                        "left": cursorRect.left,
                        "top": cursorRect.top,
                        "width": cursorRect.width,
                        "height": cursorRect.height,
                    },
                })

        elif isinstance(action, frames.CaseActions.VarSet):
            actionId = 10
            actionValue = {
                "name": action.varName,
                "value": action.value,
            }

        elif isinstance(action, frames.CaseActions.VarAdd):
            actionId = 11
            actionValue = {
                "name": action.varName,
                "value": str(action.value),
            }

        elif isinstance(action, frames.CaseActions.VarEval):
            actionId = 14
            actionValue = {
                "expression": action.expression,
                "trueFid": str(self._getFrameDict(action.trueFrame)["iid"]),
                "falseFid": str(self._getFrameDict(action.falseFrame)["iid"]),
            }

        if actionId == -1:
            raise TypeError('unknown case action')

        actionObject = {
            "id": actionId,
            "value": actionValue,
        }
        frameDict['caseAction'] = actionObject

    def compile(self) -> dict:
        self._recordMap = []
        courtRecord = {
            'evidence': [],
            'profiles': [],
        }
        for items, recordKey in (self.evidence, 'evidence'), (self.profiles, 'profiles'):
            for i, item in enumerate(items):
                recordObject = {
                    "iid": i + 1,
                    "name": item.name,
                    "iconUrl": item.iconUrl,
                    "url": item.checkUrl,
                    "description": item.description,
                    "hide": item.hidden,
                }
                courtRecord[recordKey].append(recordObject)
                self._recordMap.append((item, recordObject))
        LimitWarning.checkList(
            courtRecord['evidence'], self.options.MAX_EVIDENCE, 'evidence')
        LimitWarning.checkList(
            courtRecord['profiles'], self.options.MAX_PROFILES, 'profiles')
        
        objectionDict = super().compile()
        objectionDict['courtRecord'] = courtRecord

        frame: Frame
        frameDict: dict
        processedList = []
        for i in range(2): # Looping twice to process newly-generated press frames too
            for frame, frameDict in [*self._frameMap]:
                self._post_process_frame(processedList, frame, frameDict)

        return objectionDict


class LimitWarning(Warning):
    """
    Displayed when the limit of an individual objection component is exceeded.
    
    By default, they match the limits of the objection.lol GUI, but can be modified in the objection's Options."""
    @classmethod
    def warn(cls, limit: int, limitTarget: str, value: int):
        warn(
            f'exceeded limit of {limit} {limitTarget} (at {value}) - objection.lol support is not guaranteed', LimitWarning)

    @classmethod
    def checkList(cls, lst: Sized, limit: Optional[int], limitTarget: str):
        if limit is not None and len(lst) > limit:
            cls.warn(limit, limitTarget, len(lst))

class IOWarning(Warning):
    """Warning for the use cases of IOError."""
    pass

class ObjectionError(Exception):
    """Error of unspecified type during objection compilation."""
    pass


def _checkPresetId(characterId: int) -> Optional[int]:
    if characterId >= 1000:
        return characterId
    return None


def _getEnumByValue(enum: 'EnumMeta', value: Any, enumType: 'EnumT') -> 'EnumT':
    if value is None: return value
    for member in enum: # type: ignore
        if member.value == value: # type: ignore
            return member # type: ignore
    raise KeyError(f'Value "{value}" not found in {enum}')


def _getFrameDictAction(frameDict: dict, actionId: int, suppressWarnings: bool) -> Any:
    actions = frameDict.get('frameActions')
    if actions:
        param: Any = None
        found = False
        for action in actions:
            if action['actionId'] == actionId:
                if found:
                    if suppressWarnings: warn(f"Duplicate case action of id {actionId} found at frame {frameDict['iid']} (\"{frameDict['text']}\")", IOWarning)
                    continue
                param = action.get('actionParam')
                if (param is None):
                    param = '' # A random placeholder
                found = True
        return param


def _loadJSONFrame(frameDict: dict, frameClass: type, pairList: list, frameMap: list, frameIIDs: dict, suppressWarnings: bool) -> Frame:
    pair: Optional[dict] = None
    pairedIs1: bool = False
    for pairDict in pairList:
        if pairDict['pairId'] == frameDict['pairId']:
            pair = pairDict
            pairedCharIs1 = frameDict['characterId'] == _checkPresetId(pairDict['characterId2'])
            break

    flipString = frameDict['flipped'] if frameDict['flipped'] else '000'
    
    charAsset = assets.Character(0)
    if frameDict['characterId'] is None:
        for char in preset.collectionValues(preset.Characters):
            for pose in char.poses:
                if pose['id'] == frameDict['poseId']:
                    charAsset = char
                    break
    else:
        charAsset = assets.Character(frameDict['characterId'], _loaded=(frameDict['characterId'] is None))
    char = frames.FrameCharacter(
        character=charAsset,
        poseId=frameDict['poseId'],
        flip=bool(int(flipString[1])),
        isActive=True,
    )

    pairChar = None
    if pair:
        char.pairOffset = (pair['offsetX'], pair['offsetY']) if pairedIs1 else (pair['offsetX2'], pair['offsetY2'])
        char.isFront = pair['front'] if pairedIs1 else not pair['front']

        pairCharId = pair['characterId'] if frameDict['characterId'] == _checkPresetId(pair['characterId2']) else pair['characterId2']
        pairCharAsset = assets.Character(0)
        if pairCharId >= 1000:
            pairCharAsset = assets.Character(pairCharId)
        else:
            for char in preset.collectionValues(preset.Characters):
                if char.id == pairCharId:
                    charAsset = char
                    break
        pairChar = frames.FrameCharacter(
            character=pairCharAsset,
            poseId=frameDict['pairPoseId'],
            flip=bool(int(flipString[2])),
            isActive=False,
            pairOffset=(pair['offsetX2'], pair['offsetY2']) if pairedIs1 else (pair['offsetX'], pair['offsetY']),
            isFront=not pair['front'] if pairedIs1 else pair['front'],
        )

    frame: Frame = frameClass(
        char=char,
        pairChar=pairChar,
        text=frameDict['text'],
        customName=frameDict['username'],
        bubble=frameDict['bubbleType'],
        background=assets.Background(frameDict['backgroundId']) if frameDict['backgroundId'] else None,
        backgroundFlip=bool(int(flipString[0])),
        wideX=frameDict['transition']['left']/100 if frameDict['transition'] and 'left' in frameDict['transition'] else None,
        popup=assets.Popup(frameDict['popupId']) if frameDict['popupId'] else None,

        talk=not frameDict['doNotTalk'],
        poseAnim=frameDict['poseAnimation'],
        goNext=frameDict['goNext'],
        merge=frameDict['mergeNext'],
        offScreen=_getFrameDictAction(frameDict, 6, suppressWarnings) is not None,
        centerText=_getFrameDictAction(frameDict, 9, suppressWarnings) is not None,
        presetBlip=_getEnumByValue(enums.PresetBlip, int(_getFrameDictAction(frameDict, 4, suppressWarnings)), enums.PresetBlip.KATONK) if _getFrameDictAction(frameDict, 4, suppressWarnings) else None,
        presetPopup=_getEnumByValue(enums.PresetPopup, int(_getFrameDictAction(frameDict, 7, suppressWarnings)), enums.PresetPopup.CROSS_EXAMINATION) if _getFrameDictAction(frameDict, 7, suppressWarnings) else None,

        fade=frames.Fade(
            direction=_getEnumByValue(enums.FadeDirection, frameDict['frameFades'][0].get('direction'), enums.FadeDirection.IN),
            target=_getEnumByValue(enums.FadeTarget, frameDict['frameFades'][0].get('target'), enums.FadeTarget.BACKGROUND),
            duration=frameDict['frameFades'][0].get('duration'),
            easing=_getEnumByValue(enums.Easing, frameDict['frameFades'][0].get('easing'), enums.Easing.EASE),
            color=frames.Color(frameDict['frameFades'][0].get('color')),
        ) if frameDict['frameFades'] and len(frameDict['frameFades']) > 0 else None,
        filter=frames.Filter(
            type=_getEnumByValue(enums.FilterType, frameDict['filter'].get('type'), enums.FilterType.GRAYSCALE),
            target=_getEnumByValue(enums.FilterTarget, frameDict['filter'].get('target'), enums.FilterTarget.BACKGROUND),
            amount=frameDict['filter'].get('amount'),
        ) if frameDict['filter'] else None,
        transition=frames.Transition(
            duration=frameDict['transition'].get('duration'),
            easing=_getEnumByValue(enums.Easing, frameDict['transition'].get('easing'), enums.Easing.EASE),
        ) if frameDict['transition'] else None,
        options=frames.OptionModifiers(
            autoplaySpeed=_getFrameDictAction(frameDict, 15, suppressWarnings),
            dialogueBox=_getEnumByValue(enums.PresetDialogueBox, _getFrameDictAction(frameDict, 12, suppressWarnings), enums.PresetDialogueBox.CLASSIC),
            dialogueBoxVisible=bool(int(_getFrameDictAction(frameDict, 1, suppressWarnings))) if _getFrameDictAction(frameDict, 1, suppressWarnings) else None,
            defaultTextSpeed=_getFrameDictAction(frameDict, 13, suppressWarnings),
            blipFrequency=_getFrameDictAction(frameDict, 14, suppressWarnings),
            frameSkip=bool(int(_getFrameDictAction(frameDict, 16, suppressWarnings))) if _getFrameDictAction(frameDict, 16, suppressWarnings) else None,
        )
    )
    if _getFrameDictAction(frameDict, 5, suppressWarnings) is not None:
        if frame.presetBlip is not None:
            frame.presetBlip = enums.PresetBlip.MUTE
        else:
            if suppressWarnings: warn(f"Conflicting speech blip Set and Mute actions at frame {frameDict['iid']} (\"{frameDict['text']}\")", IOWarning)
    if _getFrameDictAction(frameDict, 8, suppressWarnings) is not None:
        if frame.presetPopup is not None:
            frame.presetPopup = enums.PresetPopup.TESTIMONY_LABEL_HIDE
        else:
            if suppressWarnings: warn(f"Unsupported combination of popup Display and Remove actions at frame {frameDict['iid']} (\"{frameDict['text']}\")", IOWarning)
    
    for action in frameDict['frameActions']:
        id, param = action['actionId'], action.get('actionParam')
        if id == 2 or id == 10:
            if suppressWarnings: warn(f"Importing Gallery Assign actions is not yet supported at frame {frameDict['iid']} (\"{frameDict['text']}\")", IOWarning)
        elif id == 3 or id == 11:
            location = _getEnumByValue(enums.CharacterLocation, param, enums.CharacterLocation.DEFENSE)
            if location not in frame.options.galleryRemove:
                frame.options.galleryRemove.append(location)
    
    frameMap.append((frame, frameDict))
    frameIIDs[frameDict['iid']] = frame
    return frame


def loadJSONDict(objectionDict: dict, suppressWarnings: bool = False) -> Union[Scene, Case]:
    """
    Load objectionpy objection from existing .objection in form of a JSON string.

    Args:
        - `objectionDict : dict`
            - Parsed JSON dictionary of an objection.lol .objection
        - `suppressWarnings : bool`
            - Defaults to False.

    Raises:
        - `IOError`
            - A JSON object's type is unknown or unsupported

    Returns:
        Scene or case parsed from the .objection JSON.
    """
    if objectionDict['version'] != LATEST_OBJECTION_VERSION:
        raise IOError(f"Objection version {objectionDict['version']} cannot be loaded. Objection.py currently supports version {LATEST_OBJECTION_VERSION}. If your autopsy- sorry, if your objection is outdated, load file into objection.lol and re-download to update its version")
    
    objection: _ObjectionBase
    if objectionDict['type'] == 'scene':
        objection = Scene()
    elif objectionDict['type'] == 'case':
        objection = Case()
    else:
        raise IOError('Unknown objection type "' + str(objectionDict['type']) + '"')
    
    dialogueBox = _getEnumByValue(enums.PresetDialogueBox, objectionDict['options']['chatbox'], enums.PresetDialogueBox.CLASSIC)
    objection.options = Options(
        dialogueBox=dialogueBox,
        defaultTextSpeed=objectionDict['options']['textSpeed'],
        blipFrequency=objectionDict['options']['textBlipFrequency'],
        autoplaySpeed=objectionDict['options']['autoplaySpeed'],
        continueSoundUrl=objectionDict['options']['continueSoundUrl'],
    )

    for alias in objectionDict['aliases']:
        objection.aliases[alias['from']] = alias['to']
    
    recordMap = {}
    if type(objection) is Case:
        for recordName, recordList, recordType in (('evidence', objection.evidence, enums.RecordType.EVIDENCE), ('profiles', objection.profiles, enums.RecordType.PROFILE)):
            for item in objectionDict['courtRecord'][recordName]:
                recordItem = Case.RecordItem(
                    type=recordType,
                    name=item.get('name'),
                    iconUrl=item.get('iconUrl'),
                    checkUrl=item.get('url'),
                    description=item.get('description'),
                    hidden=item.get('hidden'),
                )
                recordList.append(recordItem)
                recordMap[recordItem._getIid(objMap=[(recordItem, item)])] = recordItem
    
    frameMap = []
    frameIIDs = {}
    groupIIDs = {}
    for groupDict in objectionDict['groups']:
        group: Group
        if groupDict['type'] == 'n':
            group = Group()
        elif groupDict['type'] == 'ce':
            group = CEGroup()
        elif groupDict['type'] == 'go':
            group = GameOverGroup()
        else:
            raise IOError('Unknown group type "' + str(groupDict['type']) + '"')
        objection._groups.append(group)
        group.name = groupDict['name']
        group.frames.append

        groupIIDs[groupDict['iid']] = group

        mainFrameClass = frames.Frame
        if type(group) is CEGroup:
            for frameDict in groupDict['counselFrames']:
                frame = _loadJSONFrame(frameDict, frames.Frame, objectionDict['pairs'], frameMap, frameIIDs, suppressWarnings)
                group.counselSequence.append(frame)
            for frameDict in groupDict['failureFrames']:
                frame = _loadJSONFrame(frameDict, frames.Frame, objectionDict['pairs'], frameMap, frameIIDs, suppressWarnings)
                group.failureSequence.append(frame)
            mainFrameClass = frames.CEFrame

        for frameDict in groupDict['frames']:
            frame = _loadJSONFrame(frameDict, mainFrameClass, objectionDict['pairs'], frameMap, frameIIDs, suppressWarnings)
            group.frames.append(frame)
    
    if type(objection) is Case:
        processedList = []
        frame: Frame
        for i in range(2):
            for frame, frameDict in frameMap:
                if frame in processedList:
                    continue
                processedList.append(frame)
                if frameDict['caseAction']:
                    id, param = frameDict['caseAction']['id'], frameDict['caseAction']['value']

                    if id == 16:
                        frame.caseAction = frames.CaseActions.ToggleEvidence(
                            show=[recordMap[iid] for iid in param['show']],
                            hide=[recordMap[iid] for iid in param['hide']],
                        )
                    elif id == 3:
                        frame.caseAction = frames.CaseActions.ToggleFrames(
                            show=[frameIIDs[int(iid)] for iid in param['show'].split()],
                            hide=[frameIIDs[int(iid)] for iid in param['hide'].split()],
                        )
                    elif id == 4:
                        frame.caseAction = frames.CaseActions.GoToFrame(frameIIDs[int(param)])
                    elif id == 15:
                        frame.caseAction = frames.CaseActions.SetGameOverGroup(groupIIDs[int(param)])
                    elif id == 5:
                        frame.caseAction = frames.CaseActions.EndGame()
                    elif id == 6:
                        if param['type'] == 0:
                            frame.caseAction = frames.CaseActions.HealthSet(param['amount']/100)
                        elif param['type'] == 1:
                            frame.caseAction = frames.CaseActions.HealthAdd(param['amount']/100)
                        elif param['type'] == 2:
                            frame.caseAction = frames.CaseActions.HealthRemove(param['amount']/100)
                    elif id == 7:
                        frame.caseAction = frames.CaseActions.FlashingHealth(int(param)/100)
                    elif id == 8:
                        frame.caseAction = frames.CaseActions.PromptPresent(
                            failFrame=frameIIDs[int(param['falseFid'])],
                            presentEvidence=param['evidence'],
                            presentProfiles=param['profiles'],
                            choices=[(recordMap[item['eid']], frameIIDs[int(item['fid'])]) for item in param['items']],
                        )
                    elif id == 9:
                        frame.caseAction = frames.CaseActions.PromptChoice([
                            (choice['text'], frameIIDs[int(choice['fid'])]) for choice in param
                        ])
                    elif id == 12:
                        if param['type'] == 'int':
                            frame.caseAction = frames.CaseActions.PromptInt(param['name'])
                        else:
                            frame.caseAction = frames.CaseActions.PromptStr(
                                varName=param['name'],
                                allowSpaces=param['type'] == "string",
                                toLower=param['lowercase'],
                            )
                    elif id == 17:
                        frame.caseAction = frames.CaseActions.PromptCursor(
                            failFrame=frameIIDs[int(param['falseFid'])],
                            previewImageUrl=param['imageUrl'],
                            prompt=param['prompt'],
                            cursorColor=frames.Color(param['color']),
                        )
                        for area in param['areas']:
                            frame.caseAction.choices.append((
                                frames.CursorRect(area['shape']['left'], area['shape']['top'], area['shape']['width'], area['shape']['height']),
                                frameIIDs[int(area['fid'])],
                            ))
                    elif id == 10:
                        frame.caseAction = frames.CaseActions.VarSet(param['name'], param['value'])
                    elif id == 11:
                        frame.caseAction = frames.CaseActions.VarAdd(param['name'], param['value'])
                    elif id == 14:
                        frame.caseAction = frames.CaseActions.VarEval(
                            trueFrame=frameIIDs[int(param['trueFid'])],
                            falseFrame=frameIIDs[int(param['falseFid'])],
                            expression=param['expression'],
                        )
                    elif id == 13:
                        operator: str
                        if param['type'] == "equals":
                            operator = '=='
                        elif param['type'] == "notEquals":
                            operator = '!='
                        elif param['type'] == "greaterThan":
                            operator = '>'
                        elif param['type'] == "lessThan":
                            operator = '<'
                        else:
                            raise IOError(f"Unknown variable evaluation operator \"{param['type']}\" at frame {frameDict['iid']} (\"{frameDict['text']}\")")
                        frame.caseAction = frames.CaseActions.VarEval(
                            trueFrame=frameIIDs[int(param['trueFid'])],
                            falseFrame=frameIIDs[int(param['falseFid'])],
                            expression=param['name'] + operator + param['value'],
                        )
                
                if type(frame) is frames.CEFrame:
                    if 'contradictions' in frameDict:
                        for contraDict in frameDict['contradictions']:
                            frame.contradictions.append((
                                recordMap[contraDict['eid']],
                                frameIIDs[int(contraDict['fid'])],
                            ))
                    if 'pressFrames' in frameDict:
                        for pressDict in frameDict['pressFrames']:
                            pressFrame = _loadJSONFrame(pressDict, Frame, objectionDict['pairs'], frameMap, frameIIDs, suppressWarnings)
                            frame.pressSequence.append(pressFrame)
    
    return objection

def loadJSONStr(objection: str, suppressWarnings: bool = False) -> Union[Scene, Case]:
    """
    Load objectionpy objection from existing .objection in form of a JSON string.

    Args:
        - `objection : str`
            - JSON string of an objection.lol .objection
        - `suppressWarnings : bool`
            - Defaults to False.

    Raises:
        - `IOError`
            - A JSON object's type is unknown or unsupported

    Returns:
        Scene or case parsed from the .objection JSON.
    """
    return loadJSONDict(loads(objection))

def loadB64(objection: str, suppressWarnings: bool = False) -> Union[Scene, Case]:
    """
    Load objectionpy objection from existing .objection in form of base64-encoded JSON.

    Args:
        - `objection : str`
            - Base64-encoded JSON string of an objection.lol .objection
        - `suppressWarnings : bool`
            - Defaults to False.

    Raises:
        - `IOError`
            - A JSON object's type is unknown or unsupported

    Returns:
        Scene or case parsed from the .objection JSON.
    """
    return loadJSONStr(b64decode(objection).decode("utf-8"))
