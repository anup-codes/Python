'''
Q-1: Rectangle Class
Write a Rectangle class in Python language, allowing you to build a rectangle with length and width attributes.

Create a Perimeter() method to calculate the perimeter of the rectangle and a Area() method to calculate the area of ​​the rectangle.

Create a method display() that display the length, width, perimeter and area of an object created using an instantiation on rectangle class.

Eg. After making above classes and methods, on executing below code:-

my_rectangle = Rectangle(3 , 4)
my_rectangle.display()
Output:

The length of rectangle is:  3
The width of rectangle is:  4
The perimeter of rectangle is:  14
The area of rectangle is:  12 
'''



class Rectangle :
  def __init__(self,x,y):
    self.length = x
    self.width = y
    self.display()

  def display(self):
    print("The length of rectangle is:",self.length)
    print("The width of rectangle is: ", self.width)
    print("The perimeter of rectangle is: ", self.parameter())
    print("The area of rectangle is: ", self.area())
   

  def parameter(self):
    parameter = 2*(self.length + self.width)
    return parameter
  
  def area (self):
    area = self.length*self.width
    return area
  

rec = Rectangle(4,5)
rec.display





'''
Q-2: Bank Class
Create a Python class called BankAccount which represents a bank account, having as attributes: accountNumber (numeric type), name (name of the account owner as string type), balance.
Create a constructor with parameters: accountNumber, name, balance.
Create a Deposit() method which manages the deposit actions.
Create a Withdrawal() method which manages withdrawals actions.
Create an bankFees() method to apply the bank fees with a percentage of 5% of the balance account.
Create a display() method to display account details. Give the complete code for the BankAccount class.

Eg. After making above classes and methods, on executing below code:-

newAccount = BankAccount(2178514584, "Mandy" , 2800)

newAccount.Withdrawal(700)

newAccount.Deposit(1000)

newAccount.display()
Output:

Account Number :  2178514584
Account Name :  Mandy
Account Balance :  3100 ₹
'''

class BankAccount:

  def __init__(self,acc_no,name,balance):
    self.Acc_number = acc_no
    self.__name = name
    self.__balance = balance
  

  def display(self):
    print("Account Number : ", self.Acc_number)
    print("Account Name:", self.__name)
    print("Account Balance:", self.__balance)

  def deposit (self,amount):
    self.__balance = self.__balance + amount
    

  def Withdrawal(self,amount):
    if amount <= self.__balance:
      self.__balance = self.__balance - amount
    else :
      print("Aukart Ma Samja")


newAccount = BankAccount(2178514584, "Mandy" , 2800)

newAccount.Withdrawal(700)

newAccount.deposit(1000)

newAccount.display()




'''
Q-3:Computation class
Create a Computation class with a default constructor (without parameters) allowing to perform various calculations on integers numbers.

Create a method called Factorial() which allows to calculate the factorial of an integer n. Integer n as parameter for this method

Create a method called naturalSum() allowing to calculate the sum of the first n integers 1 + 2 + 3 + .. + n. Integer n as parameter for this method.

Create a method called testPrime() in the Calculation class to test the primality of a given integer n, n is Prime or Not? Integer n as parameter for this method.

Create a method called testPrims() allowing to test if two numbers are prime between them. Two integers are prime to one another if they have only 1 as their common divisor. Eg. 4 and 9 are prime to each other.

Create a tableMult() method which creates and displays the multiplication table of a given integer. Then create an allTablesMult() method to display all the integer multiplication tables 1, 2, 3, ..., 9.

Create a static listDiv() method that gets all the divisors of a given integer on new list called Ldiv. Create another listDivPrim() method that gets all the prime divisors of a given integer.
'''


class  Computation :

  def __init__(self):
    print("here we go ")

  def Factorial(self, n):
    fact = 1
    for i in range(1,n+1):
      fact = fact*i
    print(fact)


  def naturalSum(self,n):
    sum = 0 
    for i in range(1,n+1):
      sum = sum + i
    print(sum)


  def TestPrime(self,x):
    flag = 0
    for i in range (2,x//2):
      if x % i == 0:
        flag+=1
      
    if flag ==0:
      print("prime no ")
    else :
      print("not prime")

  def testPrims(self,x,y):
    flag = 0
    for i in range (2,min(x, y) + 1):
      if x % i == 0 and y%i==0:
        flag+=1
      
    if flag ==0:
      print("prime to each other. ")
    else :
      print("not prime to each other.")




  # def tableMult(self,x):


  # def allTablesMult(self):



  # def listDiv(self,x):


  # def listDivPrim(self,x):



com = Computation()
com.Factorial(5)
com.naturalSum(5)
com.TestPrime(8)
com.testPrims(4,9)



'''
Q-4: Build flashcard using class in Python.
Build a flashcard using class in python. A flashcard is a card having information on both sides, which can be used as an aid in memoization. Flashcards usually have a question on one side and an answer on the other.

Example 1:

Approach:

Create a class named FlashCard.
Initialize dictionary fruits using init() method. Here you have to define fruit name as key and it's color as value. E.g., {"Banana": "yellow", "Strawberries": "pink"}
Now randomly choose a pair from fruits by using random module and store the key in variable fruit and value in variable color.
Now prompt the user to answer the color of the randomly chosen fruit.
If correct print correct else print wrong.
Output:

welcome to fruit quiz
What is the color of Strawberries
pink
Correct answer
Enter 0, if you want to play again: 0
What is the color of watermelon
green
Correct answer
Enter 0, if you want to play again: 1
'''

import random

class FlashCard :

  def __init__(self):
    self.__fruits = {
      'apple' : 'red',
      'banana' : 'yellow',
      'watermelon' : 'green',
      'strawberry' : 'pink',
      'guava': 'green'
      }
    
  def quiz(self):

    while True:
      fruit,color = random.choices(list(self.__fruits.items()))[0]
      
      print('what are the color of {}'.format(fruit))
      user_answer = input()

      if user_answer.lower() == color:
        print('correct')
      else :
        print("try again better ")


      option = int(input('enter 0 to play again and 1 to exit'))
      if option == 1:
        break


fc = FlashCard()
fc.quiz()



'''
Q-5: Problem 5 based on OOP Python.
TechWorld, a technology training center, wants to allocate courses for instructors. An instructor is identified by name, technology skills, experience and average feedback. An instructor is allocated a course, if he/she satisfies the below two conditions:

eligibility criteria:
if experience is more than 3 years, average feedback should be 4.5 or more
if experience is 3 years or less, average feedback should be 4 or more
he/she should posses the technology skill for the course
Identify the class name and attributes to represent instructors. Write a Python program to implement the class chosen with its attributes and methods.

Note:

Consider all instance variables to be private and methods to be public.
An instructor may have multiple technology skills, so consider instance variable, technology_skill to be a list.
check_eligibility(): Return true if eligibility criteria is satisfied by the instructor. Else, return false
allocate_course(technology): Return true if the course which requires the given technology can be allocated to the instructor. Else, return false.
Represent a few objects of the class, initialize instance variables using setter methods, invoke appropriate methods and test your program.
'''

class Instructor :

  def __init__(self,name, technology,experience, feedback):
    self.__name = name
    self.__technology = technology
    self.__experience = experience
    self.__feedback = feedback

  def check_eligibility(self):

    if self.__experience > 3 and self.__feedback >=4.5:
      return True
    elif self.__experience  <= 3 and self.__feedback >=4:
      return True
    else:
      return False
    
  def allocate_course(self,tech):
    is_eligible = self.check_eligibility()

    if is_eligible:
      if tech in self.__technology:
        return 'padha sakta hai'
      else:
        return 'ye to usko aata he nhi hai '
      
    else:
      return 'aacha nhi padhata hai '
    

ins = Instructor('anup',['data science','web devlopment'],5,4.5)
print(ins.allocate_course('data '))
