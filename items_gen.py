import json

classes = [
    "Soldat",
    "Rook",
    "Mortician",
    "Officer",
    "Jaeger",
    "Lancer",
    "Vanguard"
    #cowboy eventually maybe
]

class_equipment = [
    ["Ammunition Pouches", ["SoldatC"]],
    ["Heavy Pickaxe", ["RookC"]],
    ["Mining Bomb Launcher", ["RookC", "Weapon"]],
    ["Construct Hammer", ["RookC"]],
    ["Medical Syrettes", ["MorticianC"]],
    ["Stimulant Compounds", ["MorticianC"]],
    ["Trench Whistle", ["OfficerC"]],
    ["Recon Kit", ["OfficerC"]],
    ["Hunter Kit", ["JaegerC"]],
    ["Smokescreen Bombs", ["JaegerC"]],
    ["Heavy Lance", ["LancerC", "Weapon"]],
    ["Throwing Axes", ["LancerC", "Weapon"]],
    ["Painkiller Injector", ["LancerC"]],
    ["Bulwark's Shield", ["BulwarkC"]],
    ["Rally Banner", ["BulwarkC"]]
]

shocks = [
    "Storm Trooper",
    "Anti-Material Trooper",
    "Flame Trooper",
    "Radio Trooper",
    "Geist Trooper",
    "Trench Trooper",
    "Bulwark Trooper"
]

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

perks = [
    "Greyhound",
    "Hippocratic",
    "Apparition",
    "Butcher",
    "Chemist",
    "Tunnel-Rat",
    "Ambidextrous",
    "Leatherneck",
    "Marksman",
    "Snake Eyes",
    "Devil Dog",
    "Veteran",
    "Black Hand",
    "Survivalist"
]

tools = [
    "Melee Sheath",
    "Mining Pick",
    "First Aid Pouch"
]

output = []
for c in classes:
    obj = {}
    obj["count"] = 1
    obj["name"] = c
    obj["category"] = ["Classes", c + "C"]
    obj["progression"] = True
    output.append(obj)

for e in class_equipment:
    obj = {}
    obj["count"] = 1
    obj["name"] = e[0]
    cat = ["Class Equipment"]
    cat.extend(e[1])
    obj["category"] = cat
    obj["progression"] = True
    output.append(obj)

for s in shocks:
    obj = {}
    obj["count"] = 1
    obj["name"] = s
    obj["category"] = ["Shock Troopers"]
    obj["useful"] = True
    output.append(obj)

for g in primaries:
    obj = {}
    obj["count"] = 1
    obj["name"] = g
    obj["category"] = ["Weapons", "Primaries"]
    obj["progression"] = True
    output.append(obj)

for g in secondaries:
    obj = {}
    obj["count"] = 1
    obj["name"] = g
    obj["category"] = ["Weapons", "Secondaries"]
    if g == "'Hope' Automatic Pistol":
        obj["category"].append("Hope")

    obj["progression"] = True
    output.append(obj)

for g in mods:
    obj = {}
    obj["count"] = 1
    obj["name"] = g
    if g == "'Knell' Bandit Revolver" or g == "'Honour' Insurgent Pistol":
        obj["category"] = ["Weapons", "Mods", "Secondaries"]
    else:
        obj["category"] = ["Weapons", "Mods", "Primaries"]
    obj["progression"] = True
    output.append(obj)

for p in perks:
    obj = {}
    obj["count"] = 1
    obj["name"] = p
    obj["category"] = ["Perks"]
    obj["progression"] = True
    output.append(obj)

for t in tools:
    obj = {}
    obj["count"] = 1
    obj["name"] = t
    obj["category"] = ["Tools"]
    obj["progression"] = True
    output.append(obj)

with open("items.json", "w") as file:
    json.dump(output, file, indent=4)