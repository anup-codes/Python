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