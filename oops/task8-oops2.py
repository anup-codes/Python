'''
Q1:Count number of instances of a class created in Python?
Example: Say Car is any class.

maruti = Car()
bmw = Car()
honda = Car()
So after creating above instances. We want to count how many instances are created of Car class.

For above example no of instances = 3.

Write a program for above problem.
'''

class Car() :

  __count = 0

  def __init__(self):
    Car.__count +=1

  def __str__(self):
     return ' no of instances = {}'.format(self.__count)

  def get_counter():
    return 'no of instances',Car.__count 
  
maruti = Car()
print(maruti)
bmw = Car()
print(bmw)

honda = Car()
print(honda)


print(Car.get_counter())



'''
Q-2: Create a deck of cards class. Internally, the deck of cards should use another class, a card class. Your requirements are:
The Deck class should have a deal method to deal a single card from the deck
After a card is dealt, it is removed from the deck.
There should be a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
Deck Class

It is class of all possible cards in a deck. Total 52 cards.
Methods - deal() it will take out one card from the deck of cards.
Deck of cards should get shuffeled while creating the deck object.
no of cards remaining in deck - <number> should dsiplay on printing any deck object.
Card class

It is a class of card
Atrributes - suit and value
<suit> of <value> should dsiplay on printing any card object.

'''
import random
class Card :

  def __init__(self,suit,value):
    self.suit = suit
    self.value = value

  def __repr__(self):
    return "{}-->{}".format(self.suit,self.value)
  

class Deck :
  def __init__(self):
    suits = ['Heart', 'Diamonds', 'Clubs','Spades']
    values = ['A','2','3','4','5','6','7','8','9','10','J','K','Q']
    self.cards = [Card(suit,value) for suit in suits for value in values]
    
  def __str__(self):
    return "Cards left " + str(len(self.cards))

  def shuffle(self):
    if len(self.cards) <52:
      print('only full deck can be shuffled')
    else:
      random.shuffle(self.cards)
    return self.cards

  def deal(self):
    if len(self.cards) ==0:
      print('All cards have been deal')
    return self.cards.pop()


deck = Deck()
deck.shuffle()
print(deck.deal())
print(deck.deal())
print(deck.deal())
print(deck)


'''
Q-3: Find the area of a rectangle.
Approach:

The class name should be Rectangle.
The constructor should accept two parameters length and height but you can't pass the values directly to it while creating the constructor. E.g., rectangle = Rectangle(length=10, height=8) <-- you can't do that while creating the instances.
Create a method called area() which has no parameters.
Create a method called is_square() which also has no parameters. Return True if the rectangle is a square otherwise return False.
If you are using a if-else block inside the is_square() method, then use the one-linear syntax. 
'''


class Rectangle :

  def __init__(self,length,height):
    self.length = length
    self.height = height

  @classmethod
  def property(cls,len,bre):
    return cls(len,bre)

  def area(self):
    area = self.length * self.height
    return area

  def is_square(self):
    return True if self.length == self.height else False
  

r = Rectangle.property(4,4)
print (r.area())
print(r.is_square())




'''
Q-4: Problem 4
Statement: Write a program that uses datetime module within a class. Enter manufacturing date and expiry date of the product. The program must display the years, months and days that are left for expiry.
'''

import datetime

class Product:

  def __init__(self):
    self.manufacture_date = input("enter manufacturing date (MM/DD/YYYY)")
    self.expiry_date = input('enter expiry date (MM/DD/YYYY)')

    self.manufacture_date = datetime.datetime.strptime(self.manufacture_date, '%m/%d/%Y')
    self.expiry_date = datetime.datetime.strptime(self.expiry_date, '%m/%d/%Y')

  def time_to_expire(self):
    today = datetime.datetime.now()

    if today > self.expiry_date:
      print('product already expired')
    else:
      date_left = self.expiry_date.date() - today.date()
      print(str(date_left))

obj = Product()
print(obj.time_to_expire())




'''
Q-5: Problem 5
Statement: A university wants to automate their admission process. Students are admitted based on the marks scored in the qualifying exam. A student is identified by student id, age and marks in qualifying exam. Data are valid, if:

Age is greater than 20
Marks is between 0 and 100 (both inclusive)
A student qualifies for admission, if

Age and marks are valid and
Marks is 65 or more
Write a python program to represent the students seeking admission in the university. The details of student class are given below.
'''

class Student:

  def __init__(self):
    self.__sid = None
    self.__marks = None
    self.__age = None

  def set_sid(self,sid):
    self.__sid = sid
  def set_marks(self,marks):
    self.__marks = marks
  def set_age(self,age):
    self.__age = age
  
  def get_sid(self):
    return self.__sid
  def get_marks(self):
    return self.__marks
  def get_age(self):
    return self.__age
  

  def validate_age(self):
    return self.__age>20 
  
  def validate_marks(self):
    return self.__marks >=0 and self.__marks<=100

  def check_qualification(self):
    if self.validate_age() and self.validate_marks():
      return self.__marks>=65
    else :
      return False
    

stu1 = Student()
stu1.set_marks(65)
stu1.set_age(21)
stu1.set_sid(101)

print(stu1.check_qualification())



'''
Q-6: Ice-Cream Scoops and Bowl shop
Create a class Scoop which has one public property flavor and one private proptery price. Take flavor values during object creation.

Create a class Bowl with private prperty scoop_list which will have list of scoopd object.

Create a method add_scoops in Bowl class which will add any no of Scoop objects given as parameter and store it in scoops_list.

Make getter and setter method for price property.

Make a method display to display flavour and price of each Scoop in scoop_list and print total price of the bowl by adding all flavour scoops prices.

Make a method sold in both Scoop class and Bowl class to print no of quantity sold.

Ex.-

choco = Scoop('chocolate')
print(choco)
choco.set_price(100)

berry = Scoop('berry')
berry.set_price(120)
print(berry)

vanilla = Scoop('vanilla')
vanilla.set_price(150)

bowl = Bowl()

bowl.add_scoops(choco) # Giving one parameter
bowl.add_scoops(berry, vanilla) # Multiple
# add_scoops should handle both scenerios

print(bowl)

bowl.display()

Scoop.sold()
Bowl.sold()

Output

Flavor - chocolate Price - None
Flavor - berry Price - 120
chocolate
berry
vanilla
Dsiplaying Bowl
Flavor - chocolate Price - 100
Flavor - berry Price - 120
Flavor - vanilla Price - 150
Price of Bowl - 370
3 scoops sold
1 bowls sold

'''

class Scoop :

  __counter = 0


  def __init__(self,flavor):
    self.flavor = flavor
    self.__price = None
    Scoop.__counter +=1

  def set_price(self,price):
    self.__price = price

  def get__price(self):
    return self.__price
  
  def __str__(self):
    return "flavor - {} and price - {}".format(self.flavor,self.__price)
  
  @staticmethod
  def sold():
    return Scoop.__counter


class Bowl:

  __counter = 0

  def __init__(self):
    self.__scoop_list = []

  def add_scoops (self,*new_scoops):
    for sccop in new_scoops:
      self.__scoop_list.append(sccop)

  def display(self):
    total = 0
    for scoop in self.__scoop_list:
      print(scoop)
      total = total + scoop.get__price()

    print('total price',total)

  @staticmethod
  def sold():
    return Bowl.__counter


choco = Scoop('chocolate')
print(choco)
choco.set_price(100)

berry = Scoop('berry')
berry.set_price(120)
print(berry)

vanilla = Scoop('vanilla')
vanilla.set_price(150)

bowl = Bowl()

bowl.add_scoops(choco) # Giving one parameter
bowl.add_scoops(berry, vanilla) # Multiple
# add_scoops should handle both scenerios

print(bowl)

bowl.display()

Scoop.sold()
Bowl.sold()


