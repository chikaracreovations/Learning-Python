my_dict = {
    "name": "Ansh",
    "age": 25,
    "job": "Engineer"
}

print(my_dict["name"])     # Alice
print(my_dict.get("age"))  # 25
print(my_dict.get("city", "Not found"))  # Default value if key not found

my_dict["city"] = "New York"   # Add new key-value
my_dict["age"] = 26            # Update existing key
my_dict.pop("job")        # Removes 'job'
del my_dict["name"]       # Deletes 'name'
my_dict.clear()           # Clears entire dictionary


for key in my_dict:
    print(key, my_dict[key])

# OR

for key, value in my_dict.items():
    print(f"{key} = {value}")
    
    
student = {
    "name": "John",
    "marks": [85, 90, 78],
    "pass": True
}

print(student["marks"][1])     # 90

for k, v in student.items():
    print(f"{k}: {v}")
    
    
users = {
    "alice": {"age": 25, "city": "Paris"},
    "bob": {"age": 30, "city": "Berlin"}
}

print(users["alice"]["city"])  # Paris


# Python Dictionary Methods Reference

my_dict = {"a": 1, "b": 2, "c": 3}

# .get(key, default=None) → Returns the value for key if key is in the dictionary
value = my_dict.get("a")           # 1
missing = my_dict.get("x", "N/A")  # "N/A"

# .keys() → Returns a view of all keys
keys = my_dict.keys()  # dict_keys(['a', 'b', 'c'])

# .values() → Returns a view of all values
values = my_dict.values()  # dict_values([1, 2, 3])

# .items() → Returns a view of all (key, value) pairs
pairs = my_dict.items()  # dict_items([('a', 1), ('b', 2), ('c', 3)])

# .update(other_dict) → Updates the dictionary with elements from another dictionary
my_dict.update({"d": 4, "a": 10})  # Updates 'a' to 10, adds 'd'

# .pop(key, default) → Removes key and returns its value (or default if key not found)
value = my_dict.pop("b")  # Removes and returns 2

# .popitem() → Removes and returns the last inserted (key, value) pair (Python 3.7+)
last_pair = my_dict.popitem()

# .setdefault(key, default=None) → Returns the value of key. If not present, adds key with default value
v = my_dict.setdefault("e", 99)  # Adds 'e': 99 if not exists

# .clear() → Removes all items from the dictionary
my_dict.clear()  # Now it's {}

# len(dictionary) → Number of key-value pairs
length = len(my_dict)

# "key" in my_dict → Checks if key exists
exists = "a" in my_dict

# dict.fromkeys(keys, value) → Creates a new dict with given keys and same value
keys = ["x", "y", "z"]
new_dict = dict.fromkeys(keys, 0)  # {'x': 0, 'y': 0, 'z': 0}