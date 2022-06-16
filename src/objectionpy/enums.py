"""Enums used by the library."""

from enum import Enum


class CharacterLocation(Enum):
    """"""
    DEFENSE = 'defense'
    PROSECUTION = 'prosecution'
    COUNSEL = 'counsel'
    WITNESS = 'witness'
    JUDGE = 'judge'
    GALLERY = 'gallery'


class Easing(Enum):
    """"""
    LINEAR = "linear"
    SPRING = "spring"
    EASE = "ease"
    EASE_IN = "ease-in"
    EASE_OUT = "ease-out"
    EASE_IN_OUT = "ease-in-out"
    EASE_IN_SINE = "ease-in-sine"
    EASE_OUT_SINE = "ease-out-sine"
    EASE_IN_OUT_SINE = "ease-in-out-sine"
    EASE_IN_QUAD = "ease-in-quad"
    EASE_OUT_QUAD = "ease-out-quad"
    EASE_IN_OUT_QUAD = "ease-in-out-quad"
    EASE_IN_CUBIC = "ease-in-cubic"
    EASE_OUT_CUBIC = "ease-out-cubic"
    EASE_IN_OUT_CUBIC = "ease-in-out-cubic"
    EASE_IN_QUART = "ease-in-quart"
    EASE_OUT_QUART = "ease-out-quart"
    EASE_IN_OUT_QUART = "ease-in-out-quart"
    EASE_IN_QUINT = "ease-in-quint"
    EASE_OUT_QUINT = "ease-out-quint"
    EASE_IN_OUT_QUINT = "ease-in-out-quint"
    EASE_IN_EXPONENTIAL = "ease-in-exponential"
    EASE_OUT_EXPONENTIAL = "ease-out-exponential"
    EASE_IN_OUT_EXPONENTIAL = "ease-in-out-exponential"
    EASE_IN_CIRCULAR = "ease-in-circular"
    EASE_OUT_CIRCULAR = "ease-out-circular"
    EASE_IN_OUT_CIRCULAR = "ease-in-out-circular"


class FadeDirection(Enum):
    """"""
    OUT = 0
    IN = 1
    OUT_IN = 2


class FadeTarget(Enum):
    """"""
    BACKGROUND = 0
    CHARACTER = 1
    SCENE = 2
    EVERYTHING = 3
    PAIRED_CHARACTER = 4
    CHARACTERS = 5


class FilterType(Enum):
    """"""
    GRAYSCALE = 'grayscale'
    INVERT = 'invert'
    SEPIA = 'sepia'
    HUE_ROTATE = 'hue-rotate'


class FilterTarget(Enum):
    """"""
    BACKGROUND = 0
    CHARACTERS = 1
    EVERYTHING = 2


class GroupType(Enum):
    """"""
    NORMAL = "n"
    CE = "ce"
    GAME_OVER = "go"


class ObjectionType(Enum):
    """"""
    SCENE = 0
    CASE = 1


class PresetBlip(Enum):
    """"""
    MALE = 1
    FEMALE = 2
    TYPEWRITER = 3
    ECHOING = 4
    KATONK = 5
    MUTE = -1


class PresetDialogueBox(Enum):
    """"""
    CLASSIC = 0
    TRILOGY = 1
    APOLLO_JUSTICE = 2
    AJ = 2
    THE_GREAT_ACE_ATTORNEY = 3
    TGAA = 3


class PresetPopup(Enum):
    """"""
    WITNESS_TESTIMONY = 1
    CROSS_EXAMINATION = 2
    TESTIMONY_LABEL = 3
    GUILTY = 4
    NOT_GUILTY = 5
    TESTIMONY_LABEL_HIDE = -1


class RecordType(Enum):
    """"""
    EVIDENCE = 0
    PROFILE = 1
