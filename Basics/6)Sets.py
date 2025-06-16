"""A set is:
Unordered → no indexing or order
Unindexed → can’t access items with [ ]
Mutable → you can add or remove items
Unique → no duplicates allowed """

my_set = {1, 2, 3, 4}
print(my_set)

#Creating Sets
s = {1, 2, 3}
print(s)  # {1, 2, 3}

empty = set()     # correct way to create an empty set
print(empty)
not_a_set = {}    # this creates a dictionary!


#Set Methods

s = {1, 2, 3}
s.add(4)          # Adds 4
print(s)

s.remove(2)       # Removes 2 (error if not present)
print(s)


s.discard(5)      # Removes 5 if present (no error)
print(s)

s.clear()         # Removes everything
print(s)

#Set functions
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))        # {1, 2, 3, 4, 5}
print(a.intersection(b)) # {3}
print(a.difference(b))   # {1, 2}
print(b.difference(a))   # {4, 5}
print(a.symmetric_difference(b))  # {1, 2, 4, 5}

s ={1,2,3,4}
len(s)        # number of elements
print(len(s))
min(s)        # smallest
max(s)        # largest
sum(s)        # sum of all


for item in {"apple", "banana", "cherry"}:
    print(item)
    
    
a = {1, 2, 2, 3, 3, 3}
print(a)
