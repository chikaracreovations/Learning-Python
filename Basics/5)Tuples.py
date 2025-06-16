#Tupes

""" A tuple is like a list, but with one big difference:
Tuples are immutable — once created, you cannot change, add, or remove items.
"""

my_tuple = (1, 2, 3)
another = 4, 5, 6
single = (42,)    # This is a tuple
not_a_tuple = (42)  # This is just an integer
print(my_tuple)
print(another)

fruits = ("apple", "banana", "mango")
print(fruits[0])         # apple
print(fruits[-1])        # mango
print(len(fruits))       # 3
print("banana" in fruits)  # True

#❌ Can't Modify Tuples

#They're faster than lists (internally)
#They're safe (accidental modification is not possible)
#Often used to represent fixed collections
#Can be used as dictionary keys (lists can’t)


#🔁 Tuple Unpacking:
#We can extract values from a tuple like this:

person = ("Alice", 25, "Engineer")
name, age, job = person
print(name)  # Alice
print(age)   # 25
print(job)  #Engineer

people = [("Alice", 30), ("Bob", 25)]

for name, age in people:
    print(f"{name} is {age} years old")
 
numbers = (1, 2, 3, 4, 5)
a, *b = numbers
#The * operator tells Python:
# “Put everything else into this variable as a list.”

print(a)  # 1
print(b)  # [2, 3, 4, 5]

#Tuple Functions

t = (1, 2, 2, 4, 3)

print(t.count(2))    # 2 → how many times 2 appears
print(t.index(3))    # 3 → index of item 3

#nested tuples
nested2 = (1, 2, (3, 4), ["a", "b"])
print(nested2[2][1])  # 4
print(nested2[3][0])  # 'a'


nested = ("apple", (1, 2, 3), ["x", "y"])
print(nested[0])       # apple
print(nested[1])       # (1, 2, 3)
print(nested[1][1])    # 2
print(nested[2][0])    # x

#Even though the outer structure is immutable, the list inside it can be changed:
nested[2][1] = "z"
print(nested)  # ('apple', (1, 2, 3), ['x', 'z'])


#Using Tuples as Dictionary Keys
my_dict = {("x", 1): "value"}

locations = {
    ("Paris", "France"): "Eiffel Tower",
    ("Rome", "Italy"): "Colosseum"
}

print(locations[("Paris", "France")])  # Eiffel Tower
