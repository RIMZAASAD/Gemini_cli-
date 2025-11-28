"""
Simple Calculator Module
Provides basic arithmetic operations: addition, subtraction, multiplication, and division.
"""


def add(a, b):
    """Add two numbers."""
    return a + b


def subtract(a, b):
    """Subtract two numbers."""
    return a - b


def multiply(a, b):
    """Multiply two numbers."""
    return a * b


def divide(a, b):
    """Divide two numbers. Raises ValueError if dividing by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def main():
    """Interactive calculator loop."""
    print("=" * 40)
    print("     Simple Calculator")
    print("=" * 40)
    
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        choice = input("\nEnter choice (1/2/3/4/5): ").strip()
        
        if choice == "5":
            print("Thank you for using the calculator. Goodbye!")
            break
        
        if choice not in ["1", "2", "3", "4"]:
            print("Invalid input. Please select a valid operation.")
            continue
        
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == "1":
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == "2":
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == "3":
                print(f"{num1} × {num2} = {multiply(num1, num2)}")
            elif choice == "4":
                print(f"{num1} ÷ {num2} = {divide(num1, num2)}")
        
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Invalid input. Please enter valid numbers.")


if __name__ == "__main__":
    main()
