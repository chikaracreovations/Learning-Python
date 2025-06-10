# ✅ Define basic math operation functions

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    # ✅ Handle division by zero safely
    try:
        return x / y
    except ZeroDivisionError:
        return "❌ Cannot divide by zero"

# ✅ Show menu to user
def show_menu():
    print("\n📱 SIMPLE CALCULATOR")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

# ✅ Main calculator loop
def main():
    while True:
        show_menu()
        choice = input("➡️ Choose an option (1-5): ").strip()

        if choice == "5":
            print("👋 Goodbye!")
            break

        # ✅ Validate number input
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("❌ Please enter valid numbers.")
            continue

        # ✅ Perform chosen operation
        if choice == "1":
            result = add(num1, num2)
        elif choice == "2":
            result = subtract(num1, num2)
        elif choice == "3":
            result = multiply(num1, num2)
        elif choice == "4":
            result = divide(num1, num2)
        else:
            print("❌ Invalid option.")
            continue

        print(f"🧮 Result: {result}")


# ✅ Run the calculator
if __name__ == "__main__":
    main()