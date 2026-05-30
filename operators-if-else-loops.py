# Problem 1: Write a program that will give you in hand monthly salary after deduction on CTC - HRA(10%), DA(5%), PF(3%) and taxes deduction as below:
# Salary(Lakhs) : Tax(%)

# Below 5 : 0%
# 5-10 : 10%
# 10-20 : 20%
# aboove 20 : 30%


salary_lakhs = float(input("Enter your annual salary (in Lakhs): "))

salary = salary_lakhs * 100000

# Deductions
hra = salary * 0.10
da  = salary * 0.05
pf  = salary * 0.03

# Tax calculation
if salary_lakhs < 5:
    tax = 0
    tax_rate = "0%"
elif salary_lakhs < 10:
    tax = salary * 0.10
    tax_rate = "10%"
elif salary_lakhs < 20:
    tax = salary * 0.20
    tax_rate = "20%"
else:
    tax = salary * 0.30
    tax_rate = "30%"

total_deduction = hra + da + pf + tax
in_hand_annual  = salary - total_deduction
monthly_salary  = in_hand_annual / 12

# Output
print(f"\n{'='*40}")
print(f"  Gross Annual CTC      : ₹{salary:>12,.2f}")
print(f"{'='*40}")
print(f"  HRA (10%)             : ₹{hra:>12,.2f}")
print(f"  DA  (5%)              : ₹{da:>12,.2f}")
print(f"  PF  (3%)              : ₹{pf:>12,.2f}")
print(f"  Tax ({tax_rate:<3})            : ₹{tax:>12,.2f}")
print(f"  Total Deductions      : ₹{total_deduction:>12,.2f}")
print(f"{'='*40}")
print(f"  In-hand Annual Salary : ₹{in_hand_annual:>12,.2f}")
print(f"  In-hand Monthly Salary: ₹{monthly_salary:>12,.2f}")
print(f"{'='*40}\n")


# Problem 2: Write a program that take a user input of three angles and will find out whether it can form a triangle or not.


a = int(input("enter 1st angle of the trinangle: "))
b = int(input("enter 2nd angle of the triangle: "))
c = int(input("enter 3rd angle of the triangle: "))

sum = a+b+c
if sum == 180 :
    print(" it can form a triangle")
else :
    print("canot form the triangle")



# Problem 3: Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit.

cost = int(input("enter the cost price "))
sell = int(input("enter the selling price "))

diff = sell - cost
if diff<1 :
    print ("you are in lose")
else :
    print("you are in profit")
    

# Problem 4: Write a menu-driven program -
# 1. cm to ft
# 2.km to miles
# 3.USD to INR
# 4.exit

print("choose action to perform")
print("1.cm to ft" )
print("2. km to miles" )
print("3. USD to INR" )
print("4.exit")
choice = int(input("enter your choice: "))
if choice==1:
  cm = int(input("enter cm to convert"))
  feet = cm/30.48
  print(cm,"cm in feet =",feet)

elif choice == 2:
  km = int(input("enter km to convert"))
  miles = km*0.621371
  print(km,"in miles =",miles)
elif choice == 3:
  USD = int(input("enter USD to convert in INR"))
  INR = USD*94.99
  print(USD,"in INR =",INR)
elif choice == 4:
  exit()

else:
  print("wrong input")



# Problem 5 - Exercise 12: Display Fibonacci series up to 10 terms.
# Note: The Fibonacci Sequence is a series of numbers. The next number is found by adding up the two numbers before it. The first two numbers are 0 and 1. For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. The next number in this series above is 13+21 = 34

num1, num2 = 0,1

for i in range(10):
  print(num1)

  next = num1 + num2

  num1 = num2
  num2 = next 

  # Problem 6 - Find the factorial of a given number.
# Write a program to use the loop to find the factorial of a given number.

# The factorial (symbol: !) means to multiply all whole numbers from the chosen number down to 1.

# For example: calculate the factorial of 5

# 5! = 5 × 4 × 3 × 2 × 1 = 120
# Output:

# 120

num = int(input("enter number"))
fact = 1
for i in range (1,num+1):
  fact = fact*i
  

print(fact)


# Problem 7 - Reverse a given integer number.
# Example:

# Input:

# 76542
# Output:

# 24567

num = int(input("enter number"))
rev = 0

while num>0:
  last = num%10
  rev = rev*10 + last
  num = num//10
  
print(rev)


