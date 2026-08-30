import json

#do i even need this if i have to create weapon kill counts using hooks
#and if kits are randomly generated thats also in hook

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

equipment = [
    "Mining Bomb Launcher"
    "Heavy Lance",
    "Throwing Axes"
]

output = []

for i in primaries:
    obj = {}
    obj["name"] = "X kills with " + i
    obj["category"] = ["Weapons", "Primaries"]
    output.append(obj)

for i in secondaries:
    obj = {}
    obj["name"] = "X kills with " + i
    obj["category"] = ["Weapons", "Secondaries"]
    output.append(obj)

for i in mods:
    obj = {}
    obj["name"] = "X kills with " + i
    if i == "'Knell' Bandit Revolver" or i == "'Honour' Insurgent Pistol":
        obj["category"] = ["Weapons", "Secondaries"]
    else:
        obj["category"] = ["Weapons", "Primaries"]
    output.append(obj)

for i in equipment:
    obj = {}
    obj["name"] = "X kills with " + i
    if i == "Mining Bomb Launcher":
        obj["region"] = "RookR"
    else:
        obj["region"] = "LancerR"
    obj["category"] = ["Weapons", "Class Equipment"]

with open("locations.json", "w") as file:
    json.dump(output, file, indent=4)