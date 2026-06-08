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