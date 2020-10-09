import re


print("Our magical calculator")
print("Type 'quit' to exit\n")

# holds result of previously calculated equation
previous = 0
run = True

# define the function to make the calculator work

# eval is a built-in python function


def performMath():
    global run
    global previous
    equation = ""
    if previous == 0:
        equation = input("Enter equation: ")
    else:
        equation = input(str(previous))

    if equation == 'quit':
        print("Goodbye")
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()" "]', '', equation)

        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)

# use a while loop
while run:
    performMath()
