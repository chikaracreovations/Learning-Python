
"""
Learning about try , except &  infinite while loops
"""

while True:
    try:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        break  # ✅ Exit loop if both inputs are valid
    except:
        print("❌ Invalid input. Please enter numbers only.")


try:
    # Risky code here
    a = x / y
    print(a)
except:
    #In case of ZeroDivisionError
    print("Something went wrong")