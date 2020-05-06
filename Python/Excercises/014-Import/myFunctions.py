def reverseWord(word):
    return word[::-1]


def isPalindrome(wordToCheck):
    reverse = reverseWord(wordToCheck)

    if wordToCheck == reverse:
        return True
    return False


def isOddOrEven(num):
    if (num % 2) == 0:
        print("{0} is Even".format(num))
    else:
        print("{0} is Odd".format(num))


hasOnlyInts = False


def containsOnlyInt(input):
    global hasOnlyInts
    for element in input:
        if type(element) != int:
            hasOnlyInts = False
            break
        else:
            hasOnlyInts = True

    if hasOnlyInts:
        print("You input contains only integers")
    else:
        print("Your input contains multiple data types")


def sumList(listToCheck):
    containsOnlyInt(listToCheck)
    if hasOnlyInts:
        sumOfList = sum(listToCheck)
        print(sumOfList)
    else:
        print("Your list contains multiple data types which cannot be added together")
