# List & List Methods
fruits = ["apple", "banana"]
print(fruits)

print()
print("Adding using append")
fruits.append("mango")
print(fruits)
fruits.append("guava")
print(fruits)
fruits.append("grape")       # add to end
print(fruits)

print()
print("Changing value at a index (here 1)")
fruits[1] = "orange"
print(fruits)  

print()
print("Adding a new value at a particular index (here 1)")
fruits.insert(1, "kiwi")     # insert at index
print(fruits)

print()
print("After sorting alphabetically")
fruits.sort()
print(fruits)

print()
print("After Reversing")
fruits.reverse()
print(fruits)

print()
print("Removing using value kiwi")
fruits.remove("kiwi")
print(fruits)

print()
print("Removing using pop index 0")
fruits.pop(0)
print(fruits)

print()
print("Extending list")
fruits2 = ["Banana" , "Lychee" , ]
fruits.extend(fruits2)
print(fruits)

print()
print("Counting No of times Banana appears ")
cnt = fruits.count("Banana")
print(cnt)

#____________________________________________

# Python List Methods Reference

my_list = [1, 2, 3, 4, 5]

# .append(x)         → Adds item x to the end of the list
my_list.append(6)

# .insert(i, x)      → Inserts item x at position i
my_list.insert(2, 99)

# .extend(iterable)  → Adds all elements from another iterable (like a list)
my_list.extend([7, 8])

# .remove(x)         → Removes the first occurrence of item x (error if not found)
my_list.remove(99)

# .pop([i])          → Removes and returns item at index i (last item if index not given)
my_list.pop()         # removes 8
my_list.pop(1)        # removes item at index 1

# .clear()           → Removes all items from the list
# my_list.clear()

# .index(x)          → Returns the index of the first occurrence of x
idx = my_list.index(4)

# .count(x)          → Returns the number of times x appears in the list
cnt = my_list.count(2)

# .sort()            → Sorts the list in ascending order (modifies the original list)
my_list.sort()

# .reverse()         → Reverses the elements of the list in place
my_list.reverse()

# .copy()            → Returns a shallow copy of the list
new_list = my_list.copy()

# len(list)          → Number of items
# sum(list)          → Sum of items (must be numbers)
# min(list)          → Smallest item
# max(list)          → Largest item
# list()             → Convert something to a list