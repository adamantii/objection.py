from objectionpy import objection
from dataclasses import dataclass, field
from typing import Callable, Optional
from copy import deepcopy
from objectionpy import enums, assets


@dataclass
class FrameCharacter:
    character: assets.Character
    poseId: Optional[int]
    flip: bool = False
    pairOffset: tuple[int, int] = (0, 0)
    isActive: Optional[bool] = None
    isFront: Optional[bool] = None

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
    color: Optional[str] = None


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
class FrameProperties:
    talk: bool = True
    poseAnim: bool = True
    moveNext: bool = False
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
class OptionModifiers:
    autoplaySpeed: Optional[int] = None
    dialogueBox: Optional[enums.PresetDialogueBox] = None
    dialogueBoxVisible: Optional[bool] = None
    galleryAssign: GalleryModifier = field(default_factory=GalleryModifier)
    galleryRemove: list[enums.CharacterLocation] = field(default_factory=list)
    defaultTextSpeed: Optional[int] = None
    blipFrequency: Optional[int] = None
    frameSkip: Optional[bool] = None


@dataclass
class Frame:
    char: Optional[FrameCharacter]
    pairChar: Optional[FrameCharacter] = None
    text: str = ''

    customName: Optional[str] = None
    bubble: Optional[int] = None
    background: Optional[assets.Background] = None
    backgroundFlip: bool = False
    wideLeft: Optional[float] = None
    popup: Optional[assets.Popup] = None

    fade: Optional[Fade] = None
    filter: Optional[Filter] = None
    transition: Optional[Transition] = None
    properties: FrameProperties = field(default_factory=FrameProperties)
    options: OptionModifiers = field(default_factory=OptionModifiers)

    tag: Optional[str] = None  # The frame's identifier for case actions
    caseAction: None = None

    onCompile: Optional[Callable[[dict], dict]] = None

    def copy(self) -> 'Frame':
        return deepcopy(self)


@dataclass
class Contradiction:
    evidence: objection.Case.RecordItem
    targetTag: str


@dataclass
class CEFrame(Frame):
    pressFrames: list[Frame] = field(default_factory=list)
    contradictions: list[Contradiction] = field(default_factory=list)


noneCharacter = FrameCharacter(
    assets.Character(None, loaded=True),
    None,
    False,
    isActive=False,
    isFront=False,
)
