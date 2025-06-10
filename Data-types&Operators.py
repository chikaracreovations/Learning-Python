
""" Learning About Different Data types and operators """


a = 4 # int
b= 2.0 # float
c = True # boolean
d = "Hey"   # string
e = ["name", "age" ,"country"]   #list
#dictionary
f = {
    "name": "Alice",
    "age": 30,
    "country": "Canada"
}   #dictionary

print(a)
print(b)
print(c)
print(d)
print(e)
print(e[0])
print(e[1])
print(e[2])
print(f)
print(f["name"])
print(f["age"])
print(f["country"])


#Arithmetic operators

g = a+b
h = a-b
i = a*b
j= a/b

print(g)
print(h)
print(i)
print(j)

# Assignment operators

k = 10 #assign 10 to k
l = 10
l += 1
print(l)
l -= 2
print(l)
l *= 2
print(l)
l /= 3
print(l)

# Relational Operators

if a > b:
    print("a is greater")  # we can use >= also
   
if b<a:
    print("b is smaller")  # we can use <= also

if a!=b:
    print("a is not equal to b")
else:
    print("a is equal to b")
    
  
# Logical operators and or not

if a>b or b>a:
    print("one or both is true")
 
if a>b and a!=b:
    print("both are true")

if  not a==b:
    print("condition was false but turned true")

