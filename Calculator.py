import math
while True:
    choice = input("Regular calculator(c) or quadratic calculator(q): ")
    print("")
    if choice == "q":
        # Printing headers
        print("QUADRATIC FORMULA CALCULATOR")
        print()
        print("ax^2 + bx + c = 0")
        print()
        # Taking input from user to define variables
        a = float(input("a = "))
        b = float(input("b = "))
        c = float(input("c = "))
        # Checking if formula will squareroot a negative number based on users input; if not else will run
        sqrt = b**2-4*a*c
        if 0 > sqrt:
            print()
            print("No solution")
        else:
            x = (-b + math.sqrt(b**2-4*a*c))/(2*a)
            y = (-b - math.sqrt(b**2-4*a*c))/(2*a)
            print()
            if x == y:
                print("Answer:",round(x,2))
            else:
                print("Answers:", str(round(y,2)) +"," + "",str(round(x,2)))
    if choice == "c":            
        number1 = int(input("Enter the first number: "))
        number2 = int(input("Enter the second number: "))
        function = input("Addition(add), Subtraction(sub), Multiply(mul), Divide(div) or Exponent(expo): ")

        if function == "add":
            result = number1 + number2
            print(number1, "+", number2, "=", result)

        if function == "sub":
            result = number1 - number2
            print(number1, "-", number2, "=", result)

        if function == "mul":
            result = number1 * number2
            print(number1, "*", number2, "=", result)

        if function == "div":
            result = number1 / number2
            print(number1, "/", number2, "=", result)
            
        if function == "expo":
            result = number1 ** number2
            print(number1, "**", number2, "=", result)
        
