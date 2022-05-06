#==========================================
# Day 010 - Project: Calculator
#==========================================

def calculate(n1, n2, op):
    match op:
            case '+':
                return n1 + n2
            case '-':
                return n1 - n2
            case '/':
                if n2 != 0:
                    return n1 / n2
                else:
                    return "Error - You cannot divde by Zero"
            case '*':
                return n1 * n2                
            case _:        
                return "Error - Operator not found"


option = ""
result = 0

while option != "f":
    if option != "y":
        number1 = float(input("What's your first number?: "))
    else:
        number1 = result
    operation = input("Pic an operation (+,-,/,*): ")
    number2 = float(input("What's your next number: "))
    result = calculate(number1, number2, operation)
    print(f"Result: {result}")
    option = input(f"Enter 'y' to continue calculation with {result}, 'n' to start again or 'f' no Finish: ")