# --------- Data -------- #

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
ajax = "AFC Ajax"
vitesse = "Vitesse"

# --------- Classes ---------#


class Player:
    def __init__(self, fullName, team):
        self.fullName = fullName
        self.team = team


class Goals:
    def __init__(self, goalScorer, time):
        self.goalScorer = goalScorer
        self.time = time


class Team:
    def __init__(self, team):
        self.team = team


# listofTeams = [Team(ajax), Team(vitesse)]
# for team in listofTeams:
#   print(team.team)


class Match:
    pass


class Referee:
    def __init__(self, referee):
        self.referee = referee


class Location:
    def __init__(self, city, stadium):
        self.city = city
        self.stadium = stadium


class Coach:
    def __init__(self, coach):
        self.coach = coach


# ----------- Ajax Players ------------#

Heinz = Player("Heinz Stuy", ajax)
Barry = Player("Barry Hulshoff", ajax)
Gerrie = Player("Gerrie Muhren", ajax)
Ruud = Player("Ruud Krol", ajax)
Wim = Player("Wim Suurbier", ajax)
Horst = Player("Horst Blankenburg", ajax)
Sjaak = Player("Sjaak Swart", ajax)
Arie = Player("Arie Haan", ajax)
Johan = Player("Johan Neeskens", ajax)
Cruyff = Player("Johan Cruyff", ajax)
DickAjax = Player("Dick van Dijk", ajax)
Johnny = Player("Johnny Rep", ajax)


# ----------- Vitesse Players ------------#

DickVitesse = Player("Dick Beukhof", vitesse)
BenGerritsen = Player("Ben Gerritsen", vitesse)
WillyMelchers = Player("Willy Melchers", vitesse)
BenBosma = Player("Ben Bosma", vitesse)
Nico = Player("Nico Kunst", vitesse)
Herman = Player("Herman Veenendaal", vitesse)
WillyVeenstra = Player("Willy Veenstra", vitesse)
Bram = Player("Bram van Kerkhof", vitesse)
Co = Player("Co Prins", vitesse)
Thei = Player("Thei Rutten", vitesse)
HenkVleeming = Player("Henk Vleeming", vitesse)
HenkHofs = Player("Henk Hofs", vitesse)
John = Player("John Meeuwsen", vitesse)

# ---------- All PLayers -------------#

playerObjects = [
    Heinz,
    Barry,
    Gerrie,
    Ruud,
    Wim,
    Horst,
    Sjaak,
    Arie,
    Johan,
    Cruyff,
    DickAjax,
    Johnny,
    DickVitesse,
    BenGerritsen,
    WillyMelchers,
    BenBosma,
    Nico,
    Herman,
    WillyVeenstra,
    Bram,
    Co,
    Thei,
    HenkVleeming,
    HenkHofs,
    John,
]
# for footballer in playerObjects:
#    print(footballer.fullName, footballer.team)
# -------------- Goals --------------#
goalObjects = [
    Goals("Johan Neeskens", 10),
    Goals("Johan Neeskens", 28),
    Goals("Johan Cruyff", 32),
    Goals("Johan Cruyff", 42),
    Goals("Johan Cruyff", 47),
    Goals("Dick van Dijk", 49),
    Goals("Dick van Dijk", 51),
    Goals("Gerrie Muhren", 63),
    Goals("Barry Hulshoff", 70),
    Goals("Herman Veenendaal", 75),
    Goals("Johan Cruyff", 78),
    Goals("Dick van Dijk", 81),
    Goals("Johan Neeskens", 88),
]
# for goal in goalObjects:
#    print(goal.goalScorer)

# class Goal:

goalInfo = []


# Functions
def getGoalInfo(players=playerObjects, goals=goalObjects):
    for goal in goals:
        for player in players:
            if goal.goalScorer == player.fullName:
                goalInfo.append(
                    {
                        "playerName": player.fullName,
                        "time": goal.time,
                        "team": player.team,
                    }
                )
    return goalInfo


# getGoalInfo()
# print(goalInfo)


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
        if goal["team"] == ajax:
            ajaxScore += 1
            reportSentance(goal, ajaxScore, vitesseScore)
        else:
            vitesseScore += 1
            reportSentance(goal, ajaxScore, vitesseScore)

    print(">>>Ajax beat Vitesse with an end score of", ajaxScore, "-", vitesseScore)


# matchReport()
