from logo import logo

print(logo)



def add(x, a):
    return x + a


def subtract(x, a):
    return x - a


def multiply(x, a):
    return x * a


def divide(x, a):
    if a == 0 or x == 0:
        return "Error! Division by zero."
    else:
        return x / a


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


from logo import logo
print(logo)
num1 = float(input("What is your first number: "))
for symbol in operations:
    print(symbol)
should_continue = True
while should_continue:
    operation_symbol = input("pick an operation ")
    num2 = float('What is your next number')
    calculator_function = operations[operation_symbol]
    answer = calculator_function(num1,num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    y = input(f"Type 'i' to continue calculating with {answer}, Type 'n' To start new calculation and 'e' exit program")
    if y == 'y':
        num1 = answer
    elif y == 'n':
        should_continue = True
    else:
        print("exit")
        should_continue = False