# Adds support for floating point numbers.

import sys

def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def isint(value):
    try:
        int(value)
        return True
    except ValueError:
        return False
    
def main(expression):
    stack = expression.split(" ")
    stack = [int(element) if isint(element) else float(element) if isfloat(element) else element for element in stack]
    numbers = []
    operator = ["+", "-", "*", "/"]
    operator_lst = []
    i = 0
    j = 0

    for element in stack:
        if isinstance(element, int):
            numbers.append(element)
        elif isinstance(element, float):
            numbers.append(element)
        elif element in operator:
            operator_lst.append(element)
        else:
            print("Input contains invalid characters.")

    numbers.reverse()
    check = ((len(operator_lst) + 1) == len(numbers)) and (len(stack) != 0)

    print(f"Stack: {stack}, Count: {len(stack)} \nNumbers:{numbers}, Count: {len(numbers)} \nOperators:{operator_lst}, Count: {len(operator_lst)} \nCheck Status: {check}")

    if check == True:
        while i < len(numbers) and j < len(operator_lst):
            first = numbers[0]
            second = numbers[1]
            current_operator = operator_lst[j]
            try:
                if current_operator == "+":
                    result = first + second
                elif current_operator == "-":
                    result = second - first
                elif current_operator == "*":
                    result = first * second
                elif current_operator == "/":
                    result = second / first
            except ZeroDivisionError:
                print("Cannot divide by zero.")
                break

            numbers = [result] + numbers[2:]
            position = stack.index(first)
            stack[position] = result
            stack.remove(second)
            stack.remove(current_operator)
            j += 1
            print(stack)
    elif check == False:
        print("Invalid stack.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("Please provide a stack as an argument.")
