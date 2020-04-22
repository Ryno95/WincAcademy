isRaining = False
isSunny = True
isDayTime = True
areCowsGrazing = True
isWindy = True
isManurePitFull = True
cowsNeedToBeMilked = True
isAutumn = True

# 1 If the cows need to be milked they need to be brought inside
if cowsNeedToBeMilked and areCowsGrazing == False:
    print("Cows are inside and can be milked")
else:
    print("Cows need to be brought inside")

# 2 If the cows are grazing in the evening and it;s raining they need to be brought inside
if areCowsGrazing and isDayTime == False and isRaining:
    print("Cows need to be brought inside")
else:
    print("Cows can stay outside")


# 3 If there is a lot of wind the cows need to be brought inside, and they can also be milked
if isWindy and areCowsGrazing and cowsNeedToBeMilked:
    print("Cows need to be brought inside and milked")
elif isWindy and areCowsGrazing:
    print("Cows need to be brought inside")
else:
    print("No worries the milka moos can stay outside")


# 4 If it;s raining and the manure pit is full the land needs to be fertilized
if isRaining and isManurePitFull and areCowsGrazing:
    print("Bring the cows inside, and fertilize the fields")
elif isRaining and isManurePitFull:
    print("Fertilize the lands")
else:
    print("Easy day on the farm, nothing needs to happen")

# 5 If it's autumn and the sun is shining, cut the grass for hay
if isAutumn and isSunny and areCowsGrazing:
    print("Bring the cows in and mow the grass for hay")
elif isAutumn and isSunny:
    print("Shut the hell up and mow yo doamn lawn!")
else:
    print("Another day in the good life of the farm life")

# 6 If it's autumn, sun is shing then the cows can go outside
if isSunny and isAutumn and not areCowsGrazing:
    print("Sun is shining, and so are you, take those beautiful beasts for a stroll")
else:
    print("Leave dem bad boys be")
