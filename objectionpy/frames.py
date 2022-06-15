"""Contains everything related to individual frame properties."""

from dataclasses import dataclass, field
from re import fullmatch
from typing import Callable, Optional, Union, TYPE_CHECKING
from . import enums, assets
if TYPE_CHECKING:
    from .objection import Case, Group


class Color:
    """Color.
    
    Must use hex format, either #aaa or #ababab. Case-insensitive."""
    def __init__(self, string: str) -> None:
        if (fullmatch('#[a-fA-F0-9]{3}', string)): string = '#' + string[1] + string[1] + string[2] + string[2] + string[3] + string[3]
        if (not fullmatch('#[a-fA-F0-9]{6}', string)): raise ValueError('Invalid color ' + string + ', must be in hex #aaa or #ababab format')
        self.string = string.upper()
    
    def __repr__(self) -> str:
        return self.string


@dataclass
class CursorRect:
    """An area targettable by the cursor in the "point to an area" case action."""
    left: int
    top: int
    width: int
    height: int


class CaseActions:
    """Stores all case action types."""
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
        """
        Attributes:
            - `show : list[<Frame Target>]`
                - List of references or caseTags of frames to show.
            - `hide : list[<Frame Target>]`
                - List of references or caseTags of frames to hide.
        """
        show: list[Union[str, 'Frame']] = field(default_factory=list)
        hide: list[Union[str, 'Frame']] = field(default_factory=list)

    @dataclass
    class GoToFrame(_CaseAction):
        """
        Attributes:
            - `frame : <Frame Target>`
                - Reference or caseTag of a frame to jump to.
        """
        frame: Union[str, 'Frame']

    @dataclass
    class SetGameOverGroup(_CaseAction):
        """
        Attributes:
            - `group : <Group Target>`
                - Reference or caseTag of the target group.
        """
        group: Union[str, 'Group']

    class EndGame(_CaseAction):
        pass

    @dataclass
    class HealthSet(_CaseAction):
        """
        Attributes:
            - `amount : float`
                - Fraction of the max health to set the health to, from 0 to 1.
        """
        amount: float

    @dataclass
    class HealthAdd(_CaseAction):
        """
        Attributes:
            - `amount : float`
                - Fraction of the max health to add to the health, from 0 to 1.
        """
        amount: float

    @dataclass
    class HealthRemove(_CaseAction):
        """
        Attributes:
            - `amount : float`
                - Fraction of the max health to subtract from the health, from 0 to 1.
        """
        amount: float

    @dataclass
    class FlashingHealth(_CaseAction):
        """
        Attributes:
            - `amount : float`
                - Fraction of the max health to start flashing, from 0 to 1.
        """
        amount: float

    @dataclass
    class PromptPresent(_CaseAction):
        """
        Attributes:
            - `failFrame : <Frame Target>`
                - Reference or caseTag of a frame to display upon presenting the wrong item.
            - `choices : list[tuple[RecordItem, <Frame Target>]]`
                - List of tuples mapping evidence and profiles to present to caseTags/frame references.
            - `presentEvidence : bool`
            - `presentProfiles : bool`
        """
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
        """
        Attributes:
            - `choices : list[tuple[str, <Frame Target>]]`
                - List of tuples mapping choice text to caseTags/frame references.
        """
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
        """
        Attributes:
            - `prompt : str`
                - Prompt text below the frame.
            - `failFrame : <Frame Target>`
                - Reference or caseTag of a frame to display upon presenting the wrong item.
            - `cursorColor : str`
                - Defaults to red (#F000.
            - `previewImageUrl : str`
                - Preview image URL for the action. (Only useful in the objection.lol Maker GUI)
            - `choices : list[tuple[CursorRect, <Frame Target>]]`
                - List of tuples mapping pointable area rects to caseTags/frame references.
        """
        prompt: str
        failFrame: Union[str, 'Frame']
        cursorColor: Color = Color('#F00')
        previewImageUrl: str = ''

        choices: list[
            tuple[
                'CursorRect',
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
        """
        Attributes:
            - `expression : str`
                - Condition expression. Can contain:
                    - Variable names
                    - Math operators `+ - * / %`
                    - Comparisons `> < >= <= == !=`
                    - Logical operators `&& || !`
            - `trueFrame : <Frame Target>`
                - Reference or caseTag of a frame to display if the condition is true.
            - `falseFrame : <Frame Target>`
                - Reference or caseTag of a frame to display if the condition is false.
        """
        expression: str
        trueFrame: Union[str, 'Frame']
        falseFrame: Union[str, 'Frame']


@dataclass
class Fade:
    """
    Fade a target.
    
    Color attribute doesn't apply to character targets.
    Target attribute doesn't apply to OUT_IN direction.
    """
    direction: enums.FadeDirection
    target: enums.FadeTarget
    duration: int
    easing: enums.Easing = enums.Easing.LINEAR
    color: Optional[Color] = None


@dataclass
class Filter:
    """
    Color filter to a specific target.
    
    Amount attribute doesn't apply to INVERT and SEPIA types.
    """
    type: enums.FilterType
    target: enums.FilterTarget
    amount: int = 100


@dataclass
class FrameCharacter:
    """
    Specifies the attributes of a displayed character.
    
    Attributes:
        - `character : assets.Character`
            - The character to display.
        - `poseId : Optional[int]`
            - The ID of the displayed pose. Must be in this character's pose list. Either poseId or poseSubstr must be set.
        - `poseSubstr : Optional[str]`
            - A substring to identify this character's pose by using Character.lookupPoseSubstr. Either poseId or poseSubstr must be set.
        - `flip : bool`
            - Whether this character is flipped.
        - `pairOffset : tuple[int, int]`
            - On compilation, automatically generates a pair group to set the offset. (Duplicate pair groups are avoided.)
        - `isActive : Optional[bool]`
            - Whether this is the character that acts in the frame. Only applies when character is paired with another.
        - `isFront : Optional[bool]`
            - Whether this character displayed is in front of the other. Only applies when character is paired with another.
    """
    character: assets.Character
    poseId: Optional[int] = None
    poseSubstr: Optional[str] = None
    flip: bool = False
    pairOffset: tuple[int, int] = (0, 0)
    isActive: Optional[bool] = None
    isFront: Optional[bool] = None

    def __post_init__(self):
        if self.poseId is None:
            if self.poseSubstr is not None:
                self.poseId = self.character.lookupPoseSubstr(self.poseSubstr)
            else:
                raise AttributeError('Either poseId or poseSubstr must be set to identify the pose in a FrameCharacter.')

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
class GalleryModifier:
    """Specify characters for each gallery location.
    
    Any location set to None remains unchanged. (Custom characters not yet supported)"""
    defense: Optional[assets.Character] = None
    prosecution:  Optional[assets.Character] = None
    counsel: Optional[assets.Character] = None
    witness: Optional[assets.Character] = None
    judge: Optional[assets.Character] = None


@dataclass
class OptionModifiers:
    """
    Specify values for setting objection options affecting future frames.

    Any option set to None remains unchanged.
    """
    autoplaySpeed: Optional[int] = None
    dialogueBox: Optional[enums.PresetDialogueBox] = None
    dialogueBoxVisible: Optional[bool] = None
    galleryAssign: GalleryModifier = field(default_factory=GalleryModifier)
    galleryRemove: list[enums.CharacterLocation] = field(default_factory=list)
    defaultTextSpeed: Optional[int] = None
    blipFrequency: Optional[int] = None
    frameSkip: Optional[bool] = None

    def __post_init__(self):
        for character in self.galleryAssign.__dict__.values():
            if character and not character.isPreset:
                raise FutureWarning('Gallery assign modifiers not yet implemented to work for custom characters')


@dataclass
class Transition:
    """Camera transition on wide backgrounds."""
    duration: int
    easing: enums.Easing = enums.Easing.LINEAR


@dataclass
class Frame:
    """
    A frame of an objection.

    Attributes:
        - `char : Optional[FrameCharacter]`
            - Displayed character.
        - `pairChar : Optional[FrameCharacter]`
            - An optional second character. The talking and acting character is determined by the FrameCharacter.active attribute.
        - `text : str`
            - Displayed text. Defaults to empty, implying no effect on textbox.
        - `customName : Optional[str]`
            - The name displayed in the dialogue box's nameplate.
        - `bubble : Optional[int]`
            - ID of a speech bubble to be played. Must be in the character's speech bubble list. Preset characters always use 1-3, sometimes 4 and 5.
        - `background : Optional[assets.Background]`
            - Displayed background.
        - `backgroundFlip : Optional[bool]`
            - Whether the background is flipped.
        - `wideX : Optional[float]`
            - Percentage of the background's width to offset the camera by, from 0 to 1. Only applies to wide backgrounds.
        - `popup : Optional[assets.Popup]`
            - Displayed custom pop-up. (Use presetPopup for preset pop-ups)
        - `talk : bool`
            - Whether the talking character's talking animation is displayed. Defaults to True.
        - `poseAnim : bool`
            - Whether the active character's pose animation is displayed. Defaults to True.
        - `goNext : bool`
            - Moves to the next frame instantly and without requiring the user to continue. Defaults to False.
        - `merge : bool`
            - Does not reset the text in the textbox before the next frame. Defaults to False.
        - `offScreen : bool`
            - If True, the frame's character, text and popup are not displayed, only their speech bubble. Defaults to False.
        - `centerText : bool`
            - Whether the text in the dialogue box is centered. Defaults to False.
        - `presetPopup : Optional[enums.PresetPopup]`
            - Displayed pre-set pop-up.
        - `presetBlip : Optional[enums.PresetBlip]`
            - The speech blip played during character talking. If None, uses the character's default blip.
        - `fade : Optional[Fade]`
            - The frame's fade.
        - `filter : Optional[Filter]`
            - The frame's filter.
        - `transition : Optional[Transition]`
            - The frame's transition.
            - Only applies to wide backgrounds, when the previous frame's background is unchanged.
        - `options : OptionModifiers`
            - Can be used to modify objection options affecting future frames.
        - `hidden : bool`
            - Whether the frame is hidden by default. Only useful in cases. Defaults to False.
        - `caseTag : Optional[str]`
            - A unique tag used to identify the frame in case actions. (A direct reference to the frame object works too)
        - `caseAction : Optional[CaseActions._CaseAction]`
            - The frame's case action.
        - `onCompile : Optional[Callable[[dict], dict]]`
            - A callback for if it's absolutely necessary to access the frame's raw JSON dict upon compilation.
    """
    char: Optional[FrameCharacter]
    pairChar: Optional[FrameCharacter] = None
    text: str = ''

    customName: Optional[str] = None
    bubble: Optional[int] = None
    background: Optional[assets.Background] = None
    backgroundFlip: Optional[bool] = None
    wideX: Optional[float] = None
    popup: Optional[assets.Popup] = None

    talk: bool = True
    poseAnim: bool = True
    goNext: bool = False
    merge: bool = False
    offScreen: bool = False
    centerText: bool = False
    presetPopup: Optional[enums.PresetPopup] = None
    presetBlip: Optional[enums.PresetBlip] = None

    fade: Optional[Fade] = None
    filter: Optional[Filter] = None
    transition: Optional[Transition] = None
    options: OptionModifiers = field(default_factory=OptionModifiers)

    hidden: bool = False
    caseTag: Optional[str] = None
    caseAction: Optional[CaseActions._CaseAction] = None

    onCompile: Optional[Callable[[dict], dict]] = None # Optional function if it's absolutely necessary to work with the raw compiled frame dict


@dataclass
class CEFrame(Frame):
    """
    A special frame representing a cross-examination testimony statement in a CEGroup.

    Attributes:
        - `char : Optional[FrameCharacter]`
            - Displayed character.
        - `pairChar : Optional[FrameCharacter]`
            - An optional second character. The talking and acting character is determined by the FrameCharacter.active attribute.
        - `text : str`
            - Displayed text. Defaults to empty, implying no effect on textbox.
        - `customName : Optional[str]`
            - The name displayed in the dialogue box's nameplate.
        - `bubble : Optional[int]`
            - ID of a speech bubble to be played. Must be in the character's speech bubble list. Preset characters always use 1-3, sometimes 4 and 5.
        - `background : Optional[assets.Background]`
            - Displayed background.
        - `backgroundFlip : Optional[bool]`
            - Whether the background is flipped.
        - `wideX : Optional[float]`
            - Percentage of the background's width to offset the camera by, from 0 to 1. Only applies to wide backgrounds.
        - `popup : Optional[assets.Popup]`
            - Displayed custom pop-up. (Use presetPopup for preset pop-ups)
        - `talk : bool`
            - Whether the talking character's talking animation is displayed. Defaults to True.
        - `poseAnim : bool`
            - Whether the active character's pose animation is displayed. Defaults to True.
        - `goNext : bool`
            - Moves to the next frame instantly and without requiring the user to continue. Defaults to False.
        - `merge : bool`
            - Does not reset the text in the textbox before the next frame. Defaults to False.
        - `offScreen : bool`
            - If True, the frame's character, text and popup are not displayed, only their speech bubble. Defaults to False.
        - `centerText : bool`
            - Whether the text in the dialogue box is centered. Defaults to False.
        - `presetPopup : Optional[enums.PresetPopup]`
            - Displayed pre-set pop-up.
        - `presetBlip : Optional[enums.PresetBlip]`
            - The speech blip played during character talking. If None, uses the character's default blip.
        - `fade : Optional[Fade]`
            - The frame's fade.
        - `filter : Optional[Filter]`
            - The frame's filter.
        - `transition : Optional[Transition]`
            - The frame's transition.
            - Only applies to wide backgrounds, when the previous frame's background is unchanged.
        - `options : OptionModifiers`
            - Can be used to modify objection options affecting future frames.
        - `hidden : bool`
            - Whether the frame is hidden by default. Only useful in cases. Defaults to False.
        - `caseTag : Optional[str]`
            - A unique tag used to identify the frame in case actions. (A direct reference to the frame object works too)
        - `caseAction : Optional[CaseActions._CaseAction]`
            - The frame's case action.
        - `onCompile : Optional[Callable[[dict], dict]]`
            - A callback for if it's absolutely necessary to access the frame's raw JSON dict upon compilation.
        - `pressSequence : list[Frame]`
            - A sequence of frames played when the testimony statement is pressed.
        - `contradictions : list[tuple[RecordItem, <Frame Target>]]`
            - List of tuples mapping evidence and profiles to present to caseTags/frame references.
    """
    pressSequence: list[Frame] = field(default_factory=list)
    contradictions: list[
            tuple[
                'Case.RecordItem',
                Union[str, 'Frame']
            ]
        ] = field(default_factory=list)


noneCharacter = FrameCharacter(
    assets.Character(None, _loaded=True),
    poseId=0,
    flip=False,
    isActive=False,
    isFront=False,
)
