# Global Variables
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
        allPlayersDict.append({"fullName": player, "id": i, "team": "ajax"})
        i += 1

j = 0
for player in vitessePlayers:
    if j < len(vitessePlayers):
        allPlayersDict.append({"fullName": player, "id": (j + 12), "team": "vitesse"})
        j += 1


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

goalInfo = []


# Functions
def getGoalInfo(players=allPlayersDict, goals=goalsScored):
    for goal in goals:
        for player in players:
            if goal["goalScorer"] in player["fullName"]:
                goalInfo.append(
                    {
                        "playerName": player["fullName"],
                        "time": goal["time"],
                        "team": player["team"],
                    }
                )
    return goalInfo


def reportSentance(singleGoal, ajaxScore, vitesseScore):
    print(
        singleGoal["playerName"],
        "scored in the " + str(singleGoal["time"]) + "th minute. Ajax",
        ajaxScore,
        "- Vitesse",
        vitesseScore,
    )


def matchReport(goalInfo=goalInfo):
    getGoalInfo()
    ajaxScore = 0
    vitesseScore = 0

    for goal in goalInfo:
        if goal["team"] == "ajax":
            ajaxScore += 1
            reportSentance(goal, ajaxScore, vitesseScore)
        else:
            vitesseScore += 1
            reportSentance(goal, ajaxScore, vitesseScore)

    print(">>>Ajax beat Vitesse with an end score of", ajaxScore, "-", vitesseScore)


matchReport()
