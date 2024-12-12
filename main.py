def add(num1, num2):
    return num1+num2


def sub(num1, num2):
    return num1-num2


def mul(num1, num2):
    return num1*num2


def floor_div(num1, num2):
    if num2 == 0:
        return "Error! Division by zero is not allowed."
    return num1//num2