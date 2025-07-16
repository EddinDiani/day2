# calculator_cli.py
def add(x, y):      return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def main():
    print("Select operation:")
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")

    while True:
        choice = input("Enter choice (1/2/3/4): ")
        if choice not in ('1','2','3','4'):
            print("Invalid Input, try again.")
            continue

        try:
            num1 = float(input("First number: "))
            num2 = float(input("Second number: "))
        except ValueError:
            print("Please enter valid numbers.")
            continue

        try:
            if choice == '1':
                result = add(num1, num2)
            elif choice == '2':
                result = subtract(num1, num2)
            elif choice == '3':
                result = multiply(num1, num2)
            else:
                result = divide(num1, num2)
        except ValueError as e:
            print(e)
        else:
            print(f"Result: {result}")

        if input("Calculate again? (y/n): ").lower() != 'y':
            break

if __name__ == "__main__":
    main()
