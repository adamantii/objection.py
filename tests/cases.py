from objectionpy import preset, enums, assets
from objectionpy.objection import *
from objectionpy.frames import *

case = Case(Options(
    dialogueBox = enums.PresetDialogueBox.TRILOGY,
))

mainGroup = Group(case, 'Main')

case.evidence.append(Case.RecordItem(
    name='Test Evidence',
    type=enums.RecordType.EVIDENCE,
    iconUrl='https://cdn.discordapp.com/attachments/934093239856791602/934306438677934150/act10.png',
    description='Title.',
))
case.profiles.append(Case.RecordItem(
    name='Test Profile',
    type=enums.RecordType.PROFILE,
    iconUrl='https://cdn.discordapp.com/attachments/934093239856791602/934306438677934150/act10.png',
    description="It's great how this test icon works as both evidence and a profile!",
))

thonk = FrameCharacter(
    character=preset.Characters.Defense.PhoenixWright,
    poseSubstr='think',
)

mainGroup.frames.append(Frame(
    char = thonk,
    text = f"""{preset.Music.Trial}This case is a test of objection.lol case features."""
))
mainGroup.frames.append(Frame(
    char = thonk,
    text = f"This frame is meant to be hidden using the 'Hide' feature. If you see this, the 'Hide' feature failed miserably.",
    hidden = True,
))
mainGroup.frames.append(Frame(
    char = thonk,
    text = f"By the way, I suggest checking the court record - it should have a piece of evidence and a profile now."
))
mainGroup.frames.append(Frame(
    char = thonk,
    text = f"Well, this frame should hide the record items.",
    caseAction=CaseActions.ToggleEvidence(
        hide=[case.evidence[0], case.profiles[0]],
    )
))
mainGroup.frames.append(Frame(
    char = thonk,
    text = f"This frame should re-show the record items. Next...",
    caseAction=CaseActions.ToggleEvidence(
        show=[case.evidence[0], case.profiles[0]],
    )
))
mainGroup.frames.append(Frame(
    char = thonk,
    text = f"This frame should hide the next frame. Hopefully you won't see it.",
    caseAction=CaseActions.ToggleFrames(
        hide=['to hide'],
    )
))
mainGroup.frames.append(Frame(
    char = FrameCharacter(
        character=preset.Characters.Defense.PhoenixWright,
        poseSubstr='cornered',
    ),
    text = f"If you see this frame unhidden, then the last case action failed miserably.",
    caseTag = 'to hide',
))

toSkipTo = Frame(
    char = thonk,
    text = f"This is the frame that should have been skipped to. If you didn't see the wrong frame, then the last action succeeded.",
)
mainGroup.frames.append(Frame(
    char = thonk,
    text = f"This frame should skip over the next frame. Hopefully you won't see it either.[#p1000]",
    caseAction=CaseActions.GoToFrame(
        frame=toSkipTo
    )
))
mainGroup.frames.append(Frame(
    char = FrameCharacter(
        character=preset.Characters.Defense.PhoenixWright,
        poseSubstr='cornered',
    ),
    text = f"If you see this frame wrongly unskipped, then the last case action failed miserably.",
))
mainGroup.frames.append(toSkipTo)

mainGroup.frames.append(Frame(
    char = thonk,
    text = f"This frame should set your health to half its value.",
    caseAction=CaseActions.HealthSet(
        amount=0.5
    )
))
mainGroup.frames.append(Frame(
    char = thonk,
    text = f"This frame should recover half of that.",
    caseAction=CaseActions.HealthAdd(
        amount=0.25
    )
))
mainGroup.frames.append(Frame(
    char = thonk,
    text = f"This frame would like to change its mind on the last action.",
    caseAction=CaseActions.HealthRemove(
        amount=0.25
    )
))
mainGroup.frames.append(Frame(
    char = thonk,
    text = f"This frame likes (half) flashy things.",
    caseAction=CaseActions.FlashingHealth(
        amount=0.25
    )
))
mainGroup.frames.append(Frame(
    char = thonk,
    text = f"This frame should ask you to present a really handsome profile.",
    caseTag='present-profile',
    caseAction=CaseActions.PromptPresent(
        failFrame='present-profile-fail',
        choices=[
            (case.profiles[0], 'present-profile-failnt'),
        ],
        presentEvidence=True,
        presentProfiles=True,
    )
))
mainGroup.frames.append(Frame(
    char = FrameCharacter(
        character=preset.Characters.Defense.PhoenixWright,
        poseSubstr='cornered',
    ),
    text = f"You failed that one, huh?[#p200] At least you know the failFrame works.[#p1000]",
    caseTag='present-profile-fail',
    caseAction=CaseActions.GoToFrame(
        frame='present-profile'
    )
))
mainGroup.frames.append(Frame(
    char = thonk,
    text = f"This frame should ask you to present a really handsome piece of evidence. You also shouldn't be able to mess this one up.",
    caseTag='present-profile-failnt',
    caseAction=CaseActions.PromptPresent(
        failFrame='present-evidence-fail',
        choices=[
            (case.evidence[0], 'present-evidence-failnt'),
        ],
        presentEvidence=True,
    )
))
mainGroup.frames.append(Frame(
    char = FrameCharacter(
        character=preset.Characters.Defense.PhoenixWright,
        poseSubstr='cornered',
    ),
    text = f"There actually shouldn't be a way for you to see this one outside of Maker. Huh.[#p1000]",
    caseTag='present-evidence-fail',
    caseAction=CaseActions.GoToFrame(
        frame='present-profile-failnt'
    )
))
mainGroup.frames.append(Frame(
    char = thonk,
    text = f"Of the three options, please choose '1'.",
    caseTag='present-evidence-failnt',
    caseAction=CaseActions.PromptChoice(choices=[
        ('1', 'choice-failnt'),
        ('2', 'present-evidence-failnt'),
        ('3', 'present-evidence-failnt'),
    ])
))
mainGroup.frames.append(Frame(
    char = thonk,
    text = f"Now, pick a number.",
    caseTag='choice-failnt',
    caseAction=CaseActions.PromptInt(
        varName='test'
    )
))
mainGroup.frames.append(Frame(
    char = thonk,
    text = f"Your number was [var:test]. Quite remarkable. Now, type your favorite word.",
    caseAction=CaseActions.PromptStr(
        varName='test',
        allowSpaces=False,
    )
))
mainGroup.frames.append(Frame(
    char = thonk,
    text = f"""The word "[var:test]"?. Quite flamboyant, I must say. Now, type your favorite sentence.""",
    caseAction=CaseActions.PromptStr(
        varName='test',
        toLower=True,
    )
))
mainGroup.frames.append(Frame(
    char = thonk,
    text = f""""[var:test]" was so excessively exuberant, we were forced to lowercase it. Anyway, please point at the odd item in the room.[#p1000][#evd537209]""",
    caseTag='cursor',
    caseAction=CaseActions.PromptCursor(
        previewImageUrl="https://cdn.discordapp.com/attachments/870053209362800651/935489824259981322/unknown.png",
        prompt="Point at the item that's not meant to be there.",
        failFrame="cursor-fail",
        choices=[
            (CursorRect(24, 50, 14, 20), 'cursor-failnt')
        ]
    )
))
mainGroup.frames.append(Frame(
    char = FrameCharacter(
        character=preset.Characters.Defense.PhoenixWright,
        poseSubstr='silly',
    ),
    text = f"""Unfortunately, that object was not the impostor. The crewmates lose.[#p1000]""",
    caseTag='cursor-fail',
    caseAction=CaseActions.GoToFrame(
        frame='cursor'
    )
))
mainGroup.frames.append(Frame(
    char = thonk,
    text = f"""[#evdh]Correct. Moving on from having to actively engage your participation, this frame should simply set the test variable to 5.""",
    caseTag='cursor-failnt',
    caseAction=CaseActions.VarSet(
        varName='test',
        value=5
    )
))
mainGroup.frames.append(Frame(
    char = thonk,
    text = f"""The test variable is now set to: "[var:test]". This frame should add 10 to the test variable.""",
    caseAction=CaseActions.VarAdd(
        varName='test',
        value=10
    )
))
mainGroup.frames.append(Frame(
    char = thonk,
    text = f"""The test variable is now set to: "[var:test]". This frame should now evaluate whether the test variable equals 15 or not.[#p1000]""",
    caseTag='eval',
    caseAction=CaseActions.VarEval(
        expression='test == 15',
        trueFrame='eval-true',
        falseFrame='eval-truent',
    )
))
mainGroup.frames.append(Frame(
    char = thonk,
    text = f"""Evaluation: the test variable equals 15.""",
    caseTag='eval-true',
    caseAction=CaseActions.VarAdd(
        varName='test',
        value=5
    )
))
mainGroup.frames.append(Frame(
    char = thonk,
    text = f"""However, that last frame added 5 more to it. Now let us rewind back a couple steps.[#p1000]""",
    caseAction=CaseActions.GoToFrame(
        frame='eval'
    )
))

goGroupFake = GameOverGroup(case, 'Fake Game Over')
goGroupFake.frames.append(Frame(
    char = FrameCharacter(
        character=preset.Characters.Defense.PhoenixWright,
        poseSubstr='silly',
    ),
    text = """This is the wrong game over group. If you're reading this, the last action failed miserably."""
))
goGroupReal = GameOverGroup(case, 'Real Game Over')

mainGroup.frames.append(Frame(
    char = thonk,
    text = f"""Evaluation: the test variable no longer equals 15. Now, this frame should change the game over group.""",
    caseTag='eval-truent',
    caseAction=CaseActions.SetGameOverGroup(
        group=goGroupReal
    )
))

mainGroup.frames.append(Frame(
    char = FrameCharacter(
        character=preset.Characters.Defense.PhoenixWright,
        poseSubstr='read',
    ),
    text = f"""To test that, a second demonstration of the health-setting action will be shown as your health will be demolished.[#p1000]""",
    caseAction=CaseActions.HealthSet(
        amount=0
    )
))

goGroupReal.frames.append(Frame(
    char = thonk,
    text = """This is the correct game over group. The last action succeeded."""
))
goGroupReal.frames.append(Frame(
    char = thonk,
    text = """Now, we will test cross-examination groups."""
))
goGroupReal.frames.append(Frame(
    char = thonk,
    text = """[#/r]Cross-examination[/#]""",
    presetPopup=enums.PresetPopup.CROSS_EXAMINATION,
    centerText=True,
    options=OptionModifiers(
        dialogueBoxVisible=False,
    ),
))
goGroupReal.frames.append(Frame(
    char = thonk,
    caseAction=CaseActions.GoToFrame('cross-exam')
))

ceGroup = CEGroup(case)
ceGroup.frames.append(CEFrame(
    char = thonk,
    text = """This is the first half of the testimony.""",
    caseTag='cross-exam',
    pressSequence=[
        Frame(
            char = thonk,
            text = """This is a test press frame.""",
            bubble=preset.SpeechBubbles.HoldIt,
        )
    ],
))
ceGroup.frames.append(CEFrame(
    char = thonk,
    text = """This is the second half of the testimony.""",
    pressSequence=[
        Frame(
            char = thonk,
            text = """You should present the profile on this second statement.""",
            bubble=preset.SpeechBubbles.HoldIt,
        )
    ],
    contradictions=[
        (case.profiles[0], 'cross-exam-contra')
    ],
))

ceGroup.counselSequence.append(Frame(
    char = thonk,
    text = """This is a test counsel frame.""",
))
ceGroup.failureSequence.append(Frame(
    char = thonk,
    text = """This is a test failure frame.""",
    bubble=preset.SpeechBubbles.Objection,
))

goGroupReal.frames.append(Frame(
    char = thonk,
    text = """Good job, you have found the contradiction.""",
    bubble=preset.SpeechBubbles.Objection,
    caseTag='cross-exam-contra',
))
goGroupReal.frames.append(Frame(
    char = FrameCharacter(
        character=preset.Characters.Defense.PhoenixWright,
        poseSubstr='stand',
    ),
    text = """Now,[#p500] for the final case action,[#p500] this frame should end this case.""",
    caseAction=CaseActions.EndGame()
))
goGroupReal.frames.append(Frame(
    char = FrameCharacter(
        character=preset.Characters.Defense.PhoenixWright,
        poseSubstr='silly',
    ),
    text = """The case should have ended by now. If you're reading this, the last action failed miserably.""",
))

with open('./cases.objection', 'w') as f:
    f.write(case.makeObjectionFile(case.compile()))
