from dataclasses import dataclass, field
from re import fullmatch
from typing import Callable, Optional, Union, TYPE_CHECKING
from . import enums, assets
if TYPE_CHECKING:
    from .objection import Case, Group


class Color:
    def __init__(self, string: str) -> None:
        if (fullmatch('#[a-fA-F0-9]{3}', string)): string = '#' + string[1] + string[1] + string[2] + string[2] + string[3] + string[3]
        if (not fullmatch('#[a-fA-F0-9]{6}', string)): raise ValueError('Invalid color ' + string + ', must be in hex #aaa or #ababab form')
        self.string = string.upper()
    
    def __repr__(self) -> str:
        return self.string



@dataclass
class FrameCharacter:
    character: assets.Character
    poseId: Optional[int] = None
    poseSubstr: Optional[str] = None
    flip: bool = False
    pairOffset: tuple[int, int] = (0, 0)
    isActive: Optional[bool] = None
    isFront: Optional[bool] = None

    def __post_init__(self):
        if self.poseId is None and self.poseSubstr is not None:
            self.poseId = self.character.lookupPoseSubstr(self.poseSubstr)

    @property
    def isNone(self) -> bool:
        return self.character.id is None and self.poseId is None

    def _getIndividualValue(self, value) -> int:
        if value is False or self.isNone:
            return -1
        elif value is True:
            return 1
        else:
            return 0


@dataclass
class Fade:
    direction: enums.FadeDirection
    target: enums.FadeTarget
    duration: int
    easing: enums.Easing = enums.Easing.LINEAR
    color: Optional[Color] = None


@dataclass
class Filter:
    type: enums.FilterType
    target: enums.FilterTarget
    amount: int = 100


@dataclass
class Transition:
    duration: int
    easing: enums.Easing = enums.Easing.LINEAR


@dataclass
class Properties:
    talk: bool = True
    poseAnim: bool = True
    goNext: bool = False
    merge: bool = False
    offScreen: bool = False
    centerText: bool = False
    presetPopup: Optional[enums.PresetPopup] = None
    presetBlip: Optional[enums.PresetBlip] = None


@dataclass
class GalleryModifier:
    defense: Optional[assets.Character] = None
    prosecution:  Optional[assets.Character] = None
    counsel: Optional[assets.Character] = None
    witness: Optional[assets.Character] = None
    judge: Optional[assets.Character] = None


@dataclass
class CursorRect:
    top: int
    left: int
    width: int
    height: int


@dataclass
class OptionModifiers:
    autoplaySpeed: Optional[int] = None
    dialogueBox: Optional[enums.PresetDialogueBox] = None
    dialogueBoxVisible: Optional[bool] = None
    galleryAssign: GalleryModifier = field(default_factory=GalleryModifier)
    galleryRemove: list[enums.CharacterLocation] = field(default_factory=list)
    defaultTextSpeed: Optional[int] = None
    blipFrequency: Optional[int] = None
    frameSkip: Optional[bool] = None

    def __post_init__(self):
        if len(self.galleryRemove) > 0 or self.galleryAssign.defense or self.galleryAssign.prosecution or self.galleryAssign.counsel or self.galleryAssign.witness or self.galleryAssign.judge:
            raise NotImplementedError('Gallery assign & remove modifiers have not yet been implemented')


class CaseActions:
    def __init__(self) -> None:
        raise NotImplementedError('')

    class _CaseAction:
        pass

    @dataclass
    class ToggleEvidence(_CaseAction):
        show: list['Case.RecordItem'] = field(default_factory=list)
        hide: list['Case.RecordItem'] = field(default_factory=list)

    @dataclass
    class ToggleFrames(_CaseAction):
        show: list[Union[str, 'Frame']] = field(default_factory=list)
        hide: list[Union[str, 'Frame']] = field(default_factory=list)

    @dataclass
    class GoToFrame(_CaseAction):
        frame: Union[str, 'Frame']

    @dataclass
    class SetGameOverGroup(_CaseAction):
        group: Union[str, 'Group']

    class EndGame(_CaseAction):
        pass

    @dataclass
    class HealthSet(_CaseAction):
        amount: float # 0 to 1 fraction

    @dataclass
    class HealthAdd(_CaseAction):
        amount: float

    @dataclass
    class HealthRemove(_CaseAction):
        amount: float

    @dataclass
    class FlashingHealth(_CaseAction):
        amount: float

    @dataclass
    class PromptPresent(_CaseAction):
        failFrame: Union[str, 'Frame']
        choices: list[
            tuple[
                'Case.RecordItem',
                Union[str, 'Frame']
            ]
        ] = field(default_factory=list)

        presentEvidence: bool = False
        presentProfiles: bool = False

    @dataclass
    class PromptChoice(_CaseAction):
        choices: list[
            tuple[
                str, Union[str, 'Frame']
            ]
        ] = field(default_factory=list)

        def __post_init__(self):
            if len(self.choices) > 4:
                raise IndexError(self.__class__.__name__ + ' cannot have over 4 choices')
            elif len(self.choices) == 0:
                raise IndexError(self.__class__.__name__ + ' has 0 choices')

    @dataclass
    class PromptInt(_CaseAction):
        varName: str

    @dataclass
    class PromptStr(_CaseAction):
        varName: str
        allowSpaces: bool = True
        toLower: bool = False

    @dataclass
    class PromptCursor(_CaseAction):
        imageUrl: str
        prompt: str
        failFrame: Union[str, 'Frame']
        cursorColor: Color = Color('#F00')

        choices: list[
            tuple[
                CursorRect,
                Union[str, 'Frame']
            ]
        ] = field(default_factory=list)

    @dataclass
    class VarSet(_CaseAction):
        varName: str
        value: Union[int, str]

    @dataclass
    class VarAdd(_CaseAction):
        varName: str
        value: int

    @dataclass
    class VarEval(_CaseAction):
        expression: str
        trueFrame: Union[str, 'Frame']
        falseFrame: Union[str, 'Frame']


@dataclass
class Frame:
    char: Optional[FrameCharacter]
    pairChar: Optional[FrameCharacter] = None
    text: str = ''

    customName: Optional[str] = None
    bubble: Optional[int] = None
    background: Optional[assets.Background] = None
    backgroundFlip: Optional[bool] = None
    wideX: Optional[float] = None
    popup: Optional[assets.Popup] = None

    fade: Optional[Fade] = None
    filter: Optional[Filter] = None
    transition: Optional[Transition] = None
    properties: Properties = field(default_factory=Properties)
    options: OptionModifiers = field(default_factory=OptionModifiers)

    caseTag: Optional[str] = None
    caseAction: Optional[CaseActions._CaseAction] = None

    onCompile: Optional[Callable[[dict], dict]] = None # Optional function if it's absolutely necessary to work with the raw compiled frame dict


@dataclass
class CEFrame(Frame):
    pressSequence: list[Frame] = field(default_factory=list)
    contradictions: list[
            tuple[
                'Case.RecordItem',
                Union[str, 'Frame']
            ]
        ] = field(default_factory=list)


noneCharacter = FrameCharacter(
    assets.Character(None, loaded=True),
    None,
    flip=False,
    isActive=False,
    isFront=False,
)
