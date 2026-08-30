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

maps = [
    "Banland",
    "BOGIO Skatepark",
    "Chaos Canyon",
    "Craterdust Capital",
    "Darkage Cliffs",
    "DODGEBALL!",
    "Domino Valley",
    "Doomspire",
    "Hotel Elephant",
    "King of the Hill",
    "Nuke The Whales",
    "Protect Telamon",
    "Raven Rock",
    "ROBLOX Arcade",
    "ROBLOX Bowling Alley",
    "ROBLOX City",
    "ROBLOX HQ",
    "ROBLOX Laundromat",
    "ROBLOX Mall",
    "ROBLOX Museum",
    "Rob the ROBLOX Bank",
    "Rocket Arena",
    "Shooting Teapot Observatory",
    "Space Knights",
    "Sword Fight On The Heights",
    "Sword Fighting Tournament",
    "The Bread Factory",
    "The Iron Cafe",
    "Train Demolition",
    "Underground War"
]

mvp_badges = [
    "MVP",
    "SVP",
    "sidekick",
    "perfection",
    "unstoppable",
    "berserker",
    "bloodbath",
    "scourge",
    "bulwark"
]

#skins = {
#    "Sword": ["Sci-Fi Sword", "Marshmallow Sword", "Follower Sword", "Sunburst Sword", "Harpy Sword"],
#    "Skateboard": ["Hoverboard", "Snowboard", "Egobworder", "Surfboard", "Hellboarder"],
#    "Biograft": ["Floatie Biograft", "Biocarved", "Betagraft", "Cocoagraft", "Biohazard", "Beetlegraft"],
#    "Katana": ["Kramptana", "Moaitana", "Cybertana", "Follower Katana", "Katana Neo", "Fishertana"],
#    "Ban Hammer": ["Frankenhammer", "Sunkenhammer", "Clownhammer", "Rockhammer"],
#    "Rocket": ["PJ Rocket", "Buster Rocket", "Stargazer Rocket", "Party Rocket"],
#    "Slingshot": ["Catshot", "Cozyshot", "Cursedshot", "Seashot", "Bugshot"],
#    "Hyperlaser": ["Witchlaser", "Seraphlaser", "Yulaser", "Kittylaser"],
#    "Shuriken": ["Shurifin", "Shuri-long", "Astroken", "Shurisuit"],
#    "Scythe": ["Dutchman Scythe", "Reaper Scythe"],
#    "Medkit": ["Medcarrot", "Pirate Medkit", "Sianachkit", "7MK0", "Bivekit", "Madkit", "Wranglerkit"],
#    "Boombox": ["Cooler Boombox", "Eggsquerade Boombox", "Rainbox", "Astrobox", "Boomwave"],
#    "Subspace": ["Exorspace", "Cutiespace", "Jesterspace", "Grieferspace", "Outerspace", "Glitchspace"],
#    "Vine Staff": ["Valleystaff", "Vine Splash", "Vineberry", "Mothstaff"],
#    "Coil": ["Coil 2.0", "Sharkbite Coil", "Punk Coil", "Werecoil"]
#}

skin_count = 50
sticker_count = 50

rng = [
    "a x13 round",
    "a x66.6 round",
    "Fractured Space"
]

bonus_rounds = [
    "One for All",
    "Phighter Beans",
    "Random Phighters",
    "25% more damage",
    "25% more speed",
    "25% more phinisher charge rate"
]

sword_events = [
    "Firebrand",
    "Windforce",
    "Icedagger",
    "Ghostwalker",
    "Venomshank",
    "Darkheart",
    "Illumina",
    "Dom",
    "Valk"
]

phest_titles = [
    "Fan",
    "Member",
    "Enjoyer",
    "Lover",
    "Pawn",
    "Player",
    "Phighter",
    "Pro",
    "Ace",
    "Expert",
    "Knight",
    "Paladin",
    "Champion",
    "Boss",
    "Master",
    "Ruler",
    "Emperor",
    "Monarch",
    "Idol",
    "Divinity",
    "Deity",
    "God",
    "Celestial",
    "Immortal",
    "a +"
]

badges = [ #option check if abilitysanity is turned on then requires ability unlock
    ["welcome phighter!", ""],
    ["stuck sword", "Sword", "{OptOne(|Sword Phinisher Unlock|)}"],
    ["direct detonation", "Rocket", "{OptOne(|Rocket M2 Unlock|)}"],
    ["sharp shooter", "Slingshot", "{OptOne(|Slingshot Q Unlock|)}"],
    ["guardian angel", "Medkit", "{OptOne(|Medkit Phinisher Unlock|)}"],
    ["bass drop", "Boombox", "{OptOne(|Boombox Phinisher Unlock|)}"],
    ["vehicular manslaughter", "Skateboard", "{OptOne(|Skateboard E Unlock|) or OptOne(|Skateboard Offboard E Unlock)}"], #okay but like fr what the fuck am i putting here sob sob
    ["your demise", "Biograft", "{OptOne(|Biograft Q Unlock|)}"],
    ["bounty collected", "Hyperlaser", "{OptOne(|Hyperlaser Phinisher Unlock|)}"],
    ["experiment successful", "Subspace", "{OptOne(|Subspace Phinisher Unlock|)}"],
    ["sever the soul", "Katana", "{OptOne(|Katana Phinisher Unlock|)}"],
    ["silver shadow", "Shuriken", "{OptAll(|Shuriken Phinisher Unlock| and |Shuriken Q Unlock|)}"],
    #["new beginnings", "Vine Staff", "|Vine Staff Phinisher Unlock|"], #oookay is this one even possible who knows
    ["adjourned", "Ban Hammer", "{OptOne(|Ban Hammer Phinisher Unlock|)}"],
    ["headhunter", "Scythe"], #L no requirements
    ["cold snap", "Coil", "{OptOne(|Coil Phinisher Unlock|)}"],
    ["first steps", ""],
    ["PWNED!", ""],
    ["the one", "Challenge"], #this one needs its own category lmaooo
    #ive nearly gotten a penta like 5 times it pmo
    ["devil's game", ""], #this is also just the x66 location
    ["Supreme Survivor", "Challenge"], #this too
    #["caged by the dead", ""], #this already exists as doomsekkar location so like... idk
    #["level 25"] ??
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