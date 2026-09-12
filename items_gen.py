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

filler_nation = [
        "This war is not the first and it will not be the last, fight for our future!",
        "We are stronger than this, Soldiers! Do not give in to these freaks!",
        "Press on to victory!",
        "The Nation salutes you!",
        "Send them all to hell!",
        "These fanatics think they can rule our proud Nation, show them our might and what true conviction is!",
        "These tyrants know nothing of freedom! Cut them down and we shall liberate the world from this plague!"
]
filler_empire = [
    "Onwards to victory, for the Golden Empire, and the Golden Era.",
    "The Reaper looms large over their corrupted hearts. Let them regret being weeds in the garden of God.",
    "Let these heretics fall by your blade, win this skirmish for the Golden Empire and our future.",
    "You are blessed this righteous day.",
    "Fight on and do not falter.",
    "Maintain your pace.",
    "The Empire blesses you this day, ensure the dogs do not see the light of day."
]

for i in filler_nation:
    obj = {}
    obj["count"] = 0
    obj["name"] = "King's Decree: " + i
    obj["filler"] = True
    output.append(obj)

for i in filler_empire:
    obj = {}
    obj["count"] = 0
    obj["name"] = "Queen's Will: " + i
    obj["filler"] = True
    output.append(obj)

with open("items.json", "w") as file:
    json.dump(output, file, indent=4)