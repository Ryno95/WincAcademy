import myFunctions
import myData


# ------------- #1 ----------#
check = myFunctions.isPalindrome("malayalam")


if check:
    print("Yes your input is a palindrome")
else:
    print("No your input is not a palindrome")


myFunctions.isOddOrEven(myData.lst1)

# --------------- #2 ----------#

myFunctions.containsOnlyInt(myData.lst1)
myFunctions.containsOnlyInt(myData.lst2)

myFunctions.sumList(myData.lst1)
