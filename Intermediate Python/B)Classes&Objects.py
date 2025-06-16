#A class is a blueprint for creating objects.
#Class = recipe
#Object = cake made from that recipe

#Every time you use a class to make something, you’re creating an object, also called an instance.

#A class groups:
#Attributes (data) → like name, price
#Methods (functions that operate on that data)

class Car:
    pass  # blueprint, not a real car


class book:
    def __init__(self , name , price): #This is the constructor. It runs automatically when you create a new object.
        self.name = name # When you write self.name = name, you're saying:
#> “Take the value from the argument name, and store it in this object’s own name field.”
        self.price = price#Attributes are the data stored in an object.
             
b1 = book("White Nights" , 249)
print(b1.name , b1.price)
   
b2 = book("A Little Life" , 399) 
print(b2.name , b2.price)

#Methods
# Instance methods, class methods, static methods

class dog:
    def bark( self):
        print("woof!")
        
d1 = dog()
d1.bark()


class Bill:
    total_bills =0 
    
    def __init__(self, title):
        self.title=title
        Bill.total_bills += 1
    
    @classmethod    
    def get_total(cls):
        return cls.total_bills

b22 = Bill("Parle")
b33 = Bill("Nutrella")
print(b33.total_bills)


# class variables
class Cat:
    species = "Feline"  # class variable

    def __init__(self, name):
        self.name = name  # instance variable

c1 = Cat("Whiskers")
c2 = Cat("Luna")

print(c1.species)  # Feline
print(c2.name)     # Luna
print(c2.species)



#Inheritance

class publication:
    def __init__( self , publisher , isbn):
        self.publisher = publisher
        self.isbn = isbn 


class newspaper(publication):
    def __init__(self , name , date , price , publisher , isbn ):
        super().__init__(publisher , isbn)
        self.name= name
        self.date= date
        self.price= price
        
n1 = newspaper("The Times" , "21/07/25" , 2.99 , "penguin" , 2345643 )
print(n1.name , n1.date , n1.price , n1.publisher , n1.isbn )


class Math:
    @staticmethod
    def square(x):
        return x * x
        
print(Math.square(5))


#Dunder Methods (Magic Methods)
"""
__str__	What shows when you print the object
__len__	Enables len(obj)
__eq__	Enables obj1 == obj2
__add__	Enables obj1 + obj2
"""

class Book2:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book2: {self.name}"

b = Book2("1984")
print(b)  # ➜ Book: 1984


#Polymorphism

class Dog:
    def speak(self):
        print("Woof")

class Cat:
    def speak(self):
        print("Meow")

def animal_sound(animal):
    animal.speak()

animal_sound(Dog())
animal_sound(Cat())


#object composition

class Engine:
    def start(self):
        print("Engine on")

class Car:
    def __init__(self):
        self.engine = Engine()

    def drive(self):
        self.engine.start()
        print("Driving...")
        
        
 #encapsulation
class Product:
    def __init__(self, price):
        self.__price = price

    def get_price(self):
        return self.__price

    def set_price(self, value):
        if value > 0:
            self.__price = value
            
            
p = Product(67)
print(p.get_price())
p.set_price(78)
#print(p.__price) not possible
print(p._Product__price) # possible , bad practice
print(p.get_price())

#abstract methods
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self): #must be in sub - classesfrom abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

d = Dog()
c = Cat()

d.make_sound()  # Woof!
c.make_sound()  # Meow!
        pass

class Dog(Animal):
    def make_sound(self):
        print("Wooooof!")

class Cat(Animal):
    def make_sound(self):
        print("Meeeooow!")

d = Dog()
c = Cat()

d.make_sound()  # Woof!
c.make_sound()  # Meow!