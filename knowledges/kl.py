# List

myList=['mouse','lion','tiger','cat','dog']

# Access a list item
print(myList[1]) # lion
print(myList[-1]) # dog

# Slicing
myList=[1,2,3,4,5,6,7,8,9,10]
print(myList[1:3]) # Subtract one from the last index
print(myList[:]) # Return all the items that has the list
print(myList[::3]) # Returns the set of numbers going 3 by 3 [1,4,7,10]
print(myList[::-1]) # Return the list going one at a time but in reverse order [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


# Go through the list
for i in myList:
  print(i) # Return all the elements of the list in order

# Find an element in a list using an if 
if 'lion' in myList:
  print('Lion is on the list')
else:
  print('Lion is not on the list')

# MOST IMPORTANT METHODS
list=['apple','banana','cherry','orange','kiwi','melon','mango']

# -Adds an item to the list in the last position
list.append('grape') # ['apple','banana','cherry','orange','kiwi','melon','mango','grape']

# -Adds an item to the list at a given position
list.insert(2, 'pineapple') # ['apple','banana','pineapple','cherry','orange','kiwi','melon','mango','grape']

# -Deletes the last item from the list and prints out which item was removed.
popIt=list.pop() 
print(popIt) # grape

# -Removes the given item
list.remove('melon') 
print(list) # The list without 'melon'

# -Clean the list, empty list
# list.clear()
# print(list)

# -Reverses the list
list.reverse()
print(list)

# -Sort the list
numList=[3,6,12,7,4,8,9,23]
numList.sort()
print(numList)

numList2=[1,41,6,42,5,8,-2,-5]
newListSorted=sorted(numList2)
print(newListSorted)

# We can multiply the number of elements we want the list to have
multList=[0]*5
print(multList)

multList2=['word']*4
print(multList2)

multList3=['word1','word2','word3']*3
print(multList3)

# -Concat list
cList1=[1,2,3,4,5]
cList2=[6,7,8,9,10,'supu']

newConcatList=cList1+cList2
print(newConcatList)

# Copy a list to work with it and dont affect the original list
original_list=[2,4,6,8,10]
copy_list=original_list.copy()

copy_list.append(12)

print(original_list)
print(copy_list)

# Trick to get the squares of the numbers of a list
numbers=[1,2,3,4,5,6,7,8,9,10]
squareList=[i*i for i in numbers] # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print(squareList)








