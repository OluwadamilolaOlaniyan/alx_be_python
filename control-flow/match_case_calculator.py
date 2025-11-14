num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ") 
match operation:
    case '+':
        result = num1 + num2 
        print(f"The result is: {result}.")
    case '-':
        result = num2 - num1
        print(f"The result is: {result}.")
    case '*':
        result = num1 * num2 
        print(f"The result is: {result}.")
    case '/':
        if num2 == 0 or num1 == 0:
            print("Error:Cannot divide by zero")  
        else:
            result = num1 / num2
            print(f"The result of {num1} {operation} {num2} is: {result}")
    case _:
        print("Invalid operation")