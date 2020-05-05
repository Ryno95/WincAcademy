import math

# Create a function to calculate the newton of
# different objects on different celestial bodies


def gramToKilogram(gram):
    inKilogram = gram / 1000
    return inKilogram


def milligramToKilogram(milligram):
    inKilogram = milligram / 1000000
    return inKilogram


def kilometerToMeter(kilometer):
    inMeters = kilometer * 1000
    return inMeters


def newtonForce(mass, gravity):
    force = round(mass * gravity, 2)
    print(force)


# mass in kilograms
newtonForce(gramToKilogram(100), 9.8)  # Apple of 100gr on earth
newtonForce(800, 9.8)  # Cow of 800kg on earth
newtonForce(gramToKilogram(100), 24.9)  # 100gr on Jupiter
newtonForce(milligramToKilogram(15), 274)  # 15mg on the Sun

# 2 Create a function that determines the gravitational pull between 2 objects
# Writing exponentials, math.pow(2, 3) = 8
# force = g * ((objectOneMass * objectTwoMass) / math.pow(distanceBetweenObjects, 2))


def gravitationalForce(objectOneMass, objectTwoMass, distanceBetweenObjects):
    G = 6.674 * (math.pow(10, -11))
    force = G * ((objectOneMass * objectTwoMass) / math.pow(distanceBetweenObjects, 2))
    return force


# gravitational pull in newton between an apple (100gr)and the earth(5.972 * 10tothepowerof24), 6371km apart(surface of the earth)
gravitationalForce(
    gramToKilogram(100), (5.972 * math.pow(10, 24)), kilometerToMeter(6371)
)

# 3
# Distance is in AU https://en.wikipedia.org/wiki/Astronomical_unit
distanceCombinations = [
    {"from": "Mercury", "to": "Venus", "distance": 0.34},
    {"from": "Mercury", "to": "Earth", "distance": 0.61},
    {"from": "Mercury", "to": "Mars", "distance": 1.14},
    {"from": "Mercury", "to": "Jupiter", "distance": 4.82},
    {"from": "Mercury", "to": "Saturn", "distance": 9.14},
    {"from": "Mercury", "to": "Uranus", "distance": 18.82},
    {"from": "Mercury", "to": "Neptune", "distance": 29.70},
    {"from": "Venus", "to": "Earth", "distance": 0.28},
    {"from": "Venus", "to": "Mars", "distance": 0.8},
    {"from": "Venus", "to": "Jupiter", "distance": 4.48},
    {"from": "Venus", "to": "Saturn", "distance": 8.80},
    {"from": "Venus", "to": "Uranus", "distance": 18.49},
    {"from": "Venus", "to": "Neptune", "distance": 29.37},
    {"from": "Earth", "to": "Mars", "distance": 0.52},
    {"from": "Earth", "to": "Jupiter", "distance": 4.2},
    {"from": "Earth", "to": "Saturn", "distance": 8.52},
    {"from": "Earth", "to": "Uranus", "distance": 18.21},
    {"from": "Earth", "to": "Neptune", "distance": 29.09},
    {"from": "Mars", "to": "Jupiter", "distance": 3.68},
    {"from": "Mars", "to": "Saturn", "distance": 7.99},
    {"from": "Mars", "to": "Uranus", "distance": 17.69},
    {"from": "Mars", "to": "Neptune", "distance": 28.56},
    {"from": "Jupiter", "to": "Saturn", "distance": 4.32},
    {"from": "Jupiter", "to": "Uranus", "distance": 14.01},
    {"from": "Jupiter", "to": "Neptune", "distance": 24.89},
    {"from": "Saturn", "to": "Uranus", "distance": 9.7},
    {"from": "Saturn", "to": "Neptune", "distance": 20.57},
    {"from": "Uranus", "to": "Neptune", "distance": 10.88},
]

# Weight is in 10 ** 24 kg
weight = {
    "Mercury": 0.33,
    "Venus": 4.87,
    "Earth": 5.97,
    "Mars": 0.64,
    "Jupiter": 1898,
    "Saturn": 568,
    "Uranus": 86.8,
    "Neptune": 102,
}

planetWeights = []
for planet in weight:
    planetWeights.append({"planetName": planet, "planetWeight": weight[planet]})


def auToMeters(au):
    meters = au * (1.495978707 * math.pow(10, 11))
    return meters


def trueWeight(givenWeight):
    usuableWeight = givenWeight * math.pow(10, 24)
    return usuableWeight


def gravitationalPull(objectOneMass, objectTwoMass, distanceBetweenObjects):
    G = 6.674 * (math.pow(10, -11))
    gravitaionalForce = G * (
        (objectOneMass * objectTwoMass) / math.pow(distanceBetweenObjects, 2)
    )
    print(f"     {gravitaionalForce} Newtons")


def gravitationalPullReport(combinations=distanceCombinations):
    for combination in combinations:
        planetOneKey = combination["from"]
        planetTwoKey = combination["to"]
        print(f"{planetOneKey} en {planetTwoKey} attract each other with a force of: ")
        gravitationalPull(
            trueWeight(weight[planetOneKey]),
            trueWeight(weight[planetTwoKey]),
            auToMeters(combination["distance"]),
        )


gravitationalPullReport()
