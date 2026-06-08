# Problem-1: Write a Python function that takes a list and returns a new list with unique elements of the first list.
# Exercise 1:

# Input:

# [1,2,3,3,3,3,4,5]
# Output:

# [1, 2, 3, 4, 5]

def uniqueElement (L):

  newL = []
  for  i in L:
    if i not in newL:
      newL.append(i)

  return newL

L=[1,2,3,3,3,3,4,5]
print(uniqueElement(L))
    


# Problem-2: Write a Python function that accepts a hyphen-separated sequence of words as parameter and returns the words in a hyphen-separated sequence after sorting them alphabetically.
# Example 1:

# Input:

# green-red-yellow-black-white
# Output:

# black-green-red-white-yellow

def sortArray (ss):
  temp =[]

  for i in sorted(ss.split('-')):
    temp.append(i)

  return "-".join(temp)


s = "green-red-yellow-black-white"

print(sortArray(s))



# Problem 3: Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
# Sample String : 'CampusX is an Online Mentorship Program fOr EnginEering students.'
# Expected Output :
# No. of Upper case characters :  9
# No. of Lower case Characters :  47

def char_Case_Counter (str):
  ucount = 0
  lcount = 0
  
  for i in str:
    if i.isupper() :
      ucount += 1
    elif i.islower():
      lcount += 1

  print("No. of Upper case characters : ",ucount)
  print("No. of lower case characters : ",lcount)


s = 'CampusX is an Online Mentorship Program fOr EnginEering students.'
char_Case_Counter(s)



# Problem 5: Write a Python function to check whether a number is perfect or not.
# A Perfect number is a number that is half the sum of all of its positive divisors (including itself).

# Example :

# The first perfect number is 6, because 1, 2, and 3 are its proper positive divisors, and 1 + 2 + 3 = 6. 
# Equivalently, the number 6 is equal to half the sum of all its positive divisors: ( 1 + 2 + 3 + 6 ) / 2 = 6. 

# The next perfect number is 28 = 1 + 2 + 4 + 7 + 14. This is followed by the perfect numbers 496 and 8128.


def is_Perfect(num):
  divisor =[]
  for i in range (1,num):
    if num % i ==0 :
      divisor.append(i)

  total = sum(divisor)
  grand_total = total + num
 
  if total == num and grand_total // 2 == num:
    print("it is a perfect number")

  else :
    print("it is not a perfect number")
  


is_Perfect(8128)





# Problem-7 Write a python function that accepts a string as input and returns the word with most occurence.

# Input:
# hello how are you i am fine thank you
# Output
# you -> 2


def most_used(s):
  d ={}

  for i in s.split():
    if i in d:
      d[i] = d[i] + 1
    else :
      d[i] = 1

  max_val = max(d.values())

  for i in d :
    if d[i] == max_val:
      print(i,'-->',d[i])
      break
    



most_used('hello how are you i am fine thank you ')