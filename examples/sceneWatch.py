from objectionpy import preset, enums, assets, objection
from objectionpy.frames import *

projAssets = assets.AssetBank()
scene = objection.Scene(objection.Options(
    dialogueBox = enums.PresetDialogueBox.TRILOGY,
))

projAssets.loadAssetIDs(
    assets.Character,
    {
        'skye': 20566,
        'edgeworth': 308180,
    }
)
projAssets.loadAssetIDs(
    assets.Music,
    {
        'larry 2009': 86956,
    }
)

scene.frames.append(Frame(
    char = FrameCharacter(
        character=projAssets.chars['skye'],
        poseSubstr='confident',
    ),
    text = f"""[#ts50]...[#ts35][#fm]{preset.Sound.Lightbulb}{projAssets.music['larry 2009']}I'm lovin' my new watch!"""
))
scene.frames.append(Frame(
    char = FrameCharacter(
        character=projAssets.chars['edgeworth'],
        poseSubstr='crossed',
        flip=True,
    ),
    text = f"""Mhm[#ts50]..."""
))
scene.frames.append(Frame(
    char = FrameCharacter(
        character=projAssets.chars['skye'],
        poseSubstr='write',
    ),
    text = f"""Just look at this design![#p300] {preset.Sound.Realization}[#fs][#ss][#ts45]So minimalist!.."""
))
scene.frames.append(Frame(
    char = FrameCharacter(
        character=projAssets.chars['edgeworth'],
        poseSubstr='point',
        flip=True,
    ),
    text = f"""[#ts50]...So then,[#p200] [#ts35]what,[#p100] pray tell,[#p100] {preset.Sound.Lightbulb}[#fm]is the time?"""
))
scene.frames.append(Frame(
    char = FrameCharacter(
        character=projAssets.chars['skye'],
        poseSubstr='determined',
    ),
    text = f"""I,[#p200] uhh...[#p400] """,
    merge = True,
    goNext = True,
))
scene.frames.append(Frame(
    char = FrameCharacter(
        character=projAssets.chars['skye'],
        poseSubstr='confident',
    ),
    text = f"""{preset.Sound.Yell}[#fl][#sm]I've got no idea![#p300]"""
))
scene.frames.append(Frame(
    char = FrameCharacter(
        character=projAssets.chars['edgeworth'],
        poseSubstr='damage',
        flip=True,
    ),
    text = f"""[#fl]{preset.Sound.Yell2}[#sm]Then what is the point?!""",
    poseAnim=False,
))

with open('./sceneWatch.objection', 'w') as f:
    f.write(scene.makeObjectionFile(scene.compile()))
