# Problem 1: Combine two lists index-wise(columns wise)
# Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.

# Given List:

# list1 = ["M", "na", "i", "Kh"]
# list2 = ["y", "me", "s", "an"]
# Output:

# [['M','y'], ['na', me'], ['i', 's'], ['Kh', 'an']]


list1 = ["M", "na", "i", "Kh"]
list2 = ["y", "me", "s", "an"]

result = [[a, b] for a, b in zip(list1, list2)]

if len(list1) > len(list2):
    result.extend(list1[len(list2):])
else:
    result.extend(list2[len(list1):])

print(result)



# Problem 2: Add new item to list after a specified item
# Write a program to add item 7000 after 6000 in the following Python List

# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# Output:

# [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)    


# Problem 3: Update no of items available
# Suppose you are given a list of candy and another list of same size representing no of items of respective candy.

# i.e -

# candy_list = ['Jelly Belly','Kit Kat','Double Bubble','Milky Way','Three Musketeers']
# no_of_items = [10,20,34,74,32]
# Write a program to show no. of items of each candy type.

# Output:

# Jelly Belly-10
# Kit Kat-20
# Double Bubble-34
# Milky Way-74
# Three Musketeers-32


candy_list = ['Jelly Belly','Kit Kat','Double Bubble','Milky Way','Three Musketeers']

no_of_items = [10,20,34,74,32]

for (i,j) in zip(candy_list , no_of_items):
  print(i,"-",j)


# Problem 4: Running Sum on list
# Write a program to print a list after performing running sum on it.

# i.e:

# Input:

# list1 = [1,2,3,4,5,6]
# Output:

# [1,3,6,10,15,21]

list1 = [1,2,3,4,5,6]
sum = 0
result = []
for i in list1:
  sum = sum +  i
  result.append(sum)

print(result)


# Problem 5: You are given a list of integers. You are asked to make a list by running through elements of the list by adding all elements greater and itself.
# i.e. Say given list is [2,4,6,10,1] resultant list will be [22,20,10,23].

# For 1st element 2 ->> these are greater (4+6+10) values and 2 itself so on adding becomes 22.

# For 2nd element 4 ->> greater elements are (6, 10) and 4 itself, so on adding 20

# like wise for all other elememts.

# [2,4,6,10,1]-->[22,20,16,10,23]

lst = [2,4,6,10,1]
result = []

for i in lst:
  sum=0
  for j in lst:
    if i<=j:
      sum = sum+j
      
  result.append(sum)
  

print(result)


# Problem 6: Find list of common unique items from two list. and show in increasing order
# Input

# num1 = [23,45,67,78,89,34]
# num2 = [34,89,55,56,39,67]
# Output:

# [34, 67, 89]


num1 = [23,45,67,78,89,34]
num2 = [34,89,55,56,39,67]

common = []

for i in num1:
  if i in num2:
    if i not in common:
      common.append(i)

print(sorted(common))


# Problem 7: Sort a list of alphanumeric strings based on product value of numeric character in it. If in any string there is no numeric character take it's product value as 1.
# Input:

# ['1ac21', '23fg', '456', '098d','1','kls']
# Output:

# ['456', '23fg', '1ac21', '1', 'kls', '098d']






# Problem 8: Split String of list on K character.

# Example :

# Input:

# ['CampusX is a channel', 'for data-science', 'aspirants.']
# Output:

# ['CampusX', 'is', 'a', 'channel', 'for', 'data-science', 'aspirants.']

L = ['CampusX is a channel', 'for data-science', 'aspirants.']
inp = ' '

result = []

for i in L:
  result.extend(i.split(inp))

print(result)