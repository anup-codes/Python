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
    

 