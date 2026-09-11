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

equipment = [
    "Mining Bomb Launcher"
    "Heavy Lance",
    "Throwing Axes"
]

output = []
victory = {
    "name": "victory",
    "requires": "{OptionCount(@Weapons, win_count}",
    "victory": True
}
output.append(victory)

for i in primaries:
    obj = {}
    obj["name"] = "<placeholder> kills with " + i
    obj["category"] = ["Weapons", "Primaries"]
    output.append(obj)

for i in secondaries:
    obj = {}
    obj["name"] = "<placeholder> kills with " + i
    obj["category"] = ["Weapons", "Secondaries"]
    if i == "'Hope' Automatic Pistol":
        obj["category"].append("Hope")

    output.append(obj)

for i in mods:
    obj = {}
    obj["name"] = "<placeholder> kills with " + i
    if i == "'Knell' Bandit Revolver" or i == "'Honour' Insurgent Pistol":
        obj["category"] = ["Weapons", "Secondaries"]
    else:
        obj["category"] = ["Weapons", "Primaries"]
    output.append(obj)

for i in equipment:
    obj = {}
    obj["name"] = "<placeholder> kills with " + i
    if i == "Mining Bomb Launcher":
        obj["region"] = "RookR"
    else:
        obj["region"] = "LancerR"
    obj["category"] = ["Weapons", "Class Equipment"]
    output.append(obj)

# evil ass random locations
# name, category, region, requirement
# name and category determined by the script
# region determined by class
# requirement determined by everything else
# if hope is turned off, replace with honour
# for future, pick randomly from the lists above so no read function is needed (cough multiple options cough)
temp_suggestions = [
    ["Soldat", "Prince", "Hope/Honour", "Apparition"],
    ["Soldat", "Equine Sawed", "Grace", "Tunnel-Rat"],
    ["Soldat", "Judgement", "Grace", "Black Hand"],
    ["Soldat", "Talon Cavalry", "Talon", "Veteran"],
    ["Soldat", "Crossbow", "Talon", "Apparition"],
    ["Soldat", "Whisper", "Knell", "Apparition"],
    ["Soldat", "Equine", "Knell Bandit", "Greyhound"],
    ["Soldat", "Hellion", "Grace/Knell", "Apparition"], #jester this is highkey appa slop bro
    ["Soldat", "Volk Front", "Talon", "Black Hand"],
    ["Soldat", "Negotiator Long", "Negotiator", "Greyhound"],
    ["Soldat", "Judgement Incendiary", "Grace", "Devil Dog"],
    ["Rook", "Volk", "Talon/Negotiator", "Survivalist"],
    ["Rook", "Crossbow", "", "Devil Dog"],
    ["Mortician", "Hellion Heavy", "", "Black Hand"],
    ["Mortician", "Crestfall Ranger", "", "Devil Dog"],
    ["Mortician", "Judgement", "", "Greyhound"],
    ["Mortician", "Judgement", "", "Marksman"],
    ["Mortician", "Negotiator", "Negotiator", "Butcher"],
    ["Mortician", "Grace", "Grace", "Ambidextrous"], #you can really tell which classes jester plays
    ["Mortician", "Honour Insurgent", "Honour Insurgent", "Ambidextrous"],
    ["Mortician", "Kingslayer", "", "Tunnel-Rat"],
    ["Mortician", "Adjudicator", "", "Veteran"],
    ["Mortician", "Whisper Flyboy", "", "Chemist"],
    ["Mortician", "Equine Sawed", "", "Tunnel-Rat"],
    ["Officer", "Judgement Incendiary", "Talon", "Survivalist"],
    ["Officer", "Talon", "Talon", "Devil Dog"],
    ["Jaeger", "Grace", "Union", "Apparition"],
    ["Jaeger", "Crestfall", "", "Tunnel-Rat"],
    ["Vanguard", "Grace", "", "Butcher"],
    ["Lancer", "", "", "Apparition"],
    ["Lancer", "", "Grace", "Survivalist"]
]

def read_require(weapon: str):
    final = ""

    if "/" in weapon:
        weaponlist = weapon.rsplit("/")
        weapons = []
        for i in weaponlist:
            weapons.append(get_weapon(i))
        final = weapons[0] + "| or |" + weapons[1]
    elif " " in weapon:
        mod = weapon.rsplit(" ")
        final = get_weapon_mod(mod[0])
    else:
        final = get_weapon(weapon)
    return "|" + final + "|"

def get_weapon(weapon: str):
    for i in primaries:
        if weapon in i:
            return i

    for i in secondaries:
        if weapon in i:
            return i

def get_weapon_mod(weapon: str):
    for i in mods:
        if weapon in i:
            return i

def get_perk(perk: str):
    for i in perks:
        if perk in i:
            return i

for i in temp_suggestions:
    obj = {}
    obj["name"] = "<placeholder-random> kills on: "
    for index in range(4):
        obj["name"] += i[index]
        if index != 3:
            obj["name"] += ", "

    obj["category"] = "Random Kits"
    obj["region"] = i[0] + "R"
    requirestring = ""
    for j in range(3):
        if j != 2 and i[j+1] != "":
            requirestring += read_require(i[j+1])
            requirestring += " and "
        elif i[j+1] != "":
            requirestring += "|" + get_perk(i[j+1]) + "|"
    obj["requires"] = requirestring
    output.append(obj)

with open("locations.json", "w") as file:
    json.dump(output, file, indent=4)