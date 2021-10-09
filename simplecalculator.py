
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
            "+": add,
            "-": subtract,
            "*": multiply,
            "/": divide
}



def calc():
    run_calc = True

    num1 = float(input("What's the number?: "))
    for sign in operations:
        print(sign)
    operation_symbol = input("Which operation do you want to use? ")
    num2 = float(input("What's the number?: "))

    calc_func = operations[operation_symbol]
    answer = calc_func(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")


    while run_calc:
        if input(f"Do you want to add a number after {answer}? 'y' or 'n':\n") == 'y':
            answer1 = answer
            operation_symbol = input("Which operation do you want to use? ")
            num3 = float(input("What's the number?: "))

            calc_func = operations[operation_symbol]
            answer = calc_func(answer1, num3)

            print(f"{answer1} {operation_symbol} {num3} = {answer}")


        else:
            run_calc = False
            print("Restarting Calculator")
            calc()

calc()
