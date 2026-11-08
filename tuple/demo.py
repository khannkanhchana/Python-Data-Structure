# A tuple is used to store multiple items in a single variable.
# Tuples are ordered, immutable (unchangeable), and allow duplicate values.

# 1. CREATE A TUPLE
# Create a tuple named fruits containing 3 fruit names.
# Print the entire tuple.

fruits = ("apple", "banana", "cherry","cherry")
print(fruits)

# 2. CREATE A TUPLE WITH ONE ITEM
# Create a tuple containing only "apple".
# Print the tuple and its data type.
# Remember: A single-item tuple requires a comma, without comma it is just a string.

# fruits= ("apple",)
print(type(fruits)) 

# 3. ACCESS TUPLE ITEMS
# Print the first item in the tuple.
# Print the last item in the tuple using [-1].
# Remember: Python indexing starts from 0.

print(fruits[0])  # First item

# 4. TRY TO MODIFY A TUPLE ITEM
# Try to change "banana" to "grape".
# Print the tuple.
# Observe what happens when you try to modify a tuple.

# fruits[1] = "grape"  # This will raise an error because tuples are immutable
# print(fruits)

# 5. CONVERT A TUPLE TO A LIST
# Convert the fruits tuple into a list.
# Add one new fruit to the list.
# Convert the list back into a tuple.
# Print the final tuple.

print(type(fruits))
new_list = list(fruits)

new_list[1] = "grape"
print(new_list)
print(tuple(new_list))


# 6. ADD ITEMS TO A TUPLE
# Tuples do not have append() or insert() methods.
# Use the + operator to create a new tuple with one additional fruit.
# Print the new tuple.

new_fruits = fruits + ("orange",)
print(new_fruits)

# 7. FIND THE LENGTH OF A TUPLE
# Use len() to count how many items are in the tuple.
# Print the result.



# 8. LOOP THROUGH A TUPLE
# Use a for loop to print each fruit on a separate line.

for i in fruits:
    print(i)

# 9. COUNT DUPLICATED ITEMS
# Create a tuple containing duplicate fruit names.
# Use count() to count how many times "apple" appears.
# Print the result.

count_cherry = fruits.count("cherry")
print(count_cherry)


# 10. FIND THE INDEX OF AN ITEM
# Use index() to find the position of "orange" in the tuple.
# Print the result.

index_banana = fruits.index("banana")
print(index_banana)

# 11. RETURN MULTIPLE VALUES FROM A FUNCTION
# When a function returns multiple comma-separated values,
# Python automatically packs them into a tuple.

def get_student():
    return "Dara", 20, "IT"

result = get_student()

print(result)
print(type(result))
print(f"Name: {result[0]}, Age: {result[1]}, Major: {result[2]}")
# print(type(result))