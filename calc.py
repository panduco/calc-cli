import argparse
import math
import sys
import os

HISTORY_FILE = "calc_history.txt"

def calculate(expression):
    """Parses and calculates a single expression string."""
    parts = expression.split()
    
    # --- Handle Scientific Functions (e.g., sqrt 16) ---
    if len(parts) == 2:
        func = parts[0].lower()
        try:
            num = float(parts[1])
            if func == "sqrt":
                return math.sqrt(num)
            elif func == "sin":
                return math.sin(math.radians(num)) # Convert degrees to radians
            elif func == "cos":
                return math.cos(math.radians(num))
            elif func == "tan":
                return math.tan(math.radians(num))
            elif func == "log":
                return math.log10(num)
        except ValueError:
            return "Error: Invalid number for function."

    # --- Handle Basic Arithmetic (e.g., 5 + 5) ---
    if len(parts) != 3:
        return "Error: Format must be 'Num Op Num' or 'Func Num' (e.g., 5 + 5 or sqrt 16)"

    try:
        num1 = float(parts[0])
        operator = parts[1]
        num2 = float(parts[2])

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator in ["*", "x", "X"]:
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                return "Error: Division by zero"
            result = num1 / num2
        elif operator == "^":
            result = num1 ** num2
        elif operator == "%":
            result = num1 % num2
        else:
            return f"Error: Unknown operator '{operator}'"

        # Clean output (remove .0 for whole numbers)
        return int(result) if result.is_integer() else round(result, 4)

    except ValueError:
        return "Error: Invalid numbers provided."

def save_to_history(entry):
    with open(HISTORY_FILE, "a") as f:
        f.write(entry + "\n")

def show_history():
    if not os.path.exists(HISTORY_FILE):
        print("No history yet.")
        return
    print("\n--- Calculation History ---")
    with open(HISTORY_FILE, "r") as f:
        print(f.read())

def interactive_mode():
    print("\n--- Advanced Calculator (Interactive) ---")
    print("Type 'exit' to quit, 'history' to view past calculations.")
    print("Format: '5 + 5' or 'sqrt 16'\n")
    
    while True:
        try:
            user_input = input("calc > ").strip()
            
            if user_input.lower() == 'exit':
                print("Goodbye!")
                break
            elif user_input.lower() == 'history':
                show_history()
                continue
            elif not user_input:
                continue

            result = calculate(user_input)
            print(f"= {result}")
            
            # Save to history
            save_to_history(f"{user_input} = {result}")

        except KeyboardInterrupt:
            print("\nGoodbye!")
            break

def main():
    parser = argparse.ArgumentParser(description="Advanced CLI Calculator")
    
    # Mutually exclusive group: either interactive mode OR a direct expression
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-i", "--interactive", action="store_true", help="Start interactive mode")
    group.add_argument("equation", nargs="*", help="The equation to solve (e.g., 5 + 5)")
    
    args = parser.parse_args()

    if args.interactive:
        interactive_mode()
    elif args.equation:
        # Direct mode: python calc.py 5 + 5
        expression = " ".join(args.equation)
        result = calculate(expression)
        print(f"Result: {result}")
        save_to_history(f"{expression} = {result}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()