# Because Python is a strong typed language, operators only work on the same kind of operands ex 9+7 or "str" + "str"
preiPrijsPerKilo = 2

print("Prei kost " + str(preiPrijsPerKilo) + " euro per kilo")

preiOrder = "prei 4"

preiOrderAmount = int(preiOrder[preiOrder.find(" ") + 1 :])
print(type(preiOrderAmount))

preiOrderCost = preiPrijsPerKilo * preiOrderAmount
print("De totale kosten van de bestelling is:", preiOrderCost, "euro")


broccoliPrysPerKilo = 2.34
broccoliOrderAmount = 1.6
broccoliOrderCost = round(broccoliOrderAmount * broccoliPrysPerKilo, 2)
print(
    str(broccoliOrderAmount) + " kilo broccoli kost " + str(broccoliOrderCost) + " euro"
)
