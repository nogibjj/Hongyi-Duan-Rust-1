import sys
from lib import add, subtract, multiply, divide

def main():
    if len(sys.argv) != 4:
        print("Usage: main.py [add|subtract|multiply|divide] num1 num2")
        sys.exit(1)
    operation = sys.argv[1]
    num1 = float(sys.argv[2])
    num2 = float(sys.argv[3])

    if operation == 'add':
        result = add(num1, num2)
    elif operation == 'subtract':
        result = subtract(num1, num2)
    elif operation == 'multiply':
        result = multiply(num1, num2)
    elif operation == 'divide':
        result = divide(num1, num2)
    else:
        print("Unknown operation.")
        sys.exit(1)

    print(f"The result is: {result}")

if __name__ == "__main__":
    main()
