# Default parameters are keywords how already have an default value assigned to them.
# def function(<keyword> = <value>)
# def function(defParameter = 'This is a default parameter')

# 1
userName = input("What's your name?: ")


def greet(name, greeting="Hello"):
    print(f"{greeting} {name}!")


# greet(userName)


# 2
def greetComplete(name, greetingSentence="Hola name! Cuanto tiempo chancho!"):
    print(greetingSentence.replace("name", name))


greetComplete(userName)
