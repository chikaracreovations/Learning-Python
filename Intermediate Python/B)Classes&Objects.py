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

# methods

class dog:
    def bark( self):
        print("woof!")
        
d1 = dog()
d1.bark()


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


    