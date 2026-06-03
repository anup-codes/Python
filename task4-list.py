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

