import json

primaries = [
    "'Prince' Long Rifle",
    "'Adjudicator' Repeating Rifle",
    "'Kingslayer' Percussion Revolver",
    "'Okhotnik' Hunting Crossbow",
    "'Whisper' Silenced Rifle",
    "'Crestfall' Lever Rifle",
    "'Jesse' Combat Rifle",
    "'Equine' Riding Shotgun",
    "'Volk' Scoped Rifle",
    "'Judgement' Breech Rifle",
    "'Hellion' Automatic Shotgun"
]

secondaries = [
    "'Grace' Service Revolver",
    "'Hope' Automatic Pistol",
    "'Honour' Duty Pistol",
    "'Talon' Army Revolver",
    "Cavalry Sword",
    "'Negotiator' Pocket Shotgun",
    "'Knell' Silenced Revolver",
    "'Union' Military Pistol",
    "'Auclair' Lever Pistol"
]

mods = [
    "'Whisper' Flyboy Rifle",
    "'Negotiator' Long Shotgun",
    "'Union' Stocked Pistol",
    "'Hellion' Heavy Shotgun",
    "'Judgement' Incendiary Rifle",
    "'Talon' Cavalry Revolver",
    "'Volk' Frontline Rifle",
    "'Crestfall' Ranger Rifle",
    "'Jesse' Precision Rifle",
    "'Equine' Sawed Shotgun",
    "'Knell' Bandit Revolver",
    "'Honour' Insurgent Pistol"
]

output = []

victory = {
    "name": "victory",
    "victory": True,
    "requires": "{OptionCount(@Win Progression, total_phighter_win_count)}"
}
output.append(victory)

for m in maps:
    for phighter in phighters:
        obj = {}
        obj["name"] = "Win on " + m + " - " + phighter
        obj["region"] = phighter
        obj["category"] = ["Map Wins", phighter + " Map Wins"]
        output.append(obj)

for b in mvp_badges:
    for phighter in phighters:
        obj = {}
        if b.endswith("VP"):
            obj["name"] = "Be the " + b + " - " + phighter
        else:
            obj["name"] = "Get the " + b + " badge - " + phighter
        
        obj["region"] = phighter
        obj["category"] = ["MVP Badges", phighter + " MVP Badges"]
        output.append(obj)

healer = ["Medkit", "Vine Staff", "Coil"]
for h in healer:
    obj = {
        "name": "Get the guardian badge - " + h,
        "region": h,
        "category": ["MVP Badges", h + " MVP Badges"]
    }
    output.append(obj)

        
for hi in rng:
    obj = {
        "name": "Experience " + hi,
        "category": ["Luck Rounds"]
    }
    output.append(obj)
    
for hi in bonus_rounds:
    obj = {
        "name": "Experience " + hi,
        "category": ["Bonus Rounds"]
    }
    output.append(obj)

for hi in sword_events:
    obj = {
        "name": "\"Meet\" " + hi,
        "category": ["Sword Events"]
    }
    output.append(obj)

for title in phest_titles:
    obj = {
        "name": "Earn " + title,
        "category": ["Phest Titles"]
    }
    output.append(obj)

doomsekkar = {
    "name": "Defeat Doomsekkar",
    "category": ["Doomsekkar"]
}
output.append(doomsekkar)

boomball = {
    "name": "Play Boomball",
    "category": ["Boomball"]
}

#for phighter, skin in skins.items():
#    for s in skin:
#        obj = {
#           "name": "Purchase " + s,
#            "region": phighter,
#            "category": ["Skins"]
#        }
#    output.append(obj)

for i in range(skin_count):
    obj = {
        "name": "Purchase " + str(i+1) + " skin(s)",
        "category": ["Skins"]
    }
    output.append(obj)

for i in range(sticker_count):
    obj = {
        "name": "Purchase " + str(i+1) + " sticker(s)",
        "category": ["Stickers"]
    }
    output.append(obj)

for i in badges:
    obj = {}
    obj["name"] = "Get the " + i[0] + " achievement"
    cat_list = ["Achievements"]
    if i[1] == "Challenge":
        cat_list.append(i[1])
    elif i[1] != "":
        obj["region"] = i[1]

    obj["category"] = cat_list

    if 3 == len(i):
        obj["requires"] = i[2]

    output.append(obj)

with open("data.json", "w") as file:
    json.dump(output, file, indent=4)