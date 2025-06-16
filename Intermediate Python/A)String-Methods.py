text = "  Hello, Python World!  "

# .strip() – removes leading/trailing whitespace
print(text.strip())  # "Hello, Python World!"

# .lower() / .upper()
print(text.lower())  # "  hello, python world!  "
print(text.upper())  # "  HELLO, PYTHON WORLD!  "

# .replace(old, new)
print(text.replace("Python", "Coding"))  # "  Hello, Coding World!  "

# .split(separator)
print(text.split())  # ['Hello,', 'Python', 'World!'] — splits by space

# .join(iterable)
words = ["Learn", "Python", "Fast"]
print(" ".join(words))  # "Learn Python Fast"

# .find(substring)
print(text.find("Python"))  # 9 — returns index

# .startswith() / .endswith()
print(text.strip().startswith("Hello"))  # True
print(text.strip().endswith("World!"))   # True

# .count(substring)
print(text.count("o"))  # 3

# .isalpha(), .isdigit(), .isalnum()
print("abc123".isalnum())  # True
print("123".isdigit())     # True
print("abc".isalpha())     # True

s = "hello world"

# .capitalize() – first letter uppercase
print(s.capitalize())  # "Hello world"

# .title() – capitalize each word
print(s.title())  # "Hello World"

# .swapcase() – flip case
print(s.swapcase())  # "HELLO WORLD" if s was lowercase

# .center(width, char) – center string with padding
print(s.center(20, "-"))  # "---hello world----"

# .zfill(width) – pad numbers with zeros
num = "42"
print(num.zfill(5))  # "00042"

# .rjust() / .ljust()
print(s.rjust(15))  # right-aligned
print(s.ljust(15, "."))  # left-aligned with dots

# .startswith() / .endswith() again
print(s.startswith("he"))  # True
print(s.endswith("ld"))    # True

#String Formatting Techniques (must-know)

name = "Alicia"
age = 30
print(f"My name is {name} and I’m {age} years old.")

print("My name is {} and I’m {} years old.".format(name, age))

print("My name is %s and I’m %d years old." % (name, age))

"""
Escape Characters 

\n	New line
\t	Tab
\\	Backslash
\"	Double quote
\'	Single quote
"""

print("Hello\nWorld")  # Newline

#String Slicing & Indexing

text = "Python"
print(text[0])     # P
print(text[-1])    # n
print(text[1:4])   # yth
print(text[::-1])  # reversed string → "nohtyP"


for char in text:
    print(char)