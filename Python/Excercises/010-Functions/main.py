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

# print(allPlayersDict)

# 1 write a function that prints the end result of the game using the players and goals lists
goalsScored = [
    {"goalScorer": "Johan Neeskens", "time": 10},
    {"goalScorer": "Johan Neeskens", "time": 28},
    {"goalScorer": "Johan Cruyff", "time": 32},
    {"goalScorer": "Johan Cruyff", "time": 42},
    {"goalScorer": "Johan Cruyff", "time": 47},
    {"goalScorer": "Dick van Dijk", "time": 49},
    {"goalScorer": "Dick van Dijk", "time": 51},
    {"goalScorer": "Gerrie Muhren", "time": 63},
    {"goalScorer": "Barry Hulshoff", "time": 70},
    {"goalScorer": "Herman Veenendaal", "time": 75},
    {"goalScorer": "Johan Cruyff", "time": 78},
    {"goalScorer": "Dick van Dijk", "time": 81},
    {"goalScorer": "Johan Neeskens", "time": 88},
]


def endResult(players=allPlayersDict, goals=goalsScored):
    ajaxScore = 0
    vitesseScore = 0
    for goal in goals:  # Loop over each goal scored
        for player in players:  # Loop over each player
            # Find the player who scored the goal in allPLayersDict
            if goal["goalScorer"] in player["fullName"]:
                # Check to which team the goal scorer belongs
                if player["team"] == "Ajax":
                    ajaxScore += 1
                else:
                    vitesseScore += 1
    print(">>>Ajax beat Vitesse with an end score of", ajaxScore, "-", vitesseScore)


endResult()

# 2 Write a function that prints a match report for every
#   goal and also the end result
# In de 28e minuut scoort Johan Neeskens voor Ajax, het is 2-0.


def gameReport(players=allPlayersDict, goals=goalsScored):
    ajaxScore = 0
    vitesseScore = 0
    for goal in goals:  # Loop over each goal scored
        for player in players:  # Loop over each player
            if goal["goalScorer"] in player["fullName"]:
                # Check to which team the goal scorer belongs
                if player["team"] == "Ajax":
                    ajaxScore += 1
                    print(
                        goal["goalScorer"],
                        "scored in the " + str(goal["time"]) + "th minute. Ajax",
                        ajaxScore,
                        "- Vitesse",
                        vitesseScore,
                    )
                else:
                    vitesseScore += 1
                    print(
                        goal["goalScorer"],
                        "scored in the " + str(goal["time"]) + "th minute. Ajax",
                        ajaxScore,
                        "- Vitesse",
                        vitesseScore,
                    )

    print(">>>Ajax beat Vitesse with an end score of", ajaxScore, "-", vitesseScore)


gameReport()
