# --------- Classes ---------#


class Player:
    def __init__(self, fullName, team):
        self.fullName = fullName
        self.team = team


class Goal:
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

    def printMatchDiscription(self):
        print(
            f"On {self.date}, {self.homeTeam.teamName} played against {self.awayTeam.teamName} at {self.matchLocation.stadium} stadium in {self.matchLocation.city}."
        )
        print(
            f"A total of {self.attendance} supporters came out to cheer on their respective teams"
        )
        print(f"The referee for the match was {self.referee.referee}.")

    def printMatchReport(self):
        ajaxScore = 0
        vitesseScore = 0
        for goal in self.goals:
            if goal["team"] == ajax:
                ajaxScore += 1
                print(
                    f'{goal["playerName"]} scored {str(goal["time"])} minutes into the game for {goal["team"]}. Ajax: {ajaxScore}, - Vitesse: {vitesseScore}.'
                )
            else:
                vitesseScore += 1
                print(
                    f'{goal["playerName"]} scored {str(goal["time"])} minutes into the game for {goal["team"]}. Ajax: {ajaxScore}, - Vitesse: {vitesseScore}.'
                )
        print(
            ">>>AFC Ajax beat Vitesse with an end score of",
            ajaxScore,
            "-",
            vitesseScore,
        )


# --------- Data and Global Variables -------- #

ajaxList = [
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

vitesseList = [
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
ajaxTeamName = ajax

ajaxCoach = Coach("Ștefan Kovács", ajax)

ajaxPlayers = [Player(player, ajax) for player in ajaxList]

AjaxTeamObject = Team(ajaxTeamName, ajaxCoach, ajaxPlayers)

# ----------- Vitesse Team ------------#
vitesseTeamName = vitesse

vitesseCoach = Coach("Cor Brom", vitesse)

vitessePlayers = [Player(player, vitesse) for player in vitesseList]


VitesseTeamObject = Team(vitesseTeamName, vitesseCoach, vitessePlayers)

# ---------- All Players -------------#

playerObjects = ajaxPlayers + vitessePlayers


# -------------- Goals --------------#
goalObjects = [
    Goal("Johan Neeskens", 10),
    Goal("Johan Neeskens", 28),
    Goal("Johan Cruyff", 32),
    Goal("Johan Cruyff", 42),
    Goal("Johan Cruyff", 47),
    Goal("Dick van Dijk", 49),
    Goal("Dick van Dijk", 51),
    Goal("Gerrie Muhren", 63),
    Goal("Barry Hulshoff", 70),
    Goal("Herman Veenendaal", 75),
    Goal("Johan Cruyff", 78),
    Goal("Dick van Dijk", 81),
    Goal("Johan Neeskens", 88),
]

goalInfo = []
for goal in goalObjects:
    for player in playerObjects:
        if goal.goalScorer == player.fullName:
            goalInfo.append(
                {"playerName": player.fullName, "time": goal.time, "team": player.team}
            )

# -------------- Running Operations --------- #

matchDetails = Match(
    gameDate,
    matchLocation,
    attendance,
    referee,
    AjaxTeamObject,
    VitesseTeamObject,
    goalInfo,
)

matchDetails.printMatchDiscription()
matchDetails.printMatchReport()
