# Simple finite while loops
n = 5
while n > 0:
    n -= 1
    print(n)


a = ["foo", "bar", "baz"]
while a:  # != ['']
    print(a.pop(-1))


# while loop with an else statement
# while <expr>:
#    <statement(s)>
# else:
#    <additional_statement(s)>


n = 5
while n > 0:
    n -= 1
    print(n)
else:
    print("Loop done.")
