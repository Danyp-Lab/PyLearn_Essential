import math

# clear Workspace
operation = FirstNumber = SecondNumber = Number = 0

# Calculator
print("Welcome to Calculator v0.01 CLI")

print(
    "Operation List \n 1:- \n 2:+ \n 3:* \n 4:/ \n 5:sqrt \n 6:factorial ,\n 7:sin \n 8:cos \n 9:tan \n 10:cot "
)
operation = int(input(" What math operation do you want to do ? (operation number 1...10) "))

# Condition for knowing how many number we need
if operation in range(1, 5):
    FirstNumber = float(input("Write First number"))
    SecondNumber = float(input("Write Second number"))
elif operation in range(5, 7):
    Number = int(input("Write Number"))
elif operation in range(7, 11):
    Degree = int(input("Write degree"))
    Radian = math.radians(Degree)
else:
    print("Operation input is wrong")

# Zero Div Condition
if operation == 4 and SecondNumber == 0:
    print("zero Div Error")

else:
    # for python 3.10+ we use match-case for switching behavior
    # List  1:-  2:+  3:*  4:/  5:sqrt 6:factorial 7:sin  8:cos  9:tan  10:cot
    match operation:
        case 1:
            print("Result=>", FirstNumber, "+", SecondNumber, "=", FirstNumber + SecondNumber)
        case 2:
            print("Result=>", FirstNumber, "-", SecondNumber, "=", FirstNumber - SecondNumber)
        case 3:
            print("Result=>", FirstNumber, "*", SecondNumber, "=", FirstNumber * SecondNumber)
        case 4:
            print("Result=>", FirstNumber, " / ", SecondNumber, "=", FirstNumber / SecondNumber)
        case 5:
            print("Result=>", "Sqrt(", Number, ")=", math.sqrt(Number))
        case 6:
            print("Result=>", "Factorial(", Number, ")=", math.factorial(Number))
        case 7:
            print("Result=>", "Sin(", Degree, ")=", math.sin(Radian))
        case 8:
            print("Result=>", "Cos(", Degree, ")=", math.cos(Radian))
        case 9:
            print("Result=>", "Tan(", Degree, ")=", math.tan(Radian))
        case 10:
            print("Result=>", "Cot(", Degree, ")=", 1 / math.tan(Radian))

        case _:
            print("Your Operation not supported or Wrong")
