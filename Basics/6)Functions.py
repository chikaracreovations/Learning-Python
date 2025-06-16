
#Basic Functions & Calling

def greet():
    print("Hello!")  
greet()  # runs the code inside greet()

#____________________________________________

#Passing arguement to functions

def greet(name):
    print("Hello, " + name + "!")

greet("Alice")   # prints Hello, Alice!

#____________________________________________

#Using Return statememt to return a value from a function

def add(a, b):
    return a + b


c = int(input("enter first number: "))
d= int(input("enter second number: "))
result = add(c, d)
print("Sum =")
print(result)    # prints sum

#____________________________________________

#some more basic functions with conditions and loops

def grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    else:
        return "C"

print(grade(96))  # Output: A
print(grade(85))  # Output: B
print(grade(70))  # Output: C


def simple_program():
    
    print( "The Sun rises in the east")
    answer= input("Enter your answer: ")

    if answer == "true":
       print("Right answer")
    elif answer =="false":
       print("Wrong answer")
    else:
       print("invalid answer , please enter true or false")
       simple_program()
       
simple_program()

def fun_game():
    while True:
        value=input("Do you love me? ")
        if value == "yes":
            print("I love you too!")
            break
        print("wrong answer")
    
fun_game()
        

#____________________________________________


