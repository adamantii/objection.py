"""
Stores all preset objection.lol assets for easy access.

All asset names were converted into alphanumeric CamelCase.
"""

from . import assets, enums


_defaultBackgrounds = {
    'classic': {
        enums.CharacterLocation.DEFENSE: 189,
        enums.CharacterLocation.PROSECUTION: 194,
        enums.CharacterLocation.COUNSEL: 187,
        enums.CharacterLocation.WITNESS: 197,
        enums.CharacterLocation.JUDGE: 192,
        enums.CharacterLocation.GALLERY: 9,
    },
    'aj': {
        enums.CharacterLocation.DEFENSE: 177,
        enums.CharacterLocation.PROSECUTION: 182,
        enums.CharacterLocation.COUNSEL: 175,
        enums.CharacterLocation.WITNESS: 186,
        enums.CharacterLocation.JUDGE: 178,
        enums.CharacterLocation.GALLERY: 16,
    },
}

_blips = {
    'male': '/Audio/blip.wav',
    'female': '/Audio/blip-female.wav',
}


def _speechBubble(id: int, name: str, sound: str = ''):
    return {
        'id': id,
        'name': name,
        'soundUrl': sound,
        'imageUrl': 'https://objection.lol/Images/Bubbles/' + str(id) + '.png',
        'order': 0,
        'shake': True,
        'duration': 0,
    }


def _builtinCharacter(
    id: int,
    name: str,
    namePlate: str,
    blipUrl: str,
    side: enums.CharacterLocation,
    backgroundStyle: dict[enums.CharacterLocation, int],
    gallery: str,
    poses: list,
    customBubbles: dict[str, str] = {},
) -> assets.Character:
    character = assets.Character(id, _loaded=True)

    character.name = name
    character.namePlate = namePlate
    character.poses = poses
    character.blipUrl = blipUrl

    character.side = side
    character.backgroundId = backgroundStyle[side]
    if backgroundStyle is _defaultBackgrounds['aj']:
        character._aj = True
        character.galleryAJImageUrl = gallery
    else:
        character.galleryImageUrl = gallery
    character.bubbles = [
        _speechBubble(1, 'Objection!', ''),
        _speechBubble(2, 'Hold It!', ''),
        _speechBubble(3, 'Take That!', ''),
    ]
    for bubbleId, soundUrl in sorted(customBubbles.items()):
        bubbleId = int(bubbleId)
        bubbleIndex = -1
        for i, bubble in enumerate(character.bubbles):
            if bubble['id'] == bubbleId:
                bubbleIndex = i
                break
        if bubbleIndex == -1:
            character.bubbles.append(_speechBubble(
                bubbleId, 'Gotcha!' if bubbleId == 4 else 'Eureka!' if bubbleId == 5 else 'Unknown Speech', ''))
        character.bubbles[bubbleIndex]['soundUrl'] = soundUrl

    return character


def collectionValues(collection: type) -> list:
    """
    Get all values in an asset collection class.

    If the class has nested classes, it retrieves assets from the nested classes.

    Args:
        - `collection : type`
            - Class containing pre-set assets to be retrieved.

    Returns:
        List of assets in the collection class.
    """
    values = []
    for key, value in collection.__dict__.items():
        if key[:2] == '__':
            continue
        elif type(value) is type:
            values += collectionValues(value)
        else:
            values.append(value)
    return values


class Characters:
    class Defense:
        PhoenixWright = _builtinCharacter(
            1,
            "Phoenix Wright",
            "Phoenix",
            _blips['male'],
            enums.CharacterLocation.DEFENSE,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/1.png",
            [
                {
                    "id": 1,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/1/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/1/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/1.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 1
                },
                {
                    "id": 2,
                    "name": "Desk Slam",
                    "idleImageUrl": "https://objection.lol/Images/Characters/1/Slam_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/1/Slam_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/2.png",
                    "order": 0,
                    "musicFileName": "truth2002",
                    "states": [
                        {
                            "imageUrl": "Slam",
                            "nextPoseDelay": 1100
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "deskslam",
                            "time": 175,
                            "volume": 1
                        }
                    ],
                    "functionTicks": [],
                    "characterId": 1
                },
                {
                    "id": 3,
                    "name": "Point",
                    "idleImageUrl": "https://objection.lol/Images/Characters/1/Point_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/1/Point_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/3.png",
                    "order": 0,
                    "musicFileName": "cornered",
                    "states": [
                        {
                            "imageUrl": "Point_Start",
                            "nextPoseDelay": 500,
                            "speakDelay": 150
                        }
                    ],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 1
                },
                {
                    "id": 4,
                    "name": "Confident",
                    "idleImageUrl": "https://objection.lol/Images/Characters/1/Smirk_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/1/Smirk_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/4.png",
                    "order": 0,
                    "musicFileName": "objection2004",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 1
                },
                {
                    "id": 33,
                    "name": "Thinking",
                    "idleImageUrl": "https://objection.lol/Images/Characters/1/Think_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/1/Think_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/33.png",
                    "order": 0,
                    "musicFileName": "trial2",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 1
                },
                {
                    "id": 34,
                    "name": "Cornered",
                    "idleImageUrl": "https://objection.lol/Images/Characters/1/Cornered.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/1/Cornered_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/34.png",
                    "order": 0,
                    "musicFileName": "allegro2004",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 1
                },
                {
                    "id": 35,
                    "name": "Silly",
                    "idleImageUrl": "https://objection.lol/Images/Characters/1/Silly_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/1/Silly_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/35.png",
                    "order": 0,
                    "musicFileName": "trial2",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 1
                },
                {
                    "id": 59,
                    "name": "Read",
                    "idleImageUrl": "https://objection.lol/Images/Characters/1/Read_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/1/Read_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/59.png",
                    "order": 0,
                    "musicFileName": "objection",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 1
                },
                {
                    "id": 76,
                    "name": "Sip Mug",
                    "idleImageUrl": "https://objection.lol/Images/Characters/1/Sip_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/1/Sip_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/76.png",
                    "order": 0,
                    "musicFileName": "truth2007",
                    "states": [
                        {
                            "imageUrl": "Sip_Stand",
                            "nextPoseDelay": 300
                        },
                        {
                            "imageUrl": "Sip",
                            "nextPoseDelay": 1000
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "chug",
                            "time": 500,
                            "volume": 1
                        }
                    ],
                    "functionTicks": [],
                    "characterId": 1
                },
                {
                    "id": 100,
                    "name": "Nod",
                    "idleImageUrl": "https://objection.lol/Images/Characters/1/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/1/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/100.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [
                        {
                            "imageUrl": "Nod",
                            "nextPoseDelay": 675
                        }
                    ],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 1
                },
                {
                    "id": 101,
                    "name": "Headshake",
                    "idleImageUrl": "https://objection.lol/Images/Characters/1/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/1/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/101.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [
                        {
                            "imageUrl": "Headshake",
                            "nextPoseDelay": 875
                        }
                    ],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 1
                },
                {
                    "id": 129,
                    "name": "Damage",
                    "idleImageUrl": "https://objection.lol/Images/Characters/1/Cornered.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/1/Cornered_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/129.png",
                    "order": 0,
                    "musicFileName": "truth2001",
                    "states": [
                        {
                            "imageUrl": "Damage",
                            "nextPoseDelay": 1075
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "damage",
                            "time": 100,
                            "volume": 0.8
                        }
                    ],
                    "functionTicks": [
                        {
                            "functionName": "Flash",
                            "functionParam": "m",
                            "time": 100
                        }
                    ],
                    "characterId": 1
                },
                {
                    "id": 406,
                    "name": "Damage (custom)",
                    "idleImageUrl": "https://objection.lol/Images/Characters/1/Damage.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/1/Damage.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/406.png",
                    "order": 0,
                    "musicFileName": "truth2001",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 1
                },
                {
                    "id": 140,
                    "name": "Breakdown",
                    "idleImageUrl": "https://objection.lol/Images/Characters/1/Breakdown.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/1/Breakdown.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/140.png",
                    "order": 0,
                    "musicFileName": "truth2001",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 1
                },
                {
                    "id": 188,
                    "name": "Coffee Stained",
                    "idleImageUrl": "https://objection.lol/Images/Characters/1/Coffee_Stained_Idle.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/1/Coffee_Stained_Idle.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/188.png",
                    "order": 0,
                    "musicFileName": "darkcoffee",
                    "states": [
                        {
                            "imageUrl": "Coffee_Stained",
                            "nextPoseDelay": 1200
                        }
                    ],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 1
                },
                {
                    "id": 271,
                    "name": "Yell",
                    "idleImageUrl": "https://objection.lol/Images/Characters/1/Yell_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/1/Yell_Talk.gif",
                    "isSpeedlines": True,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/271.png",
                    "order": 0,
                    "musicFileName": "truth2001",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 1
                },
                {
                    "id": 358,
                    "name": "Hair Stained",
                    "idleImageUrl": "https://objection.lol/Images/Characters/1/Hair_Stained.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/1/Hair_Stained.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/358.png",
                    "order": 0,
                    "musicFileName": "moderato2001",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 1
                },
                {
                    "id": 519,
                    "name": "Super Objection",
                    "idleImageUrl": "https://objection.lol/Images/Characters/1/Super.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/1/Super.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/519.png",
                    "order": 0,
                    "musicFileName": "cornered2004 - pursuit",
                    "states": [
                        {
                            "imageUrl": "Super",
                            "nextPoseDelay": 4400,
                            "speakDelay": 4400
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "objection_super",
                            "time": 1,
                            "volume": 0.9
                        }
                    ],
                    "functionTicks": [],
                    "characterId": 1
                }
            ],
            {
                "1": "https://objection.lol/Audio/Vocal/1/1.mp3",
                "2": "https://objection.lol/Audio/Vocal/2/1.mp3",
                "3": "https://objection.lol/Audio/Vocal/3/1.mp3"
            }
        )
        MiaFey = _builtinCharacter(
            4,
            "Mia Fey",
            "Mia",
            _blips['female'],
            enums.CharacterLocation.DEFENSE,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/4.png",
            [
                {
                    "id": 15,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/4/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/4/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/15.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 4
                },
                {
                    "id": 16,
                    "name": "Desk Slam",
                    "idleImageUrl": "https://objection.lol/Images/Characters/4/Desk_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/4/Desk_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/16.png",
                    "order": 0,
                    "musicFileName": "objection",
                    "states": [
                        {
                            "imageUrl": "Slam",
                            "nextPoseDelay": 400
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "deskslam",
                            "time": 50,
                            "volume": 1
                        }
                    ],
                    "functionTicks": [],
                    "characterId": 4
                },
                {
                    "id": 17,
                    "name": "Point",
                    "idleImageUrl": "https://objection.lol/Images/Characters/4/Point_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/4/Point_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/17.png",
                    "order": 0,
                    "musicFileName": "crossexamining",
                    "states": [
                        {
                            "imageUrl": "Special_2",
                            "nextPoseDelay": 500,
                            "speakDelay": 150
                        }
                    ],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 4
                },
                {
                    "id": 18,
                    "name": "Confident",
                    "idleImageUrl": "https://objection.lol/Images/Characters/4/Confident.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/4/Confident_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/18.png",
                    "order": 0,
                    "musicFileName": "crossexaminingvariation",
                    "states": [
                        {
                            "imageUrl": "Special_1",
                            "nextPoseDelay": 1500
                        }
                    ],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 4
                },
                {
                    "id": 38,
                    "name": "Thinking",
                    "idleImageUrl": "https://objection.lol/Images/Characters/4/Think_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/4/Think_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/38.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 4
                },
                {
                    "id": 39,
                    "name": "Cornered",
                    "idleImageUrl": "https://objection.lol/Images/Characters/4/Cornered.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/4/Cornered_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/39.png",
                    "order": 0,
                    "musicFileName": "allegro2001",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 4
                },
                {
                    "id": 244,
                    "name": "Damage",
                    "idleImageUrl": "https://objection.lol/Images/Characters/4/Damage.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/4/Damage.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/244.png",
                    "order": 0,
                    "musicFileName": "allegro2001",
                    "states": [
                        {
                            "imageUrl": "Damage",
                            "nextPoseDelay": 1
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "yell2",
                            "time": 25,
                            "volume": 0.9
                        }
                    ],
                    "functionTicks": [
                        {
                            "functionName": "Flash",
                            "functionParam": "s",
                            "time": 25
                        },
                        {
                            "functionName": "Shake",
                            "functionParam": "s",
                            "time": 25
                        }
                    ],
                    "characterId": 4
                },
                {
                    "id": 409,
                    "name": "Damage (custom)",
                    "idleImageUrl": "https://objection.lol/Images/Characters/4/Damage.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/4/Damage.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/409.png",
                    "order": 0,
                    "musicFileName": "allegro2001",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 4
                },
                {
                    "id": 273,
                    "name": "Yell",
                    "idleImageUrl": "https://objection.lol/Images/Characters/4/Yell_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/4/Yell_Talk.gif",
                    "isSpeedlines": True,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/273.png",
                    "order": 0,
                    "musicFileName": "truth2001",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 4
                }
            ],
            {
                "1": "https://objection.lol/Audio/Vocal/1/4.mp3",
                "2": "https://objection.lol/Audio/Vocal/2/4.mp3",
                "3": "https://objection.lol/Audio/Vocal/3/4.mp3"
            }
        )
        ApolloJustice = _builtinCharacter(
            11,
            "Apollo Justice",
            "Apollo",
            _blips['male'],
            enums.CharacterLocation.DEFENSE,
            _defaultBackgrounds['aj'],
            "https://objection.lol/Images/Gallery/11.png",
            [
                {
                    "id": 60,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/11/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/11/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/60.png",
                    "order": 0,
                    "musicFileName": "trial4",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 11
                },
                {
                    "id": 55,
                    "name": "Confident",
                    "idleImageUrl": "https://objection.lol/Images/Characters/11/Confident.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/11/Confident_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/55.png",
                    "order": 0,
                    "musicFileName": "truth2007",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 11
                },
                {
                    "id": 402,
                    "name": "Smile",
                    "idleImageUrl": "https://objection.lol/Images/Characters/11/Smile.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/11/Confident_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/402.png",
                    "order": 0,
                    "musicFileName": "truth2007",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 11
                },
                {
                    "id": 56,
                    "name": "Silly (eyes closed)",
                    "idleImageUrl": "https://objection.lol/Images/Characters/11/Silly.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/11/Silly_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/56.png",
                    "order": 0,
                    "musicFileName": "trial5",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 11
                },
                {
                    "id": 403,
                    "name": "Silly",
                    "idleImageUrl": "https://objection.lol/Images/Characters/11/Silly2.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/11/Silly2_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/403.png",
                    "order": 0,
                    "musicFileName": "trial5",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 11
                },
                {
                    "id": 57,
                    "name": "Desk slam",
                    "idleImageUrl": "https://objection.lol/Images/Characters/11/Slam_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/11/Slam_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/57.png",
                    "order": 0,
                    "musicFileName": "objection2007",
                    "states": [
                        {
                            "imageUrl": "Slam",
                            "nextPoseDelay": 950
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "deskslam",
                            "time": 150,
                            "volume": 1
                        }
                    ],
                    "functionTicks": [],
                    "characterId": 11
                },
                {
                    "id": 58,
                    "name": "Read",
                    "idleImageUrl": "https://objection.lol/Images/Characters/11/Read.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/11/Read_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/58.png",
                    "order": 0,
                    "musicFileName": "moderato2007",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 11
                },
                {
                    "id": 61,
                    "name": "Point",
                    "idleImageUrl": "https://objection.lol/Images/Characters/11/Point_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/11/Point_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/61.png",
                    "order": 0,
                    "musicFileName": "cornered2007",
                    "states": [
                        {
                            "imageUrl": "Point",
                            "nextPoseDelay": 700,
                            "speakDelay": 400
                        }
                    ],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 11
                },
                {
                    "id": 62,
                    "name": "Cornered",
                    "idleImageUrl": "https://objection.lol/Images/Characters/11/Cornered.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/11/Cornered_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/62.png",
                    "order": 0,
                    "musicFileName": "trial4",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 11
                },
                {
                    "id": 63,
                    "name": "Think",
                    "idleImageUrl": "https://objection.lol/Images/Characters/11/Think.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/11/Think_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/63.png",
                    "order": 0,
                    "musicFileName": "moderato2007",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 11
                },
                {
                    "id": 415,
                    "name": "Think (eyes closed)",
                    "idleImageUrl": "https://objection.lol/Images/Characters/11/Think2.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/11/Think2_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/415.png",
                    "order": 0,
                    "musicFileName": "moderato2007",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 11
                },
                {
                    "id": 404,
                    "name": "Damage",
                    "idleImageUrl": "https://objection.lol/Images/Characters/11/Damage.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/11/Damage.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/404.png",
                    "order": 0,
                    "musicFileName": "allegro2007",
                    "states": [
                        {
                            "imageUrl": "Damage",
                            "nextPoseDelay": 1
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "damage",
                            "time": 50,
                            "volume": 0.85
                        }
                    ],
                    "functionTicks": [
                        {
                            "functionName": "Flash",
                            "functionParam": "m"
                        }
                    ],
                    "characterId": 11
                },
                {
                    "id": 405,
                    "name": "Damage (custom)",
                    "idleImageUrl": "https://objection.lol/Images/Characters/11/Damage.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/11/Damage.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/405.png",
                    "order": 0,
                    "musicFileName": "allegro2007",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 11
                },
                {
                    "id": 416,
                    "name": "Yell",
                    "idleImageUrl": "https://objection.lol/Images/Characters/11/Yell.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/11/Yell_Talk.gif",
                    "isSpeedlines": True,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/416.png",
                    "order": 0,
                    "musicFileName": "cornered2007",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 11
                }
            ],
            {
                "1": "https://objection.lol/Audio/Vocal/1/11.mp3",
                "2": "https://objection.lol/Audio/Vocal/2/11.mp3",
                "3": "https://objection.lol/Audio/Vocal/3/11.mp3",
                "4": "https://objection.lol/Audio/Vocal/4/11.mp3"
            }
        )
        MilesEdgeworthDefense = _builtinCharacter(
            94,
            "Miles Edgeworth (defense)",
            "Edgeworth",
            _blips['male'],
            enums.CharacterLocation.DEFENSE,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/94.png",
            [
                {
                    "id": 690,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/94/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/94/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/690.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 94
                },
                {
                    "id": 691,
                    "name": "Desk Slam",
                    "idleImageUrl": "https://objection.lol/Images/Characters/94/Desk_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/94/Desk_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/691.png",
                    "order": 0,
                    "musicFileName": "crossexamining",
                    "states": [
                        {
                            "imageUrl": "Desk_Slam",
                            "nextPoseDelay": 600
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "deskslam",
                            "time": 250,
                            "volume": 1
                        }
                    ],
                    "functionTicks": [],
                    "characterId": 94
                },
                {
                    "id": 692,
                    "name": "Point",
                    "idleImageUrl": "https://objection.lol/Images/Characters/94/Point_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/94/Point_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/692.png",
                    "order": 0,
                    "musicFileName": "cornered",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 94
                },
                {
                    "id": 693,
                    "name": "Arms Crossed",
                    "idleImageUrl": "https://objection.lol/Images/Characters/94/Arms_Crossed.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/94/Arms_Crossed_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/693.png",
                    "order": 0,
                    "musicFileName": "trial2",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 94
                },
                {
                    "id": 694,
                    "name": "Confident Shrug",
                    "idleImageUrl": "https://objection.lol/Images/Characters/94/Confident.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/94/Confident_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/694.png",
                    "order": 0,
                    "musicFileName": "objection2004",
                    "states": [
                        {
                            "imageUrl": "Special_2",
                            "nextPoseDelay": 1300
                        }
                    ],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 94
                },
                {
                    "id": 695,
                    "name": "Cornered",
                    "idleImageUrl": "https://objection.lol/Images/Characters/94/Cornered.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/94/Cornered_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/695.png",
                    "order": 0,
                    "musicFileName": "truth2001",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 94
                },
                {
                    "id": 696,
                    "name": "Confident Smirk",
                    "idleImageUrl": "https://objection.lol/Images/Characters/94/Confident.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/94/Confident_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/696.png",
                    "order": 0,
                    "musicFileName": "crossexamining",
                    "states": [
                        {
                            "imageUrl": "Special_1",
                            "nextPoseDelay": 1900
                        }
                    ],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 94
                },
                {
                    "id": 697,
                    "name": "Smirk",
                    "idleImageUrl": "https://objection.lol/Images/Characters/94/Special_1.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/94/Special_1.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/697.png",
                    "order": 0,
                    "musicFileName": "crossexamining",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 94
                },
                {
                    "id": 698,
                    "name": "Read",
                    "idleImageUrl": "https://objection.lol/Images/Characters/94/Read.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/94/Read_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/698.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 94
                },
                {
                    "id": 699,
                    "name": "Damage",
                    "idleImageUrl": "https://objection.lol/Images/Characters/94/Cornered.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/94/Cornered_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/699.png",
                    "order": 0,
                    "musicFileName": "truth2001",
                    "states": [
                        {
                            "imageUrl": "Damage",
                            "nextPoseDelay": 500
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "damage",
                            "time": 100,
                            "volume": 0.7
                        }
                    ],
                    "functionTicks": [
                        {
                            "functionName": "Shake",
                            "functionParam": "s",
                            "time": 50
                        },
                        {
                            "functionName": "Flash",
                            "functionParam": "m",
                            "time": 300
                        }
                    ],
                    "characterId": 94
                },
                {
                    "id": 700,
                    "name": "Damage (custom)",
                    "idleImageUrl": "https://objection.lol/Images/Characters/94/Damage.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/94/Damage.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/700.png",
                    "order": 0,
                    "musicFileName": "truth2001",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 94
                },
                {
                    "id": 701,
                    "name": "Yell",
                    "idleImageUrl": "https://objection.lol/Images/Characters/94/Yell_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/94/Yell_Talk.gif",
                    "isSpeedlines": True,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/701.png",
                    "order": 0,
                    "musicFileName": "truth2001",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 94
                }
            ],
            {
                "1": "https://objection.lol/Audio/Vocal/1/94.mp3",
                "2": "https://objection.lol/Audio/Vocal/2/94.mp3",
                "3": "https://objection.lol/Audio/Vocal/3/94.mp3",
                "5": "https://objection.lol/Audio/Vocal/5/94.mp3"
            }
        )

    class Prosecution:
        MilesEdgeworth = _builtinCharacter(
            2,
            "Miles Edgeworth",
            "Edgeworth",
            _blips['male'],
            enums.CharacterLocation.PROSECUTION,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/2.png",
            [
                {
                    "id": 5,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/2/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/2/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/5.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 2
                },
                {
                    "id": 6,
                    "name": "Desk Slam",
                    "idleImageUrl": "https://objection.lol/Images/Characters/2/Desk_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/2/Desk_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/6.png",
                    "order": 0,
                    "musicFileName": "crossexamining",
                    "states": [
                        {
                            "imageUrl": "Desk_Slam",
                            "nextPoseDelay": 600
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "deskslam",
                            "time": 250,
                            "volume": 1
                        }
                    ],
                    "functionTicks": [],
                    "characterId": 2
                },
                {
                    "id": 7,
                    "name": "Point",
                    "idleImageUrl": "https://objection.lol/Images/Characters/2/Point_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/2/Point_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/7.png",
                    "order": 0,
                    "musicFileName": "cornered",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 2
                },
                {
                    "id": 8,
                    "name": "Arms Crossed",
                    "idleImageUrl": "https://objection.lol/Images/Characters/2/Arms_Crossed.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/2/Arms_Crossed_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/8.png",
                    "order": 0,
                    "musicFileName": "trial2",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 2
                },
                {
                    "id": 9,
                    "name": "Confident Shrug",
                    "idleImageUrl": "https://objection.lol/Images/Characters/2/Confident.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/2/Confident_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/9.png",
                    "order": 0,
                    "musicFileName": "objection2004",
                    "states": [
                        {
                            "imageUrl": "Special_2",
                            "nextPoseDelay": 1300
                        }
                    ],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 2
                },
                {
                    "id": 36,
                    "name": "Cornered",
                    "idleImageUrl": "https://objection.lol/Images/Characters/2/Cornered.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/2/Cornered_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/36.png",
                    "order": 0,
                    "musicFileName": "truth2001",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 2
                },
                {
                    "id": 47,
                    "name": "Confident Smirk",
                    "idleImageUrl": "https://objection.lol/Images/Characters/2/Confident.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/2/Confident_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/47.png",
                    "order": 0,
                    "musicFileName": "crossexamining",
                    "states": [
                        {
                            "imageUrl": "Special_1",
                            "nextPoseDelay": 1900
                        }
                    ],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 2
                },
                {
                    "id": 185,
                    "name": "Smirk",
                    "idleImageUrl": "https://objection.lol/Images/Characters/2/Special_1.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/2/Special_1.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/185.png",
                    "order": 0,
                    "musicFileName": "crossexamining",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 2
                },
                {
                    "id": 89,
                    "name": "Read",
                    "idleImageUrl": "https://objection.lol/Images/Characters/2/Read.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/2/Read_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/89.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 2
                },
                {
                    "id": 90,
                    "name": "Damage",
                    "idleImageUrl": "https://objection.lol/Images/Characters/2/Cornered.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/2/Cornered_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/90.png",
                    "order": 0,
                    "musicFileName": "truth2001",
                    "states": [
                        {
                            "imageUrl": "Damage",
                            "nextPoseDelay": 500
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "damage",
                            "time": 100,
                            "volume": 0.7
                        }
                    ],
                    "functionTicks": [
                        {
                            "functionName": "Shake",
                            "functionParam": "s",
                            "time": 50
                        },
                        {
                            "functionName": "Flash",
                            "functionParam": "m",
                            "time": 300
                        }
                    ],
                    "characterId": 2
                },
                {
                    "id": 407,
                    "name": "Damage (custom)",
                    "idleImageUrl": "https://objection.lol/Images/Characters/2/Damage.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/2/Damage.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/407.png",
                    "order": 0,
                    "musicFileName": "truth2001",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 2
                },
                {
                    "id": 189,
                    "name": "Bow",
                    "idleImageUrl": "https://objection.lol/Images/Characters/2/Bow_Idle.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/2/Bow_Idle.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/189.png",
                    "order": 0,
                    "musicFileName": "truth2002",
                    "states": [
                        {
                            "imageUrl": "Bow",
                            "nextPoseDelay": 450
                        }
                    ],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 2
                },
                {
                    "id": 272,
                    "name": "Yell",
                    "idleImageUrl": "https://objection.lol/Images/Characters/2/Yell_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/2/Yell_Talk.gif",
                    "isSpeedlines": True,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/272.png",
                    "order": 0,
                    "musicFileName": "truth2001",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 2
                }
            ],
            {
                "1": "https://objection.lol/Audio/Vocal/1/2.mp3",
                "2": "https://objection.lol/Audio/Vocal/2/2.mp3",
                "3": "https://objection.lol/Audio/Vocal/3/2.mp3",
                "5": "https://objection.lol/Audio/Vocal/5/2.mp3"
            }
        )
        MilesEdgeworthYoung = _builtinCharacter(
            3,
            "Miles Edgeworth (young)",
            "Edgeworth",
            _blips['male'],
            enums.CharacterLocation.PROSECUTION,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/3.png",
            [
                {
                    "id": 10,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/3/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/3/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/10.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 3
                },
                {
                    "id": 11,
                    "name": "Desk Slam",
                    "idleImageUrl": "https://objection.lol/Images/Characters/3/Desk_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/3/Desk_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/11.png",
                    "order": 0,
                    "musicFileName": "crossexamining",
                    "states": [
                        {
                            "imageUrl": "Desk_Slam",
                            "nextPoseDelay": 500
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "deskslam",
                            "time": 100,
                            "volume": 1
                        }
                    ],
                    "functionTicks": [],
                    "characterId": 3
                },
                {
                    "id": 12,
                    "name": "Point",
                    "idleImageUrl": "https://objection.lol/Images/Characters/3/Point_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/3/Point_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/12.png",
                    "order": 0,
                    "musicFileName": "truth2002",
                    "states": [
                        {
                            "imageUrl": "Special_1",
                            "nextPoseDelay": 1100
                        }
                    ],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 3
                },
                {
                    "id": 13,
                    "name": "Arms Crossed",
                    "idleImageUrl": "https://objection.lol/Images/Characters/3/Arms_Crossed.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/3/Arms_Crossed_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/13.png",
                    "order": 0,
                    "musicFileName": "trial2",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 3
                },
                {
                    "id": 14,
                    "name": "Confident",
                    "idleImageUrl": "https://objection.lol/Images/Characters/3/Confident_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/3/Confident_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/14.png",
                    "order": 0,
                    "musicFileName": "crossexaminingvariation",
                    "states": [
                        {
                            "imageUrl": "Special_2",
                            "nextPoseDelay": 1300
                        }
                    ],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 3
                },
                {
                    "id": 37,
                    "name": "Cornered",
                    "idleImageUrl": "https://objection.lol/Images/Characters/3/Cornered.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/3/Cornered_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/37.png",
                    "order": 0,
                    "musicFileName": "objection2004",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 3
                },
                {
                    "id": 141,
                    "name": "Damage",
                    "idleImageUrl": "https://objection.lol/Images/Characters/3/Cornered.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/3/Cornered_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/141.png",
                    "order": 0,
                    "musicFileName": "objection2004",
                    "states": [
                        {
                            "imageUrl": "Stand",
                            "nextPoseDelay": 250
                        },
                        {
                            "imageUrl": "Damage",
                            "nextPoseDelay": 800
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "damage",
                            "time": 200,
                            "volume": 0.8
                        }
                    ],
                    "functionTicks": [
                        {
                            "functionName": "Shake",
                            "functionParam": "s",
                            "time": 200
                        },
                        {
                            "functionName": "Flash",
                            "functionParam": "s",
                            "time": 195
                        },
                        {
                            "functionName": "Flash",
                            "functionParam": "s",
                            "time": 1000
                        }
                    ],
                    "characterId": 3
                },
                {
                    "id": 408,
                    "name": "Damage (custom)",
                    "idleImageUrl": "https://objection.lol/Images/Characters/3/Damage.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/3/Damage.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/408.png",
                    "order": 0,
                    "musicFileName": "objection2004",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 3
                }
            ],
            {
                "1": "https://objection.lol/Audio/Vocal/1/3.mp3",
                "2": "https://objection.lol/Audio/Vocal/2/3.mp3",
                "3": "https://objection.lol/Audio/Vocal/3/3.mp3",
                "5": "https://objection.lol/Audio/Vocal/5/3.mp3"
            }
        )
        WinstonPayne = _builtinCharacter(
            6,
            "Winston Payne",
            "Payne",
            _blips['male'],
            enums.CharacterLocation.PROSECUTION,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/6.png",
            [
                {
                    "id": 19,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/6/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/6/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/19.png",
                    "order": 0,
                    "musicFileName": "trial2",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 6
                },
                {
                    "id": 20,
                    "name": "Confident",
                    "idleImageUrl": "https://objection.lol/Images/Characters/6/Confident_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/6/Confident_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/20.png",
                    "order": 0,
                    "musicFileName": "truth2002",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 6
                },
                {
                    "id": 40,
                    "name": "Cornered",
                    "idleImageUrl": "https://objection.lol/Images/Characters/6/Cornered.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/6/Cornered_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/40.png",
                    "order": 0,
                    "musicFileName": "objection",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 6
                },
                {
                    "id": 190,
                    "name": "Damage",
                    "idleImageUrl": "https://objection.lol/Images/Characters/6/Damage.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/6/Damage.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/190.png",
                    "order": 0,
                    "musicFileName": "objection",
                    "states": [
                        {
                            "imageUrl": "Damage",
                            "nextPoseDelay": 1
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "damage",
                            "time": 25,
                            "volume": 0.85
                        }
                    ],
                    "functionTicks": [
                        {
                            "functionName": "Flash",
                            "functionParam": "s",
                            "time": 25
                        },
                        {
                            "functionName": "Shake",
                            "functionParam": "s",
                            "time": 25
                        }
                    ],
                    "characterId": 6
                },
                {
                    "id": 410,
                    "name": "Damage (custom)",
                    "idleImageUrl": "https://objection.lol/Images/Characters/6/Damage.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/6/Damage.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/410.png",
                    "order": 0,
                    "musicFileName": "objection",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 6
                }
            ],
            {
                "1": "https://objection.lol/Audio/Vocal/1/6.mp3"
            }
        )
        FranziskaVonKarma = _builtinCharacter(
            7,
            "Franziska von Karma",
            "von Karma",
            _blips['female'],
            enums.CharacterLocation.PROSECUTION,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/7.png",
            [
                {
                    "id": 21,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/7/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/7/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/21.png",
                    "order": 0,
                    "musicFileName": "trial2",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 7
                },
                {
                    "id": 22,
                    "name": "Confident",
                    "idleImageUrl": "https://objection.lol/Images/Characters/7/Confident.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/7/Confident_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/22.png",
                    "order": 0,
                    "musicFileName": "objection",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 7
                },
                {
                    "id": 23,
                    "name": "Desk Slam",
                    "idleImageUrl": "https://objection.lol/Images/Characters/7/Desk_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/7/Desk_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/23.png",
                    "order": 0,
                    "musicFileName": "truth2002",
                    "states": [
                        {
                            "imageUrl": "Slam",
                            "nextPoseDelay": 2000
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "sound/deskslam2",
                            "time": 420,
                            "volume": 1
                        },
                        {
                            "fileName": "sound/deskslam2",
                            "time": 1325,
                            "volume": 1
                        },
                        {
                            "fileName": "sound/deskslam2",
                            "time": 1650,
                            "volume": 1
                        }
                    ],
                    "functionTicks": [],
                    "characterId": 7
                },
                {
                    "id": 24,
                    "name": "Arms Crossed",
                    "idleImageUrl": "https://objection.lol/Images/Characters/7/Arms_Crossed_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/7/Arms_Crossed_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/24.png",
                    "order": 0,
                    "musicFileName": "trial2",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 7
                },
                {
                    "id": 25,
                    "name": "Point",
                    "idleImageUrl": "https://objection.lol/Images/Characters/7/Point_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/7/Point_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/25.png",
                    "order": 0,
                    "musicFileName": "crossexamining",
                    "states": [
                        {
                            "imageUrl": "Special_1",
                            "nextPoseDelay": 200
                        }
                    ],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 7
                },
                {
                    "id": 26,
                    "name": "Whip Desk",
                    "idleImageUrl": "https://objection.lol/Images/Characters/7/Whip_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/7/Whip_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/26.png",
                    "order": 0,
                    "musicFileName": "crossexaminingvariation",
                    "states": [
                        {
                            "imageUrl": "Special_2",
                            "nextPoseDelay": 1400
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "whip",
                            "time": 530,
                            "volume": 1
                        },
                        {
                            "fileName": "whack",
                            "time": 580,
                            "volume": 0.7
                        },
                        {
                            "fileName": "bam",
                            "time": 1450,
                            "volume": 1
                        }
                    ],
                    "functionTicks": [
                        {
                            "functionName": "Flash",
                            "functionParam": "m",
                            "time": 570
                        },
                        {
                            "functionName": "Flash",
                            "functionParam": "l",
                            "time": 1450
                        }
                    ],
                    "characterId": 7
                },
                {
                    "id": 41,
                    "name": "Cornered",
                    "idleImageUrl": "https://objection.lol/Images/Characters/7/Cornered.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/7/Cornered_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/41.png",
                    "order": 0,
                    "musicFileName": "truth2004",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 7
                },
                {
                    "id": 192,
                    "name": "Damage",
                    "idleImageUrl": "https://objection.lol/Images/Characters/7/Damage.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/7/Damage.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/192.png",
                    "order": 0,
                    "musicFileName": "truth2002",
                    "states": [
                        {
                            "imageUrl": "Damage",
                            "nextPoseDelay": 1
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "yell2",
                            "time": 25,
                            "volume": 0.9
                        }
                    ],
                    "functionTicks": [
                        {
                            "functionName": "Flash",
                            "functionParam": "s",
                            "time": 25
                        },
                        {
                            "functionName": "Shake",
                            "functionParam": "s",
                            "time": 25
                        }
                    ],
                    "characterId": 7
                },
                {
                    "id": 411,
                    "name": "Damage (custom)",
                    "idleImageUrl": "https://objection.lol/Images/Characters/7/Damage.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/7/Damage.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/411.png",
                    "order": 0,
                    "musicFileName": "truth2002",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 7
                },
                {
                    "id": 193,
                    "name": "Bow",
                    "idleImageUrl": "https://objection.lol/Images/Characters/7/Bow.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/7/Bow.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/193.png",
                    "order": 0,
                    "musicFileName": "moderato2002",
                    "states": [
                        {
                            "imageUrl": "Bow",
                            "nextPoseDelay": 600
                        }
                    ],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 7
                },
                {
                    "id": 274,
                    "name": "Yell",
                    "idleImageUrl": "https://objection.lol/Images/Characters/7/Yell_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/7/Yell_Talk.gif",
                    "isSpeedlines": True,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/274.png",
                    "order": 0,
                    "musicFileName": "truth2001",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 7
                }
            ],
            {
                "1": "https://objection.lol/Audio/Vocal/1/7.mp3"
            }
        )
        ManfredVonKarma = _builtinCharacter(
            8,
            "Manfred von Karma",
            "Karma",
            _blips['male'],
            enums.CharacterLocation.PROSECUTION,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/8.png",
            [
                {
                    "id": 27,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/8/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/8/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/27.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 8
                },
                {
                    "id": 28,
                    "name": "Confident",
                    "idleImageUrl": "https://objection.lol/Images/Characters/8/Confident.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/8/Confident_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/28.png",
                    "order": 0,
                    "musicFileName": "truth2001",
                    "states": [
                        {
                            "imageUrl": "Special_1",
                            "nextPoseDelay": 1500
                        }
                    ],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 8
                },
                {
                    "id": 29,
                    "name": "Arms Crossed",
                    "idleImageUrl": "https://objection.lol/Images/Characters/8/Arms_Crossed.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/8/Arms_Crossed_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/29.png",
                    "order": 0,
                    "musicFileName": "truth2002",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 8
                },
                {
                    "id": 42,
                    "name": "Cornered",
                    "idleImageUrl": "https://objection.lol/Images/Characters/8/Cornered.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/8/Cornered_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/42.png",
                    "order": 0,
                    "musicFileName": "truth2004",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 8
                },
                {
                    "id": 43,
                    "name": "Snap Finger",
                    "idleImageUrl": "https://objection.lol/Images/Characters/8/Take_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/8/Take_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/43.png",
                    "order": 0,
                    "musicFileName": "allegro2001",
                    "states": [
                        {
                            "imageUrl": "Special_2",
                            "nextPoseDelay": 500
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "snap",
                            "time": 250,
                            "volume": 0.85
                        }
                    ],
                    "functionTicks": [
                        {
                            "functionName": "Flash",
                            "functionParam": "m",
                            "time": 300
                        }
                    ],
                    "characterId": 8
                },
                {
                    "id": 191,
                    "name": "Damage",
                    "idleImageUrl": "https://objection.lol/Images/Characters/8/Damage_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/8/Damage_Stand.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/191.png",
                    "order": 0,
                    "musicFileName": "truth2009",
                    "states": [
                        {
                            "imageUrl": "Damage",
                            "nextPoseDelay": 550
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "deskslam",
                            "time": 225,
                            "volume": 0.85
                        }
                    ],
                    "functionTicks": [],
                    "characterId": 8
                },
                {
                    "id": 412,
                    "name": "Damage (custom)",
                    "idleImageUrl": "https://objection.lol/Images/Characters/8/Damage.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/8/Damage.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/412.png",
                    "order": 0,
                    "musicFileName": "truth2009",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 8
                },
                {
                    "id": 309,
                    "name": "Breakdown (1)",
                    "idleImageUrl": "https://objection.lol/Images/Characters/8/Breakdown1.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/8/Breakdown1.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/309.png",
                    "order": 0,
                    "musicFileName": "truth2001",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 8
                },
                {
                    "id": 310,
                    "name": "Breakdown (2)",
                    "idleImageUrl": "https://objection.lol/Images/Characters/8/Breakdown2.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/8/Breakdown2.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/310.png",
                    "order": 0,
                    "musicFileName": "truth2001",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 8
                }
            ],
            {
                "1": "https://objection.lol/Audio/Vocal/1/8.mp3"
            }
        )
        GodotDS = _builtinCharacter(
            9,
            "Godot",
            "Godot",
            _blips['male'],
            enums.CharacterLocation.PROSECUTION,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/9.png",
            [
                {
                    "id": 48,
                    "name": "Desk Slam (with mug)",
                    "idleImageUrl": "https://objection.lol/Images/Characters/9/Desk_Stand_Mug.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/9/Desk_Talk_Mug.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/48.png",
                    "order": 0,
                    "musicFileName": "crossexaminingvariation",
                    "states": [
                        {
                            "imageUrl": "Special3",
                            "nextPoseDelay": 1800
                        },
                        {
                            "id": 20,
                            "imageUrl": "Desk_Slam_Mug",
                            "nextPoseDelay": 550
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "chug-quick",
                            "time": 5,
                            "volume": 0.8
                        },
                        {
                            "fileName": "gavel",
                            "time": 2025,
                            "volume": 0.85
                        }
                    ],
                    "functionTicks": [],
                    "characterId": 9
                },
                {
                    "id": 49,
                    "name": "Desk Slam",
                    "idleImageUrl": "https://objection.lol/Images/Characters/9/Desk_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/9/Desk_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/49.png",
                    "order": 0,
                    "musicFileName": "truth2004",
                    "states": [
                        {
                            "imageUrl": "Desk_Slam",
                            "nextPoseDelay": 600
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "deskslam",
                            "time": 250,
                            "volume": 1
                        }
                    ],
                    "functionTicks": [],
                    "characterId": 9
                },
                {
                    "id": 50,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/9/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/9/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/50.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 9
                },
                {
                    "id": 51,
                    "name": "New Mug Sip",
                    "idleImageUrl": "https://objection.lol/Images/Characters/9/Sip_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/9/Sip_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/51.png",
                    "order": 0,
                    "musicFileName": "darkcoffee",
                    "states": [
                        {
                            "imageUrl": "Special1",
                            "nextPoseDelay": 750
                        },
                        {
                            "id": 24,
                            "imageUrl": "Special2",
                            "nextPoseDelay": 1900
                        },
                        {
                            "id": 25,
                            "imageUrl": "Sip",
                            "nextPoseDelay": 2000
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "chug",
                            "time": 3350,
                            "volume": 0.9
                        },
                        {
                            "fileName": "mug-slide",
                            "time": 150,
                            "volume": 0.85
                        }
                    ],
                    "functionTicks": [],
                    "characterId": 9
                },
                {
                    "id": 52,
                    "name": "Point (with mug)",
                    "idleImageUrl": "https://objection.lol/Images/Characters/9/Point_Mug_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/9/Point_Mug_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/52.png",
                    "order": 0,
                    "musicFileName": "crossexamining",
                    "states": [
                        {
                            "imageUrl": "Special3",
                            "nextPoseDelay": 1800
                        },
                        {
                            "imageUrl": "Point_Mug",
                            "nextPoseDelay": 500,
                            "speakDelay": 200
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "chug-quick",
                            "time": 5,
                            "volume": 0.8
                        },
                        {
                            "fileName": "bam",
                            "time": 1950,
                            "volume": 0.9
                        }
                    ],
                    "functionTicks": [
                        {
                            "functionName": "Flash",
                            "functionParam": "m",
                            "time": 1950
                        }
                    ],
                    "characterId": 9
                },
                {
                    "id": 53,
                    "name": "Point",
                    "idleImageUrl": "https://objection.lol/Images/Characters/9/Point_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/9/Point_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/53.png",
                    "order": 0,
                    "musicFileName": "crossexamining",
                    "states": [
                        {
                            "imageUrl": "Point",
                            "nextPoseDelay": 500,
                            "speakDelay": 200
                        }
                    ],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 9
                },
                {
                    "id": 54,
                    "name": "Cornered",
                    "idleImageUrl": "https://objection.lol/Images/Characters/9/Cornered.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/9/Cornered_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/54.png",
                    "order": 0,
                    "musicFileName": "objection2004",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 9
                },
                {
                    "id": 138,
                    "name": "Confident",
                    "idleImageUrl": "https://objection.lol/Images/Characters/9/Smile_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/9/Smile_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/138.png",
                    "order": 0,
                    "musicFileName": "truth2002",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 9
                },
                {
                    "id": 139,
                    "name": "Confident (with mug)",
                    "idleImageUrl": "https://objection.lol/Images/Characters/9/Smile_Stand_Mug.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/9/Smile_Talk_Mug.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/139.png",
                    "order": 0,
                    "musicFileName": "darkcoffee",
                    "states": [
                        {
                            "imageUrl": "Special1",
                            "nextPoseDelay": 750
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "mug-slide",
                            "time": 150,
                            "volume": 0.85
                        }
                    ],
                    "functionTicks": [],
                    "characterId": 9
                },
                {
                    "id": 183,
                    "name": "Sip Mug",
                    "idleImageUrl": "https://objection.lol/Images/Characters/9/Sip_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/9/Sip_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/183.png",
                    "order": 0,
                    "musicFileName": "darkcoffee",
                    "states": [
                        {
                            "id": 25,
                            "imageUrl": "Sip",
                            "nextPoseDelay": 2000
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "chug",
                            "time": 700,
                            "volume": 0.9
                        }
                    ],
                    "functionTicks": [],
                    "characterId": 9
                }
            ],
            {
                "1": "https://objection.lol/Audio/Vocal/1/9.mp3"
            }
        )
        KlavierGavin = _builtinCharacter(
            12,
            "Klavier Gavin",
            "Klavier",
            _blips['male'],
            enums.CharacterLocation.PROSECUTION,
            _defaultBackgrounds['aj'],
            "https://objection.lol/Images/Gallery/12.png",
            [
                {
                    "id": 64,
                    "name": "Cornered",
                    "idleImageUrl": "https://objection.lol/Images/Characters/12/Cornered.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/12/Cornered_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/64.png",
                    "order": 0,
                    "musicFileName": "truth2007",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 12
                },
                {
                    "id": 65,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/12/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/12/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/65.png",
                    "order": 0,
                    "musicFileName": "trial5",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 12
                },
                {
                    "id": 66,
                    "name": "Point",
                    "idleImageUrl": "https://objection.lol/Images/Characters/12/Point_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/12/Point_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/66.png",
                    "order": 0,
                    "musicFileName": "klavier",
                    "states": [
                        {
                            "imageUrl": "Point",
                            "nextPoseDelay": 500,
                            "speakDelay": 335
                        }
                    ],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 12
                },
                {
                    "id": 67,
                    "name": "Think",
                    "idleImageUrl": "https://objection.lol/Images/Characters/12/Think.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/12/Think_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/67.png",
                    "order": 0,
                    "musicFileName": "trial4",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 12
                },
                {
                    "id": 68,
                    "name": "Laugh",
                    "idleImageUrl": "https://objection.lol/Images/Characters/12/Laugh_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/12/Laugh_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/68.png",
                    "order": 0,
                    "musicFileName": "moderato2007",
                    "states": [
                        {
                            "imageUrl": "Laugh",
                            "nextPoseDelay": 2200
                        }
                    ],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 12
                },
                {
                    "id": 69,
                    "name": "Air Guitar",
                    "idleImageUrl": "https://objection.lol/Images/Characters/12/Slam_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/12/Slam_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/69.png",
                    "order": 0,
                    "musicFileName": "objection2007",
                    "states": [
                        {
                            "imageUrl": "Guitar",
                            "nextPoseDelay": 5050
                        },
                        {
                            "imageUrl": "Slam",
                            "nextPoseDelay": 1000
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "airguitar",
                            "time": 1,
                            "volume": 1
                        },
                        {
                            "fileName": "deskslam",
                            "time": 5250,
                            "volume": 1
                        }
                    ],
                    "functionTicks": [],
                    "characterId": 12
                },
                {
                    "id": 70,
                    "name": "Look Up",
                    "idleImageUrl": "https://objection.lol/Images/Characters/12/Up.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/12/Up_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/70.png",
                    "order": 0,
                    "musicFileName": "truth2007",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 12
                },
                {
                    "id": 217,
                    "name": "Wall Slam",
                    "idleImageUrl": "https://objection.lol/Images/Characters/12/Slam_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/12/Slam_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/217.png",
                    "order": 0,
                    "musicFileName": "objection2007",
                    "states": [
                        {
                            "imageUrl": "Slam",
                            "nextPoseDelay": 1000
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "deskslam",
                            "time": 200,
                            "volume": 1
                        }
                    ],
                    "functionTicks": [],
                    "characterId": 12
                },
                {
                    "id": 401,
                    "name": "Damage",
                    "idleImageUrl": "https://objection.lol/Images/Characters/12/Damage.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/12/Damage.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/401.png",
                    "order": 0,
                    "musicFileName": "truth2007",
                    "states": [
                        {
                            "imageUrl": "Damage",
                            "nextPoseDelay": 1
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "Sound/guitar error",
                            "time": 50,
                            "volume": 0.85
                        }
                    ],
                    "functionTicks": [],
                    "characterId": 12
                },
                {
                    "id": 414,
                    "name": "Damage (custom)",
                    "idleImageUrl": "https://objection.lol/Images/Characters/12/Damage.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/12/Damage.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/414.png",
                    "order": 0,
                    "musicFileName": "truth2007",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 12
                },
                {
                    "id": 689,
                    "name": "Yell",
                    "idleImageUrl": "https://objection.lol/Images/Characters/12/Yell.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/12/Yell_Talk.gif",
                    "isSpeedlines": True,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/689.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 12
                },
                {
                    "id": 745,
                    "name": "Cornered 2",
                    "idleImageUrl": "https://objection.lol/Images/Characters/12/Cornered2.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/12/Cornered2_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/745.png",
                    "order": 0,
                    "musicFileName": "truth2007",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 12
                }
            ],
            {
                "1": "https://objection.lol/Audio/Vocal/1/12.mp3"
            }
        )
        Godot = _builtinCharacter(
            25,
            "Godot",
            "Godot",
            _blips['male'],
            enums.CharacterLocation.PROSECUTION,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/25.png",
            [
                {
                    "id": 173,
                    "name": "Desk Slam (with mug)",
                    "idleImageUrl": "https://objection.lol/Images/Characters/25/Desk_Stand_Mug.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/25/Desk_Talk_Mug.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/173.png",
                    "order": 0,
                    "musicFileName": "crossexaminingvariation",
                    "states": [
                        {
                            "imageUrl": "Special3",
                            "nextPoseDelay": 1800
                        },
                        {
                            "id": 20,
                            "imageUrl": "Desk_Slam_Mug",
                            "nextPoseDelay": 550
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "chug-quick",
                            "time": 5,
                            "volume": 0.8
                        },
                        {
                            "fileName": "gavel",
                            "time": 1950,
                            "volume": 0.85
                        }
                    ],
                    "functionTicks": [],
                    "characterId": 25
                },
                {
                    "id": 174,
                    "name": "Desk Slam",
                    "idleImageUrl": "https://objection.lol/Images/Characters/25/Desk_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/25/Desk_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/174.png",
                    "order": 0,
                    "musicFileName": "truth2004",
                    "states": [
                        {
                            "imageUrl": "Desk_Slam",
                            "nextPoseDelay": 600
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "deskslam",
                            "time": 250,
                            "volume": 1
                        }
                    ],
                    "functionTicks": [],
                    "characterId": 25
                },
                {
                    "id": 175,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/25/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/25/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/175.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 25
                },
                {
                    "id": 176,
                    "name": "New Mug Sip",
                    "idleImageUrl": "https://objection.lol/Images/Characters/25/Sip_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/25/Sip_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/176.png",
                    "order": 0,
                    "musicFileName": "darkcoffee",
                    "states": [
                        {
                            "imageUrl": "Special1",
                            "nextPoseDelay": 750
                        },
                        {
                            "id": 24,
                            "imageUrl": "Special2",
                            "nextPoseDelay": 1500
                        },
                        {
                            "id": 25,
                            "imageUrl": "Sip",
                            "nextPoseDelay": 1700
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "chug",
                            "time": 2800,
                            "volume": 0.9
                        },
                        {
                            "fileName": "mug-slide",
                            "time": 150,
                            "volume": 0.85
                        }
                    ],
                    "functionTicks": [],
                    "characterId": 25
                },
                {
                    "id": 177,
                    "name": "Point (with mug)",
                    "idleImageUrl": "https://objection.lol/Images/Characters/25/Point_Mug_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/25/Point_Mug_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/177.png",
                    "order": 0,
                    "musicFileName": "crossexamining",
                    "states": [
                        {
                            "imageUrl": "Special3",
                            "nextPoseDelay": 1800
                        },
                        {
                            "imageUrl": "Point_Mug",
                            "nextPoseDelay": 500,
                            "speakDelay": 200
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "chug-quick",
                            "time": 5,
                            "volume": 0.8
                        },
                        {
                            "fileName": "bam",
                            "time": 1950,
                            "volume": 0.9
                        }
                    ],
                    "functionTicks": [
                        {
                            "functionName": "Flash",
                            "functionParam": "m",
                            "time": 1950
                        }
                    ],
                    "characterId": 25
                },
                {
                    "id": 178,
                    "name": "Point",
                    "idleImageUrl": "https://objection.lol/Images/Characters/25/Point_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/25/Point_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/178.png",
                    "order": 0,
                    "musicFileName": "crossexamining",
                    "states": [
                        {
                            "imageUrl": "Point",
                            "nextPoseDelay": 500,
                            "speakDelay": 200
                        }
                    ],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 25
                },
                {
                    "id": 179,
                    "name": "Cornered",
                    "idleImageUrl": "https://objection.lol/Images/Characters/25/Cornered.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/25/Cornered_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/179.png",
                    "order": 0,
                    "musicFileName": "objection2004",
                    "states": [
                        {
                            "imageUrl": "Cornered_Mug",
                            "nextPoseDelay": 520,
                            "speakDelay": 520
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "mug-slide",
                            "time": 100,
                            "volume": 0.85
                        }
                    ],
                    "functionTicks": [],
                    "characterId": 25
                },
                {
                    "id": 180,
                    "name": "Confident",
                    "idleImageUrl": "https://objection.lol/Images/Characters/25/Smile_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/25/Smile_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/180.png",
                    "order": 0,
                    "musicFileName": "truth2002",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 25
                },
                {
                    "id": 181,
                    "name": "Confident (with mug)",
                    "idleImageUrl": "https://objection.lol/Images/Characters/25/Smile_Stand_Mug.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/25/Smile_Talk_Mug.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/181.png",
                    "order": 0,
                    "musicFileName": "darkcoffee",
                    "states": [
                        {
                            "imageUrl": "Special1",
                            "nextPoseDelay": 750
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "mug-slide",
                            "time": 150,
                            "volume": 0.85
                        }
                    ],
                    "functionTicks": [],
                    "characterId": 25
                },
                {
                    "id": 182,
                    "name": "Think",
                    "idleImageUrl": "https://objection.lol/Images/Characters/25/Think.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/25/Think_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/182.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 25
                },
                {
                    "id": 184,
                    "name": "Mug Sip",
                    "idleImageUrl": "https://objection.lol/Images/Characters/25/Sip_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/25/Sip_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/184.png",
                    "order": 0,
                    "musicFileName": "darkcoffee",
                    "states": [
                        {
                            "id": 25,
                            "imageUrl": "Sip",
                            "nextPoseDelay": 1400
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "chug",
                            "time": 550,
                            "volume": 0.9
                        }
                    ],
                    "functionTicks": [],
                    "characterId": 25
                },
                {
                    "id": 218,
                    "name": "Damage",
                    "idleImageUrl": "https://objection.lol/Images/Characters/25/Damage.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/25/Damage.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/218.png",
                    "order": 0,
                    "musicFileName": "truth2004",
                    "states": [
                        {
                            "imageUrl": "Damage",
                            "nextPoseDelay": 10
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "damage2",
                            "time": 5,
                            "volume": 0.9
                        }
                    ],
                    "functionTicks": [
                        {
                            "functionName": "Flash",
                            "functionParam": "m",
                            "time": 25
                        },
                        {
                            "functionName": "Shake",
                            "functionParam": "m",
                            "time": 25
                        }
                    ],
                    "characterId": 25
                },
                {
                    "id": 413,
                    "name": "Damage (custom)",
                    "idleImageUrl": "https://objection.lol/Images/Characters/25/Damage.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/25/Damage.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/413.png",
                    "order": 0,
                    "musicFileName": "truth2004",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 25
                },
                {
                    "id": 219,
                    "name": "Throw Mug",
                    "idleImageUrl": "https://objection.lol/Images/Characters/25/Point_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/25/Point_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/219.png",
                    "order": 0,
                    "musicFileName": "darkcoffee",
                    "states": [
                        {
                            "imageUrl": "Throw",
                            "nextPoseDelay": 325
                        }
                    ],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 25
                },
                {
                    "id": 275,
                    "name": "Yell",
                    "idleImageUrl": "https://objection.lol/Images/Characters/25/Yell_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/25/Yell_Talk.gif",
                    "isSpeedlines": True,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/275.png",
                    "order": 0,
                    "musicFileName": "truth2001",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 25
                },
                {
                    "id": 520,
                    "name": "Mask Explosion",
                    "idleImageUrl": "https://objection.lol/Images/Characters/25/Explode.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/25/Explode.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/520.png",
                    "order": 0,
                    "musicFileName": "cornered2004 - pursuit variation",
                    "states": [
                        {
                            "imageUrl": "Explode",
                            "nextPoseDelay": 1
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "damage2",
                            "time": 1,
                            "volume": 1
                        }
                    ],
                    "functionTicks": [],
                    "characterId": 25
                }
            ],
            {
                "1": "https://objection.lol/Audio/Vocal/1/25.mp3"
            }
        )
        WinstonPayneOld = _builtinCharacter(
            58,
            "Winston Payne (old)",
            "Payne",
            _blips['male'],
            enums.CharacterLocation.PROSECUTION,
            _defaultBackgrounds['aj'],
            "https://objection.lol/Images/Gallery/58.png",
            [
                {
                    "id": 438,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/58/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/58/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/438.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 58
                },
                {
                    "id": 439,
                    "name": "Confident",
                    "idleImageUrl": "https://objection.lol/Images/Characters/58/Confident.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/58/Confident_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/439.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 58
                },
                {
                    "id": 440,
                    "name": "Cornered",
                    "idleImageUrl": "https://objection.lol/Images/Characters/58/Cornered.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/58/Cornered_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/440.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 58
                },
                {
                    "id": 441,
                    "name": "Smug",
                    "idleImageUrl": "https://objection.lol/Images/Characters/58/Smug.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/58/Smug.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/441.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [
                        {
                            "imageUrl": "Smug",
                            "nextPoseDelay": 1
                        }
                    ],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 58
                },
                {
                    "id": 442,
                    "name": "Damage",
                    "idleImageUrl": "https://objection.lol/Images/Characters/58/Damage.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/58/Damage.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/442.png",
                    "order": 0,
                    "musicFileName": "objection",
                    "states": [
                        {
                            "imageUrl": "Damage",
                            "nextPoseDelay": 1
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "yell2",
                            "time": 25,
                            "volume": 0.85
                        }
                    ],
                    "functionTicks": [
                        {
                            "functionName": "Flash",
                            "functionParam": "s",
                            "time": 25
                        },
                        {
                            "functionName": "Shake",
                            "functionParam": "s",
                            "time": 25
                        }
                    ],
                    "characterId": 58
                },
                {
                    "id": 443,
                    "name": "Damage (custom)",
                    "idleImageUrl": "https://objection.lol/Images/Characters/58/Damage.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/58/Damage.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/443.png",
                    "order": 0,
                    "musicFileName": "objection",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 58
                }
            ],
            {
                "1": "https://objection.lol/Audio/Vocal/1/58.mp3"
            }
        )
        WinstonPayneYoung = _builtinCharacter(
            73,
            "Winston Payne (young)",
            "Payne",
            _blips['male'],
            enums.CharacterLocation.PROSECUTION,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/73.png",
            [
                {
                    "id": 564,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/73/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/73/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/564.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 73
                },
                {
                    "id": 565,
                    "name": "Confident",
                    "idleImageUrl": "https://objection.lol/Images/Characters/73/Confident.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/73/Confident_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/565.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 73
                },
                {
                    "id": 566,
                    "name": "Cornered",
                    "idleImageUrl": "https://objection.lol/Images/Characters/73/Cornered.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/73/Cornered_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/566.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 73
                },
                {
                    "id": 567,
                    "name": "Damage",
                    "idleImageUrl": "https://objection.lol/Images/Characters/73/Damage.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/73/Damage.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/567.png",
                    "order": 0,
                    "musicFileName": "objection",
                    "states": [
                        {
                            "imageUrl": "Damage",
                            "nextPoseDelay": 1
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "yell2",
                            "time": 25,
                            "volume": 0.85
                        }
                    ],
                    "functionTicks": [
                        {
                            "functionName": "Flash",
                            "functionParam": "s",
                            "time": 25
                        },
                        {
                            "functionName": "Shake",
                            "functionParam": "s",
                            "time": 25
                        }
                    ],
                    "characterId": 73
                },
                {
                    "id": 568,
                    "name": "Damage (custom)",
                    "idleImageUrl": "https://objection.lol/Images/Characters/73/Damage.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/73/Damage.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/568.png",
                    "order": 0,
                    "musicFileName": "objection",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 73
                },
                {
                    "id": 569,
                    "name": "Breakdown",
                    "idleImageUrl": "https://objection.lol/Images/Characters/73/Breakdown.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/73/Breakdown.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/569.png",
                    "order": 0,
                    "musicFileName": "objection",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 73
                },
                {
                    "id": 570,
                    "name": "Stand (hairless)",
                    "idleImageUrl": "https://objection.lol/Images/Characters/73/Stand_H.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/73/Stand_Talk_H.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/570.png",
                    "order": 0,
                    "musicFileName": "objection",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 73
                },
                {
                    "id": 571,
                    "name": "Cornered (hairless)",
                    "idleImageUrl": "https://objection.lol/Images/Characters/73/Cornered_H.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/73/Cornered_Talk_H.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/571.png",
                    "order": 0,
                    "musicFileName": "objection",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 73
                }
            ],
            {
                "1": "https://objection.lol/Audio/Vocal/1/73.mp3"
            }
        )

    class Counsel:
        DiegoArmando = _builtinCharacter(
            5,
            "Diego Armando",
            "Armando",
            _blips['male'],
            enums.CharacterLocation.COUNSEL,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/5.png",
            [
                {
                    "id": 45,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/5/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/5/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/45.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 5
                },
                {
                    "id": 46,
                    "name": "Stand 2",
                    "idleImageUrl": "https://objection.lol/Images/Characters/5/Stand2.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/5/Stand2_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/46.png",
                    "order": 0,
                    "musicFileName": "allegro2004",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 5
                },
                {
                    "id": 91,
                    "name": "Stand 3",
                    "idleImageUrl": "https://objection.lol/Images/Characters/5/Stand3.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/5/Stand3_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/91.png",
                    "order": 0,
                    "musicFileName": "truth2002",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 5
                },
                {
                    "id": 417,
                    "name": "Break Cup",
                    "idleImageUrl": "https://objection.lol/Images/Characters/5/Break_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/5/Break_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/417.png",
                    "order": 0,
                    "musicFileName": "objection2007",
                    "states": [
                        {
                            "imageUrl": "Break",
                            "nextPoseDelay": 4000,
                            "speakDelay": 4000
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "sound/break",
                            "time": 1600,
                            "volume": 1
                        }
                    ],
                    "functionTicks": [],
                    "characterId": 5
                }
            ],
            {
                "1": "https://objection.lol/Audio/Vocal/1/5.mp3"
            }
        )
        MayaFey = _builtinCharacter(
            16,
            "Maya Fey",
            "Maya",
            _blips['female'],
            enums.CharacterLocation.COUNSEL,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/16.png",
            [
                {
                    "id": 102,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/16/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/16/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/102.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 16
                },
                {
                    "id": 103,
                    "name": "Angry",
                    "idleImageUrl": "https://objection.lol/Images/Characters/16/Angry.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/16/Angry_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/103.png",
                    "order": 0,
                    "musicFileName": "moderato2001",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 16
                },
                {
                    "id": 104,
                    "name": "Dull",
                    "idleImageUrl": "https://objection.lol/Images/Characters/16/Dull.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/16/Dull_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/104.png",
                    "order": 0,
                    "musicFileName": "moderato2001",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 16
                },
                {
                    "id": 105,
                    "name": "Thinking",
                    "idleImageUrl": "https://objection.lol/Images/Characters/16/Think.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/16/Think_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/105.png",
                    "order": 0,
                    "musicFileName": "moderato2001",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 16
                },
                {
                    "id": 106,
                    "name": "Determined",
                    "idleImageUrl": "https://objection.lol/Images/Characters/16/Determined.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/16/Determined_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/106.png",
                    "order": 0,
                    "musicFileName": "allegro2001",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 16
                }
            ]
        )
        MiaFey = _builtinCharacter(
            19,
            "Mia Fey",
            "Mia",
            _blips['female'],
            enums.CharacterLocation.COUNSEL,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/19.png",
            [
                {
                    "id": 121,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/19/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/19/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/121.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 19
                },
                {
                    "id": 122,
                    "name": "Surprised",
                    "idleImageUrl": "https://objection.lol/Images/Characters/19/Surprised.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/19/Surprised_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/122.png",
                    "order": 0,
                    "musicFileName": "truth2001",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 19
                },
                {
                    "id": 123,
                    "name": "Dull",
                    "idleImageUrl": "https://objection.lol/Images/Characters/19/Dull.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/19/Dull_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/123.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 19
                },
                {
                    "id": 124,
                    "name": "Sad",
                    "idleImageUrl": "https://objection.lol/Images/Characters/19/Sad.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/19/Sad_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/124.png",
                    "order": 0,
                    "musicFileName": "truth2001",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 19
                }
            ],
            {
                "1": "https://objection.lol/Audio/Vocal/1/19.mp3",
                "2": "https://objection.lol/Audio/Vocal/2/19.mp3",
                "3": "https://objection.lol/Audio/Vocal/3/19.mp3"
            }
        )
        EmaSkye = _builtinCharacter(
            46,
            "Ema Skye",
            "Ema",
            _blips['female'],
            enums.CharacterLocation.COUNSEL,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/46.png",
            [
                {
                    "id": 353,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/46/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/46/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/353.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 46
                },
                {
                    "id": 354,
                    "name": "Think",
                    "idleImageUrl": "https://objection.lol/Images/Characters/46/Think.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/46/Think_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/354.png",
                    "order": 0,
                    "musicFileName": "moderato2001",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 46
                },
                {
                    "id": 355,
                    "name": "Determined",
                    "idleImageUrl": "https://objection.lol/Images/Characters/46/Determined.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/46/Determined_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/355.png",
                    "order": 0,
                    "musicFileName": "moderato2001",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 46
                },
                {
                    "id": 356,
                    "name": "Angry",
                    "idleImageUrl": "https://objection.lol/Images/Characters/46/Angry.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/46/Angry_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/356.png",
                    "order": 0,
                    "musicFileName": "moderato2001",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 46
                }
            ]
        )
        MarvinGrossberg = _builtinCharacter(
            47,
            "Marvin Grossberg",
            "Grossberg",
            _blips['male'],
            enums.CharacterLocation.COUNSEL,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/47.png",
            [
                {
                    "id": 359,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/47/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/47/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/359.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 47
                },
                {
                    "id": 360,
                    "name": "Cornered",
                    "idleImageUrl": "https://objection.lol/Images/Characters/47/Cornered.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/47/Cornered_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/360.png",
                    "order": 0,
                    "musicFileName": "moderato2001",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 47
                }
            ]
        )
        MaggeyByrde = _builtinCharacter(
            50,
            "Maggey Byrde",
            "Byrde",
            _blips['female'],
            enums.CharacterLocation.COUNSEL,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/50.png",
            [
                {
                    "id": 369,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/50/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/50/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/369.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 50
                },
                {
                    "id": 370,
                    "name": "Pumped",
                    "idleImageUrl": "https://objection.lol/Images/Characters/50/Pumped.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/50/Pumped_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/370.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 50
                }
            ]
        )
        PhoenixWrightOld = _builtinCharacter(
            57,
            "Phoenix Wright (old)",
            "Phoenix",
            _blips['male'],
            enums.CharacterLocation.COUNSEL,
            _defaultBackgrounds['aj'],
            "https://objection.lol/Images/Gallery/57.png",
            [
                {
                    "id": 434,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/57/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/57/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/434.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 57
                },
                {
                    "id": 435,
                    "name": "Confident",
                    "idleImageUrl": "https://objection.lol/Images/Characters/57/Confident.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/57/Confident_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/435.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 57
                },
                {
                    "id": 436,
                    "name": "Serious",
                    "idleImageUrl": "https://objection.lol/Images/Characters/57/Serious.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/57/Serious_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/436.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 57
                },
                {
                    "id": 437,
                    "name": "Point",
                    "idleImageUrl": "https://objection.lol/Images/Characters/57/Point_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/57/Point_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/437.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [
                        {
                            "imageUrl": "Point",
                            "nextPoseDelay": 250
                        }
                    ],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 57
                }
            ],
            {
                "1": "https://objection.lol/Audio/Vocal/1/57.mp3",
                "2": "https://objection.lol/Audio/Vocal/2/57.mp3",
                "3": "https://objection.lol/Audio/Vocal/3/57.mp3"
            }
        )
        KristophGavin = _builtinCharacter(
            60,
            "Kristoph Gavin",
            "Kristoph",
            _blips['male'],
            enums.CharacterLocation.COUNSEL,
            _defaultBackgrounds['aj'],
            "https://objection.lol/Images/Gallery/60.png",
            [
                {
                    "id": 458,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/60/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/60/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/458.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 60
                },
                {
                    "id": 459,
                    "name": "Side",
                    "idleImageUrl": "https://objection.lol/Images/Characters/60/Side.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/60/Side_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/459.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 60
                },
                {
                    "id": 460,
                    "name": "Smile",
                    "idleImageUrl": "https://objection.lol/Images/Characters/60/Smile2.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/60/Smile_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/460.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 60
                }
            ],
            {
                "1": "https://objection.lol/Audio/Vocal/1/60.mp3"
            }
        )
        TrucyWright = _builtinCharacter(
            72,
            "Trucy Wright",
            "Trucy",
            _blips['female'],
            enums.CharacterLocation.COUNSEL,
            _defaultBackgrounds['aj'],
            "https://objection.lol/Images/Gallery/72.png",
            [
                {
                    "id": 560,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/72/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/72/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/560.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 72
                },
                {
                    "id": 561,
                    "name": "Think",
                    "idleImageUrl": "https://objection.lol/Images/Characters/72/Think.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/72/Think_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/561.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 72
                },
                {
                    "id": 562,
                    "name": "Determined",
                    "idleImageUrl": "https://objection.lol/Images/Characters/72/Determined.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/72/Determined_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/562.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 72
                },
                {
                    "id": 563,
                    "name": "Side",
                    "idleImageUrl": "https://objection.lol/Images/Characters/72/Side.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/72/Side_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/563.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 72
                }
            ]
        )
        MiaAsMaya = _builtinCharacter(
            99,
            "Mia (as Maya)",
            "Mia",
            _blips['female'],
            enums.CharacterLocation.COUNSEL,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/99.png",
            [
                {
                    "id": 725,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/99/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/99/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/725.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 99
                },
                {
                    "id": 726,
                    "name": "Nod",
                    "idleImageUrl": "https://objection.lol/Images/Characters/99/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/99/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/726.png",
                    "order": 0,
                    "musicFileName": "moderato2001",
                    "states": [
                        {
                            "imageUrl": "Nod",
                            "nextPoseDelay": 1280
                        }
                    ],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 99
                },
                {
                    "id": 727,
                    "name": "Headshake",
                    "idleImageUrl": "https://objection.lol/Images/Characters/99/Dull.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/99/Dull_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/727.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [
                        {
                            "imageUrl": "Headshake",
                            "nextPoseDelay": 1280
                        }
                    ],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 99
                },
                {
                    "id": 728,
                    "name": "Dull",
                    "idleImageUrl": "https://objection.lol/Images/Characters/99/Dull.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/99/Dull_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/728.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 99
                },
                {
                    "id": 729,
                    "name": "Angry",
                    "idleImageUrl": "https://objection.lol/Images/Characters/99/Stare.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/99/Stare_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/729.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 99
                }
            ],
            {
                "1": "https://objection.lol/Audio/Vocal/1/99.mp3",
                "2": "https://objection.lol/Audio/Vocal/2/99.mp3",
                "3": "https://objection.lol/Audio/Vocal/3/99.mp3"
            }
        )

    class Witness:
        FrankSahwit = _builtinCharacter(
            13,
            "Frank Sahwit",
            "Sahwit",
            _blips['male'],
            enums.CharacterLocation.WITNESS,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/13.png",
            [
                {
                    "id": 71,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/13/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/13/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/71.png",
                    "order": 0,
                    "musicFileName": "moderato2001",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 13
                },
                {
                    "id": 72,
                    "name": "Nervous",
                    "idleImageUrl": "https://objection.lol/Images/Characters/13/Nervous.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/13/Nervous_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/72.png",
                    "order": 0,
                    "musicFileName": "allegro2001",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 13
                },
                {
                    "id": 73,
                    "name": "Damage",
                    "idleImageUrl": "https://objection.lol/Images/Characters/13/Damage_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/13/Damage_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/73.png",
                    "order": 0,
                    "musicFileName": "cornered",
                    "states": [
                        {
                            "imageUrl": "Damage",
                            "nextPoseDelay": 300
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "damage",
                            "time": 25,
                            "volume": 0.7
                        }
                    ],
                    "functionTicks": [
                        {
                            "functionName": "Flash",
                            "functionParam": "s",
                            "time": 30
                        },
                        {
                            "functionName": "Shake",
                            "functionParam": "m",
                            "time": 50
                        },
                        {
                            "functionName": "Flash",
                            "functionParam": "s",
                            "time": 155
                        }
                    ],
                    "characterId": 13
                },
                {
                    "id": 74,
                    "name": "Angry",
                    "idleImageUrl": "https://objection.lol/Images/Characters/13/Damage_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/13/Damage_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/74.png",
                    "order": 0,
                    "musicFileName": "cornered",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 13
                },
                {
                    "id": 75,
                    "name": "Cornered",
                    "idleImageUrl": "https://objection.lol/Images/Characters/13/Cornered.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/13/Cornered_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/75.png",
                    "order": 0,
                    "musicFileName": "cornered",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 13
                },
                {
                    "id": 399,
                    "name": "Throw",
                    "idleImageUrl": "https://objection.lol/Images/Characters/13/Throw.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/13/Throw.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/399.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 13
                },
                {
                    "id": 400,
                    "name": "Breakdown",
                    "idleImageUrl": "https://objection.lol/Images/Characters/13/Breakdown.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/13/Breakdown.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/400.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [
                        {
                            "imageUrl": "Fall",
                            "nextPoseDelay": 1,
                            "playAtTextEnd": True
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "Sound/Fall",
                            "time": 800,
                            "volume": 1,
                            "playAtTextEnd": True
                        }
                    ],
                    "functionTicks": [],
                    "characterId": 13
                }
            ]
        )
        MayaFey = _builtinCharacter(
            14,
            "Maya Fey",
            "Maya",
            _blips['female'],
            enums.CharacterLocation.WITNESS,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/14.png",
            [
                {
                    "id": 77,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/14/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/14/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/77.png",
                    "order": 0,
                    "musicFileName": "maya",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 14
                },
                {
                    "id": 78,
                    "name": "Think",
                    "idleImageUrl": "https://objection.lol/Images/Characters/14/Think_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/14/Think_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/78.png",
                    "order": 0,
                    "musicFileName": "maya",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 14
                },
                {
                    "id": 79,
                    "name": "Happy",
                    "idleImageUrl": "https://objection.lol/Images/Characters/14/Happy_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/14/Happy_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/79.png",
                    "order": 0,
                    "musicFileName": "maya",
                    "states": [
                        {
                            "imageUrl": "Happy",
                            "nextPoseDelay": 875
                        }
                    ],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 14
                },
                {
                    "id": 80,
                    "name": "Angry",
                    "idleImageUrl": "https://objection.lol/Images/Characters/14/Angry_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/14/Angry_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/80.png",
                    "order": 0,
                    "musicFileName": "allegro2004",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 14
                },
                {
                    "id": 81,
                    "name": "Crying",
                    "idleImageUrl": "https://objection.lol/Images/Characters/14/Cry_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/14/Cry_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/81.png",
                    "order": 0,
                    "musicFileName": "reminiscence",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 14
                },
                {
                    "id": 82,
                    "name": "Sad",
                    "idleImageUrl": "https://objection.lol/Images/Characters/14/Sad_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/14/Sad_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/82.png",
                    "order": 0,
                    "musicFileName": "reminiscence",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 14
                },
                {
                    "id": 83,
                    "name": "Determined",
                    "idleImageUrl": "https://objection.lol/Images/Characters/14/Determined_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/14/Determined_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/83.png",
                    "order": 0,
                    "musicFileName": "truth2002",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 14
                },
                {
                    "id": 84,
                    "name": "Smirk",
                    "idleImageUrl": "https://objection.lol/Images/Characters/14/Smirk_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/14/Smirk_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/84.png",
                    "order": 0,
                    "musicFileName": "maya",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 14
                },
                {
                    "id": 85,
                    "name": "Surprised",
                    "idleImageUrl": "https://objection.lol/Images/Characters/14/Surprised_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/14/Surprised_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/85.png",
                    "order": 0,
                    "musicFileName": "truth2001",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 14
                },
                {
                    "id": 86,
                    "name": "Worried",
                    "idleImageUrl": "https://objection.lol/Images/Characters/14/Worried_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/14/Worried_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/86.png",
                    "order": 0,
                    "musicFileName": "allegro2004",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 14
                },
                {
                    "id": 87,
                    "name": "Anguished",
                    "idleImageUrl": "https://objection.lol/Images/Characters/14/Anguished_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/14/Anguished_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/87.png",
                    "order": 0,
                    "musicFileName": "reminiscence",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 14
                },
                {
                    "id": 479,
                    "name": "Damage",
                    "idleImageUrl": "https://objection.lol/Images/Characters/14/Damage.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/14/Damage.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/479.png",
                    "order": 0,
                    "musicFileName": "allegro2001",
                    "states": [
                        {
                            "imageUrl": "Damage",
                            "nextPoseDelay": 1
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "yell2",
                            "volume": 0.9,
                            "time": 1
                        }
                    ],
                    "functionTicks": [
                        {
                            "functionName": "Flash",
                            "functionParam": "s",
                            "time": 1
                        }
                    ],
                    "characterId": 14
                }
            ]
        )
        DamonGant = _builtinCharacter(
            15,
            "Damon Gant",
            "Gant",
            _blips['male'],
            enums.CharacterLocation.WITNESS,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/15.png",
            [
                {
                    "id": 92,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/15/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/15/Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/92.png",
                    "order": 0,
                    "musicFileName": "gant",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 15
                },
                {
                    "id": 749,
                    "name": "Stand (eyes closed)",
                    "idleImageUrl": "https://objection.lol/Images/Characters/15/Stand2.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/15/Talk2.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/749.png",
                    "order": 0,
                    "musicFileName": "gant",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 15
                },
                {
                    "id": 93,
                    "name": "Smile",
                    "idleImageUrl": "https://objection.lol/Images/Characters/15/Smile.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/15/Smile_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/93.png",
                    "order": 0,
                    "musicFileName": "congratulations",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 15
                },
                {
                    "id": 94,
                    "name": "Clap",
                    "idleImageUrl": "https://objection.lol/Images/Characters/15/Smile.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/15/Clap.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/94.png",
                    "order": 0,
                    "musicFileName": "congratulations",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 15
                },
                {
                    "id": 95,
                    "name": "Wondering",
                    "idleImageUrl": "https://objection.lol/Images/Characters/15/Wondering.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/15/Wondering_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/95.png",
                    "order": 0,
                    "musicFileName": "gant",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 15
                },
                {
                    "id": 96,
                    "name": "Smirking",
                    "idleImageUrl": "https://objection.lol/Images/Characters/15/Smirk.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/15/Smirk_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/96.png",
                    "order": 0,
                    "musicFileName": "gant",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 15
                },
                {
                    "id": 97,
                    "name": "Impatient",
                    "idleImageUrl": "https://objection.lol/Images/Characters/15/Impatient.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/15/Impatient_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/97.png",
                    "order": 0,
                    "musicFileName": "allegro2001",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 15
                },
                {
                    "id": 98,
                    "name": "Cornered",
                    "idleImageUrl": "https://objection.lol/Images/Characters/15/Cornered.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/15/Cornered_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/98.png",
                    "order": 0,
                    "musicFileName": "crossexamining",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 15
                },
                {
                    "id": 99,
                    "name": "Damage",
                    "idleImageUrl": "https://objection.lol/Images/Characters/15/Damage.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/15/Damage.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/99.png",
                    "order": 0,
                    "musicFileName": "cornered",
                    "states": [
                        {
                            "imageUrl": "Cornered",
                            "nextPoseDelay": 800
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "damage2",
                            "time": 860,
                            "volume": 0.8
                        }
                    ],
                    "functionTicks": [
                        {
                            "functionName": "Shake",
                            "functionParam": "s",
                            "time": 880
                        },
                        {
                            "functionName": "Flash",
                            "functionParam": "m",
                            "time": 850
                        }
                    ],
                    "characterId": 15
                },
                {
                    "id": 311,
                    "name": "Breakdown (1)",
                    "idleImageUrl": "https://objection.lol/Images/Characters/15/Breakdown1.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/15/Breakdown1.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/311.png",
                    "order": 0,
                    "musicFileName": "truth2001",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 15
                },
                {
                    "id": 312,
                    "name": "Breakdown (2)",
                    "idleImageUrl": "https://objection.lol/Images/Characters/15/Breakdown2.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/15/Breakdown2.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/312.png",
                    "order": 0,
                    "musicFileName": "truth2001",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 15
                }
            ]
        )
        ReddWhite = _builtinCharacter(
            17,
            "Redd White",
            "White",
            _blips['male'],
            enums.CharacterLocation.WITNESS,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/17.png",
            [
                {
                    "id": 107,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/17/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/17/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/107.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 17
                },
                {
                    "id": 108,
                    "name": "Shrug",
                    "idleImageUrl": "https://objection.lol/Images/Characters/17/Shrug_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/17/Shrug_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/108.png",
                    "order": 0,
                    "musicFileName": "allegro2004",
                    "states": [
                        {
                            "imageUrl": "Shrug",
                            "nextPoseDelay": 900
                        }
                    ],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 17
                },
                {
                    "id": 109,
                    "name": "Anguished",
                    "idleImageUrl": "https://objection.lol/Images/Characters/17/Anguish_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/17/Anguish_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/109.png",
                    "order": 0,
                    "musicFileName": "allegro2001",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 17
                },
                {
                    "id": 110,
                    "name": "Arms Crossed",
                    "idleImageUrl": "https://objection.lol/Images/Characters/17/Arms_Crossed.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/17/Arms_Crossed_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/110.png",
                    "order": 0,
                    "musicFileName": "moderato2001",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 17
                },
                {
                    "id": 111,
                    "name": "Cornered",
                    "idleImageUrl": "https://objection.lol/Images/Characters/17/Cornered.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/17/Cornered_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/111.png",
                    "order": 0,
                    "musicFileName": "allegro2001",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 17
                },
                {
                    "id": 112,
                    "name": "Breakdown",
                    "idleImageUrl": "https://objection.lol/Images/Characters/17/Breakdown_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/17/.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/112.png",
                    "order": 0,
                    "musicFileName": "crossexamining",
                    "states": [
                        {
                            "imageUrl": "Breakdown",
                            "nextPoseDelay": 1
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "deskslam",
                            "time": 1785,
                            "volume": 0.8
                        }
                    ],
                    "functionTicks": [],
                    "characterId": 17
                },
                {
                    "id": 357,
                    "name": "Shine",
                    "idleImageUrl": "https://objection.lol/Images/Characters/17/Shine.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/17/Shine.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/357.png",
                    "order": 0,
                    "musicFileName": "truth2002",
                    "states": [
                        {
                            "imageUrl": "Shine",
                            "nextPoseDelay": 1
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "Sound/shiny",
                            "time": 300,
                            "volume": 0.8
                        }
                    ],
                    "functionTicks": [],
                    "characterId": 17
                }
            ]
        )
        LottaHart = _builtinCharacter(
            18,
            "Lotta Hart",
            "Lotta",
            _blips['female'],
            enums.CharacterLocation.WITNESS,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/18.png",
            [
                {
                    "id": 113,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/18/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/18/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/113.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 18
                },
                {
                    "id": 114,
                    "name": "Stand2",
                    "idleImageUrl": "https://objection.lol/Images/Characters/18/Stand2.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/18/Stand2_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/114.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 18
                },
                {
                    "id": 115,
                    "name": "Silly",
                    "idleImageUrl": "https://objection.lol/Images/Characters/18/Silly.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/18/Silly_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/115.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 18
                },
                {
                    "id": 116,
                    "name": "Relieved",
                    "idleImageUrl": "https://objection.lol/Images/Characters/18/Disappointed.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/18/Disappointed_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/116.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 18
                },
                {
                    "id": 117,
                    "name": "Smile",
                    "idleImageUrl": "https://objection.lol/Images/Characters/18/Smile.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/18/Smile_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/117.png",
                    "order": 0,
                    "musicFileName": "congratulations",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 18
                },
                {
                    "id": 118,
                    "name": "Angry",
                    "idleImageUrl": "https://objection.lol/Images/Characters/18/Angry.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/18/Angry_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/118.png",
                    "order": 0,
                    "musicFileName": "truth2002",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 18
                },
                {
                    "id": 119,
                    "name": "Stare",
                    "idleImageUrl": "https://objection.lol/Images/Characters/18/Stare.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/18/Stare_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/119.png",
                    "order": 0,
                    "musicFileName": "allegro2001",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 18
                },
                {
                    "id": 120,
                    "name": "Uncertain",
                    "idleImageUrl": "https://objection.lol/Images/Characters/18/Uncertain.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/18/Uncertain_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/120.png",
                    "order": 0,
                    "musicFileName": "allegro2001",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 18
                },
                {
                    "id": 478,
                    "name": "Damage",
                    "idleImageUrl": "https://objection.lol/Images/Characters/18/Damage.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/18/Damage.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/478.png",
                    "order": 0,
                    "musicFileName": "allegro2001",
                    "states": [
                        {
                            "imageUrl": "Damage",
                            "nextPoseDelay": 1
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "yell2",
                            "volume": 0.9,
                            "time": 1
                        }
                    ],
                    "functionTicks": [
                        {
                            "functionName": "Flash",
                            "functionParam": "s",
                            "time": 1
                        }
                    ],
                    "characterId": 18
                }
            ]
        )
        DickGumshoe = _builtinCharacter(
            21,
            "Dick Gumshoe",
            "Gumshoe",
            _blips['male'],
            enums.CharacterLocation.WITNESS,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/21.png",
            [
                {
                    "id": 130,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/21/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/21/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/130.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 21
                },
                {
                    "id": 131,
                    "name": "Confident",
                    "idleImageUrl": "https://objection.lol/Images/Characters/21/Confident.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/21/Confident_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/131.png",
                    "order": 0,
                    "musicFileName": "truth2002",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 21
                },
                {
                    "id": 132,
                    "name": "Giggle",
                    "idleImageUrl": "https://objection.lol/Images/Characters/21/Giggle.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/21/Giggle_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/132.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 21
                },
                {
                    "id": 133,
                    "name": "Pumped",
                    "idleImageUrl": "https://objection.lol/Images/Characters/21/Pumped.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/21/Pumped_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/133.png",
                    "order": 0,
                    "musicFileName": "moderato2001",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 21
                },
                {
                    "id": 134,
                    "name": "Sad",
                    "idleImageUrl": "https://objection.lol/Images/Characters/21/Sad.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/21/Sad_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/134.png",
                    "order": 0,
                    "musicFileName": "objection2004",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 21
                },
                {
                    "id": 135,
                    "name": "Stare",
                    "idleImageUrl": "https://objection.lol/Images/Characters/21/Stare.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/21/Stare_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/135.png",
                    "order": 0,
                    "musicFileName": "moderato2001",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 21
                },
                {
                    "id": 136,
                    "name": "Angry",
                    "idleImageUrl": "https://objection.lol/Images/Characters/21/Angry.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/21/Angry_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/136.png",
                    "order": 0,
                    "musicFileName": "truth2001",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 21
                },
                {
                    "id": 137,
                    "name": "Headscratch",
                    "idleImageUrl": "https://objection.lol/Images/Characters/21/Wonder.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/21/Wonder_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/137.png",
                    "order": 0,
                    "musicFileName": "truth2001",
                    "states": [
                        {
                            "imageUrl": "Headscratch",
                            "nextPoseDelay": 900
                        }
                    ],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 21
                }
            ]
        )
        EmaSkye = _builtinCharacter(
            22,
            "Ema Skye",
            "Ema",
            _blips['female'],
            enums.CharacterLocation.WITNESS,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/22.png",
            [
                {
                    "id": 142,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/22/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/22/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/142.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 22
                },
                {
                    "id": 143,
                    "name": "Happy",
                    "idleImageUrl": "https://objection.lol/Images/Characters/22/Happy.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/22/Happy_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/143.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 22
                },
                {
                    "id": 144,
                    "name": "Confident",
                    "idleImageUrl": "https://objection.lol/Images/Characters/22/Confident.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/22/Confident_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/144.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 22
                },
                {
                    "id": 145,
                    "name": "Think",
                    "idleImageUrl": "https://objection.lol/Images/Characters/22/Think.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/22/Think_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/145.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 22
                },
                {
                    "id": 146,
                    "name": "Surprised",
                    "idleImageUrl": "https://objection.lol/Images/Characters/22/Surprised.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/22/Surprised_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/146.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 22
                },
                {
                    "id": 147,
                    "name": "Worried",
                    "idleImageUrl": "https://objection.lol/Images/Characters/22/Worried.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/22/Worried_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/147.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 22
                },
                {
                    "id": 148,
                    "name": "Write",
                    "idleImageUrl": "https://objection.lol/Images/Characters/22/Write.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/22/Write_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/148.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 22
                },
                {
                    "id": 149,
                    "name": "Angry",
                    "idleImageUrl": "https://objection.lol/Images/Characters/22/Angry.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/22/Angry_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/149.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 22
                },
                {
                    "id": 150,
                    "name": "Determined",
                    "idleImageUrl": "https://objection.lol/Images/Characters/22/Determined.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/22/Determined_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/150.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 22
                },
                {
                    "id": 151,
                    "name": "Reminiscence",
                    "idleImageUrl": "https://objection.lol/Images/Characters/22/Reminiscence.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/22/Reminiscence_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/151.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 22
                },
                {
                    "id": 684,
                    "name": "Scared",
                    "idleImageUrl": "https://objection.lol/Images/Characters/22/Scared.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/22/Scared_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/684.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 22
                }
            ]
        )
        JakeMarshall = _builtinCharacter(
            23,
            "Jake Marshall",
            "Marshall",
            _blips['male'],
            enums.CharacterLocation.WITNESS,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/23.png",
            [
                {
                    "id": 152,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/23/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/23/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/152.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 23
                },
                {
                    "id": 153,
                    "name": "Point",
                    "idleImageUrl": "https://objection.lol/Images/Characters/23/Point.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/23/Point_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/153.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 23
                },
                {
                    "id": 154,
                    "name": "Drink (new bottle)",
                    "idleImageUrl": "https://objection.lol/Images/Characters/23/Drink_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/23/Drink_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/154.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [
                        {
                            "imageUrl": "Bottle_Cap",
                            "nextPoseDelay": 825
                        },
                        {
                            "imageUrl": "Drink",
                            "nextPoseDelay": 1200
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "chug",
                            "time": 925,
                            "volume": 0.75
                        },
                        {
                            "fileName": "chug",
                            "time": 1300,
                            "volume": 0.75
                        }
                    ],
                    "functionTicks": [],
                    "characterId": 23
                },
                {
                    "id": 155,
                    "name": "Drink",
                    "idleImageUrl": "https://objection.lol/Images/Characters/23/Drink_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/23/Drink_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/155.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [
                        {
                            "imageUrl": "Drink",
                            "nextPoseDelay": 1200
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "chug",
                            "time": 100,
                            "volume": 0.75
                        },
                        {
                            "fileName": "chug",
                            "time": 475,
                            "volume": 0.75
                        }
                    ],
                    "functionTicks": [],
                    "characterId": 23
                },
                {
                    "id": 156,
                    "name": "Hat Off",
                    "idleImageUrl": "https://objection.lol/Images/Characters/23/Hat.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/23/Hat_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/156.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 23
                },
                {
                    "id": 157,
                    "name": "Nervous",
                    "idleImageUrl": "https://objection.lol/Images/Characters/23/Nervous_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/23/Nervous_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/157.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [
                        {
                            "imageUrl": "Nervous",
                            "nextPoseDelay": 3725
                        }
                    ],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 23
                },
                {
                    "id": 159,
                    "name": "Serious",
                    "idleImageUrl": "https://objection.lol/Images/Characters/23/Serious.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/23/Serious_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/159.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 23
                },
                {
                    "id": 160,
                    "name": "Damage",
                    "idleImageUrl": "https://objection.lol/Images/Characters/23/Damage.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/23/Damage.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/160.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [
                        {
                            "fileName": "damage2",
                            "time": 50,
                            "volume": 0.9
                        }
                    ],
                    "functionTicks": [],
                    "characterId": 23
                },
                {
                    "id": 161,
                    "name": "Cornered",
                    "idleImageUrl": "https://objection.lol/Images/Characters/23/Damage_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/23/Damage_Stand.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/161.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 23
                },
                {
                    "id": 162,
                    "name": "Shave",
                    "idleImageUrl": "https://objection.lol/Images/Characters/23/Shave.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/23/Shave_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/162.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 23
                }
            ]
        )
        DahliaHawthorne = _builtinCharacter(
            24,
            "Dahlia Hawthorne",
            "Dahlia",
            _blips['female'],
            enums.CharacterLocation.WITNESS,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/24.png",
            [
                {
                    "id": 164,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/24/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/24/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/164.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 24
                },
                {
                    "id": 165,
                    "name": "Happy",
                    "idleImageUrl": "https://objection.lol/Images/Characters/24/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/24/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/165.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [
                        {
                            "imageUrl": "Happy",
                            "nextPoseDelay": 1000,
                            "playAtTextEnd": True
                        }
                    ],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 24
                },
                {
                    "id": 166,
                    "name": "Cry",
                    "idleImageUrl": "https://objection.lol/Images/Characters/24/Cry.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/24/Cry_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/166.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 24
                },
                {
                    "id": 167,
                    "name": "Nervous",
                    "idleImageUrl": "https://objection.lol/Images/Characters/24/Nervous.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/24/Nervous_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/167.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 24
                },
                {
                    "id": 168,
                    "name": "Uncertain",
                    "idleImageUrl": "https://objection.lol/Images/Characters/24/Uncertain.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/24/Uncertain_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/168.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 24
                },
                {
                    "id": 169,
                    "name": "Hair Play",
                    "idleImageUrl": "https://objection.lol/Images/Characters/24/Hair_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/24/Hair_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/169.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [
                        {
                            "imageUrl": "Hair_Stand",
                            "nextPoseDelay": 200
                        },
                        {
                            "imageUrl": "Hair",
                            "nextPoseDelay": 1300
                        }
                    ],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 24
                },
                {
                    "id": 170,
                    "name": "Look Away",
                    "idleImageUrl": "https://objection.lol/Images/Characters/24/Angry.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/24/Angry.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/170.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 24
                },
                {
                    "id": 171,
                    "name": "Damage",
                    "idleImageUrl": "https://objection.lol/Images/Characters/24/Damage.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/24/Damage.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/171.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [
                        {
                            "fileName": "damage2",
                            "time": 50,
                            "volume": 0.9
                        }
                    ],
                    "functionTicks": [],
                    "characterId": 24
                },
                {
                    "id": 172,
                    "name": "Angry",
                    "idleImageUrl": "https://objection.lol/Images/Characters/24/Angry_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/24/Angry_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/172.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 24
                }
            ]
        )
        LanaSkye = _builtinCharacter(
            26,
            "Lana Skye",
            "Lana",
            _blips['female'],
            enums.CharacterLocation.WITNESS,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/26.png",
            [
                {
                    "id": 194,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/26/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/26/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/194.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 26
                },
                {
                    "id": 195,
                    "name": "Stand2",
                    "idleImageUrl": "https://objection.lol/Images/Characters/26/Stand2.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/26/Stand2_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/195.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 26
                },
                {
                    "id": 196,
                    "name": "Stand3",
                    "idleImageUrl": "https://objection.lol/Images/Characters/26/Stand3.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/26/Stand3_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/196.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 26
                },
                {
                    "id": 197,
                    "name": "Cornered",
                    "idleImageUrl": "https://objection.lol/Images/Characters/26/Cornered.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/26/Cornered_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/197.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 26
                },
                {
                    "id": 198,
                    "name": "Damage",
                    "idleImageUrl": "https://objection.lol/Images/Characters/26/Cornered.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/26/Cornered_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/198.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [
                        {
                            "imageUrl": "Damage",
                            "nextPoseDelay": 600
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "damage",
                            "time": 50,
                            "volume": 0.9
                        }
                    ],
                    "functionTicks": [
                        {
                            "functionName": "Flash",
                            "functionParam": "s",
                            "time": 50
                        }
                    ],
                    "characterId": 26
                },
                {
                    "id": 199,
                    "name": "Surprised",
                    "idleImageUrl": "https://objection.lol/Images/Characters/26/Surprised.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/26/Surprised_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/199.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 26
                },
                {
                    "id": 200,
                    "name": "Face Side",
                    "idleImageUrl": "https://objection.lol/Images/Characters/26/Side.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/26/Side_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/200.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 26
                },
                {
                    "id": 201,
                    "name": "Face Behind",
                    "idleImageUrl": "https://objection.lol/Images/Characters/26/Behind.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/26/Behind.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/201.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 26
                },
                {
                    "id": 202,
                    "name": "Face Behind (movement)",
                    "idleImageUrl": "https://objection.lol/Images/Characters/26/Behind.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/26/Behind.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/202.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [
                        {
                            "imageUrl": "Face Behind (movement)",
                            "nextPoseDelay": 800
                        }
                    ],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 26
                },
                {
                    "id": 203,
                    "name": "Face Front (movement)",
                    "idleImageUrl": "https://objection.lol/Images/Characters/26/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/26/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/203.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [
                        {
                            "imageUrl": "Face Front (movement)",
                            "nextPoseDelay": 800
                        }
                    ],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 26
                },
                {
                    "id": 204,
                    "name": "Happy",
                    "idleImageUrl": "https://objection.lol/Images/Characters/26/Happy.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/26/Happy_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/204.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 26
                },
                {
                    "id": 205,
                    "name": "Serious",
                    "idleImageUrl": "https://objection.lol/Images/Characters/26/Serious.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/26/Serious_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/205.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 26
                }
            ]
        )
        LarryButz = _builtinCharacter(
            27,
            "Larry Butz",
            "Butz",
            _blips['male'],
            enums.CharacterLocation.WITNESS,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/27.png",
            [
                {
                    "id": 206,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/27/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/27/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/206.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 27
                },
                {
                    "id": 207,
                    "name": "Happy",
                    "idleImageUrl": "https://objection.lol/Images/Characters/27/Happy.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/27/Happy_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/207.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 27
                },
                {
                    "id": 208,
                    "name": "Think",
                    "idleImageUrl": "https://objection.lol/Images/Characters/27/Think.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/27/Think_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/208.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 27
                },
                {
                    "id": 209,
                    "name": "Think 2",
                    "idleImageUrl": "https://objection.lol/Images/Characters/27/Think2.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/27/Think2_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/209.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 27
                },
                {
                    "id": 210,
                    "name": "Cry",
                    "idleImageUrl": "https://objection.lol/Images/Characters/27/Cry.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/27/Cry_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/210.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 27
                },
                {
                    "id": 211,
                    "name": "Cornered",
                    "idleImageUrl": "https://objection.lol/Images/Characters/27/Cornered.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/27/Cornered_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/211.png",
                    "order": 0,
                    "musicFileName": "truth2002",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 27
                },
                {
                    "id": 212,
                    "name": "Nervous",
                    "idleImageUrl": "https://objection.lol/Images/Characters/27/Nervous.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/27/Nervous_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/212.png",
                    "order": 0,
                    "musicFileName": "allegro2001",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 27
                },
                {
                    "id": 213,
                    "name": "Thumbs Up",
                    "idleImageUrl": "https://objection.lol/Images/Characters/27/Thumbs.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/27/Thumbs_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/213.png",
                    "order": 0,
                    "musicFileName": "allegro2001",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 27
                },
                {
                    "id": 214,
                    "name": "Surprised",
                    "idleImageUrl": "https://objection.lol/Images/Characters/27/Surprised.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/27/Surprised_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/214.png",
                    "order": 0,
                    "musicFileName": "allegro2001",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 27
                }
            ]
        )
        MilesEdgeworth = _builtinCharacter(
            29,
            "Miles Edgeworth",
            "Edgeworth",
            _blips['male'],
            enums.CharacterLocation.WITNESS,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/29.png",
            [
                {
                    "id": 220,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/29/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/29/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/220.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 29
                },
                {
                    "id": 221,
                    "name": "Angry",
                    "idleImageUrl": "https://objection.lol/Images/Characters/29/Angry.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/29/Angry_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/221.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 29
                },
                {
                    "id": 222,
                    "name": "Stare",
                    "idleImageUrl": "https://objection.lol/Images/Characters/29/Stare.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/29/Stare_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/222.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 29
                },
                {
                    "id": 223,
                    "name": "Wonder",
                    "idleImageUrl": "https://objection.lol/Images/Characters/29/Wonder.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/29/Wonder_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/223.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 29
                },
                {
                    "id": 224,
                    "name": "Smirk",
                    "idleImageUrl": "https://objection.lol/Images/Characters/29/Smirk.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/29/Smirk_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/224.png",
                    "order": 0,
                    "musicFileName": "congratulations",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 29
                },
                {
                    "id": 225,
                    "name": "Arms Crossed",
                    "idleImageUrl": "https://objection.lol/Images/Characters/29/Arms_Crossed.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/29/Arms_Crossed_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/225.png",
                    "order": 0,
                    "musicFileName": "truth2002",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 29
                },
                {
                    "id": 226,
                    "name": "Reminiscence",
                    "idleImageUrl": "https://objection.lol/Images/Characters/29/Reminiscence.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/29/Reminiscence_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/226.png",
                    "order": 0,
                    "musicFileName": "allegro2001",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 29
                },
                {
                    "id": 227,
                    "name": "Point",
                    "idleImageUrl": "https://objection.lol/Images/Characters/29/Point.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/29/Point.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/227.png",
                    "order": 0,
                    "musicFileName": "allegro2001",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 29
                },
                {
                    "id": 418,
                    "name": "Smug",
                    "idleImageUrl": "https://objection.lol/Images/Characters/29/Smug.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/29/Smug_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/418.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 29
                }
            ],
            {
                "1": "https://objection.lol/Audio/Vocal/1/29.mp3",
                "2": "https://objection.lol/Audio/Vocal/2/29.mp3",
                "3": "https://objection.lol/Audio/Vocal/3/29.mp3",
                "5": "https://objection.lol/Audio/Vocal/5/29.mp3"
            }
        )
        WendyOldbag = _builtinCharacter(
            30,
            "Wendy Oldbag",
            "Oldbag",
            _blips['female'],
            enums.CharacterLocation.WITNESS,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/30.png",
            [
                {
                    "id": 228,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/30/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/30/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/228.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 30
                },
                {
                    "id": 229,
                    "name": "Angry",
                    "idleImageUrl": "https://objection.lol/Images/Characters/30/Angry.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/30/Angry_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/229.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 30
                },
                {
                    "id": 230,
                    "name": "Confident",
                    "idleImageUrl": "https://objection.lol/Images/Characters/30/Confident.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/30/Confident_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/230.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 30
                },
                {
                    "id": 231,
                    "name": "Wave",
                    "idleImageUrl": "https://objection.lol/Images/Characters/30/Wave.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/30/Wave_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/231.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 30
                },
                {
                    "id": 232,
                    "name": "Damage",
                    "idleImageUrl": "https://objection.lol/Images/Characters/30/Damage.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/30/Damage.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/232.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [
                        {
                            "imageUrl": "Damage",
                            "nextPoseDelay": 200
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "damage",
                            "time": 50,
                            "volume": 0.8
                        }
                    ],
                    "functionTicks": [
                        {
                            "functionName": "Flash",
                            "functionParam": "m",
                            "time": 50
                        }
                    ],
                    "characterId": 30
                },
                {
                    "id": 233,
                    "name": "In Love",
                    "idleImageUrl": "https://objection.lol/Images/Characters/30/Inlove.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/30/Inlove_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/233.png",
                    "order": 0,
                    "musicFileName": "truth2002",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 30
                }
            ]
        )
        LukeAtmey = _builtinCharacter(
            31,
            "Luke Atmey",
            "Atmey",
            _blips['male'],
            enums.CharacterLocation.WITNESS,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/31.png",
            [
                {
                    "id": 234,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/31/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/31/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/234.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 31
                },
                {
                    "id": 235,
                    "name": "Shine Ring",
                    "idleImageUrl": "https://objection.lol/Images/Characters/31/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/31/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/235.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [
                        {
                            "imageUrl": "Ring",
                            "nextPoseDelay": 500
                        }
                    ],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 31
                },
                {
                    "id": 236,
                    "name": "Look Up",
                    "idleImageUrl": "https://objection.lol/Images/Characters/31/LookUp.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/31/LookUp_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/236.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 31
                },
                {
                    "id": 237,
                    "name": "Magnify",
                    "idleImageUrl": "https://objection.lol/Images/Characters/31/Magnify_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/31/Magnify_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/237.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [
                        {
                            "imageUrl": "Magnify",
                            "nextPoseDelay": 700
                        }
                    ],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 31
                },
                {
                    "id": 238,
                    "name": "Cornered",
                    "idleImageUrl": "https://objection.lol/Images/Characters/31/Cornered.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/31/Cornered_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/238.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 31
                },
                {
                    "id": 239,
                    "name": "Damage",
                    "idleImageUrl": "https://objection.lol/Images/Characters/31/Damage.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/31/Damage.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/239.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [
                        {
                            "imageUrl": "Damage",
                            "nextPoseDelay": 50
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "damage2",
                            "time": 50,
                            "volume": 0.8
                        }
                    ],
                    "functionTicks": [
                        {
                            "functionName": "Flash",
                            "functionParam": "m",
                            "time": 50
                        },
                        {
                            "functionName": "Shake",
                            "functionParam": "s",
                            "time": 50
                        }
                    ],
                    "characterId": 31
                },
                {
                    "id": 240,
                    "name": "Wipe Magnifier",
                    "idleImageUrl": "https://objection.lol/Images/Characters/31/Wipe.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/31/Wipe_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/240.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 31
                },
                {
                    "id": 241,
                    "name": "Crazy",
                    "idleImageUrl": "https://objection.lol/Images/Characters/31/Crazy.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/31/Crazy_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/241.png",
                    "order": 0,
                    "musicFileName": "truth2002",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 31
                },
                {
                    "id": 242,
                    "name": "Laugh",
                    "idleImageUrl": "https://objection.lol/Images/Characters/31/Laugh.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/31/Laugh.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/242.png",
                    "order": 0,
                    "musicFileName": "truth2002",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 31
                },
                {
                    "id": 243,
                    "name": "Breakdown",
                    "idleImageUrl": "https://objection.lol/Images/Characters/31/Laugh.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/31/Laugh.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/243.png",
                    "order": 0,
                    "musicFileName": "truth2002",
                    "states": [
                        {
                            "imageUrl": "Rise",
                            "nextPoseDelay": 4638
                        },
                        {
                            "imageUrl": "PostRise",
                            "nextPoseDelay": 200
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "earthquake",
                            "time": 1,
                            "volume": 0.85
                        }
                    ],
                    "functionTicks": [
                        {
                            "functionName": "Rise",
                            "time": 0
                        }
                    ],
                    "characterId": 31
                }
            ]
        )
        IniMiney = _builtinCharacter(
            32,
            "Ini Miney",
            "Ini",
            _blips['female'],
            enums.CharacterLocation.WITNESS,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/32.png",
            [
                {
                    "id": 245,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/32/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/32/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/245.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 32
                },
                {
                    "id": 246,
                    "name": "Think",
                    "idleImageUrl": "https://objection.lol/Images/Characters/32/Think.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/32/Think_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/246.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 32
                },
                {
                    "id": 247,
                    "name": "Silly",
                    "idleImageUrl": "https://objection.lol/Images/Characters/32/Silly.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/32/Silly_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/247.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 32
                },
                {
                    "id": 248,
                    "name": "Confident",
                    "idleImageUrl": "https://objection.lol/Images/Characters/32/Confident.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/32/Confident_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/248.png",
                    "order": 0,
                    "musicFileName": "crossexaminingvariation",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 32
                },
                {
                    "id": 249,
                    "name": "Damage",
                    "idleImageUrl": "https://objection.lol/Images/Characters/32/Damage.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/32/Damage.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/249.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 32
                },
                {
                    "id": 250,
                    "name": "Cornered",
                    "idleImageUrl": "https://objection.lol/Images/Characters/32/Cornered.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/32/Cornered_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/250.png",
                    "order": 0,
                    "musicFileName": "allegro2001",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 32
                },
                {
                    "id": 251,
                    "name": "Angry",
                    "idleImageUrl": "https://objection.lol/Images/Characters/32/Angry.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/32/Angry_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/251.png",
                    "order": 0,
                    "musicFileName": "allegro2001",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 32
                },
                {
                    "id": 252,
                    "name": "Sad",
                    "idleImageUrl": "https://objection.lol/Images/Characters/32/Sad.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/32/Sad_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/252.png",
                    "order": 0,
                    "musicFileName": "allegro2001",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 32
                },
                {
                    "id": 480,
                    "name": "Possessed",
                    "idleImageUrl": "https://objection.lol/Images/Characters/32/Possessed.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/32/Possessed.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/480.png",
                    "order": 0,
                    "musicFileName": "allegro2001",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 32
                }
            ]
        )
        MattEngarde = _builtinCharacter(
            33,
            "Matt Engarde",
            "Engarde",
            _blips['male'],
            enums.CharacterLocation.WITNESS,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/33.png",
            [
                {
                    "id": 253,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/33/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/33/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/253.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 33
                },
                {
                    "id": 254,
                    "name": "Uncertain",
                    "idleImageUrl": "https://objection.lol/Images/Characters/33/Uncertain.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/33/Uncertain_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/254.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 33
                },
                {
                    "id": 255,
                    "name": "Call",
                    "idleImageUrl": "https://objection.lol/Images/Characters/33/Call_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/33/Call_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/255.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [
                        {
                            "imageUrl": "Call",
                            "nextPoseDelay": 1075
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "call",
                            "time": 1075,
                            "volume": 0.85
                        }
                    ],
                    "functionTicks": [],
                    "characterId": 33
                },
                {
                    "id": 256,
                    "name": "On Call",
                    "idleImageUrl": "https://objection.lol/Images/Characters/33/Phone.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/33/Phone_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/256.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 33
                },
                {
                    "id": 257,
                    "name": "Evil",
                    "idleImageUrl": "https://objection.lol/Images/Characters/33/Evil_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/33/Evil_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/257.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [
                        {
                            "imageUrl": "Evil",
                            "nextPoseDelay": 1200
                        }
                    ],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 33
                },
                {
                    "id": 258,
                    "name": "Laugh",
                    "idleImageUrl": "https://objection.lol/Images/Characters/33/Laugh.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/33/Laugh_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/258.png",
                    "order": 0,
                    "musicFileName": "allegro2001",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 33
                },
                {
                    "id": 259,
                    "name": "Cornered",
                    "idleImageUrl": "https://objection.lol/Images/Characters/33/Cornered.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/33/Cornered_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/259.png",
                    "order": 0,
                    "musicFileName": "allegro2001",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 33
                },
                {
                    "id": 260,
                    "name": "Breakdown",
                    "idleImageUrl": "https://objection.lol/Images/Characters/33/Breakdown.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/33/Breakdown.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/260.png",
                    "order": 0,
                    "musicFileName": "allegro2001",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 33
                }
            ]
        )
        Iris = _builtinCharacter(
            34,
            "Iris",
            "Iris",
            _blips['female'],
            enums.CharacterLocation.WITNESS,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/34.png",
            [
                {
                    "id": 261,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/34/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/34/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/261.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 34
                },
                {
                    "id": 262,
                    "name": "Uncertain",
                    "idleImageUrl": "https://objection.lol/Images/Characters/34/Uncertain.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/34/Uncertain_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/262.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 34
                },
                {
                    "id": 263,
                    "name": "Surprised",
                    "idleImageUrl": "https://objection.lol/Images/Characters/34/Surprised.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/34/Surprised_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/263.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 34
                },
                {
                    "id": 264,
                    "name": "Cry",
                    "idleImageUrl": "https://objection.lol/Images/Characters/34/Cry.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/34/Cry_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/264.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 34
                },
                {
                    "id": 265,
                    "name": "Happy",
                    "idleImageUrl": "https://objection.lol/Images/Characters/34/Happy.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/34/Happy_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/265.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 34
                },
                {
                    "id": 266,
                    "name": "Neutral",
                    "idleImageUrl": "https://objection.lol/Images/Characters/34/Neutral.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/34/Neutral_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/266.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 34
                },
                {
                    "id": 267,
                    "name": "Smirk",
                    "idleImageUrl": "https://objection.lol/Images/Characters/34/Smirk.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/34/Smirk_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/267.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 34
                },
                {
                    "id": 268,
                    "name": "Damage",
                    "idleImageUrl": "https://objection.lol/Images/Characters/34/Damage.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/34/Damage.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/268.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 34
                },
                {
                    "id": 269,
                    "name": "Cornered",
                    "idleImageUrl": "https://objection.lol/Images/Characters/34/Cornered.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/34/Cornered_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/269.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 34
                },
                {
                    "id": 270,
                    "name": "Angry",
                    "idleImageUrl": "https://objection.lol/Images/Characters/34/Angry.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/34/Angry_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/270.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 34
                },
                {
                    "id": 485,
                    "name": "Hair Play",
                    "idleImageUrl": "https://objection.lol/Images/Characters/34/Hair_Play.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/34/Hair_Play.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/485.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 34
                },
                {
                    "id": 486,
                    "name": "Broken",
                    "idleImageUrl": "https://objection.lol/Images/Characters/34/Broken.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/34/Broken.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/486.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 34
                },
                {
                    "id": 487,
                    "name": "Maya",
                    "idleImageUrl": "https://objection.lol/Images/Characters/34/Maya_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/34/Maya_Stand.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/487.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [
                        {
                            "imageUrl": "Maya",
                            "nextPoseDelay": 1200,
                            "playAtTextEnd": True
                        }
                    ],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 34
                },
                {
                    "id": 488,
                    "name": "Maya (2)",
                    "idleImageUrl": "https://objection.lol/Images/Characters/34/Maya2.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/34/Maya2_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/488.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 34
                }
            ]
        )
        CodyHackins = _builtinCharacter(
            35,
            "Cody Hackins",
            "Cody",
            _blips['male'],
            enums.CharacterLocation.WITNESS,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/35.png",
            [
                {
                    "id": 276,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/35/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/35/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/276.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 35
                },
                {
                    "id": 277,
                    "name": "Annoyed",
                    "idleImageUrl": "https://objection.lol/Images/Characters/35/Annoyed.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/35/Annoyed_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/277.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 35
                },
                {
                    "id": 278,
                    "name": "Surprised",
                    "idleImageUrl": "https://objection.lol/Images/Characters/35/Surprised.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/35/Surprised.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/278.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 35
                },
                {
                    "id": 279,
                    "name": "Sad",
                    "idleImageUrl": "https://objection.lol/Images/Characters/35/Sad.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/35/Sad_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/279.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 35
                },
                {
                    "id": 280,
                    "name": "Cry",
                    "idleImageUrl": "https://objection.lol/Images/Characters/35/Cry.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/35/Cry.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/280.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 35
                },
                {
                    "id": 281,
                    "name": "Crying",
                    "idleImageUrl": "https://objection.lol/Images/Characters/35/Crying.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/35/Crying_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/281.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 35
                },
                {
                    "id": 282,
                    "name": "Confident",
                    "idleImageUrl": "https://objection.lol/Images/Characters/35/Confident.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/35/Confident_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/282.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 35
                },
                {
                    "id": 283,
                    "name": "Angry",
                    "idleImageUrl": "https://objection.lol/Images/Characters/35/Angry.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/35/Angry_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/283.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 35
                },
                {
                    "id": 284,
                    "name": "Happy",
                    "idleImageUrl": "https://objection.lol/Images/Characters/35/Happy.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/35/Happy_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/284.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 35
                }
            ]
        )
        FurioTigre = _builtinCharacter(
            36,
            "Furio Tigre",
            "Tigre",
            _blips['male'],
            enums.CharacterLocation.WITNESS,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/36.png",
            [
                {
                    "id": 285,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/36/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/36/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/285.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 36
                },
                {
                    "id": 286,
                    "name": "Shameless",
                    "idleImageUrl": "https://objection.lol/Images/Characters/36/Shameless.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/36/Shameless_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/286.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 36
                },
                {
                    "id": 287,
                    "name": "Angry",
                    "idleImageUrl": "https://objection.lol/Images/Characters/36/Angry.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/36/Angry_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/287.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 36
                },
                {
                    "id": 288,
                    "name": "Compliant",
                    "idleImageUrl": "https://objection.lol/Images/Characters/36/Compliant.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/36/Compliant_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/288.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 36
                },
                {
                    "id": 289,
                    "name": "Roar",
                    "idleImageUrl": "https://objection.lol/Images/Characters/36/Roar.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/36/Roar.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/289.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 36
                },
                {
                    "id": 290,
                    "name": "Cornered",
                    "idleImageUrl": "https://objection.lol/Images/Characters/36/Cornered.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/36/Cornered_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/290.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 36
                },
                {
                    "id": 291,
                    "name": "Simper",
                    "idleImageUrl": "https://objection.lol/Images/Characters/36/Simper.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/36/Simper_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/291.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 36
                },
                {
                    "id": 292,
                    "name": "Breakdown (1)",
                    "idleImageUrl": "https://objection.lol/Images/Characters/36/Breakdown_1.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/36/Breakdown_1.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/292.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 36
                },
                {
                    "id": 293,
                    "name": "Breakdown (2)",
                    "idleImageUrl": "https://objection.lol/Images/Characters/36/Breakdown_2.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/36/Breakdown_2.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/293.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 36
                }
            ]
        )
        ReginaBerry = _builtinCharacter(
            37,
            "Regina Berry",
            "Regina",
            _blips['female'],
            enums.CharacterLocation.WITNESS,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/37.png",
            [
                {
                    "id": 294,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/37/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/37/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/294.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 37
                },
                {
                    "id": 295,
                    "name": "Point",
                    "idleImageUrl": "https://objection.lol/Images/Characters/37/Point.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/37/Point_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/295.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 37
                },
                {
                    "id": 296,
                    "name": "Happy",
                    "idleImageUrl": "https://objection.lol/Images/Characters/37/Happy.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/37/Happy_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/296.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 37
                },
                {
                    "id": 297,
                    "name": "Sparkle",
                    "idleImageUrl": "https://objection.lol/Images/Characters/37/Sparkle.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/37/Sparkle_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/297.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 37
                },
                {
                    "id": 298,
                    "name": "Sparkle 2",
                    "idleImageUrl": "https://objection.lol/Images/Characters/37/Sparkle_2.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/37/Sparkle_2.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/298.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 37
                },
                {
                    "id": 299,
                    "name": "Think",
                    "idleImageUrl": "https://objection.lol/Images/Characters/37/Think.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/37/Think_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/299.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 37
                },
                {
                    "id": 300,
                    "name": "Sad",
                    "idleImageUrl": "https://objection.lol/Images/Characters/37/Sad.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/37/Sad_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/300.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 37
                },
                {
                    "id": 301,
                    "name": "Cry",
                    "idleImageUrl": "https://objection.lol/Images/Characters/37/Cry.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/37/Cry.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/301.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 37
                }
            ]
        )
        Polly = _builtinCharacter(
            38,
            "Polly",
            "Parrot",
            _blips['male'],
            enums.CharacterLocation.WITNESS,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/38.png",
            [
                {
                    "id": 302,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/38/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/38/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/302.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 38
                }
            ]
        )
        PhoenixWright = _builtinCharacter(
            39,
            "Phoenix Wright",
            "Phoenix",
            _blips['male'],
            enums.CharacterLocation.WITNESS,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/39.png",
            [
                {
                    "id": 303,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/39/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/39/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/303.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 39
                },
                {
                    "id": 304,
                    "name": "Neutral",
                    "idleImageUrl": "https://objection.lol/Images/Characters/39/Neutral.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/39/Neutral_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/304.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 39
                },
                {
                    "id": 305,
                    "name": "Sad",
                    "idleImageUrl": "https://objection.lol/Images/Characters/39/Sad.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/39/Sad_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/305.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 39
                },
                {
                    "id": 306,
                    "name": "Sneeze",
                    "idleImageUrl": "https://objection.lol/Images/Characters/39/Sneeze.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/39/Sneeze.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/306.png",
                    "order": 0,
                    "musicFileName": "crossexaminingvariation",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 39
                },
                {
                    "id": 307,
                    "name": "Serious",
                    "idleImageUrl": "https://objection.lol/Images/Characters/39/Serious.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/39/Serious_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/307.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [
                        {
                            "imageUrl": "Serious_End",
                            "nextPoseDelay": 500,
                            "playAtTextEnd": True
                        },
                        {
                            "imageUrl": "Serious",
                            "nextPoseDelay": 50,
                            "playAtTextEnd": True
                        }
                    ],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 39
                },
                {
                    "id": 308,
                    "name": "Cry",
                    "idleImageUrl": "https://objection.lol/Images/Characters/39/Cry.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/39/Cry.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/308.png",
                    "order": 0,
                    "musicFileName": "allegro2001",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 39
                }
            ]
        )
        AprilMay = _builtinCharacter(
            40,
            "April May",
            "April",
            _blips['female'],
            enums.CharacterLocation.WITNESS,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/40.png",
            [
                {
                    "id": 313,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/40/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/40/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/313.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 40
                },
                {
                    "id": 314,
                    "name": "Wink",
                    "idleImageUrl": "https://objection.lol/Images/Characters/40/Wink.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/40/Wink.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/314.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 40
                },
                {
                    "id": 315,
                    "name": "Think",
                    "idleImageUrl": "https://objection.lol/Images/Characters/40/Think.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/40/Think_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/315.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 40
                },
                {
                    "id": 316,
                    "name": "Scared",
                    "idleImageUrl": "https://objection.lol/Images/Characters/40/Scared.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/40/Scared_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/316.png",
                    "order": 0,
                    "musicFileName": "crossexaminingvariation",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 40
                },
                {
                    "id": 317,
                    "name": "Cry",
                    "idleImageUrl": "https://objection.lol/Images/Characters/40/Cry.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/40/Cry.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/317.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 40
                },
                {
                    "id": 318,
                    "name": "Annoyed",
                    "idleImageUrl": "https://objection.lol/Images/Characters/40/Annoyed.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/40/Annoyed_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/318.png",
                    "order": 0,
                    "musicFileName": "allegro2001",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 40
                },
                {
                    "id": 319,
                    "name": "Rage",
                    "idleImageUrl": "https://objection.lol/Images/Characters/40/Rage.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/40/Rage.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/319.png",
                    "order": 0,
                    "musicFileName": "allegro2001",
                    "states": [
                        {
                            "imageUrl": "Rage",
                            "nextPoseDelay": 1,
                            "playAtTextEnd": True
                        }
                    ],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 40
                },
                {
                    "id": 320,
                    "name": "Angry",
                    "idleImageUrl": "https://objection.lol/Images/Characters/40/Angry.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/40/Angry_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/320.png",
                    "order": 0,
                    "musicFileName": "allegro2001",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 40
                },
                {
                    "id": 321,
                    "name": "Angry Look Away",
                    "idleImageUrl": "https://objection.lol/Images/Characters/40/Angry Look Away.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/40/Angry Look Away_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/321.png",
                    "order": 0,
                    "musicFileName": "allegro2001",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 40
                },
                {
                    "id": 481,
                    "name": "Angry Stare",
                    "idleImageUrl": "https://objection.lol/Images/Characters/40/Annoyed_Angry.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/40/Annoyed_Angry.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/481.png",
                    "order": 0,
                    "musicFileName": "allegro2001",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 40
                }
            ]
        )
        Acro = _builtinCharacter(
            41,
            "Acro",
            "Acro",
            _blips['male'],
            enums.CharacterLocation.WITNESS,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/41.png",
            [
                {
                    "id": 322,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/41/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/41/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/322.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 41
                },
                {
                    "id": 323,
                    "name": "Sad",
                    "idleImageUrl": "https://objection.lol/Images/Characters/41/Sad.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/41/Sad_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/323.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 41
                },
                {
                    "id": 324,
                    "name": "Serious",
                    "idleImageUrl": "https://objection.lol/Images/Characters/41/Serious.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/41/Serious_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/324.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 41
                },
                {
                    "id": 325,
                    "name": "Smile",
                    "idleImageUrl": "https://objection.lol/Images/Characters/41/Smile.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/41/Smile_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/325.png",
                    "order": 0,
                    "musicFileName": "crossexaminingvariation",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 41
                },
                {
                    "id": 326,
                    "name": "Cry",
                    "idleImageUrl": "https://objection.lol/Images/Characters/41/Cry_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/41/Cry_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/326.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [
                        {
                            "imageUrl": "Cry",
                            "nextPoseDelay": 900
                        }
                    ],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 41
                }
            ]
        )
        ShellyDeKillerRadio = _builtinCharacter(
            42,
            "Shelly de Killer (radio)",
            "de Killer",
            _blips['male'],
            enums.CharacterLocation.WITNESS,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/42.png",
            [
                {
                    "id": 327,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/42/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/42/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/327.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 42
                },
                {
                    "id": 328,
                    "name": "Angry",
                    "idleImageUrl": "https://objection.lol/Images/Characters/42/Angry.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/42/Angry_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/328.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 42
                },
                {
                    "id": 329,
                    "name": "Cornered",
                    "idleImageUrl": "https://objection.lol/Images/Characters/42/Cornered.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/42/Cornered_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/329.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 42
                },
                {
                    "id": 330,
                    "name": "Break",
                    "idleImageUrl": "https://objection.lol/Images/Characters/42/Break.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/42/Break.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/330.png",
                    "order": 0,
                    "musicFileName": "crossexaminingvariation",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 42
                }
            ]
        )
        RonDeLite = _builtinCharacter(
            43,
            "Ron DeLite",
            "Ron",
            _blips['male'],
            enums.CharacterLocation.WITNESS,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/43.png",
            [
                {
                    "id": 331,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/43/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/43/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/331.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 43
                },
                {
                    "id": 332,
                    "name": "Think",
                    "idleImageUrl": "https://objection.lol/Images/Characters/43/Think.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/43/Think_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/332.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 43
                },
                {
                    "id": 333,
                    "name": "Sad",
                    "idleImageUrl": "https://objection.lol/Images/Characters/43/Sad.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/43/Sad_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/333.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 43
                },
                {
                    "id": 334,
                    "name": "Cornered",
                    "idleImageUrl": "https://objection.lol/Images/Characters/43/Cornered.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/43/Cornered_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/334.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 43
                },
                {
                    "id": 335,
                    "name": "Serious",
                    "idleImageUrl": "https://objection.lol/Images/Characters/43/Serious.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/43/Serious_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/335.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 43
                },
                {
                    "id": 336,
                    "name": "Shout",
                    "idleImageUrl": "https://objection.lol/Images/Characters/43/Shout.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/43/Shout_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/336.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 43
                },
                {
                    "id": 337,
                    "name": "Shout 2",
                    "idleImageUrl": "https://objection.lol/Images/Characters/43/Shout2.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/43/Shout2.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/337.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 43
                }
            ]
        )
        YanniYogi = _builtinCharacter(
            44,
            "Yanni Yogi",
            "Caretaker",
            _blips['male'],
            enums.CharacterLocation.WITNESS,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/44.png",
            [
                {
                    "id": 338,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/44/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/44/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/338.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 44
                },
                {
                    "id": 339,
                    "name": "Think",
                    "idleImageUrl": "https://objection.lol/Images/Characters/44/Think.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/44/Think_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/339.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 44
                },
                {
                    "id": 340,
                    "name": "Look Away",
                    "idleImageUrl": "https://objection.lol/Images/Characters/44/Look Away.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/44/Look Away_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/340.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 44
                },
                {
                    "id": 341,
                    "name": "Sleep",
                    "idleImageUrl": "https://objection.lol/Images/Characters/44/Sleep_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/44/Sleep_Stand.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/341.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [
                        {
                            "imageUrl": "Sleep",
                            "nextPoseDelay": 700
                        }
                    ],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 44
                },
                {
                    "id": 342,
                    "name": "Wake up",
                    "idleImageUrl": "https://objection.lol/Images/Characters/44/Wakeup.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/44/Wakeup.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/342.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [
                        {
                            "imageUrl": "Wakeup",
                            "nextPoseDelay": 1700
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "gavel",
                            "time": 1050,
                            "volume": 0.7
                        }
                    ],
                    "functionTicks": [],
                    "characterId": 44
                },
                {
                    "id": 343,
                    "name": "Angry",
                    "idleImageUrl": "https://objection.lol/Images/Characters/44/Angry.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/44/Angry_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/343.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 44
                },
                {
                    "id": 344,
                    "name": "Fall",
                    "idleImageUrl": "https://objection.lol/Images/Characters/44/Angry.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/44/Angry_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/344.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [
                        {
                            "imageUrl": "Fall",
                            "nextPoseDelay": 1200,
                            "playAtTextEnd": True
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "fall",
                            "time": 1000,
                            "volume": 0.8,
                            "playAtTextEnd": True
                        }
                    ],
                    "functionTicks": [],
                    "characterId": 44
                },
                {
                    "id": 345,
                    "name": "Serious",
                    "idleImageUrl": "https://objection.lol/Images/Characters/44/Serious.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/44/Serious_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/345.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 44
                },
                {
                    "id": 346,
                    "name": "Sad",
                    "idleImageUrl": "https://objection.lol/Images/Characters/44/Sad.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/44/Sad_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/346.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 44
                }
            ]
        )
        SalManella = _builtinCharacter(
            45,
            "Sal Manella",
            "Manella",
            _blips['male'],
            enums.CharacterLocation.WITNESS,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/45.png",
            [
                {
                    "id": 347,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/45/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/45/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/347.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 45
                },
                {
                    "id": 348,
                    "name": "Think",
                    "idleImageUrl": "https://objection.lol/Images/Characters/45/Think.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/45/Think_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/348.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 45
                },
                {
                    "id": 349,
                    "name": "Shameless",
                    "idleImageUrl": "https://objection.lol/Images/Characters/45/Shameless.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/45/Shameless_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/349.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 45
                },
                {
                    "id": 350,
                    "name": "Angry",
                    "idleImageUrl": "https://objection.lol/Images/Characters/45/Angry.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/45/Angry_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/350.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 45
                },
                {
                    "id": 351,
                    "name": "Damage",
                    "idleImageUrl": "https://objection.lol/Images/Characters/45/Damage.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/45/Damage.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/351.png",
                    "order": 0,
                    "musicFileName": "allegro2001",
                    "states": [
                        {
                            "imageUrl": "Damage",
                            "nextPoseDelay": 1
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "yell2",
                            "time": 25,
                            "volume": 0.9
                        }
                    ],
                    "functionTicks": [
                        {
                            "functionName": "Flash",
                            "functionParam": "s",
                            "time": 25
                        },
                        {
                            "functionName": "Shake",
                            "functionParam": "s",
                            "time": 25
                        }
                    ],
                    "characterId": 45
                },
                {
                    "id": 352,
                    "name": "Cornered",
                    "idleImageUrl": "https://objection.lol/Images/Characters/45/Cornered.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/45/Cornered_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/352.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 45
                }
            ]
        )
        FranziskaVonKarma = _builtinCharacter(
            48,
            "Franziska von Karma",
            "von Karma",
            _blips['female'],
            enums.CharacterLocation.WITNESS,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/48.png",
            [
                {
                    "id": 361,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/48/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/48/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/361.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 48
                },
                {
                    "id": 362,
                    "name": "Confident",
                    "idleImageUrl": "https://objection.lol/Images/Characters/48/Confident.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/48/Confident_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/362.png",
                    "order": 0,
                    "musicFileName": "moderato2001",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 48
                },
                {
                    "id": 363,
                    "name": "Annoyed",
                    "idleImageUrl": "https://objection.lol/Images/Characters/48/Annoyed.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/48/Annoyed_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/363.png",
                    "order": 0,
                    "musicFileName": "moderato2001",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 48
                },
                {
                    "id": 364,
                    "name": "Point",
                    "idleImageUrl": "https://objection.lol/Images/Characters/48/Point.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/48/Point_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/364.png",
                    "order": 0,
                    "musicFileName": "moderato2001",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 48
                },
                {
                    "id": 365,
                    "name": "Cry",
                    "idleImageUrl": "https://objection.lol/Images/Characters/48/Cry.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/48/Cry_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/365.png",
                    "order": 0,
                    "musicFileName": "moderato2001",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 48
                }
            ],
            {
                "1": "https://objection.lol/Audio/Vocal/1/48.mp3"
            }
        )
        ManfredVonKarma = _builtinCharacter(
            49,
            "Manfred von Karma",
            "Karma",
            _blips['male'],
            enums.CharacterLocation.WITNESS,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/49.png",
            [
                {
                    "id": 366,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/49/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/49/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/366.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 49
                },
                {
                    "id": 367,
                    "name": "Confident",
                    "idleImageUrl": "https://objection.lol/Images/Characters/49/Confident.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/49/Confident_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/367.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 49
                },
                {
                    "id": 368,
                    "name": "Threaten",
                    "idleImageUrl": "https://objection.lol/Images/Characters/49/Shock.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/49/Shock_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/368.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 49
                }
            ],
            {
                "1": "https://objection.lol/Audio/Vocal/1/49.mp3"
            }
        )
        RichardWellington = _builtinCharacter(
            51,
            "Richard Wellington",
            "Wellington",
            _blips['male'],
            enums.CharacterLocation.WITNESS,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/51.png",
            [
                {
                    "id": 371,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/51/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/51/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/371.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 51
                },
                {
                    "id": 372,
                    "name": "Shrug",
                    "idleImageUrl": "https://objection.lol/Images/Characters/51/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/51/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/372.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [
                        {
                            "imageUrl": "Shrug",
                            "nextPoseDelay": 2000
                        }
                    ],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 51
                },
                {
                    "id": 373,
                    "name": "Angry",
                    "idleImageUrl": "https://objection.lol/Images/Characters/51/Angry.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/51/Angry_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/373.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 51
                },
                {
                    "id": 374,
                    "name": "Cornered",
                    "idleImageUrl": "https://objection.lol/Images/Characters/51/Cornered.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/51/Cornered.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/374.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 51
                },
                {
                    "id": 375,
                    "name": "Cornered 2",
                    "idleImageUrl": "https://objection.lol/Images/Characters/51/Cornered2.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/51/Cornered2.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/375.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 51
                },
                {
                    "id": 376,
                    "name": "Crazy",
                    "idleImageUrl": "https://objection.lol/Images/Characters/51/Crazy_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/51/Crazy.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/376.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 51
                },
                {
                    "id": 377,
                    "name": "Damage",
                    "idleImageUrl": "https://objection.lol/Images/Characters/51/Damage.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/51/Damage.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/377.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [
                        {
                            "imageUrl": "Damage",
                            "nextPoseDelay": 1
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "yell2",
                            "volume": 0.9,
                            "time": 100
                        }
                    ],
                    "functionTicks": [
                        {
                            "functionName": "Flash",
                            "functionParam": "m",
                            "time": 100
                        }
                    ],
                    "characterId": 51
                },
                {
                    "id": 378,
                    "name": "Breakdown",
                    "idleImageUrl": "https://objection.lol/Images/Characters/51/Breakdown.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/51/Breakdown.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/378.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [
                        {
                            "imageUrl": "Fall",
                            "nextPoseDelay": 1,
                            "playAtTextEnd": True
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "deskslam",
                            "volume": 1,
                            "time": 700,
                            "playAtTextEnd": True
                        }
                    ],
                    "functionTicks": [],
                    "characterId": 51
                }
            ]
        )
        VictorKudo = _builtinCharacter(
            52,
            "Victor Kudo",
            "Kudo",
            _blips['male'],
            enums.CharacterLocation.WITNESS,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/52.png",
            [
                {
                    "id": 379,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/52/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/52/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/379.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 52
                },
                {
                    "id": 380,
                    "name": "Side",
                    "idleImageUrl": "https://objection.lol/Images/Characters/52/Side.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/52/Side_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/380.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 52
                },
                {
                    "id": 381,
                    "name": "Surprised",
                    "idleImageUrl": "https://objection.lol/Images/Characters/52/Surprised.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/52/Surprised_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/381.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 52
                },
                {
                    "id": 382,
                    "name": "Pumped",
                    "idleImageUrl": "https://objection.lol/Images/Characters/52/Pumped.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/52/Pumped_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/382.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 52
                },
                {
                    "id": 383,
                    "name": "Angry",
                    "idleImageUrl": "https://objection.lol/Images/Characters/52/Angry.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/52/Angry_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/383.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 52
                },
                {
                    "id": 384,
                    "name": "Shy",
                    "idleImageUrl": "https://objection.lol/Images/Characters/52/Shy.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/52/Shy_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/384.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 52
                },
                {
                    "id": 385,
                    "name": "Throw",
                    "idleImageUrl": "https://objection.lol/Images/Characters/52/Throw.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/52/Throw.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/385.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 52
                }
            ]
        )
        MaggeyByrde = _builtinCharacter(
            53,
            "Maggey Byrde",
            "Byrde",
            _blips['female'],
            enums.CharacterLocation.WITNESS,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/53.png",
            [
                {
                    "id": 386,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/53/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/53/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/386.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 53
                },
                {
                    "id": 387,
                    "name": "Salute",
                    "idleImageUrl": "https://objection.lol/Images/Characters/53/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/53/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/387.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [
                        {
                            "imageUrl": "Salute",
                            "nextPoseDelay": 1000
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "sound/salute",
                            "volume": 1,
                            "time": 275
                        }
                    ],
                    "functionTicks": [],
                    "characterId": 53
                },
                {
                    "id": 388,
                    "name": "Pumped",
                    "idleImageUrl": "https://objection.lol/Images/Characters/53/Pumped.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/53/Pumped_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/388.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 53
                },
                {
                    "id": 389,
                    "name": "Happy",
                    "idleImageUrl": "https://objection.lol/Images/Characters/53/Happy.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/53/Happy_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/389.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 53
                },
                {
                    "id": 390,
                    "name": "Sad",
                    "idleImageUrl": "https://objection.lol/Images/Characters/53/Sad.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/53/Sad_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/390.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 53
                }
            ]
        )
        MikeMeekins = _builtinCharacter(
            54,
            "Mike Meekins",
            "Meekins",
            _blips['male'],
            enums.CharacterLocation.WITNESS,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/54.png",
            [
                {
                    "id": 391,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/54/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/54/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/391.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 54
                },
                {
                    "id": 392,
                    "name": "Salute",
                    "idleImageUrl": "https://objection.lol/Images/Characters/54/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/54/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/392.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [
                        {
                            "imageUrl": "Salute",
                            "nextPoseDelay": 550
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "sound/salute",
                            "volume": 1,
                            "time": 200
                        }
                    ],
                    "functionTicks": [],
                    "characterId": 54
                },
                {
                    "id": 393,
                    "name": "Pumped",
                    "idleImageUrl": "https://objection.lol/Images/Characters/54/Pumped_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/54/Pumped_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/393.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [
                        {
                            "imageUrl": "Pumped",
                            "nextPoseDelay": 450
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "sound/gavel",
                            "volume": 1,
                            "time": 210
                        }
                    ],
                    "functionTicks": [],
                    "characterId": 54
                },
                {
                    "id": 394,
                    "name": "Think",
                    "idleImageUrl": "https://objection.lol/Images/Characters/54/Think.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/54/Think_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/394.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 54
                },
                {
                    "id": 395,
                    "name": "Megaphone",
                    "idleImageUrl": "https://objection.lol/Images/Characters/54/Megaphone.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/54/Megaphone_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/395.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [
                        {
                            "imageUrl": "Megaphone",
                            "nextPoseDelay": 1
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "sound/megaphone",
                            "volume": 0.9,
                            "time": 50
                        }
                    ],
                    "functionTicks": [],
                    "characterId": 54
                },
                {
                    "id": 396,
                    "name": "Damage",
                    "idleImageUrl": "https://objection.lol/Images/Characters/54/Damage.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/54/Damage.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/396.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [
                        {
                            "imageUrl": "Damage",
                            "nextPoseDelay": 1
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "sound/chicken",
                            "volume": 1,
                            "time": 200
                        }
                    ],
                    "functionTicks": [],
                    "characterId": 54
                },
                {
                    "id": 397,
                    "name": "Sad",
                    "idleImageUrl": "https://objection.lol/Images/Characters/54/Sad.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/54/Sad_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/397.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 54
                },
                {
                    "id": 398,
                    "name": "Stare",
                    "idleImageUrl": "https://objection.lol/Images/Characters/54/Stare.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/54/Stare.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/398.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 54
                }
            ]
        )
        AngelStarr = _builtinCharacter(
            55,
            "Angel Starr",
            "Angel",
            _blips['female'],
            enums.CharacterLocation.WITNESS,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/55.png",
            [
                {
                    "id": 419,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/55/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/55/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/419.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 55
                },
                {
                    "id": 420,
                    "name": "Give",
                    "idleImageUrl": "https://objection.lol/Images/Characters/55/Give_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/55/Give_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/420.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [
                        {
                            "imageUrl": "Stand",
                            "nextPoseDelay": 150
                        },
                        {
                            "imageUrl": "Give_1",
                            "nextPoseDelay": 500
                        },
                        {
                            "imageUrl": "Give_Stand",
                            "nextPoseDelay": 250
                        }
                    ],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 55
                },
                {
                    "id": 421,
                    "name": "Confident",
                    "idleImageUrl": "https://objection.lol/Images/Characters/55/Confident_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/55/Confident_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/421.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [
                        {
                            "imageUrl": "Confident",
                            "nextPoseDelay": 1000
                        }
                    ],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 55
                },
                {
                    "id": 422,
                    "name": "Happy",
                    "idleImageUrl": "https://objection.lol/Images/Characters/55/Happy.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/55/Happy_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/422.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 55
                },
                {
                    "id": 423,
                    "name": "Cornered",
                    "idleImageUrl": "https://objection.lol/Images/Characters/55/Cornered.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/55/Cornered_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/423.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 55
                },
                {
                    "id": 424,
                    "name": "Angry",
                    "idleImageUrl": "https://objection.lol/Images/Characters/55/Angry.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/55/Angry_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/424.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 55
                },
                {
                    "id": 425,
                    "name": "Damage",
                    "idleImageUrl": "https://objection.lol/Images/Characters/55/Damage.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/55/Damage.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/425.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [
                        {
                            "imageUrl": "Cornered",
                            "nextPoseDelay": 100
                        },
                        {
                            "imageUrl": "Damage",
                            "nextPoseDelay": 1
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "damage2",
                            "volume": 1,
                            "time": 110
                        }
                    ],
                    "functionTicks": [
                        {
                            "functionName": "Flash",
                            "functionParam": "m",
                            "time": 125
                        }
                    ],
                    "characterId": 55
                }
            ]
        )
        DeeVasquez = _builtinCharacter(
            56,
            "Dee Vasquez",
            "Vasquez",
            _blips['female'],
            enums.CharacterLocation.WITNESS,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/56.png",
            [
                {
                    "id": 426,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/56/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/56/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/426.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 56
                },
                {
                    "id": 427,
                    "name": "Confident",
                    "idleImageUrl": "https://objection.lol/Images/Characters/56/Confident.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/56/Confident_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/427.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 56
                },
                {
                    "id": 428,
                    "name": "Happy",
                    "idleImageUrl": "https://objection.lol/Images/Characters/56/Happy.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/56/Happy_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/428.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 56
                },
                {
                    "id": 429,
                    "name": "Eyes Closed",
                    "idleImageUrl": "https://objection.lol/Images/Characters/56/Eyes_Closed.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/56/Eyes_Closed.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/429.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 56
                },
                {
                    "id": 430,
                    "name": "Cornered",
                    "idleImageUrl": "https://objection.lol/Images/Characters/56/Cornered.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/56/Cornered_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/430.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 56
                },
                {
                    "id": 431,
                    "name": "Damage",
                    "idleImageUrl": "https://objection.lol/Images/Characters/56/Damage.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/56/Damage.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/431.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [
                        {
                            "imageUrl": "Damage",
                            "nextPoseDelay": 1
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "damage",
                            "volume": 0.85,
                            "time": 1
                        }
                    ],
                    "functionTicks": [
                        {
                            "functionName": "Flash",
                            "functionParam": "m",
                            "time": 1
                        }
                    ],
                    "characterId": 56
                },
                {
                    "id": 432,
                    "name": "Surprised",
                    "idleImageUrl": "https://objection.lol/Images/Characters/56/Surprised.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/56/Surprised.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/432.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [
                        {
                            "imageUrl": "Surprised",
                            "nextPoseDelay": 100
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "yell2",
                            "volume": 1,
                            "time": 1
                        }
                    ],
                    "functionTicks": [
                        {
                            "functionName": "Flash",
                            "functionParam": "m",
                            "time": 1
                        }
                    ],
                    "characterId": 56
                },
                {
                    "id": 433,
                    "name": "Breakdown",
                    "idleImageUrl": "https://objection.lol/Images/Characters/56/Breakdown.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/56/Breakdown.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/433.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [
                        {
                            "imageUrl": "Breakdown",
                            "nextPoseDelay": 1
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "sound/snap",
                            "volume": 1,
                            "time": 1450
                        }
                    ],
                    "functionTicks": [],
                    "characterId": 56
                }
            ]
        )
        VeraMisham = _builtinCharacter(
            59,
            "Vera Misham",
            "Vera",
            _blips['female'],
            enums.CharacterLocation.WITNESS,
            _defaultBackgrounds['aj'],
            "https://objection.lol/Images/Gallery/59.png",
            [
                {
                    "id": 444,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/59/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/59/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/444.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 59
                },
                {
                    "id": 445,
                    "name": "Happy",
                    "idleImageUrl": "https://objection.lol/Images/Characters/59/Happy.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/59/Happy_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/445.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 59
                },
                {
                    "id": 446,
                    "name": "Scared",
                    "idleImageUrl": "https://objection.lol/Images/Characters/59/Scared.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/59/Scared_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/446.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 59
                },
                {
                    "id": 447,
                    "name": "Cornered",
                    "idleImageUrl": "https://objection.lol/Images/Characters/59/Cornered.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/59/Cornered_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/447.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 59
                },
                {
                    "id": 448,
                    "name": "Damage",
                    "idleImageUrl": "https://objection.lol/Images/Characters/59/Damage.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/59/Damage.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/448.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [
                        {
                            "imageUrl": "Damage",
                            "nextPoseDelay": 1
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "damage",
                            "volume": 0.85,
                            "time": 25
                        }
                    ],
                    "functionTicks": [
                        {
                            "functionName": "Flash",
                            "functionParam": "s",
                            "time": 25
                        }
                    ],
                    "characterId": 59
                },
                {
                    "id": 449,
                    "name": "Sketch",
                    "idleImageUrl": "https://objection.lol/Images/Characters/59/Sketch.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/59/Sketch.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/449.png",
                    "order": 0,
                    "musicFileName": "objection",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 59
                },
                {
                    "id": 450,
                    "name": "Eyes Closed",
                    "idleImageUrl": "https://objection.lol/Images/Characters/59/Eyes_Closed.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/59/Eyes_Closed_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/450.png",
                    "order": 0,
                    "musicFileName": "objection",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 59
                },
                {
                    "id": 451,
                    "name": "Bite Nail",
                    "idleImageUrl": "https://objection.lol/Images/Characters/59/Bite_Nail.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/59/Bite_Nail.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/451.png",
                    "order": 0,
                    "musicFileName": "objection",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 59
                },
                {
                    "id": 452,
                    "name": "Sketch: Angry",
                    "idleImageUrl": "https://objection.lol/Images/Characters/59/Draw_Angry_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/59/Draw_Angry_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/452.png",
                    "order": 0,
                    "musicFileName": "objection",
                    "states": [
                        {
                            "imageUrl": "Draw_Angry",
                            "nextPoseDelay": 2300
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "sound/flipbook",
                            "volume": 0.7,
                            "time": 300
                        },
                        {
                            "fileName": "sound/sketch",
                            "volume": 0.7,
                            "time": 900
                        }
                    ],
                    "functionTicks": [],
                    "characterId": 59
                },
                {
                    "id": 453,
                    "name": "Sketch: Happy",
                    "idleImageUrl": "https://objection.lol/Images/Characters/59/Draw_Happy_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/59/Draw_Happy_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/453.png",
                    "order": 0,
                    "musicFileName": "objection",
                    "states": [
                        {
                            "imageUrl": "Draw_Happy",
                            "nextPoseDelay": 2300
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "sound/flipbook",
                            "volume": 0.7,
                            "time": 300
                        },
                        {
                            "fileName": "sound/sketch",
                            "volume": 0.7,
                            "time": 900
                        }
                    ],
                    "functionTicks": [],
                    "characterId": 59
                },
                {
                    "id": 454,
                    "name": "Sketch: Surprised",
                    "idleImageUrl": "https://objection.lol/Images/Characters/59/Draw_Surprised_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/59/Draw_Surprised_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/454.png",
                    "order": 0,
                    "musicFileName": "objection",
                    "states": [
                        {
                            "imageUrl": "Draw_Surprised",
                            "nextPoseDelay": 2300
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "sound/flipbook",
                            "volume": 0.7,
                            "time": 300
                        },
                        {
                            "fileName": "sound/sketch",
                            "volume": 0.7,
                            "time": 900
                        }
                    ],
                    "functionTicks": [],
                    "characterId": 59
                },
                {
                    "id": 455,
                    "name": "Sketch: Sad",
                    "idleImageUrl": "https://objection.lol/Images/Characters/59/Draw_Sad_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/59/Draw_Sad_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/455.png",
                    "order": 0,
                    "musicFileName": "objection",
                    "states": [
                        {
                            "imageUrl": "Draw_Sad",
                            "nextPoseDelay": 2300
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "sound/flipbook",
                            "volume": 0.7,
                            "time": 300
                        },
                        {
                            "fileName": "sound/sketch",
                            "volume": 0.7,
                            "time": 900
                        }
                    ],
                    "functionTicks": [],
                    "characterId": 59
                },
                {
                    "id": 456,
                    "name": "Sketch: Apollo",
                    "idleImageUrl": "https://objection.lol/Images/Characters/59/Draw_Apollo_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/59/Draw_Apollo_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/456.png",
                    "order": 0,
                    "musicFileName": "objection",
                    "states": [
                        {
                            "imageUrl": "Draw_Apollo",
                            "nextPoseDelay": 2300
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "sound/flipbook",
                            "volume": 0.7,
                            "time": 300
                        },
                        {
                            "fileName": "sound/sketch",
                            "volume": 0.7,
                            "time": 900
                        }
                    ],
                    "functionTicks": [],
                    "characterId": 59
                },
                {
                    "id": 457,
                    "name": "Sketch: Trucy",
                    "idleImageUrl": "https://objection.lol/Images/Characters/59/Draw_Trucy_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/59/Draw_Trucy_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/457.png",
                    "order": 0,
                    "musicFileName": "objection",
                    "states": [
                        {
                            "imageUrl": "Draw_Trucy",
                            "nextPoseDelay": 2300
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "sound/flipbook",
                            "volume": 0.7,
                            "time": 300
                        },
                        {
                            "fileName": "sound/sketch",
                            "volume": 0.7,
                            "time": 900
                        }
                    ],
                    "functionTicks": [],
                    "characterId": 59
                }
            ]
        )
        PhoenixWrightOld = _builtinCharacter(
            61,
            "Phoenix Wright (old)",
            "Phoenix",
            _blips['male'],
            enums.CharacterLocation.WITNESS,
            _defaultBackgrounds['aj'],
            "https://objection.lol/Images/Gallery/61.png",
            [
                {
                    "id": 461,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/61/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/61/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/461.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 61
                },
                {
                    "id": 462,
                    "name": "Confident",
                    "idleImageUrl": "https://objection.lol/Images/Characters/61/Confident.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/61/Confident_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/462.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 61
                },
                {
                    "id": 463,
                    "name": "Serious",
                    "idleImageUrl": "https://objection.lol/Images/Characters/61/Serious.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/61/Serious_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/463.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 61
                },
                {
                    "id": 464,
                    "name": "Mysterious",
                    "idleImageUrl": "https://objection.lol/Images/Characters/61/Mysterious.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/61/Mysterious_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/464.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 61
                },
                {
                    "id": 465,
                    "name": "Laugh",
                    "idleImageUrl": "https://objection.lol/Images/Characters/61/Laugh.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/61/Laugh.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/465.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 61
                },
                {
                    "id": 466,
                    "name": "Think",
                    "idleImageUrl": "https://objection.lol/Images/Characters/61/Think.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/61/Think_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/466.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 61
                },
                {
                    "id": 467,
                    "name": "Smile",
                    "idleImageUrl": "https://objection.lol/Images/Characters/61/Smile.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/61/Smile_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/467.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 61
                },
                {
                    "id": 468,
                    "name": "Sleepy",
                    "idleImageUrl": "https://objection.lol/Images/Characters/61/Sleepy.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/61/Sleepy_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/468.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 61
                }
            ],
            {
                "1": "https://objection.lol/Audio/Vocal/1/61.mp3",
                "2": "https://objection.lol/Audio/Vocal/2/61.mp3",
                "3": "https://objection.lol/Audio/Vocal/3/61.mp3"
            }
        )
        PearlFey = _builtinCharacter(
            62,
            "Pearl Fey",
            "Pearl",
            _blips['female'],
            enums.CharacterLocation.WITNESS,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/62.png",
            [
                {
                    "id": 469,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/62/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/62/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/469.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 62
                },
                {
                    "id": 470,
                    "name": "Neutral",
                    "idleImageUrl": "https://objection.lol/Images/Characters/62/Neutral.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/62/Neutral_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/470.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 62
                },
                {
                    "id": 471,
                    "name": "Worried",
                    "idleImageUrl": "https://objection.lol/Images/Characters/62/Worried.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/62/Worried_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/471.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 62
                },
                {
                    "id": 472,
                    "name": "Angry",
                    "idleImageUrl": "https://objection.lol/Images/Characters/62/Angry.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/62/Angry_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/472.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 62
                },
                {
                    "id": 473,
                    "name": "Happy",
                    "idleImageUrl": "https://objection.lol/Images/Characters/62/Happy.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/62/Happy_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/473.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 62
                },
                {
                    "id": 474,
                    "name": "Surprised",
                    "idleImageUrl": "https://objection.lol/Images/Characters/62/Surprised.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/62/Surprised_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/474.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 62
                },
                {
                    "id": 475,
                    "name": "Dream",
                    "idleImageUrl": "https://objection.lol/Images/Characters/62/Dream.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/62/Dream_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/475.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 62
                },
                {
                    "id": 476,
                    "name": "Sad",
                    "idleImageUrl": "https://objection.lol/Images/Characters/62/Sad.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/62/Sad_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/476.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 62
                },
                {
                    "id": 477,
                    "name": "Cry",
                    "idleImageUrl": "https://objection.lol/Images/Characters/62/Cry.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/62/Cry_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/477.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 62
                }
            ]
        )
        Godot = _builtinCharacter(
            63,
            "Godot",
            "Godot",
            _blips['male'],
            enums.CharacterLocation.WITNESS,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/63.png",
            [
                {
                    "id": 482,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/63/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/63/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/482.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 63
                },
                {
                    "id": 483,
                    "name": "Side",
                    "idleImageUrl": "https://objection.lol/Images/Characters/63/Side.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/63/Side_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/483.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 63
                },
                {
                    "id": 484,
                    "name": "Confident",
                    "idleImageUrl": "https://objection.lol/Images/Characters/63/Confident.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/63/Confident_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/484.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 63
                }
            ],
            {
                "1": "https://objection.lol/Audio/Vocal/1/63.mp3"
            }
        )
        JeanArmstrong = _builtinCharacter(
            64,
            "Jean Armstrong",
            "Armstrong",
            _blips['male'],
            enums.CharacterLocation.WITNESS,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/64.png",
            [
                {
                    "id": 489,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/64/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/64/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/489.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 64
                },
                {
                    "id": 490,
                    "name": "Happy",
                    "idleImageUrl": "https://objection.lol/Images/Characters/64/Happy.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/64/Happy_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/490.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 64
                },
                {
                    "id": 491,
                    "name": "Think",
                    "idleImageUrl": "https://objection.lol/Images/Characters/64/Think.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/64/Think_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/491.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 64
                },
                {
                    "id": 492,
                    "name": "Cornered",
                    "idleImageUrl": "https://objection.lol/Images/Characters/64/Cornered.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/64/Cornered_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/492.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 64
                },
                {
                    "id": 493,
                    "name": "Damage",
                    "idleImageUrl": "https://objection.lol/Images/Characters/64/Damage.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/64/Damage.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/493.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [
                        {
                            "imageUrl": "Damage",
                            "nextPoseDelay": 1
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "damage2",
                            "volume": 0.9,
                            "time": 5
                        }
                    ],
                    "functionTicks": [
                        {
                            "functionName": "Flash",
                            "functionParam": "m",
                            "time": 5
                        }
                    ],
                    "characterId": 64
                },
                {
                    "id": 494,
                    "name": "Sad",
                    "idleImageUrl": "https://objection.lol/Images/Characters/64/Sad.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/64/Sad_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/494.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 64
                },
                {
                    "id": 495,
                    "name": "Dance",
                    "idleImageUrl": "https://objection.lol/Images/Characters/64/Dance.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/64/Dance.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/495.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 64
                }
            ]
        )
        EmaSkye = _builtinCharacter(
            65,
            "Ema Skye",
            "Ema",
            _blips['female'],
            enums.CharacterLocation.WITNESS,
            _defaultBackgrounds['aj'],
            "https://objection.lol/Images/Gallery/65.png",
            [
                {
                    "id": 496,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/65/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/65/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/496.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 65
                },
                {
                    "id": 497,
                    "name": "Side",
                    "idleImageUrl": "https://objection.lol/Images/Characters/65/Side.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/65/Side_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/497.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 65
                },
                {
                    "id": 498,
                    "name": "Glasses Off",
                    "idleImageUrl": "https://objection.lol/Images/Characters/65/Glasses_Off.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/65/Glasses_Off_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/498.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 65
                },
                {
                    "id": 499,
                    "name": "Think",
                    "idleImageUrl": "https://objection.lol/Images/Characters/65/Think.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/65/Think_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/499.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 65
                },
                {
                    "id": 500,
                    "name": "Confident",
                    "idleImageUrl": "https://objection.lol/Images/Characters/65/Confident.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/65/Confident_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/500.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 65
                },
                {
                    "id": 501,
                    "name": "Surprised",
                    "idleImageUrl": "https://objection.lol/Images/Characters/65/Surprised_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/65/Surprised_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/501.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [
                        {
                            "imageUrl": "Surprised",
                            "nextPoseDelay": 1000,
                            "speakDelay": 1000
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "sound/lightbulb",
                            "volume": 0.7,
                            "time": 5
                        }
                    ],
                    "functionTicks": [
                        {
                            "functionName": "Flash",
                            "functionParam": "s",
                            "time": 5
                        }
                    ],
                    "characterId": 65
                },
                {
                    "id": 502,
                    "name": "Annoyed",
                    "idleImageUrl": "https://objection.lol/Images/Characters/65/Annoyed.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/65/Annoyed_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/502.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 65
                },
                {
                    "id": 503,
                    "name": "Eating",
                    "idleImageUrl": "https://objection.lol/Images/Characters/65/Eating.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/65/Eating_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/503.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 65
                },
                {
                    "id": 504,
                    "name": "Eating (faster)",
                    "idleImageUrl": "https://objection.lol/Images/Characters/65/Eating_Fast.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/65/Eating_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/504.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 65
                },
                {
                    "id": 505,
                    "name": "Smile",
                    "idleImageUrl": "https://objection.lol/Images/Characters/65/Smile.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/65/Smile.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/505.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 65
                },
                {
                    "id": 506,
                    "name": "Serious",
                    "idleImageUrl": "https://objection.lol/Images/Characters/65/Serious.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/65/Serious_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/506.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 65
                },
                {
                    "id": 507,
                    "name": "Glasses On",
                    "idleImageUrl": "https://objection.lol/Images/Characters/65/Glasses_On.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/65/Glasses_On_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/507.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 65
                }
            ]
        )
        KristophGavinWithBadge = _builtinCharacter(
            66,
            "Kristoph Gavin (with badge)",
            "Kristoph",
            _blips['male'],
            enums.CharacterLocation.WITNESS,
            _defaultBackgrounds['aj'],
            "https://objection.lol/Images/Gallery/66.png",
            [
                {
                    "id": 508,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/66/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/66/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/508.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 66
                },
                {
                    "id": 509,
                    "name": "Headshake",
                    "idleImageUrl": "https://objection.lol/Images/Characters/66/Headshake.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/66/Headshake.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/509.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 66
                },
                {
                    "id": 510,
                    "name": "Smile",
                    "idleImageUrl": "https://objection.lol/Images/Characters/66/Smile.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/66/Smile_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/510.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 66
                },
                {
                    "id": 511,
                    "name": "Mysterious",
                    "idleImageUrl": "https://objection.lol/Images/Characters/66/Mysterious_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/66/Mysterious_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/511.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [
                        {
                            "imageUrl": "Mysterious",
                            "nextPoseDelay": 1200
                        }
                    ],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 66
                },
                {
                    "id": 512,
                    "name": "Confident",
                    "idleImageUrl": "https://objection.lol/Images/Characters/66/Confident.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/66/Confident_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/512.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 66
                },
                {
                    "id": 513,
                    "name": "Annoyed",
                    "idleImageUrl": "https://objection.lol/Images/Characters/66/Annoyed.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/66/Annoyed_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/513.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 66
                },
                {
                    "id": 514,
                    "name": "Damage",
                    "idleImageUrl": "https://objection.lol/Images/Characters/66/Damage.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/66/Damage.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/514.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [
                        {
                            "imageUrl": "Damage",
                            "nextPoseDelay": 1,
                            "speakDelay": 1
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "damage",
                            "volume": 0.9,
                            "time": 5
                        }
                    ],
                    "functionTicks": [
                        {
                            "functionName": "Flash",
                            "functionParam": "s",
                            "time": 5
                        }
                    ],
                    "characterId": 66
                },
                {
                    "id": 515,
                    "name": "Damage (2)",
                    "idleImageUrl": "https://objection.lol/Images/Characters/66/Damage2.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/66/Damage2.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/515.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [
                        {
                            "imageUrl": "Damage2",
                            "nextPoseDelay": 1,
                            "speakDelay": 1
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "damage",
                            "volume": 0.9,
                            "time": 5
                        }
                    ],
                    "functionTicks": [
                        {
                            "functionName": "Flash",
                            "functionParam": "s",
                            "time": 5
                        }
                    ],
                    "characterId": 66
                },
                {
                    "id": 516,
                    "name": "Angry",
                    "idleImageUrl": "https://objection.lol/Images/Characters/66/Angry.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/66/Angry_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/516.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 66
                },
                {
                    "id": 517,
                    "name": "Uneasy",
                    "idleImageUrl": "https://objection.lol/Images/Characters/66/Uneasy.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/66/Uneasy_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/517.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 66
                },
                {
                    "id": 518,
                    "name": "Desk Slam",
                    "idleImageUrl": "https://objection.lol/Images/Characters/66/Slam.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/66/Slam.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/518.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [
                        {
                            "imageUrl": "Slam",
                            "nextPoseDelay": 4000,
                            "speakDelay": 4000
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "gavin-slam",
                            "volume": 0.9,
                            "time": 0
                        }
                    ],
                    "functionTicks": [
                        {
                            "functionName": "Quake",
                            "functionParam": 3500,
                            "time": 0
                        }
                    ],
                    "characterId": 66
                },
                {
                    "id": 521,
                    "name": "Glare",
                    "idleImageUrl": "https://objection.lol/Images/Characters/66/Glare.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/66/Glare_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/521.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 66
                },
                {
                    "id": 522,
                    "name": "Evil",
                    "idleImageUrl": "https://objection.lol/Images/Characters/66/Evil.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/66/Evil_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/522.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 66
                }
            ],
            {
                "1": "https://objection.lol/Audio/Vocal/1/66.mp3"
            }
        )
        KristophGavin = _builtinCharacter(
            67,
            "Kristoph Gavin",
            "Kristoph",
            _blips['male'],
            enums.CharacterLocation.WITNESS,
            _defaultBackgrounds['aj'],
            "https://objection.lol/Images/Gallery/67.png",
            [
                {
                    "id": 523,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/67/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/67/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/523.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 67
                },
                {
                    "id": 524,
                    "name": "Headshake",
                    "idleImageUrl": "https://objection.lol/Images/Characters/67/Headshake.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/67/Headshake.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/524.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 67
                },
                {
                    "id": 525,
                    "name": "Smile",
                    "idleImageUrl": "https://objection.lol/Images/Characters/67/Smile.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/67/Smile_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/525.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 67
                },
                {
                    "id": 526,
                    "name": "Mysterious",
                    "idleImageUrl": "https://objection.lol/Images/Characters/67/Mysterious_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/67/Mysterious_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/526.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [
                        {
                            "imageUrl": "Mysterious",
                            "nextPoseDelay": 1200
                        }
                    ],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 67
                },
                {
                    "id": 527,
                    "name": "Confident",
                    "idleImageUrl": "https://objection.lol/Images/Characters/67/Confident.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/67/Confident_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/527.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 67
                },
                {
                    "id": 528,
                    "name": "Annoyed",
                    "idleImageUrl": "https://objection.lol/Images/Characters/67/Annoyed.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/67/Annoyed_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/528.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 67
                },
                {
                    "id": 529,
                    "name": "Damage",
                    "idleImageUrl": "https://objection.lol/Images/Characters/67/Damage.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/67/Damage.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/529.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [
                        {
                            "imageUrl": "Damage",
                            "nextPoseDelay": 1,
                            "speakDelay": 1
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "damage",
                            "volume": 0.9,
                            "time": 5
                        }
                    ],
                    "functionTicks": [
                        {
                            "functionName": "Flash",
                            "functionParam": "s",
                            "time": 5
                        }
                    ],
                    "characterId": 67
                },
                {
                    "id": 530,
                    "name": "Damage (2)",
                    "idleImageUrl": "https://objection.lol/Images/Characters/67/Damage2.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/67/Damage2.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/530.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [
                        {
                            "imageUrl": "Damage2",
                            "nextPoseDelay": 1,
                            "speakDelay": 1
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "damage",
                            "volume": 0.9,
                            "time": 5
                        }
                    ],
                    "functionTicks": [
                        {
                            "functionName": "Flash",
                            "functionParam": "s",
                            "time": 5
                        }
                    ],
                    "characterId": 67
                },
                {
                    "id": 531,
                    "name": "Angry",
                    "idleImageUrl": "https://objection.lol/Images/Characters/67/Angry.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/67/Angry_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/531.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 67
                },
                {
                    "id": 532,
                    "name": "Uneasy",
                    "idleImageUrl": "https://objection.lol/Images/Characters/67/Uneasy.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/67/Uneasy_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/532.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 67
                },
                {
                    "id": 533,
                    "name": "Desk Slam",
                    "idleImageUrl": "https://objection.lol/Images/Characters/67/Slam.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/67/Slam.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/533.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [
                        {
                            "imageUrl": "Slam",
                            "nextPoseDelay": 4000,
                            "speakDelay": 4000
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "gavin-slam",
                            "volume": 0.9,
                            "time": 0
                        }
                    ],
                    "functionTicks": [
                        {
                            "functionName": "Quake",
                            "functionParam": 3500,
                            "time": 0
                        }
                    ],
                    "characterId": 67
                },
                {
                    "id": 534,
                    "name": "Glare",
                    "idleImageUrl": "https://objection.lol/Images/Characters/67/Glare.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/67/Glare_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/534.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 67
                },
                {
                    "id": 535,
                    "name": "Evil",
                    "idleImageUrl": "https://objection.lol/Images/Characters/67/Evil.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/67/Evil_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/535.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 67
                },
                {
                    "id": 536,
                    "name": "Cornered",
                    "idleImageUrl": "https://objection.lol/Images/Characters/67/Cornered.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/67/Cornered_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/536.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 67
                },
                {
                    "id": 537,
                    "name": "Breakdown",
                    "idleImageUrl": "https://objection.lol/Images/Characters/67/Breakdown2.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/67/.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/537.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [
                        {
                            "imageUrl": "Breakdown1",
                            "nextPoseDelay": 4395,
                            "speakDelay": 0
                        },
                        {
                            "imageUrl": "Breakdown2",
                            "nextPoseDelay": 0,
                            "speakDelay": 0
                        }
                    ],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 67
                },
                {
                    "id": 538,
                    "name": "Broken",
                    "idleImageUrl": "https://objection.lol/Images/Characters/67/Broken.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/67/Broken_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/538.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 67
                },
                {
                    "id": 539,
                    "name": "Laugh",
                    "idleImageUrl": "https://objection.lol/Images/Characters/67/Laugh.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/67/Laugh.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/539.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 67
                }
            ],
            {
                "1": "https://objection.lol/Audio/Vocal/1/67.mp3"
            }
        )
        MiaFey = _builtinCharacter(
            68,
            "Mia Fey",
            "Mia",
            _blips['female'],
            enums.CharacterLocation.WITNESS,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/68.png",
            [
                {
                    "id": 541,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/68/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/68/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/541.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 68
                },
                {
                    "id": 542,
                    "name": "Surprised",
                    "idleImageUrl": "https://objection.lol/Images/Characters/68/Surprised.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/68/Surprised_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/542.png",
                    "order": 0,
                    "musicFileName": "truth2001",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 68
                },
                {
                    "id": 543,
                    "name": "Happy",
                    "idleImageUrl": "https://objection.lol/Images/Characters/68/Happy_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/68/Happy_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/543.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [
                        {
                            "imageUrl": "Happy",
                            "nextPoseDelay": 1000
                        }
                    ],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 68
                }
            ],
            {
                "1": "https://objection.lol/Audio/Vocal/1/68.mp3",
                "2": "https://objection.lol/Audio/Vocal/2/68.mp3",
                "3": "https://objection.lol/Audio/Vocal/3/68.mp3"
            }
        )
        MorganFey = _builtinCharacter(
            69,
            "Morgan Fey",
            "Morgan",
            _blips['female'],
            enums.CharacterLocation.WITNESS,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/69.png",
            [
                {
                    "id": 544,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/69/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/69/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/544.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 69
                },
                {
                    "id": 545,
                    "name": "Sleeve",
                    "idleImageUrl": "https://objection.lol/Images/Characters/69/Sleeve.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/69/Sleeve_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/545.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 69
                },
                {
                    "id": 546,
                    "name": "Sad",
                    "idleImageUrl": "https://objection.lol/Images/Characters/69/Sad.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/69/Sad_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/546.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 69
                },
                {
                    "id": 547,
                    "name": "Angry",
                    "idleImageUrl": "https://objection.lol/Images/Characters/69/Angry.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/69/Angry_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/547.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 69
                }
            ]
        )
        BellBoy = _builtinCharacter(
            70,
            "BellBoy",
            "BellBoy",
            _blips['male'],
            enums.CharacterLocation.WITNESS,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/70.png",
            [
                {
                    "id": 548,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/70/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/70/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/548.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 70
                },
                {
                    "id": 549,
                    "name": "Shy",
                    "idleImageUrl": "https://objection.lol/Images/Characters/70/Shy.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/70/Shy_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/549.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 70
                }
            ]
        )
        AdrianAndrews = _builtinCharacter(
            71,
            "Adrian Andrews",
            "Andrews",
            _blips['female'],
            enums.CharacterLocation.WITNESS,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/71.png",
            [
                {
                    "id": 550,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/71/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/71/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/550.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 71
                },
                {
                    "id": 551,
                    "name": "Read",
                    "idleImageUrl": "https://objection.lol/Images/Characters/71/Read.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/71/Read_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/551.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 71
                },
                {
                    "id": 552,
                    "name": "Serious",
                    "idleImageUrl": "https://objection.lol/Images/Characters/71/Serious.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/71/Serious_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/552.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 71
                },
                {
                    "id": 553,
                    "name": "Think",
                    "idleImageUrl": "https://objection.lol/Images/Characters/71/Think.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/71/Think_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/553.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 71
                },
                {
                    "id": 554,
                    "name": "Surprised",
                    "idleImageUrl": "https://objection.lol/Images/Characters/71/Surprised.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/71/Surprised_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/554.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 71
                },
                {
                    "id": 555,
                    "name": "Happy",
                    "idleImageUrl": "https://objection.lol/Images/Characters/71/Happy.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/71/Happy_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/555.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 71
                },
                {
                    "id": 556,
                    "name": "Sad",
                    "idleImageUrl": "https://objection.lol/Images/Characters/71/Sad.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/71/Sad_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/556.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 71
                },
                {
                    "id": 557,
                    "name": "Damage",
                    "idleImageUrl": "https://objection.lol/Images/Characters/71/Damage.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/71/Damage.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/557.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [
                        {
                            "imageUrl": "Damage",
                            "nextPoseDelay": 1
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "damage",
                            "volume": 0.6,
                            "time": 1
                        },
                        {
                            "fileName": "sound/break2",
                            "volume": 1,
                            "time": 625
                        }
                    ],
                    "functionTicks": [
                        {
                            "functionName": "Shake",
                            "functionParam": "s",
                            "time": 1
                        }
                    ],
                    "characterId": 71
                },
                {
                    "id": 558,
                    "name": "Cornered",
                    "idleImageUrl": "https://objection.lol/Images/Characters/71/Cornered.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/71/Cornered_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/558.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 71
                },
                {
                    "id": 559,
                    "name": "Broken",
                    "idleImageUrl": "https://objection.lol/Images/Characters/71/Broken.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/71/Broken_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/559.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 71
                }
            ]
        )
        Moe = _builtinCharacter(
            74,
            "Moe",
            "Moe",
            _blips['male'],
            enums.CharacterLocation.WITNESS,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/74.png",
            [
                {
                    "id": 572,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/74/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/74/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/572.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 74
                },
                {
                    "id": 573,
                    "name": "Laugh",
                    "idleImageUrl": "https://objection.lol/Images/Characters/74/Laugh.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/74/Laugh.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/573.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 74
                },
                {
                    "id": 574,
                    "name": "Dull",
                    "idleImageUrl": "https://objection.lol/Images/Characters/74/Dull.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/74/Dull_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/574.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 74
                },
                {
                    "id": 575,
                    "name": "Point",
                    "idleImageUrl": "https://objection.lol/Images/Characters/74/Point.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/74/Point_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/575.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 74
                },
                {
                    "id": 576,
                    "name": "Damage",
                    "idleImageUrl": "https://objection.lol/Images/Characters/74/Damage.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/74/Damage.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/576.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [
                        {
                            "imageUrl": "Damage",
                            "nextPoseDelay": 1
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "yell2",
                            "time": 25,
                            "volume": 0.85
                        }
                    ],
                    "functionTicks": [
                        {
                            "functionName": "Shake",
                            "functionParam": "s",
                            "time": 25
                        }
                    ],
                    "characterId": 74
                },
                {
                    "id": 577,
                    "name": "Angry",
                    "idleImageUrl": "https://objection.lol/Images/Characters/74/Angry.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/74/Angry_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/577.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 74
                },
                {
                    "id": 578,
                    "name": "Sad",
                    "idleImageUrl": "https://objection.lol/Images/Characters/74/Sad.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/74/Sad_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/578.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 74
                }
            ]
        )
        MaximillionGalactica = _builtinCharacter(
            75,
            "Maximillion Galactica",
            "Max",
            _blips['male'],
            enums.CharacterLocation.WITNESS,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/75.png",
            [
                {
                    "id": 579,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/75/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/75/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/579.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 75
                },
                {
                    "id": 580,
                    "name": "Point",
                    "idleImageUrl": "https://objection.lol/Images/Characters/75/Point.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/75/Point_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/580.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 75
                },
                {
                    "id": 581,
                    "name": "Confident",
                    "idleImageUrl": "https://objection.lol/Images/Characters/75/Confident.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/75/Confident_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/581.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 75
                },
                {
                    "id": 582,
                    "name": "Cornered",
                    "idleImageUrl": "https://objection.lol/Images/Characters/75/Cornered.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/75/Cornered_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/582.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 75
                },
                {
                    "id": 583,
                    "name": "Cry",
                    "idleImageUrl": "https://objection.lol/Images/Characters/75/Cry.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/75/Cry_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/583.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 75
                }
            ]
        )
        WillPowers = _builtinCharacter(
            76,
            "Will Powers",
            "Powers",
            _blips['male'],
            enums.CharacterLocation.WITNESS,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/76.png",
            [
                {
                    "id": 584,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/76/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/76/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/584.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 76
                },
                {
                    "id": 585,
                    "name": "Think",
                    "idleImageUrl": "https://objection.lol/Images/Characters/76/Think.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/76/Think_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/585.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 76
                },
                {
                    "id": 586,
                    "name": "Dull",
                    "idleImageUrl": "https://objection.lol/Images/Characters/76/Dull.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/76/Dull_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/586.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 76
                },
                {
                    "id": 587,
                    "name": "Sad",
                    "idleImageUrl": "https://objection.lol/Images/Characters/76/Sad.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/76/Sad_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/587.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 76
                },
                {
                    "id": 588,
                    "name": "Happy",
                    "idleImageUrl": "https://objection.lol/Images/Characters/76/Happy.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/76/Happy_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/588.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 76
                }
            ]
        )
        TrucyWright = _builtinCharacter(
            77,
            "Trucy Wright",
            "Trucy",
            _blips['female'],
            enums.CharacterLocation.WITNESS,
            _defaultBackgrounds['aj'],
            "https://objection.lol/Images/Gallery/77.png",
            [
                {
                    "id": 589,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/77/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/77/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/589.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 77
                },
                {
                    "id": 590,
                    "name": "Think",
                    "idleImageUrl": "https://objection.lol/Images/Characters/77/Think.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/77/Think_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/590.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 77
                },
                {
                    "id": 591,
                    "name": "Happy",
                    "idleImageUrl": "https://objection.lol/Images/Characters/77/Happy.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/77/Happy_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/591.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 77
                },
                {
                    "id": 592,
                    "name": "Smile",
                    "idleImageUrl": "https://objection.lol/Images/Characters/77/Smile.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/77/Happy_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/592.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 77
                },
                {
                    "id": 593,
                    "name": "Grin",
                    "idleImageUrl": "https://objection.lol/Images/Characters/77/Grin.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/77/Happy_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/593.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 77
                },
                {
                    "id": 594,
                    "name": "Confident",
                    "idleImageUrl": "https://objection.lol/Images/Characters/77/Confident.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/77/Confident_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/594.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 77
                },
                {
                    "id": 595,
                    "name": "Silly",
                    "idleImageUrl": "https://objection.lol/Images/Characters/77/Silly.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/77/Silly.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/595.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 77
                },
                {
                    "id": 596,
                    "name": "Surprised",
                    "idleImageUrl": "https://objection.lol/Images/Characters/77/Surprised.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/77/Surprised_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/596.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 77
                },
                {
                    "id": 597,
                    "name": "Shocked",
                    "idleImageUrl": "https://objection.lol/Images/Characters/77/Shocked.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/77/Shocked.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/597.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [
                        {
                            "imageUrl": "Shocked",
                            "nextPoseDelay": 1
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "sound/lightbulb",
                            "volume": 0.7,
                            "time": 5
                        }
                    ],
                    "functionTicks": [
                        {
                            "functionName": "Flash",
                            "functionParam": "s",
                            "time": 5
                        }
                    ],
                    "characterId": 77
                },
                {
                    "id": 598,
                    "name": "Annoyed",
                    "idleImageUrl": "https://objection.lol/Images/Characters/77/Annoyed_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/77/Annoyed_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/598.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [
                        {
                            "imageUrl": "Annoyed",
                            "nextPoseDelay": 800,
                            "playAtTextEnd": True
                        }
                    ],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 77
                },
                {
                    "id": 599,
                    "name": "Determined",
                    "idleImageUrl": "https://objection.lol/Images/Characters/77/Determined.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/77/Determined_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/599.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 77
                },
                {
                    "id": 600,
                    "name": "Serious",
                    "idleImageUrl": "https://objection.lol/Images/Characters/77/Serious.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/77/Serious_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/600.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 77
                },
                {
                    "id": 601,
                    "name": "Scared",
                    "idleImageUrl": "https://objection.lol/Images/Characters/77/Worried.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/77/Worried_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/601.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 77
                },
                {
                    "id": 602,
                    "name": "Sad",
                    "idleImageUrl": "https://objection.lol/Images/Characters/77/Sad.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/77/Sad_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/602.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 77
                },
                {
                    "id": 603,
                    "name": "Cry",
                    "idleImageUrl": "https://objection.lol/Images/Characters/77/Cry.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/77/Cry.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/603.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 77
                },
                {
                    "id": 685,
                    "name": "Hand in pocket",
                    "idleImageUrl": "https://objection.lol/Images/Characters/77/Pocket.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/77/Pocket_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/685.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 77
                },
                {
                    "id": 686,
                    "name": "Mr. Hat Appears",
                    "idleImageUrl": "https://objection.lol/Images/Characters/77/MrHat_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/77/MrHat_Trucy_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/686.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [
                        {
                            "imageUrl": "MrHat",
                            "nextPoseDelay": 2800
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "sfx-nosale.wav",
                            "volume": 0.6,
                            "time": 200
                        }
                    ],
                    "functionTicks": [],
                    "characterId": 77
                },
                {
                    "id": 687,
                    "name": "Mr. Hat Talk",
                    "idleImageUrl": "https://objection.lol/Images/Characters/77/MrHat_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/77/MrHat_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/687.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 77
                },
                {
                    "id": 688,
                    "name": "Mr. Hat Talk (Trucy)",
                    "idleImageUrl": "https://objection.lol/Images/Characters/77/MrHat_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/77/MrHat_Trucy_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/688.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 77
                }
            ]
        )
        LarryButzGuard = _builtinCharacter(
            79,
            "Larry Butz (guard)",
            "Butz",
            _blips['male'],
            enums.CharacterLocation.WITNESS,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/79.png",
            [
                {
                    "id": 612,
                    "name": "Happy",
                    "idleImageUrl": "https://objection.lol/Images/Characters/79/Happy.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/79/Happy_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/612.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 79
                },
                {
                    "id": 613,
                    "name": "Think",
                    "idleImageUrl": "https://objection.lol/Images/Characters/79/Think2.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/79/Think2_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/613.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 79
                },
                {
                    "id": 614,
                    "name": "Cry",
                    "idleImageUrl": "https://objection.lol/Images/Characters/79/Cry.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/79/Cry_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/614.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 79
                },
                {
                    "id": 615,
                    "name": "Cornered",
                    "idleImageUrl": "https://objection.lol/Images/Characters/79/Cornered.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/79/Cornered_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/615.png",
                    "order": 0,
                    "musicFileName": "truth2002",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 79
                },
                {
                    "id": 616,
                    "name": "Thumbs Up",
                    "idleImageUrl": "https://objection.lol/Images/Characters/79/Thumbs.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/79/Thumbs_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/616.png",
                    "order": 0,
                    "musicFileName": "allegro2001",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 79
                }
            ]
        )
        ShellyDeKiller = _builtinCharacter(
            80,
            "Shelly de Killer",
            "de Killer",
            _blips['male'],
            enums.CharacterLocation.WITNESS,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/80.png",
            [
                {
                    "id": 617,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/80/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/80/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/617.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 80
                },
                {
                    "id": 618,
                    "name": "Stand (waiter)",
                    "idleImageUrl": "https://objection.lol/Images/Characters/80/Stand2.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/80/Stand2_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/618.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 80
                },
                {
                    "id": 619,
                    "name": "Stand (red light)",
                    "idleImageUrl": "https://objection.lol/Images/Characters/80/Stand_Red.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/80/Stand_Red.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/619.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 80
                }
            ]
        )
        TerryFawles = _builtinCharacter(
            81,
            "Terry Fawles",
            "Fawles",
            _blips['male'],
            enums.CharacterLocation.WITNESS,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/81.png",
            [
                {
                    "id": 620,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/81/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/81/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/620.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 81
                },
                {
                    "id": 621,
                    "name": "Look Away",
                    "idleImageUrl": "https://objection.lol/Images/Characters/81/Look_Away.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/81/Look_Away_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/621.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 81
                },
                {
                    "id": 622,
                    "name": "Serious",
                    "idleImageUrl": "https://objection.lol/Images/Characters/81/Serious.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/81/Serious_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/622.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 81
                },
                {
                    "id": 623,
                    "name": "Nervous",
                    "idleImageUrl": "https://objection.lol/Images/Characters/81/Nervous.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/81/Nervous.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/623.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 81
                },
                {
                    "id": 624,
                    "name": "Cry",
                    "idleImageUrl": "https://objection.lol/Images/Characters/81/Cry.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/81/Cry_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/624.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 81
                },
                {
                    "id": 625,
                    "name": "Yell",
                    "idleImageUrl": "https://objection.lol/Images/Characters/81/Yell.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/81/Yell_Talk.gif",
                    "isSpeedlines": True,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/625.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 81
                },
                {
                    "id": 626,
                    "name": "Cough",
                    "idleImageUrl": "https://objection.lol/Images/Characters/81/Cough.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/81/Cough.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/626.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 81
                },
                {
                    "id": 627,
                    "name": "Cough 2",
                    "idleImageUrl": "https://objection.lol/Images/Characters/81/Cough2.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/81/Cough2.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/627.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 81
                },
                {
                    "id": 628,
                    "name": "Cough Blood",
                    "idleImageUrl": "https://objection.lol/Images/Characters/81/Serious_Blood.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/81/Serious_Blood_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/628.png",
                    "order": 0,
                    "musicFileName": "trial2",
                    "states": [
                        {
                            "imageUrl": "Cough_Blood",
                            "nextPoseDelay": 3000
                        }
                    ],
                    "audioTicks": [],
                    "functionTicks": [
                        {
                            "functionName": "Flash",
                            "functionParam": "m",
                            "time": 500
                        }
                    ],
                    "characterId": 81
                },
                {
                    "id": 629,
                    "name": "Serious (bled)",
                    "idleImageUrl": "https://objection.lol/Images/Characters/81/Serious_Blood.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/81/Serious_Blood_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/629.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 81
                }
            ]
        )
        PennyNichols = _builtinCharacter(
            82,
            "Penny Nichols",
            "Penny",
            _blips['female'],
            enums.CharacterLocation.WITNESS,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/82.png",
            [
                {
                    "id": 630,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/82/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/82/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/630.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 82
                },
                {
                    "id": 631,
                    "name": "Confident",
                    "idleImageUrl": "https://objection.lol/Images/Characters/82/Confident.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/82/Confident_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/631.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 82
                },
                {
                    "id": 632,
                    "name": "Cards",
                    "idleImageUrl": "https://objection.lol/Images/Characters/82/Cards.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/82/Cards_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/632.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 82
                }
            ]
        )
        BenjaminTrilo = _builtinCharacter(
            83,
            "Benjamin & Trilo",
            "Ben & Trilo",
            _blips['male'],
            enums.CharacterLocation.WITNESS,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/83.png",
            [
                {
                    "id": 633,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/83/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/83/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/633.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 83
                },
                {
                    "id": 634,
                    "name": "Stand (with Trilo)",
                    "idleImageUrl": "https://objection.lol/Images/Characters/83/Stand_Trilo.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/83/Stand_Trilo_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/634.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 83
                },
                {
                    "id": 635,
                    "name": "Confident",
                    "idleImageUrl": "https://objection.lol/Images/Characters/83/Stand_Trilo.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/83/Confident.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/635.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 83
                },
                {
                    "id": 636,
                    "name": "Look Away",
                    "idleImageUrl": "https://objection.lol/Images/Characters/83/Look_Away.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/83/Look_Away_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/636.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 83
                },
                {
                    "id": 637,
                    "name": "Angry",
                    "idleImageUrl": "https://objection.lol/Images/Characters/83/Angry.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/83/Angry_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/637.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 83
                },
                {
                    "id": 638,
                    "name": "Trilo Punch",
                    "idleImageUrl": "https://objection.lol/Images/Characters/83/Trilo_Punch.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/83/Trilo_Punch_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/638.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 83
                },
                {
                    "id": 639,
                    "name": "Trilo Punch 2",
                    "idleImageUrl": "https://objection.lol/Images/Characters/83/Trilo_Punch.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/83/Trilo_Punch_Talk2.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/639.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 83
                },
                {
                    "id": 640,
                    "name": "Damage",
                    "idleImageUrl": "https://objection.lol/Images/Characters/83/Damage.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/83/Damage.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/640.png",
                    "order": 0,
                    "musicFileName": "trial2",
                    "states": [
                        {
                            "imageUrl": "Damage",
                            "nextPoseDelay": 1
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "damage2",
                            "volume": 0.9,
                            "time": 25
                        }
                    ],
                    "functionTicks": [
                        {
                            "functionName": "Flash",
                            "functionParam": "m",
                            "time": 25
                        }
                    ],
                    "characterId": 83
                }
            ]
        )
        Bikini = _builtinCharacter(
            84,
            "Bikini",
            "Bikini",
            _blips['female'],
            enums.CharacterLocation.WITNESS,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/84.png",
            [
                {
                    "id": 641,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/84/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/84/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/641.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 84
                },
                {
                    "id": 642,
                    "name": "Think",
                    "idleImageUrl": "https://objection.lol/Images/Characters/84/Think.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/84/Think_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/642.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 84
                },
                {
                    "id": 643,
                    "name": "Laugh",
                    "idleImageUrl": "https://objection.lol/Images/Characters/84/Laugh.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/84/Laugh.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/643.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 84
                },
                {
                    "id": 644,
                    "name": "Laugh 2",
                    "idleImageUrl": "https://objection.lol/Images/Characters/84/Laugh2.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/84/Laugh2.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/644.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 84
                },
                {
                    "id": 645,
                    "name": "Happy",
                    "idleImageUrl": "https://objection.lol/Images/Characters/84/Laugh_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/84/Laugh_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/645.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 84
                },
                {
                    "id": 646,
                    "name": "Serious",
                    "idleImageUrl": "https://objection.lol/Images/Characters/84/Serious.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/84/Serious_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/646.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 84
                },
                {
                    "id": 647,
                    "name": "Sad",
                    "idleImageUrl": "https://objection.lol/Images/Characters/84/Sad.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/84/Sad_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/647.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 84
                },
                {
                    "id": 648,
                    "name": "Scared",
                    "idleImageUrl": "https://objection.lol/Images/Characters/84/Scared.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/84/Scared_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/648.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 84
                }
            ]
        )
        DesireeDeLite = _builtinCharacter(
            85,
            "Desirée DeLite",
            "Desirée",
            _blips['female'],
            enums.CharacterLocation.WITNESS,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/85.png",
            [
                {
                    "id": 649,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/85/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/85/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/649.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 85
                },
                {
                    "id": 650,
                    "name": "Think",
                    "idleImageUrl": "https://objection.lol/Images/Characters/85/Think.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/85/Think_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/650.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 85
                },
                {
                    "id": 651,
                    "name": "Cornered",
                    "idleImageUrl": "https://objection.lol/Images/Characters/85/Cornered.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/85/Cornered_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/651.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 85
                },
                {
                    "id": 652,
                    "name": "Smile",
                    "idleImageUrl": "https://objection.lol/Images/Characters/85/Happy_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/85/Happy_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/652.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 85
                },
                {
                    "id": 683,
                    "name": "Happy",
                    "idleImageUrl": "https://objection.lol/Images/Characters/85/Happy.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/85/Happy.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/683.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 85
                }
            ]
        )
        DiegoArmando = _builtinCharacter(
            86,
            "Diego Armando",
            "Armando",
            _blips['male'],
            enums.CharacterLocation.WITNESS,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/86.png",
            [
                {
                    "id": 653,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/86/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/86/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/653.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 86
                },
                {
                    "id": 654,
                    "name": "Confident",
                    "idleImageUrl": "https://objection.lol/Images/Characters/86/Confident.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/86/Confident_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/654.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 86
                }
            ],
            {
                "1": "https://objection.lol/Audio/Vocal/1/86.mp3"
            }
        )
        DrewMisham = _builtinCharacter(
            87,
            "Drew Misham",
            "Drew",
            _blips['male'],
            enums.CharacterLocation.WITNESS,
            _defaultBackgrounds['aj'],
            "https://objection.lol/Images/Gallery/87.png",
            [
                {
                    "id": 655,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/87/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/87/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/655.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 87
                },
                {
                    "id": 656,
                    "name": "Think",
                    "idleImageUrl": "https://objection.lol/Images/Characters/87/Think.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/87/Think_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/656.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 87
                },
                {
                    "id": 657,
                    "name": "Cornered",
                    "idleImageUrl": "https://objection.lol/Images/Characters/87/Cornered.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/87/Cornered_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/657.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 87
                },
                {
                    "id": 658,
                    "name": "Sad",
                    "idleImageUrl": "https://objection.lol/Images/Characters/87/Sad.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/87/Sad_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/658.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 87
                }
            ]
        )
        GuyEldoon = _builtinCharacter(
            88,
            "Guy Eldoon",
            "Eldoon",
            _blips['male'],
            enums.CharacterLocation.WITNESS,
            _defaultBackgrounds['aj'],
            "https://objection.lol/Images/Gallery/88.png",
            [
                {
                    "id": 659,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/88/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/88/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/659.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 88
                },
                {
                    "id": 660,
                    "name": "Forceful",
                    "idleImageUrl": "https://objection.lol/Images/Characters/88/Confident.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/88/Confident_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/660.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 88
                },
                {
                    "id": 661,
                    "name": "Eyes Closed",
                    "idleImageUrl": "https://objection.lol/Images/Characters/88/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/88/Eyes_Closed_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/661.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 88
                },
                {
                    "id": 662,
                    "name": "Harmonica",
                    "idleImageUrl": "https://objection.lol/Images/Characters/88/Harmonica.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/88/Harmonica.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/662.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [
                        {
                            "imageUrl": "Harmonica",
                            "nextPoseDelay": 1
                        }
                    ],
                    "audioTicks": [
                        {
                            "fileName": "sound/harmonica.wav",
                            "volume": 0.9,
                            "time": 1
                        }
                    ],
                    "functionTicks": [],
                    "characterId": 88
                },
                {
                    "id": 663,
                    "name": "Slump",
                    "idleImageUrl": "https://objection.lol/Images/Characters/88/Slump.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/88/Slump.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/663.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 88
                },
                {
                    "id": 664,
                    "name": "Cornered",
                    "idleImageUrl": "https://objection.lol/Images/Characters/88/Cornered.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/88/Cornered_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/664.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 88
                },
                {
                    "id": 665,
                    "name": "Hat On",
                    "idleImageUrl": "https://objection.lol/Images/Characters/88/Hat_On.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/88/Hat_On_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/665.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 88
                },
                {
                    "id": 666,
                    "name": "Hat Off",
                    "idleImageUrl": "https://objection.lol/Images/Characters/88/Hat_Off.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/88/Hat_Off.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/666.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 88
                },
                {
                    "id": 667,
                    "name": "Serious",
                    "idleImageUrl": "https://objection.lol/Images/Characters/88/Serious.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/88/Serious_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/667.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 88
                }
            ]
        )
        MarvinGrossberg = _builtinCharacter(
            89,
            "Marvin Grossberg",
            "Grossberg",
            _blips['male'],
            enums.CharacterLocation.WITNESS,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/89.png",
            [
                {
                    "id": 668,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/89/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/89/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/668.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 89
                },
                {
                    "id": 669,
                    "name": "Cornered",
                    "idleImageUrl": "https://objection.lol/Images/Characters/89/Cornered.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/89/Cornered_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/669.png",
                    "order": 0,
                    "musicFileName": "moderato2001",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 89
                },
                {
                    "id": 670,
                    "name": "Stand (red suit)",
                    "idleImageUrl": "https://objection.lol/Images/Characters/89/Stand2.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/89/Stand2_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/670.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 89
                },
                {
                    "id": 671,
                    "name": "Cornered (red suit)",
                    "idleImageUrl": "https://objection.lol/Images/Characters/89/Cornered2.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/89/Cornered2_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/671.png",
                    "order": 0,
                    "musicFileName": "moderato2001",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 89
                }
            ]
        )
        DirectorHotti = _builtinCharacter(
            90,
            "Director Hotti",
            "Hotti",
            _blips['male'],
            enums.CharacterLocation.WITNESS,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/90.png",
            [
                {
                    "id": 672,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/90/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/90/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/672.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 90
                },
                {
                    "id": 673,
                    "name": "Whisper",
                    "idleImageUrl": "https://objection.lol/Images/Characters/90/Whisper.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/90/Whisper_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/673.png",
                    "order": 0,
                    "musicFileName": "moderato2001",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 90
                },
                {
                    "id": 674,
                    "name": "Crazy",
                    "idleImageUrl": "https://objection.lol/Images/Characters/90/Crazy.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/90/Crazy_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/674.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 90
                }
            ]
        )
        LisaBasil = _builtinCharacter(
            91,
            "Lisa Basil",
            "Basil",
            _blips['female'],
            enums.CharacterLocation.WITNESS,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/91.png",
            [
                {
                    "id": 675,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/91/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/91/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/675.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 91
                },
                {
                    "id": 676,
                    "name": "Happy",
                    "idleImageUrl": "https://objection.lol/Images/Characters/91/Happy.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/91/Happy_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/676.png",
                    "order": 0,
                    "musicFileName": "moderato2001",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 91
                },
                {
                    "id": 677,
                    "name": "Cornered",
                    "idleImageUrl": "https://objection.lol/Images/Characters/91/Cornered.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/91/Cornered_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/677.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 91
                }
            ]
        )
        EliseDeauxnim = _builtinCharacter(
            92,
            "Elise Deauxnim",
            "Elise",
            _blips['female'],
            enums.CharacterLocation.WITNESS,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/92.png",
            [
                {
                    "id": 678,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/92/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/92/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/678.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 92
                },
                {
                    "id": 679,
                    "name": "Happy",
                    "idleImageUrl": "https://objection.lol/Images/Characters/92/Happy.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/92/Happy_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/679.png",
                    "order": 0,
                    "musicFileName": "moderato2001",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 92
                }
            ]
        )
        ViolaCadaverini = _builtinCharacter(
            93,
            "Viola Cadaverini",
            "Viola",
            _blips['female'],
            enums.CharacterLocation.WITNESS,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/93.png",
            [
                {
                    "id": 680,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/93/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/93/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/680.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 93
                },
                {
                    "id": 681,
                    "name": "Laugh",
                    "idleImageUrl": "https://objection.lol/Images/Characters/93/Laugh.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/93/Laugh_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/681.png",
                    "order": 0,
                    "musicFileName": "moderato2001",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 93
                },
                {
                    "id": 682,
                    "name": "Cry",
                    "idleImageUrl": "https://objection.lol/Images/Characters/93/Cry.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/93/Cry_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/682.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 93
                }
            ]
        )
        KlavierGavin = _builtinCharacter(
            95,
            "Klavier Gavin",
            "Klavier",
            _blips['male'],
            enums.CharacterLocation.WITNESS,
            _defaultBackgrounds['aj'],
            "https://objection.lol/Images/Gallery/95.png",
            [
                {
                    "id": 702,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/95/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/95/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/702.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 95
                },
                {
                    "id": 703,
                    "name": "Lean",
                    "idleImageUrl": "https://objection.lol/Images/Characters/95/Lean.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/95/Lean_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/703.png",
                    "order": 0,
                    "musicFileName": "moderato2001",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 95
                },
                {
                    "id": 704,
                    "name": "Side",
                    "idleImageUrl": "https://objection.lol/Images/Characters/95/Side.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/95/Side_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/704.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 95
                },
                {
                    "id": 705,
                    "name": "Side 2",
                    "idleImageUrl": "https://objection.lol/Images/Characters/95/Side2.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/95/Side2_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/705.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 95
                },
                {
                    "id": 706,
                    "name": "Hair Play",
                    "idleImageUrl": "https://objection.lol/Images/Characters/95/Hair.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/95/Hair.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/706.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 95
                },
                {
                    "id": 707,
                    "name": "Angry",
                    "idleImageUrl": "https://objection.lol/Images/Characters/95/Angry.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/95/Angry_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/707.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 95
                }
            ],
            {
                "1": "https://objection.lol/Audio/Vocal/1/95.mp3"
            }
        )
        SparkBrushel = _builtinCharacter(
            96,
            "Spark Brushel",
            "Brushel",
            _blips['male'],
            enums.CharacterLocation.WITNESS,
            _defaultBackgrounds['aj'],
            "https://objection.lol/Images/Gallery/96.png",
            [
                {
                    "id": 708,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/96/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/96/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/708.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 96
                },
                {
                    "id": 709,
                    "name": "Smile",
                    "idleImageUrl": "https://objection.lol/Images/Characters/96/Smile.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/96/Smile_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/709.png",
                    "order": 0,
                    "musicFileName": "moderato2001",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 96
                },
                {
                    "id": 710,
                    "name": "Think",
                    "idleImageUrl": "https://objection.lol/Images/Characters/96/Think.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/96/Think_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/710.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 96
                },
                {
                    "id": 711,
                    "name": "Sniff",
                    "idleImageUrl": "https://objection.lol/Images/Characters/96/Nose.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/96/Nose.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/711.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 96
                },
                {
                    "id": 750,
                    "name": "Surprised",
                    "idleImageUrl": "https://objection.lol/Images/Characters/96/Surprised.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/96/Surprised_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/750.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 96
                },
                {
                    "id": 751,
                    "name": "Cornered",
                    "idleImageUrl": "https://objection.lol/Images/Characters/96/Cornered.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/96/Cornered_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/751.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 96
                },
                {
                    "id": 752,
                    "name": "Damage",
                    "idleImageUrl": "https://objection.lol/Images/Characters/96/Damage.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/96/Damage.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/752.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [
                        {
                            "fileName": "Sound/wrap",
                            "volume": 0.8,
                            "time": 100
                        },
                        {
                            "fileName": "Sound/damage2",
                            "volume": 0.9,
                            "time": 10
                        }
                    ],
                    "functionTicks": [
                        {
                            "functionName": "Flash",
                            "functionParam": "s",
                            "time": 10
                        },
                        {
                            "functionName": "Shake",
                            "functionParam": "m",
                            "time": 10
                        }
                    ],
                    "characterId": 96
                }
            ]
        )
        WockyKitaki = _builtinCharacter(
            97,
            "Wocky Kitaki",
            "Wocky",
            _blips['male'],
            enums.CharacterLocation.WITNESS,
            _defaultBackgrounds['aj'],
            "https://objection.lol/Images/Gallery/97.png",
            [
                {
                    "id": 712,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/97/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/97/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/712.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 97
                },
                {
                    "id": 713,
                    "name": "Stare",
                    "idleImageUrl": "https://objection.lol/Images/Characters/97/Stare_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/97/Stare_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/713.png",
                    "order": 0,
                    "musicFileName": "moderato2001",
                    "states": [
                        {
                            "imageUrl": "Stare",
                            "nextPoseDelay": 1210
                        }
                    ],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 97
                },
                {
                    "id": 714,
                    "name": "Think",
                    "idleImageUrl": "https://objection.lol/Images/Characters/97/Think.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/97/Think_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/714.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 97
                },
                {
                    "id": 715,
                    "name": "Fight",
                    "idleImageUrl": "https://objection.lol/Images/Characters/97/Fight_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/97/Fight_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/715.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 97
                },
                {
                    "id": 716,
                    "name": "Fight 2",
                    "idleImageUrl": "https://objection.lol/Images/Characters/97/Fight.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/97/Fight.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/716.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 97
                },
                {
                    "id": 717,
                    "name": "Cornered",
                    "idleImageUrl": "https://objection.lol/Images/Characters/97/Cornered.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/97/Cornered_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/717.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 97
                },
                {
                    "id": 718,
                    "name": "Angry",
                    "idleImageUrl": "https://objection.lol/Images/Characters/97/Angry.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/97/Angry_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/718.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 97
                },
                {
                    "id": 719,
                    "name": "Happy",
                    "idleImageUrl": "https://objection.lol/Images/Characters/97/Happy.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/97/Happy_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/719.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 97
                },
                {
                    "id": 720,
                    "name": "Sad",
                    "idleImageUrl": "https://objection.lol/Images/Characters/97/Sad.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/97/Sad_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/720.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 97
                },
                {
                    "id": 721,
                    "name": "Serious",
                    "idleImageUrl": "https://objection.lol/Images/Characters/97/Serious.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/97/Serious_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/721.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 97
                }
            ]
        )
        WinfredKitaki = _builtinCharacter(
            98,
            "Winfred Kitaki",
            "Big Wins",
            _blips['male'],
            enums.CharacterLocation.WITNESS,
            _defaultBackgrounds['aj'],
            "https://objection.lol/Images/Gallery/98.png",
            [
                {
                    "id": 722,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/98/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/98/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/722.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 98
                },
                {
                    "id": 723,
                    "name": "Brows",
                    "idleImageUrl": "https://objection.lol/Images/Characters/98/Serious.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/98/Serious_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/723.png",
                    "order": 0,
                    "musicFileName": "moderato2001",
                    "states": [
                        {
                            "imageUrl": "Brows",
                            "nextPoseDelay": 4290
                        }
                    ],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 98
                },
                {
                    "id": 724,
                    "name": "Serious",
                    "idleImageUrl": "https://objection.lol/Images/Characters/98/Serious.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/98/Serious_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/724.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 98
                }
            ]
        )
        MiaAsMaya = _builtinCharacter(
            100,
            "Mia (as Maya)",
            "Mia",
            _blips['female'],
            enums.CharacterLocation.WITNESS,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/100.png",
            [
                {
                    "id": 730,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/100/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/100/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/730.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 100
                },
                {
                    "id": 731,
                    "name": "Surprised",
                    "idleImageUrl": "https://objection.lol/Images/Characters/100/Surprised.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/100/Surprised_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/731.png",
                    "order": 0,
                    "musicFileName": "moderato2001",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 100
                },
                {
                    "id": 732,
                    "name": "Serious",
                    "idleImageUrl": "https://objection.lol/Images/Characters/100/Serious.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/100/Serious_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/732.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 100
                },
                {
                    "id": 733,
                    "name": "Happy",
                    "idleImageUrl": "https://objection.lol/Images/Characters/100/Happy.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/100/Happy_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/733.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 100
                }
            ],
            {
                "1": "https://objection.lol/Audio/Vocal/1/100.mp3",
                "2": "https://objection.lol/Audio/Vocal/2/100.mp3",
                "3": "https://objection.lol/Audio/Vocal/3/100.mp3"
            }
        )
        DaryanCrescend = _builtinCharacter(
            101,
            "Daryan Crescend",
            "Daryan",
            _blips['male'],
            enums.CharacterLocation.WITNESS,
            _defaultBackgrounds['aj'],
            "https://objection.lol/Images/Gallery/101.png",
            [
                {
                    "id": 734,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/101/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/101/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/734.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 101
                },
                {
                    "id": 735,
                    "name": "Surprised",
                    "idleImageUrl": "https://objection.lol/Images/Characters/101/Surprised.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/101/Surprised_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/735.png",
                    "order": 0,
                    "musicFileName": "moderato2001",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 101
                },
                {
                    "id": 736,
                    "name": "Laugh",
                    "idleImageUrl": "https://objection.lol/Images/Characters/101/Laugh.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/101/Laugh_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/736.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 101
                },
                {
                    "id": 737,
                    "name": "Arms Crossed",
                    "idleImageUrl": "https://objection.lol/Images/Characters/101/Arms_Crossed.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/101/Arms_Crossed_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/737.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 101
                },
                {
                    "id": 738,
                    "name": "Hair Play",
                    "idleImageUrl": "https://objection.lol/Images/Characters/101/Hair_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/101/Hair_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/738.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [
                        {
                            "imageUrl": "Hair",
                            "nextPoseDelay": 4370
                        }
                    ],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 101
                },
                {
                    "id": 739,
                    "name": "Angry",
                    "idleImageUrl": "https://objection.lol/Images/Characters/101/Angry.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/101/Angry_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/739.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 101
                },
                {
                    "id": 740,
                    "name": "Damage",
                    "idleImageUrl": "https://objection.lol/Images/Characters/101/Damage.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/101/Damage.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/740.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [
                        {
                            "fileName": "yell2",
                            "time": 50,
                            "volume": 0.9
                        }
                    ],
                    "functionTicks": [
                        {
                            "functionName": "Flash",
                            "functionParam": "m",
                            "time": 50
                        }
                    ],
                    "characterId": 101
                },
                {
                    "id": 741,
                    "name": "Damage 2",
                    "idleImageUrl": "https://objection.lol/Images/Characters/101/Damage2.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/101/Damage2.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/741.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [
                        {
                            "fileName": "yell2",
                            "time": 50,
                            "volume": 0.9
                        }
                    ],
                    "functionTicks": [
                        {
                            "functionName": "Flash",
                            "functionParam": "m",
                            "time": 50
                        }
                    ],
                    "characterId": 101
                },
                {
                    "id": 742,
                    "name": "Cornered",
                    "idleImageUrl": "https://objection.lol/Images/Characters/101/Cornered.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/101/Cornered_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/742.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 101
                },
                {
                    "id": 743,
                    "name": "Breakdown",
                    "idleImageUrl": "https://objection.lol/Images/Characters/101/Breakdown.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/101/Breakdown.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/743.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 101
                },
                {
                    "id": 744,
                    "name": "Broken",
                    "idleImageUrl": "https://objection.lol/Images/Characters/101/Broken.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/101/Broken_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/744.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 101
                }
            ]
        )

    class Judge:
        TheJudge = _builtinCharacter(
            10,
            "The Judge",
            "Judge",
            _blips['male'],
            enums.CharacterLocation.JUDGE,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/10.png",
            [
                {
                    "id": 30,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/10/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/10/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/30.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 10
                },
                {
                    "id": 31,
                    "name": "Negative",
                    "idleImageUrl": "https://objection.lol/Images/Characters/10/Negative_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/10/Negative_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/31.png",
                    "order": 0,
                    "musicFileName": "trial2",
                    "states": [
                        {
                            "imageUrl": "Special_1",
                            "nextPoseDelay": 700
                        }
                    ],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 10
                },
                {
                    "id": 32,
                    "name": "Surprised",
                    "idleImageUrl": "https://objection.lol/Images/Characters/10/Surprised_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/10/Surprised_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/32.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 10
                },
                {
                    "id": 44,
                    "name": "Positive",
                    "idleImageUrl": "https://objection.lol/Images/Characters/10/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/10/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/44.png",
                    "order": 0,
                    "musicFileName": "trial2",
                    "states": [
                        {
                            "imageUrl": "Special_2",
                            "nextPoseDelay": 650
                        }
                    ],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 10
                },
                {
                    "id": 186,
                    "name": "Eyes Closed",
                    "idleImageUrl": "https://objection.lol/Images/Characters/10/Closed_Eyes.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/10/Closed_Eyes.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/186.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 10
                },
                {
                    "id": 604,
                    "name": "Headshake",
                    "idleImageUrl": "https://objection.lol/Images/Characters/10/Headshake.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/10/Headshake.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/604.png",
                    "order": 0,
                    "musicFileName": "trial2",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 10
                }
            ],
            {
                "1": "https://objection.lol/Audio/Vocal/1/10.mp3",
                "2": "https://objection.lol/Audio/Vocal/2/10.mp3",
                "3": "https://objection.lol/Audio/Vocal/3/10.mp3"
            }
        )
        JudgesBrother = _builtinCharacter(
            20,
            "Judge's Brother",
            "Judge",
            _blips['male'],
            enums.CharacterLocation.JUDGE,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/20.png",
            [
                {
                    "id": 125,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/20/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/20/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/125.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 20
                },
                {
                    "id": 126,
                    "name": "Negative",
                    "idleImageUrl": "https://objection.lol/Images/Characters/20/Negative_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/20/Negative_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/126.png",
                    "order": 0,
                    "musicFileName": "trial2",
                    "states": [
                        {
                            "imageUrl": "Special_1",
                            "nextPoseDelay": 700
                        }
                    ],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 20
                },
                {
                    "id": 127,
                    "name": "Surprised",
                    "idleImageUrl": "https://objection.lol/Images/Characters/20/Surprised_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/20/Surprised_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/127.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 20
                },
                {
                    "id": 128,
                    "name": "Positive",
                    "idleImageUrl": "https://objection.lol/Images/Characters/20/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/20/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/128.png",
                    "order": 0,
                    "musicFileName": "trial2",
                    "states": [
                        {
                            "imageUrl": "Special_2",
                            "nextPoseDelay": 650
                        }
                    ],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 20
                },
                {
                    "id": 187,
                    "name": "Eyes Closed",
                    "idleImageUrl": "https://objection.lol/Images/Characters/20/Closed_Eyes.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/20/Closed_Eyes.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/187.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 20
                },
                {
                    "id": 605,
                    "name": "Headshake",
                    "idleImageUrl": "https://objection.lol/Images/Characters/20/Headshake.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/20/Headshake.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/605.png",
                    "order": 0,
                    "musicFileName": "trial2",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 20
                }
            ],
            {
                "1": "https://objection.lol/Audio/Vocal/1/20.mp3",
                "2": "https://objection.lol/Audio/Vocal/2/20.mp3",
                "3": "https://objection.lol/Audio/Vocal/3/20.mp3"
            }
        )
        TheJudgeAJ = _builtinCharacter(
            78,
            "The Judge (AJ)",
            "Judge",
            _blips['male'],
            enums.CharacterLocation.JUDGE,
            _defaultBackgrounds['aj'],
            "https://objection.lol/Images/Gallery/78.png",
            [
                {
                    "id": 606,
                    "name": "Stand",
                    "idleImageUrl": "https://objection.lol/Images/Characters/78/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/78/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/606.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 78
                },
                {
                    "id": 607,
                    "name": "Negative",
                    "idleImageUrl": "https://objection.lol/Images/Characters/78/Negative_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/78/Negative_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/607.png",
                    "order": 0,
                    "musicFileName": "trial2",
                    "states": [
                        {
                            "imageUrl": "Special_1",
                            "nextPoseDelay": 1200
                        }
                    ],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 78
                },
                {
                    "id": 608,
                    "name": "Surprised",
                    "idleImageUrl": "https://objection.lol/Images/Characters/78/Surprised_Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/78/Surprised_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/608.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 78
                },
                {
                    "id": 609,
                    "name": "Positive",
                    "idleImageUrl": "https://objection.lol/Images/Characters/78/Stand.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/78/Stand_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/609.png",
                    "order": 0,
                    "musicFileName": "trial2",
                    "states": [
                        {
                            "imageUrl": "Special_2",
                            "nextPoseDelay": 1050
                        }
                    ],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 78
                },
                {
                    "id": 610,
                    "name": "Eyes Closed",
                    "idleImageUrl": "https://objection.lol/Images/Characters/78/Closed_Eyes.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/78/Closed_Eyes_Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/610.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 78
                },
                {
                    "id": 611,
                    "name": "Headshake",
                    "idleImageUrl": "https://objection.lol/Images/Characters/78/Headshake.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/78/Headshake.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/611.png",
                    "order": 0,
                    "musicFileName": "trial2",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 78
                }
            ],
            {
                "1": "https://objection.lol/Audio/Vocal/1/78.mp3",
                "2": "https://objection.lol/Audio/Vocal/2/78.mp3",
                "3": "https://objection.lol/Audio/Vocal/3/78.mp3"
            }
        )

    class Gallery:
        PW = _builtinCharacter(
            28,
            "Gallery",
            "Gallery",
            _blips['male'],
            enums.CharacterLocation.GALLERY,
            _defaultBackgrounds['classic'],
            "https://objection.lol/Images/Gallery/28.png",
            [
                {
                    "id": 215,
                    "name": "Idle",
                    "idleImageUrl": "https://objection.lol/Images/Characters/28/Idle.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/28/Idle.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/215.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 28
                },
                {
                    "id": 216,
                    "name": "Talk",
                    "idleImageUrl": "https://objection.lol/Images/Characters/28/Talk.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/28/Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/216.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 28
                },
                {
                    "id": 540,
                    "name": "Empty Audience",
                    "idleImageUrl": "https://objection.lol/Images/Characters/28/Empty.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/28/Empty.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/540.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 28
                }
            ]
        )
        AJ = _builtinCharacter(
            102,
            "Gallery (AJ)",
            "Gallery",
            _blips['male'],
            enums.CharacterLocation.GALLERY,
            _defaultBackgrounds['aj'],
            "https://objection.lol/Images/Gallery/102.png",
            [
                {
                    "id": 746,
                    "name": "Idle",
                    "idleImageUrl": "https://objection.lol/Images/Characters/102/Idle.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/102/Idle.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/746.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 102
                },
                {
                    "id": 747,
                    "name": "Talk",
                    "idleImageUrl": "https://objection.lol/Images/Characters/102/Talk.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/102/Talk.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/747.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 102
                },
                {
                    "id": 748,
                    "name": "Empty Audience",
                    "idleImageUrl": "https://objection.lol/Images/Characters/102/Empty.gif",
                    "speakImageUrl": "https://objection.lol/Images/Characters/102/Empty.gif",
                    "isSpeedlines": False,
                    "iconUrl": "https://objection.lol/Images/PoseIcons/748.png",
                    "order": 0,
                    "musicFileName": "trial",
                    "states": [],
                    "audioTicks": [],
                    "functionTicks": [],
                    "characterId": 102
                }
            ]
        )


class Backgrounds:
    class Wide:
        PWCourtroom = assets.Background(72269)

    class PWCourt:
        DefenseCounsel = assets.Background(187)
        Defense = assets.Background(189)
        Judge = assets.Background(192)
        Prosecution = assets.Background(194)
        Witness = assets.Background(197)

    class AJCourt:
        DefenseCounsel = assets.Background(175)
        Defense = assets.Background(177)
        Judge = assets.Background(178)
        Prosecution = assets.Background(182)
        WitnessConcealed = assets.Background(184)
        Witness = assets.Background(186)

    AcrosRoom = assets.Background(1)
    Airport = assets.Background(4)
    AprilsHotelRoom = assets.Background(6)
    AtmeysOffice = assets.Background(9)
    Basement = assets.Background(10)
    BerryBigCircusNight = assets.Background(13)
    BerryBigCircus = assets.Background(16)
    BlueScreensInc = assets.Background(19)
    Bluecorp = assets.Background(21)
    CircusCafeteria = assets.Background(22)
    CircusCourtyard = assets.Background(23)
    CircusTent = assets.Background(24)
    DefenseLobby = assets.Background(25)
    DetentionCenterInside = assets.Background(27)
    DetentionCenterOutside = assets.Background(28)
    DuskyBridgeOut = assets.Background(29)
    DuskyBridge = assets.Background(30)
    EdgeworthsOffice = assets.Background(31)
    EvidenceLockers = assets.Background(32)
    EvidenceRoom = assets.Background(33)
    GantsOfficeLeft = assets.Background(34)
    GantsOfficeRight = assets.Background(35)
    GantsOffice = assets.Background(36)
    GatewaterHotelBallroom = assets.Background(37)
    GatewaterHotelHallway = assets.Background(38)
    GatewaterHotelLobby = assets.Background(39)
    GlobalStudiosGate = assets.Background(40)
    GlobalStudiosDressingRoom = assets.Background(42)
    GlobalStudiosStaffAreaLeft = assets.Background(43)
    GlobalStudiosStaffAreaRight = assets.Background(44)
    GourdLakeBoatRental = assets.Background(45)
    GourdLakeEntrance = assets.Background(46)
    GourdLakeForestLeft = assets.Background(47)
    GourdLakeForestRight = assets.Background(48)
    GourdLakePark2 = assets.Background(49)
    GourdLakePark = assets.Background(50)
    Gumshoe = assets.Background(55)
    HazakuraCourtyard = assets.Background(56)
    HazakuraInnerTempleLeft = assets.Background(59)
    HazakuraInnerTempleRight = assets.Background(61)
    HazakuraMainHall = assets.Background(65)
    HazakuraTempleEntrance = assets.Background(68)
    HazakuraTrainingHall = assets.Background(69)
    HeavenlyHall = assets.Background(71)
    HotelRoom = assets.Background(75)
    HottiClinic = assets.Background(77)
    InnerTempleGarden = assets.Background(78)
    InsideTheBoathouse = assets.Background(80)
    JakeMarshallsSecurityRoom = assets.Background(83)
    KBSecuritysGuardOffice = assets.Background(86)
    KBSecuritysPresidentsOffice = assets.Background(88)
    KurainMainHall = assets.Background(90)
    KurainVillage = assets.Background(92)
    KurainsSpareRoom2 = assets.Background(94)
    KurainsSpareRoom = assets.Background(96)
    LordlyTailorBasementLeft = assets.Background(99)
    LordlyTailorBasementRight = assets.Background(101)
    LordlyTailor = assets.Background(103)
    MarvinGrossbergsOffice2 = assets.Background(105)
    MarvinGrossbergsOffice = assets.Background(107)
    MaskDeMasquesLair = assets.Background(109)
    MattEngardesHotelRoom = assets.Background(112)
    MattEngardesHouse = assets.Background(114)
    MeetingRoom = assets.Background(115)
    MoesRoom = assets.Background(118)
    MrBerrysOffice = assets.Background(121)
    NightCrimeScene = assets.Background(123)
    ParkingGarageLeft = assets.Background(127)
    ParkingGarageRight = assets.Background(130)
    PhoenixsOfficeNight = assets.Background(132)
    PhoenixsOffice = assets.Background(134)
    PoliceStationEntrance2 = assets.Background(138)
    PoliceStationEntrance = assets.Background(139)
    PoliceStation = assets.Background(141)
    SecretRoom = assets.Background(144)
    Studio1 = assets.Background(147)
    Studio2Cottage = assets.Background(150)
    Studio2 = assets.Background(152)
    StudioPath = assets.Background(153)
    TenderLender = assets.Background(155)
    TrainStation = assets.Background(157)
    TrSBienFrenchRestaurantLeft = assets.Background(160)
    TrSBienFrenchRestaurantRight = assets.Background(162)
    TrSBienKitchen = assets.Background(164)
    VitaminSquare = assets.Background(167)
    VonKarma = assets.Background(169)
    WindingWay = assets.Background(172)
    GodotsMaskGlow2 = assets.Background(200)
    GodotsMaskGlow = assets.Background(202)
    PhoenixsCoffeeBlinkingEyes = assets.Background(204)
    BackstageOfColiseum = assets.Background(12882)
    BorschtBeltClub = assets.Background(12883)
    ColiseumStage2 = assets.Background(12884)
    ColiseumStage = assets.Background(12885)
    DefenseLobbyAJ = assets.Background(12886)
    DetentionCenterAJInside = assets.Background(12887)
    DetentionCenterAJOutside = assets.Background(12888)
    DrMeraktissGarage = assets.Background(12889)
    DrMeraktissOffice = assets.Background(12890)
    DrewStudioLeft = assets.Background(12891)
    DrewStudioRight = assets.Background(12892)
    DrewStudioOldLeft = assets.Background(12893)
    DrewStudioOldRight = assets.Background(12894)
    EldoonsNoodleStand = assets.Background(12895)
    EldoonsNoodle = assets.Background(12896)
    HickfieldClinicRoom = assets.Background(12897)
    HickfieldClinic = assets.Background(12898)
    KitakiHome = assets.Background(12899)
    KlaviersDressingRoom = assets.Background(12900)
    KlaviersOffice = assets.Background(12901)
    LamroirsDressingRoomLeft = assets.Background(12902)
    LamroirsDressingRoomRight = assets.Background(12903)
    MeraktisClinicEntrance = assets.Background(12904)
    MeraktisClinic = assets.Background(12905)
    PeoplePark = assets.Background(12906)
    PrisonCell = assets.Background(12907)
    SunshineColiseum2 = assets.Background(12908)
    SunshineColiseum = assets.Background(12909)
    WrightCoTalentAgency = assets.Background(12910)


class Music:
    Allegro2001 = assets.Music(1)
    Trial = assets.Music(2)
    Trial2 = assets.Music(3)
    Cornered = assets.Music(4)
    Allegro2004 = assets.Music(7)
    Objection2004 = assets.Music(8)
    Trial5 = assets.Music(9)
    Truth2002 = assets.Music(10)
    Trial4 = assets.Music(11)
    Cornered2007 = assets.Music(12)
    SearchOpening2007 = assets.Music(4490)
    SteelSamuraisBallad = assets.Music(5345)
    HazyScenery = assets.Music(7062)
    Crossexamining = assets.Music(13)
    Objection = assets.Music(14)
    Maya = assets.Music(15)
    Congratulations = assets.Music(16)
    Truth2001 = assets.Music(17)
    Moderato2001 = assets.Music(18)
    Klavier = assets.Music(19)
    Darkcoffee = assets.Music(20)
    Reminiscence = assets.Music(21)
    Crossexaminingvariation = assets.Music(22)
    Truth2004 = assets.Music(23)
    Objection2007 = assets.Music(24)
    Truth2007 = assets.Music(25)
    Gant = assets.Music(26)
    Moderato2007 = assets.Music(27)
    WildWest = assets.Music(40)
    EmaSkye = assets.Music(41)
    DahliaHawthorne = assets.Music(45)
    Cornered2004Pursuit = assets.Music(57)
    Suspense2007 = assets.Music(58)
    Presto2009 = assets.Music(60)
    SeeingThrough = assets.Music(61)
    TrucyWright = assets.Music(62)
    Truth2011 = assets.Music(63)
    Moderato2004 = assets.Music(64)
    Suspense = assets.Music(65)
    Cornered2002 = assets.Music(66)
    Presto2011 = assets.Music(67)
    Trick2007 = assets.Music(68)
    Moderato2011 = assets.Music(69)
    Truth2009 = assets.Music(70)
    Allegro2011 = assets.Music(71)
    Allegro2009 = assets.Music(72)
    Trial6 = assets.Music(73)
    Objection2011 = assets.Music(74)
    CorneredVariation = assets.Music(75)
    Objection2002 = assets.Music(76)
    Allegro2002 = assets.Music(77)
    Trick2002 = assets.Music(78)
    Trick = assets.Music(79)
    Trial3 = assets.Music(80)
    Objection2009 = assets.Music(81)
    Moderato2009 = assets.Music(82)
    Moderato2002 = assets.Music(113)
    VonKarma = assets.Music(287)
    LukeAtmey = assets.Music(288)
    MilesEdgeworth = assets.Music(289)
    SearchOpening2002 = assets.Music(325)
    SearchMidst2002 = assets.Music(326)
    WarehouseTiger = assets.Music(469)
    Circus = assets.Music(470)
    Cornered2004PursuitVariation = assets.Music(694)
    BlueBadger = assets.Music(695)
    Dl6Incident = assets.Music(696)
    Maya2 = assets.Music(697)
    Cornered2009 = assets.Music(698)
    KitakiFamily = assets.Music(699)
    Sl9Incident = assets.Music(700)
    Gumshoe = assets.Music(701)
    WonTheCase = assets.Music(702)
    TroupeGramarye = assets.Music(703)
    SteelSamurai = assets.Music(704)
    ShiLongLang = assets.Music(705)
    TheGreatTruthBurglar = assets.Music(706)
    Cornered2007Variation = assets.Music(707)
    PsychoLock = assets.Music(709)
    ScarsEtchedByFlame = assets.Music(710)
    SearchCore = assets.Music(711)
    Allegro2007 = assets.Music(712)
    Cornered2002Variation = assets.Music(744)
    Gorgeous = assets.Music(5348)
    KurainVillage = assets.Music(5349)
    Cornered2011 = assets.Music(5351)
    AHurtFox = assets.Music(4491)
    TheGuitarsSerenade = assets.Music(4492)
    AFateSmearedByTricksAndGadgets = assets.Music(4493)
    ForgottenLegend = assets.Music(4494)
    Eccentric2007 = assets.Music(4495)
    SearchCore2007 = assets.Music(4496)
    SolitaryConfinement = assets.Music(4497)
    TragicomicInterview = assets.Music(4498)
    WonTheCase2007 = assets.Music(4499)
    DrewStudio = assets.Music(4500)
    Ringtone = assets.Music(4947)
    Ringtone2 = assets.Music(4948)
    Ringtone3 = assets.Music(4949)
    DefendantLobby = assets.Music(7086)
    PearlFey = assets.Music(7091)


class Sound:
    Whoops = assets.Sound(1)
    Deskslam = assets.Sound(2)
    Realization = assets.Sound(3)
    Shock = assets.Sound(4)
    Applause = assets.Sound(5)
    Badum = assets.Sound(6)
    Damage = assets.Sound(7)
    Evidence = assets.Sound(8)
    Lightbulb = assets.Sound(9)
    Damage2 = assets.Sound(10)
    Heartbeat = assets.Sound(11)
    Yell = assets.Sound(12)
    Yell2 = assets.Sound(13)
    Shooop = assets.Sound(14)
    Smack = assets.Sound(15)
    Gavel = assets.Sound(16)
    Guilty = assets.Sound(17)
    Applause2 = assets.Sound(18)
    Whack = assets.Sound(19)
    Dramapound = assets.Sound(20)
    Snackood = assets.Sound(21)
    Gallerynoise = assets.Sound(23)
    Bang = assets.Sound(24)
    Ping = assets.Sound(25)
    Whip = assets.Sound(26)
    Thwap = assets.Sound(27)
    Explosion = assets.Sound(28)
    Gallerycheer = assets.Sound(29)
    Photosnap = assets.Sound(30)
    Gallery = assets.Sound(31)
    Earthquake = assets.Sound(126)
    Roar = assets.Sound(136)
    GavelQuick = assets.Sound(139)
    Fall = assets.Sound(255)
    Salute = assets.Sound(925)
    GuitarError = assets.Sound(928)
    Chicken = assets.Sound(929)
    Ringtone = assets.Sound(930)
    Gunshot2 = assets.Sound(931)
    Gunshot = assets.Sound(933)
    Megaphone = assets.Sound(934)
    Ringtone2 = assets.Sound(935)
    Ringtone3 = assets.Sound(936)
    Shiny = assets.Sound(937)
    Break = assets.Sound(1631)
    SnapFinger = assets.Sound(1632)
    Snap = assets.Sound(1633)
    Flipbook = assets.Sound(1637)
    Sketch = assets.Sound(1645)
    Break2 = assets.Sound(1922)
    Wrap = assets.Sound(10878)
    Deskslam2 = assets.Sound(10879)


class SpeechBubbles:
    Objection = 1
    HoldIt = 2
    TakeThat = 3
    Gotcha = 4
    Eureka = 5
