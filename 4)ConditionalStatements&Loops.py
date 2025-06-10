
# Using condtional statements and loops


x = int(input("Enter A Number between 1 to 10: "))

y = 7

if x==y:
    print("correct guess")
elif x>y:
    print("your number was greater")
else:
    print("Your number was smaller")


""" Starting with Python 3.10, Python introduced match/case, which behaves similarly to switch in other languages like Java. """

command = "start"
match command:
    case "start":
        print("Starting")
    case "stop":
        print("Stopping")
    case _:
        print("Unknown command")
        
 
# Loops 

for i in range(5):
    print(i)  
    
x = 100
while x < 105:
    print(x)
    x += 1  
 
 #using break and continue with loops
 
for i in range(10):
    if i == 5:
        break
    print(i)
    
for i in range(90, 100, 2):
    if i == 94:
        continue
    print(i)
    
Y = 500
while Y< 510:    
   if Y == 505:
       Y += 1
       continue
   print (Y)
   Y += 1

#infinite loops

while True:
    command2= input("enter a command: ")
    if command2 == "quit":
        print("exiting loop")
        break
    else :
      print("enter again")
      
 
