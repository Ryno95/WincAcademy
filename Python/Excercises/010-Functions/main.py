ajaxPlayers = [
    "Heinz Stuy",
    "Barry Hulshoff",
    "Gerrie Muhren",
    "Ruud Krol",
    "Wim Suurbier",
    "Horst Blankenburg",
    "Sjaak Swart",
    "Arie Haan",
    "Johan Neeskens",
    "Johan Cruyff",
    "Dick van Dijk",
    "Johnny Rep",
]
vitessePlayers = [
    "Dick Beukhof",
    "Ben Gerritsen",
    "Willy Melchers",
    "Ben Bosma",
    "Nico Kunst",
    "Herman Veenendaal",
    "Willy Veenstra",
    "Bram van Kerkhof",
    "Co Prins",
    "Thei Rutten",
    "Henk Vleeming",
    "Henk Hofs",
    "John Meeuwsen",
]

allPlayersDict = []
i = 0
for player in ajaxPlayers:
    if i < len(ajaxPlayers):
        allPlayersDict.append({"fullName": player, "id": i, "team": "Ajax"})
        i += 1

j = 0
for player in vitessePlayers:
    if j < len(vitessePlayers):
        allPlayersDict.append({"fullName": player, "id": (j + 12), "team": "Vitesse"})
        j += 1

print(allPlayersDict)
