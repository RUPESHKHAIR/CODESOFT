# Task 2-Calculator
def calculator(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            return "Division by zero not allowed"
        return num1 / num2
    else:
        return "Invalid Operation"


def main():
    num1 = float(input("Enter the  First Number:"))
    num2 = float(input("Enter the Second Number:"))
    operator = input("Enter the Operation from +,-,*and/ :")
    x = calculator(num1, num2, operator)
    print(f"The result of {num1} and  {num2} with {operator} is :{x}")


main()
