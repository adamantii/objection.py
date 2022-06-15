# Objection.py

A modular library for creating [objection.lol](https://objection.lol/maker) projects beyond what's possible manually.

## Overview

The .objection format is good for distribution, but doesn't work as well for production or automation.

This library focuses on providing helpful IDE suggestions, simple readability, and a class-based structure making up every piece of an objection. This structure can then compile to objection.lol's complicated JSON format.

This way, complex objections with gameplay systems that use large amounts of repetitive actions become simple to generate.

```py
scene = Scene()
scene.frames.append(Frame(
    char = FrameCharacter(
        character = preset.Characters.Defense.PhoenixWright,
        poseSubstr = 'Point',
        pairOffset = (-20, 0),
    ),
    pairChar = FrameCharacter(
        character = preset.Characters.Defense.MiaFey,
        poseSubstr = 'Point',
        pairOffset = (20, 0),
    ),
    fade = Fade(
        direction = FadeDirection.OUT,
        target = FadeTarget.BACKGROUND,
        duration = 1000,
        color = Color('#000'),
    ),
    text = f'{preset.Sound.Yell}Objection!',
))
scene.compile()
```

## Installation

Installing objection.py with pip:
```
pip install objectionpy
```

## Documentation

[View the documentation page](https://adamantii.github.io/objection.py/)

## TODO

- Complete: galleryAssign option for custom characters
- Complete: improve tests for scene features and for objection JSON loading
