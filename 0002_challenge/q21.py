operator=input("Enter an operator (+, -, *, /): ")
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))

match operator:
    case "+":
        print(f"the sum of {num1} + {num2} is {num1+num2}")
    case "-":
        print(f"the difference of {num1} - {num2} is {num1-num2}")
    case "*":
        print(f"the product of {num1} * {num2} is {num1*num2}")
    case "/":
        print(f"the quotient of {num1} / {num2} is {num1/num2}")
    case _: 
        print("invalid operator")