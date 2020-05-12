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
    def __init__(self, team, trainer, players):
        self.team = team
        self.trainer = trainer
        self.players = players


class Referee:
    def __init__(self, referee):
        self.referee = referee


class Location:
    def __init__(self, city, stadium):
        self.city = city
        self.stadium = stadium


class Coach:
    def __init__(self, fullName, team):
        self.fullName = fullName
        self.team = team


class Match:
    def __init__(self, date, matchLocation, attendance, referee, homeTeam, awayTeam):
        self.date = date
        self.matchLocation = matchLocation
        self.attendance = attendance
        self.referee = referee
        self.homeTeam = homeTeam
        self.awayTeam = awayTeam


# --------- Data and Global Variables -------- #

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


# ----------- Match Details ----------#
referee = Referee("Joop Vervoort")
attendance = 6000
gameDate = "Friday 19 Mei 1972"
matchLocation = Location("Amsterdam", "De Meer")


matchDetailsObject = Match(gameDate, matchLocation, attendance, referee, ajax, vitesse)
print(matchDetailsObject.matchLocation.city)

# ----------- Ajax Team ------------#
AjaxTeamName = "AFC Ajax"

ajaxCoach = Coach("Ștefan Kovács", ajax)

teamAjax = [
    Player("Heinz Stuy", ajax),
    Player("Barry Hulshoff", ajax),
    Player("Gerrie Muhren", ajax),
    Player("Ruud Krol", ajax),
    Player("Wim Suurbier", ajax),
    Player("Horst Blankenburg", ajax),
    Player("Sjaak Swart", ajax),
    Player("Arie Haan", ajax),
    Player("Johan Neeskens", ajax),
    Player("Johan Cruyff", ajax),
    Player("Dick van Dijk", ajax),
    Player("Johnny Rep", ajax),
]

AjaxTeamObject = Team(AjaxTeamName, ajaxCoach, teamAjax)

# ----------- Vitesse Team ------------#
vitesseTeamName = "Vitesse"

vitesseCoach = Coach("Cor Brom", vitesse)

teamVitesse = [
    Player("Dick Beukhof", vitesse),
    Player("Ben Gerritsen", vitesse),
    Player("Willy Melchers", vitesse),
    Player("Ben Bosma", vitesse),
    Player("Nico Kunst", vitesse),
    Player("Herman Veenendaal", vitesse),
    Player("Willy Veenstra", vitesse),
    Player("Bram van Kerkhof", vitesse),
    Player("Co Prins", vitesse),
    Player("Thei Rutten", vitesse),
    Player("Henk Vleeming", vitesse),
    Player("Henk Hofs", vitesse),
    Player("John Meeuwsen", vitesse),
]

VitesseTeamObject = Team(vitesseTeamName, vitesseCoach, teamVitesse)

# ---------- All Players -------------#

playerObjects = teamAjax + teamVitesse


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

# class Goal:

goalInfo = []


# ----------- Functions ------------#
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


def matchDiscriptionReport():
    print(
        f"On {matchDetailsObject.date}, {matchDetailsObject.homeTeam} played against {matchDetailsObject.awayTeam} at {matchDetailsObject.matchLocation.stadium} in {matchDetailsObject.matchLocation.city}."
    )
    print(
        f"A total of {matchDetailsObject.attendance} supporters came out to cheers on their respective teams"
    )
    print(f"The referee for the match was {matchDetailsObject.referee.referee}.")


def reportSentance(singleGoal, ajaxScore, vitesseScore):
    print(
        singleGoal["playerName"],
        "scored in the " + str(singleGoal["time"]) + "th minute. Ajax",
        ajaxScore,
        "- Vitesse",
        vitesseScore,
    )


def matchReport(goalInfo=goalInfo):
    matchDiscriptionReport()
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

    print(">>>AFC Ajax beat Vitesse with an end score of", ajaxScore, "-", vitesseScore)


matchReport()
