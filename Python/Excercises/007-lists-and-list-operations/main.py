Shane = ["Shane Embury", "bass", 1987, 2020]  # 1987-Present
Mark = ["Mark Greenway", "vocals", 1989, 2020]  # 1989-1996, 1997-present
Danny = ["Danny Herrera", "drums", 1991, 2020]  # 1991 - present
Mitch = ["Mitch Harris", "guitar", 1990, 2014]  # 1990-2014

Nicholas = ["Nicholas Bullen", "vocals", 1981, 1986]  # 1981-1986
NicolasBass = ["Nicholas Bullen", "bass", 1981, 1986]  # 1981-1986
Miles = ["Miles Ratledge", "drums", 1981, 1985]  # 1981–1985
Simon = ["Simon Oppenheimer", "guitar", 1981, 1981]  # 1981–1982
Graham = ["Graham Robertson", "guitar", 1982, 1985]  # 1982–1985
GrahamBass = ["Graham Robertson", "bass", 1982, 1982]
Daryl = ["Daryl Fedeski", "guitar", 1982, 1982]  # 1982
Finbar = ["Finbar Quinn", "bass", 1983, 1984]  # 1983–1984
Marian = ["Marian Williams", "vocals", 1984, 1984]  # 1984
Damien = ["Damien Errington", "guitar", 1985, 1985]  # 1985
Justin = ["Justin Broadrick", "guitar", 1985, 1986]  # 1985–1986
JustinVocals = ["Justin Broadrick", "vocals", 1985, 1986]  # 1985–1986
Peter = ["Peter Shaw", "bass", 1985, 1985]  # 1985
Mick = ["Mick Harris", "drums", 1985, 1991]  # 1985-1991
Jim = ["Jim Whitely", "bass", 1986, 1987]  # 1986–1987
Frank = ["Frank Healy", "guitar", 1986, 1986]  # 1986
Bill = ["Bill Steer", "guitar", 1987, 1989]  # 1987–1989
Lee = ["Lee Dorrian", "vocals", 1987, 1989]  # 1987–1989
Jesse = ["Jesse Pintado", "guitar", 1989, 2004]  # 1989–2004
Phil = ["Phil Vane", "vocals", 1996, 1997]  # 1996-1997
Erik = ["Erik Burke", "guitar", 2015, 2015]  # 2015
Jesper = ["Jesper Liverod", "bass", 2017, 2017]  # 2017

# while firstNumber > year and secondNumber < year

allBandMembers = [
    Shane,
    Mark,
    Danny,
    Mitch,
    Nicholas,
    NicolasBass,
    Miles,
    Simon,
    Graham,
    GrahamBass,
    Daryl,
    Finbar,
    Marian,
    Damien,
    Justin,
    JustinVocals,
    Peter,
    Mick,
    Jim,
    Frank,
    Bill,
    Lee,
    Jesse,
    Phil,
    Erik,
    Jesper,
]
# print(allBandMembers)

yearsActive = list(range(1981, 2021))
# print(yearsActive)

for x in yearsActive:
    print("The year is " + str(x) + ":")
    for y in allBandMembers:
        if y[2] <= x <= y[3]:
            print(y[0], "was on", y[1])

"""print(
    "Het jaar is 1981.",
    band[0][0],
    "doet",
    band[0][1],
    ",",
    band[2][0],
    "speelt",
    band[2][1],
    "en",
    band[3][0],
    "zit achter de",
    band[3][1],
    ".",
)"""

##print(Shane)
##for i in range(1981, 2021):
##    if allBandMembers[][]


"""band = [Nicholas, NicolasBass, Simon, Miles]
print(
    "Het jaar is 1981.",
    band[0][0],
    "doet",
    band[0][1],
    "en",
    band[1][1],
    ",",
    band[2][0],
    "speelt",
    band[2][1],
    "en",
    band[3][0],
    "zit achter de",
    band[3][1],
    ".",
)

band.remove(NicolasBass),
band.remove(Simon),
band.insert(1, Daryl),
band.insert(2, GrahamBass),
"""
