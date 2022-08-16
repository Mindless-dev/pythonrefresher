from art import logo

### calculator ###

print(logo)

# add function


def add(n1, n2):
    """adds two numbers together"""
    return n1+n2

# subtract


def subtract(n1, n2):
    """subtracts n1 with n2"""
    return n1-n2

# mulitply


def multiply(n1, n2):
    """multplies two numbers together"""
    return n1*n2


# divide
def divide(n1, n2):
    """divides two numbers"""
    return n1/n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide}


def calculator():
    num1 = float(input("What's the first number? "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation : ")
        num2 = float(input("What's the next number? "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f"type 'y' to continue calculating with{answer} or type 'n' to start a new calculation: ") == "y":
            num1 = answer

        else:
            should_continue = False
            calculator()


calculator()
