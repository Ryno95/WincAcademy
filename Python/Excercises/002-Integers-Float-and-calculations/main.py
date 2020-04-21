# integers, whole umbers ex int = 25
# floating points, numbers with decimals ex float = 2.5

cumin = 2.50
apricot = 7
yoghurt = 3.60
cuminAmount = 4
apricotAmount = 12
yoghurtAmount = 2
discountPercentage = 20 / 100

shopping = cumin + apricot + yoghurt
# print(shopping)


shoppingAvg = round(shopping / 3, 2)
# Use round() method to rond numbers, first argument, what you what to round, 2nd argument, until which decimal
print("Average of three items:", shoppingAvg)

totalPrice = (
    (cumin * cuminAmount) + (apricot * apricotAmount) + (yoghurt * yoghurtAmount)
)
print("Total Price:", totalPrice)

discountedPrice = round(totalPrice - (totalPrice * discountPercentage), 2)
print("Discounted Price:", discountedPrice)
