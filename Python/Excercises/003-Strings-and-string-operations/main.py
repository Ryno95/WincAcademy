hans = "Hans van Breukelen"
berry = "Berry van Aerle"
frank = "Frank Rijkaard"
ronald = "Ronald Koeman"
adri = "Adri van Tiggelen"
gerald = "Gerald Vanenburg"
arnold = "Arnold Mühren"
jan = "Jan Wouters"
erwin = "Erwin Koeman"
marco = "Marco van Basten"
ruud = "Ruud Gullit"

firstGoal = 35
secondGoal = 54

goalScorers = ruud + " " + ronald
# print(goalScorers)

print(ruud + "scoorde in de " + str(firstGoal) + "e minuut.")
print(ronald + "scoorde in de " + str(secondGoal) + "e minuut.")

# Voornaam van een speler
ronaldName = ronald[0 : ronald.find(" ")]
print(ronaldName)

# lengte van een speler achternaam
geraldAchternaamLengte = len(gerald[gerald.find(" ") + 1 :])
print(geraldAchternaamLengte)

# Allen voor letter en achternaame

AdriVoorLetterEnAchternaam = adri[0] + ". " + adri[adri.find(" ") + 1 :]
print(AdriVoorLetterEnAchternaam)


vierKeerMaco = (4 * (marco[0 : marco.find(" ")] + "! ")).rstrip()
print(vierKeerMaco)


vierKeerMacoZonderSpatie = vierKeerMaco.rstrip()
print(len(vierKeerMaco))
print(type(vierKeerMaco))


print(vierKeerMaco[26] == " ")
