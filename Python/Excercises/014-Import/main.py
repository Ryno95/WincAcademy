import myFunctions
import myData

check = myFunctions.isPalindrome("malayalam")


if check:
    print("Yes your input is a palindrome")
else:
    print("No your input is not a palindrome")

# for number in myData.lst1:
#   myFunctions.isOddOrEven(number)
# myFunctions.containsOnlyInt(myData.lst1)
# myFunctions.containsOnlyInt(myData.lst2)

myFunctions.sumList(myData.lst2)
