import argparse
import sys

def calculate(equation_list):
    """
    Parses a list of strings into an equation and solves it.
    Example: ['5', '+', '5'] -> 10.0
    """
    # Validate input length (must be: Num Op Num)
    if len(equation_list) != 3:
        return "Error: Invalid format. Use: Number Operator Number (e.g., 5 + 5)"

    try:
        # Parse parts
        num1 = float(equation_list[0])
        operator = equation_list[1]
        num2 = float(equation_list[2])

        # Perform operation
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator in ["*", "x", "X"]:
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                return "Error: Cannot divide by zero!"
            result = num1 / num2
        else:
            return f"Error: Unknown operator '{operator}'"

        # Format result (remove .0 if it's a whole number)
        if result.is_integer():
            return int(result)
        return round(result, 4)

    except ValueError:
        return "Error: Inputs must be valid numbers."

def main():
    parser = argparse.ArgumentParser(description="A simple CLI Calculator")
    # 'nargs="+"' means "capture one or more arguments into a list"
    parser.add_argument("equation", nargs="+", help="The equation to solve (e.g. 5 + 5)")
    
    args = parser.parse_args()
    
    result = calculate(args.equation)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()