# Problem 1 - Print the following pattern. Write a program to use for loop to print the following reverse number pattern.
# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1

n = 5
for i in range(0,n):
  for j in range(n-i,0,-1):
    print(j,end=" ")
  print()


# Problem 2: Print the following pattern.
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

n = 8
for i in range(0,n+1):
  for j in range(0,i):
    print("*",end=" ")
  print()

for i in range(0,n):
  for j in range(n-i-1,0,-1):
   print("*",end=" ")
  print()

  # Problem 3:Write a program to pring the following pattern
#     *
#   * * *
# * * * * *
n= 4

for i in range (1,n+1):
 print(" "*n,end="")
 print("* "*i)
 n = n-1


 # Problem 4:Write a program to print the following pattern
# 1

# 2 1

# 3 2 1

# 4 3 2 1

# 5 4 3 2 1

n = 5
for i in range (1,n+1):
  for j in range(i,0,-1):
    print(j,end='')
  print()


# Problem 7 - Find the sum of the series upto n terms.
# Write a program to calculate the sum of series up to n term. For example, if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690. Take the user input and then calculate. And the output style should match which is given in the example.

# Example 1:

# Input:

# 5
# Output:

# 2+22+222+2222+22222
# Sum of above series is: 24690

n = 5 
start=2
sum=0
for i in range (0,n):
  if i<n-1 :
   print(start,end="+")
  else:
    print(start,end="=")

  sum = sum+start
  start = start*10+2

print(sum)


# Problem 8: Write a program to print all the unique combinations of 1,2,3 and 4
# Output:

# 1 2 3 4
# 1 2 4 3
# 1 3 2 4
# 1 3 4 2
# 1 4 2 3
# 1 4 3 2
# 2 1 3 4
# 2 1 4 3
# 2 3 1 4
# 2 3 4 1
# 2 4 1 3
# .
# .
# and so on

for i in range(1,5):
  for j in range (1,5):
    for k in range (1,5):
      for m in range(1,5):
        print(i,j,k,m)








# Problem 9: Write a program that will take a decimal number as input and prints out the binary equivalent of the numbera

n=10

r =""

while n>0:
   a= n%2 
   r = str(a) + r
   n = n//2
   

print(r)


# Problem 10: Write a program that will take 2 numbers as input and prints the LCM and HCF of those 2 numbers

a = 16
b = 28

if a>b:
  c=a
else:
  c=b

i=c
while True:
  if a%i ==0 and b%i ==0:
    hcf=i 
    print(hcf )
    break
  i-=1

lcm = (a*b)//hcf
print(lcm)




# Problem 11: Create Short Form from initial character
# Given a string create short form ofthe string from Initial character. Short form should be capitalised.

# Example:

# Input:

# Data science mentorship program
# Output:

# DSMP

str = "Data science mentorship program"

res = '' 

n=len(str)

for i in  str.split():
  print(i[0].upper(),end="")



# Problem 12: Append second string in the middle of first string
# Input:

# campusx
# data
# Output:

# camdatapusx

fst = "campusx"
snd = "data"

add =""

print(fst[0:len(fst)//2] + snd + fst[len(fst)//2::])



# Problem 13:Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.
# Given:

# str1 = PyNaTive

# Expected Output:

# yaivePNT

str1 = "PyNaTive"

lower = ""
up=""
for i in str1:
  if i>="a" and i<="z":
   lower = lower + i
  
 

  else:
    up = up+i


print(lower + up)



# Problem 14:Take a alphanumeric string input and print the sum and average of the digits that appear in the string, ignoring all other characters.
# Input:

# hel123O4every093

# Output:

# Sum: 22
# Avg: 2.75

str1 = "hel123O4every093"

sum = 0
count=0

for i in str1:
  if i.isdigit() :
    sum = sum+int(i)
    count += 1

print(sum)
print(sum/count)



# Problem 16: Check whether the string is Symmetrical.
# Statement: Given a string. the task is to check if the string is symmetrical or not. A string is said to be symmetrical if both the halves of the string are the same.

# Example 1:

# Input

# khokho
# Output

# The entered string is symmetrical

s = "madma"

if len(s)%2 ==0 :
  for i in s:
    s1 = s[0:len(s)//2]
    s2 = s[len(s)//2::]

else:
   s1 = s[0:len(s)//2]
   s2 = s[len(s)//2+1::]
  
if s1 == s2:
  print("this is symmetrical")
else:
  print("not stmmetrical")



# Problem 17: Reverse words in a given String
# Statement: We are given a string and we need to reverse words of a given string.

# Example 1:

# Input:

# geeks quiz practice code
# Output:

# code practice quiz geeks
# Example 2:

# Input:

# my name is laxmi
# Output:

# laxmi is name my

s = "my name is Anup"

rev = " "

for i in  s.split():
  rev = i +" " +rev

print(rev)
 