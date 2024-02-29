#Calculator

choice1= input("What operation do you want to do: + - * /")

choice2 = float(input("What's the first number"))

choice3 = float(input("What's the second number"))

if choice1 == "+":
    answer = choice2 + choice3
    print(answer)
elif choice1 == "-":
    answer = choice2 - choice3
    print(answer)
elif choice1 == "*":
    answer = choice2 * choice3
    print(answer)
elif choice1 == "/":
    if choice2 or choice3 == 0:
        print("Stop dividing by zero")
    else:
        answer = choice2 / choice3
        print(answer)





    