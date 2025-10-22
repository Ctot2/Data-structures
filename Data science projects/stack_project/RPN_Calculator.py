

def calculator_game_loop(my_stack):
    while True:
        x = input("enter a int, +, -, *, /, or exit: ")
        if x == "+":
            addition(my_stack)
        elif x == "-":
            subtraction(my_stack)
        elif x == "*":
            multiplication(my_stack)
        elif x == "/":
            division(my_stack)
        elif x == "exit":
            break
        else:
            input_numbers(my_stack, x)

def input_numbers(my_stack, x):
    while True:
        try:
            int(x)
            my_stack.push(int(x))
            break
        except ValueError:
            print("invalid entry. please enter either a int, +, -, *, or /")
            break

def addition(my_stack):
    if my_stack.size() > 1:
        num1 = my_stack.pop()
        num2 = my_stack.pop()
        answer = num1 + num2
        my_stack.push(answer)
    else:
        print("input another number")

def subtraction(my_stack):
    if my_stack.size() > 1:
        num1 = my_stack.pop()
        num2 = my_stack.pop()
        answer = num1 - num2
        my_stack.push(answer)
    else:
        print("input another number")

def multiplication(my_stack):
    if my_stack.size() > 1:
        num1 = my_stack.pop()
        num2 = my_stack.pop()
        answer = num1 * num2
        my_stack.push(answer)
    else:
        print("input another number")

def division(my_stack):
    if my_stack.size() > 1:
        num1 = my_stack.pop()
        num2 = my_stack.pop()
        answer = num1/num2
        my_stack.push(answer)
    else:
        print("input another number")