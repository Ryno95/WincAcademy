# --------- Classes ---------#


class Player:
    def __init__(self, fullName, team):
        self.fullName = fullName
        self.team = team


# Rename to goal
class Goals:
    def __init__(self, goalScorer, time):
        self.goalScorer = goalScorer
        self.time = time


class Team:
    def __init__(self, teamName, trainer, players):
        self.teamName = teamName
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
    def __init__(
        self, date, matchLocation, attendance, referee, homeTeam, awayTeam, goals
    ):
        self.date = date
        self.matchLocation = matchLocation
        self.attendance = attendance
        self.referee = referee
        self.homeTeam = homeTeam
        self.awayTeam = awayTeam
        self.goals = goals

    def matchDiscriptionReport(self):
        print(
            f"On {self.date}, {self.homeTeam.teamName} played against {self.awayTeam.teamName} at {self.matchLocation.stadium} in {self.matchLocation.city}."
        )
        print(
            f"A total of {self.attendance} supporters came out to cheer on their respective teams"
        )
        print(f"The referee for the match was {self.referee.referee}.")

    def matchReport(self):

        ajaxScore = 0
        vitesseScore = 0
        for goal in self.goals:
            if goal["team"] == ajax:
                ajaxScore += 1
                print(
                    f'{goal["playerName"]} scored {str(goal["time"])} minutes into the game. Ajax: {ajaxScore}, - Vitesse: {vitesseScore}.'
                )
            else:
                vitesseScore += 1
                print(
                    f'{goal["playerName"]} scored {str(goal["time"])} minutes into the game. Ajax: {ajaxScore}, - Vitesse: {vitesseScore}.'
                )
        print(
            ">>>AFC Ajax beat Vitesse with an end score of",
            ajaxScore,
            "-",
            vitesseScore,
        )


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

goalInfo = []
for goal in goalObjects:
    for player in playerObjects:
        if goal.goalScorer == player.fullName:
            goalInfo.append(
                {"playerName": player.fullName, "time": goal.time, "team": player.team}
            )

# -------------- Running Operations --------- #

allMatchDetailsObject = Match(
    gameDate,
    matchLocation,
    attendance,
    referee,
    AjaxTeamObject,
    VitesseTeamObject,
    goalInfo,
)
print(allMatchDetailsObject.matchDiscriptionReport())
print(allMatchDetailsObject.matchReport())
