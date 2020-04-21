# print("Hello World")

age = 25  # Integer
name = "Ryno"  # String
alive = True  # Boolean
x = " Python"
y = " is kick-ass!"

print(age, name, alive)

print("Hi " + name + "!")

# Printing numbers and strings together will result in an error
# unless they'r seperated by a "," or the number is stringefied "str()"
if alive == True:
    print("You are " + str(age) + " years old!" + x + y)
else:
    print("R.I.P.")
