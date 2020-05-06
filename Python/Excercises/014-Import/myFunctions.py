# --------- #1 --------- #
# Create a function that checks if a word is a palindrome
# Create a function that checks if a num is odd/even


def reverseWord(word):
    return word[::-1]


def isPalindrome(wordToCheck):
    reverse = reverseWord(wordToCheck)

    if wordToCheck == reverse:
        return True
    return False


def isOddOrEven(num):
    for item in num:
        if (item % 2) == 0:
            print("{0} is Even".format(item))
        else:
            print("{0} is Odd".format(item))


# -------- # 2 ---------- #
# Create a fucntion that checks if all all list items are ints
# Followed by a function that adds all ints in a list
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
