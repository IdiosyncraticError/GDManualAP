import json

phighters = [
    "Sword",
    "Skateboard",
    "Biograft",
    "Katana",
    "Ban Hammer",
    "Rocket",
    "Slingshot",
    "Hyperlaser",
    "Shuriken",
    "Scythe",
    "Medkit",
    "Boombox",
    "Subspace",
    "Vine Staff",
    "Coil"
]

abilities = [
    "M2",
    "E",
    "Q",
    "Phinisher"
]

output = []
for phighter in phighters:
    obj = {}
    obj["count"] = 1
    obj["name"] = phighter + " Unlock"
    obj["category"] = ["Phighter Unlock"]
    obj["progression"] = True
    output.append(obj)
    
for phighter in phighters:
    if phighter == "Sword":
        types = ["", "Base ", "Empowered "]
        for t in types:
            for ab in abilities:
                if ab != "Phinisher" and (t != "Base " or t != "Empowered "):
                    obj = {}
                    obj["count"] = 1
                    obj["name"] = "Sword " + t + ab + " Unlock"
                    if t == "":
                        obj["category"] = ["Sword Ability Unlock", "!Sword Abilitysanity", "Abilitysanity"]
                    else:
                        obj["category"] = ["Sword Ability Unlock", "Sword Abilitysanity", "Abilitysanity"]
                    obj["progression"] = True
                    output.append(obj)
        phin = {
            "count": 1,
            "name": "Sword Phinisher Unlock",
            "category": ["Sword Ability Unlock", "Abilitysanity"],
            "progression": True
        }
        output.append(phin)
    elif phighter == "Skateboard":
        types = ["", "Offboard ", "Onboard "]
        for t in types:
            for ab in abilities:
                if ab != "Phinisher" and (t != "Offboard " or t != "Onboard "):
                    obj = {}
                    obj["count"] = 1
                    obj["name"] = "Skateboard " + t + ab + " Unlock"
                    if t == "":
                        obj["category"] = ["Skateboard Ability Unlock", "!Skateboard Abilitysanity", "Abilitysanity"]
                    else:
                        obj["category"] = ["Skateboard Ability Unlock", "Skateboard Abilitysanity", "Abilitysanity"]
                    obj["progression"] = True
                    output.append(obj)
        phin = {
            "count": 1,
            "name": "Skateboard Phinisher Unlock",
            "category": ["Skateboard Ability Unlock", "Abilitysanity"],
            "progression": True
        }
        output.append(phin)
    elif phighter == "Scythe":
        types = ["", "Melee ", "Ranged "]
        for t in types:
            for ab in abilities:
                obj = {}
                obj["count"] = 1
                obj["name"] = "Scythe " + t + ab + " Unlock"
                if t == "":
                    obj["category"] = ["Scythe Ability Unlock", "!Scythe Abilitysanity", "Abilitysanity"]
                else:
                    obj["category"] = ["Scythe Ability Unlock", "Scythe Abilitysanity", "Abilitysanity"]
                obj["progression"] = True
                output.append(obj)
    elif phighter == "Coil":
        types = ["", "Regen ", "Bounce ", "Haste "]
        for t in types:
            for ab in abilities:
                if ab != "Phinisher":
                    obj = {}
                    obj["count"] = 1
                    obj["name"] = "Coil " + t + ab + " Unlock"
                    if t == "":
                        obj["category"] = ["Coil Ability Unlock", "!Coil Abilitysanity", "Abilitysanity"]
                    else:
                        obj["category"] = ["Coil Ability Unlock", "Coil Abilitysanity", "Abilitysanity"]
                    obj["progression"] = True
                    output.append(obj)
                elif ab == "Phinisher" and t == "":
                    obj = {
                        "count": 1,
                        "name": "Coil Phinisher Unlock",
                        "category": ["Coil Ability Unlock", "Abilitysanity"],
                        "progression": True
                    }
                    output.append(obj)
        for ab in abilities:
            if ab != "Phinisher":
                obj = {
                    "count": 1,
                    "name": "Coil Phinisher " + ab + " Unlock",
                    "category": ["Coil Ability Unlock", "Coil Phinisher Abilitysanity", "Abilitysanity"],
                    "progression": True
                }
                output.append(obj)
    else:
        for ab in abilities:
            obj = {}
            obj["count"] = 1
            obj["name"] = phighter + " " + ab + " Unlock"
            obj["category"] = [phighter + " Ability Unlock", "Abilitysanity"]
            obj["progression"] = True
            output.append(obj)

with open("data.json", "w") as file:
    json.dump(output, file, indent=4)