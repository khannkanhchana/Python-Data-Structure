# A list is used to store multiple items in a single variable.
# Lists are ordered, mutable (changeable), and allow duplicate values.


# 1. CREATE A LIST
# Create a list named fruits containing 3 fruit names.
# Print the entire list.

fruits = ["apple", "banana", "cherry"]
print(fruits)

# 2. ACCESS LIST ITEMS
# Print the first item in the list.
# Print the last item in the list. [-1]
# Remember: Python indexing starts from 0.

print(fruits[1])  # First item

# 3. MODIFY A LIST ITEM
# Change "banana" to "mango".
# Print the updated list.

fruits[1] = "mango"
print(fruits)

# 4. ADD ITEMS TO A LIST
# .append() adds an item to the end of the list.
# .insert() adds an item at a specific index in the list.

# Use append() to add one new fruit.
# Use insert() to add a fruit at index 1.
# Print the list after each operation.

fruits.append("orange")
fruits.insert(1, "kiwi")
print(fruits)

# 5. REMOVE ITEMS FROM A LIST
# Use remove() to delete an item by value.

# Use pop() to remove an item by index.
# Use del my_list[index] remove an item by index

# Note: With pop() you can store and use the remove item but with del you can't.
# Print the list after each operation.

fruits.append("Durian")
fruits.append("Durian")
print(fruits)
# fruits.remove("Durian")
# print(fruits)


# Question 01: How does the remove method work on list with duplicated element?
fruits.remove("Durian")
print(fruits)


# Question 02: How to remove duplicated element?

for i in fruits:
    if i == "Durian":
        fruits.remove(i)
print(fruits)

# 6. FIND THE LENGTH OF A LIST
# Use len() to count how many items are in the list.

fruist_length = len(fruits)
print(fruist_length)

# 7. LOOP THROUGH A LIST
# Use a for loop to print each fruit on a separate line.
for fruit in fruits:
    print(fruit)

# 8. CHECK IF AN ITEM EXISTS
# Use keyword "in" to check the existence of the item in list
# Check whether "mango" exists in the list.
# Print the result.

print("Durain" in fruits)


# 9. SORT A LIST
# Use .sort() to sort items in ascending order. To sort in descending order use .sort(reverse=True)
# Use sorted(list) to sort items in ascending order and return the list. To sort in descending order use sorted(list, reverse=True)
# Create a list of numbers.
# Sort the numbers in ascending order.
# Print the sorted list.

numbers = [5, 2, 9, 1, 5, 6]
numbers.sort(reverse=True)
print(numbers)