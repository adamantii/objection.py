from dataclasses import dataclass, field
from functools import _lru_cache_wrapper, cache
from json import dumps
from base64 import b64encode
from typing import Any, Optional, Sized, Union
from warnings import warn

from numpy import isin
from . import enums, _utils, frames


PACKAGE_VERSION = 'v0.0'
LATEST_OBJECTION_VERSION = 4

Frame = frames.Frame


@dataclass
class ObjectionOptions:
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


@dataclass
class Group:
    type: enums.GroupType = field(default=enums.GroupType.NORMAL, init=False)
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
    type: enums.GroupType = field(
        default=enums.GroupType.CROSS_EXAMINATION, init=False)
    counselSequence: list[Frame] = field(default_factory=list, init=False)
    failureSequence: list[Frame] = field(default_factory=list, init=False)


class GameOverGroup(Group):
    type = enums.GroupType.GAME_OVER


class _ObjectionBase:
    type: enums.ObjectionType

    options: ObjectionOptions

    aliases: dict[str, str]
    _groups: list[Group]
    _nextFrameIID: int

    def __init__(self, options: Optional[ObjectionOptions] = None) -> None:
        self.options = options if options is not None else ObjectionOptions()
        self.aliases = {}
        self._groups = []

    @classmethod
    def _verifyFrameChar(cls, char: Optional[frames.FrameCharacter]) -> frames.FrameCharacter:
        return char if char is not None else frames.noneCharacter

    def _compileFrame(self, frame: Frame, frameList: list[Frame]):
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
            "goNext": frame.properties.goNext,
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
        if (frame.caseTag):
            if (frame.caseTag in self._frameTags):
                raise ObjectionError('Duplicate frame tag "' + frame.caseTag + '"')
            self._frameTags[frame.caseTag] = frameObject
        self._nextFrameIID += 1

        if frame.transition:
            frameObject['transition']['duration'] = frame.transition.duration
            frameObject['transition']['easing'] = frame.transition.easing.value
            frameObject['transition']['left'] = 0
        if frame.wideX is not None:
            frameObject['transition']['left'] = int(frame.wideX * 100)

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
            pair = self._requestPair(pairChars[0].character.id, pairChars[1].character.id, pairChars[0].pairOffset,
                               pairChars[1].pairOffset, True if chars[0] is frontChar else False)
            frameObject['pairId'] = pair['pairId']

        self._frameMap.append((frame, frameObject))

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
            'type': 'scene' if self.type is enums.ObjectionType.SCENE else 'case' if self.type is enums.ObjectionType.CASE else 'unknown',
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
        
        self._requestPair = requestPair

        self._nextFrameIID = 1
        self._groupMap = []
        self._frameMap = []
        self._groupTags = {}
        self._frameTags = {}
        for i, group in enumerate(self._groups):
            groupObject = {
                "iid": i + 1,
                "name": group.name,
                "type": group.type.value,
                "frames": [],
            }

            if (group.caseTag):
                if (group.caseTag in self._groupTags):
                    raise ObjectionError(
                        'Duplicate group tag "' + group.caseTag + '"')
                self._groupTags[group.caseTag] = groupObject

            for frame in group.frames:
                if isinstance(frame, frames.CEFrame) and not isinstance(group, CEGroup):
                    raise ObjectionError('CEFrame found in non-CE group')
                frameObject = self._compileFrame(frame, frameList=groupObject['frames'])
                groupObject['frames'].append(frameObject)

            if isinstance(group, CEGroup):
                if len(group.counselSequence) > 0:
                    groupObject["counselFrames"] = []
                    for frame in group.counselSequence:
                        if isinstance(frame, frames.CEFrame):
                            raise ObjectionError('CEFrame found within counsel sequence')
                        groupObject["counselFrames"].append(
                            self._compileFrame(frame, frameList=groupObject["counselFrames"])
                        )
                if len(group.failureSequence) > 0:
                    groupObject["failureFrames"] = []
                    for frame in group.failureSequence:
                        if isinstance(frame, frames.CEFrame):
                            raise ObjectionError('CEFrame found within failure sequence')
                        groupObject["failureFrames"].append(
                            self._compileFrame(frame, frameList=groupObject["failureFrames"])
                        )

            self._groupMap.append((group, groupObject))
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
        return b64encode(bytes(dumps(objectionObject), encoding='utf-8')).decode('utf-8')


class Scene(_ObjectionBase):
    type = enums.ObjectionType.SCENE

    def __init__(self, options: Optional[ObjectionOptions] = None) -> None:
        super().__init__(options)
        mainGroup = Group(name='Main')

    @property
    def frames(self) -> list[Frame]:
        return self._groups[0].frames


class Case(_ObjectionBase):
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

    def __init__(self, options: Optional[ObjectionOptions] = None) -> None:
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
            except StopIteration:
                raise ValueError(errorText)

    def _getFrameObject(self, frameParam: Union[str, Frame]) -> dict:
        return self._getByTagOrObj(frameParam, objMap=self._frameMap, tagMap=self._frameTags, errorText='Parsed frame object wasn\' found')

    def _getGroupObject(self, groupParam: Union[str, Group]) -> dict:
        return self._getByTagOrObj(groupParam, objMap=self._groupMap, tagMap=self._groupTags, errorText='Parsed group object wasn\' found')

    def compile(self):
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
        
        objectionObject = super().compile()
        objectionObject['courtRecord'] = courtRecord

        frame: Frame
        frameObject: dict
        for frame, frameObject in self._frameMap:
            if isinstance(frame, frames.CEFrame):
                if len(frame.pressSequence) > 0:
                    frameObject["pressFrames"] = []
                    for pressFrame in frame.pressSequence:
                        if isinstance(pressFrame, frames.CEFrame):
                            raise ObjectionError('CEFrame found within press sequence')
                        frameObject["pressFrames"].append(
                            self._compileFrame(pressFrame, frameList=frameObject["pressFrames"])
                        )

                if len(frame.contradictions) > 0:
                    frameObject["contradictions"] = []
                    for recordItem, frameParam in frame.contradictions:
                        frameObject["contradictions"].append({
                            "eid": recordItem._getIid(self._recordMap),
                            "fid": str(self._getFrameObject(frameParam)["iid"]),
                        })
            
            action = frame.caseAction
            if action is None:
                continue
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
                    targetFrameObject: dict = self._getFrameObject(frameParam)
                    actionValue["show"] += str(targetFrameObject["iid"]) + ' '
                for frameParam in action.hide:
                    targetFrameObject: dict = self._getFrameObject(frameParam)
                    actionValue["hide"] += str(targetFrameObject["iid"]) + ' '
                for key in ("show", "hide"):
                    if (len(actionValue[key]) > 0):
                        actionValue[key] = actionValue[key].strip()

            elif isinstance(action, frames.CaseActions.GoToFrame):
                actionId = 4
                actionValue = str(self._getFrameObject(action.frame)["iid"])

            elif isinstance(action, frames.CaseActions.SetGameOverGroup):
                actionId = 15
                actionValue = str(self._getGroupObject(action.group)["iid"])

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
                    "falseFid": str(self._getFrameObject(action.failFrame)["iid"]),
                    "items": [],
                }

                for recordItem, frameParam in action.choices:
                    actionValue["items"].append({
                        "eid": recordItem._getIid(self._recordMap),
                        "fid": str(self._getFrameObject(frameParam)["iid"]),
                    })

            elif isinstance(action, frames.CaseActions.PromptChoice):
                actionId = 9
                actionValue = []
                for choiceText, frameParam in action.choices:
                    actionValue.append({
                        "text": choiceText,
                        "fid": str(self._getFrameObject(frameParam)["iid"]),
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
                    "imageUrl": action.imageUrl,
                    "prompt": action.prompt,
                    "color": str(action.cursorColor),
                    "falseFid": str(self._getFrameObject(action.failFrame)["iid"]),
                    "areas": []
                }

                for cursorRect, frameParam in action.choices:
                    actionValue["areas"].append({
                        "fid": str(self._getFrameObject(frameParam)["iid"]),
                        "shape": {
                            "top": cursorRect.top,
                            "left": cursorRect.left,
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
                    "trueFid": str(self._getFrameObject(action.trueFrame)["iid"]),
                    "falseFid": str(self._getFrameObject(action.falseFrame)["iid"]),
                }

            if actionId == -1:
                raise TypeError('unknown case action')

            actionObject = {
                "id": actionId,
                "value": actionValue,
            }
            frameObject['caseAction'] = actionObject

        return objectionObject


class LimitWarning(Warning):
    @classmethod
    def warn(cls, limit: int, limitTarget: str, value: int):
        warn(
            f'exceeded limit of {limit} {limitTarget} (at {value}) - objection.lol support is not guaranteed', LimitWarning)

    @classmethod
    def checkList(cls, lst: Sized, limit: Optional[int], limitTarget: str):
        if limit is not None and len(lst) > limit:
            cls.warn(limit, limitTarget, len(lst))


class ObjectionError(Exception):
    pass
