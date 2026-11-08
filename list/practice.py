# ============================
# PRACTICE SHEET: List
# ============================
# Task 1: Create a shopping list containing at least 5 items. Include "milk" twice.


# Task 2: Print the second item, the last item, and the total
#    number of items in the list.


# Task 3: Add "eggs" to the end of the list.
#    What happens to the indexes when "bread" is inserted?
#    Insert "bread" as the second item.


# Task 4: Remove "milk" from the list once.
#    Print the updated list.


# Task 5: Check whether "milk" still exists in the list.
#    Will "milk" still exist after removing it once?
#    Does removing an item change the list's length?
#    Print the number of items remaining.


# Task 6: Use a loop to print each item on a separate line.
#    Print the total number of items after the loop.


# Task 8: Remove the last item from the list.
#    Print the removed item and the updated list.


# Task 9: Sort the final list alphabetically.
#    Keep a separate copy of the unsorted list unchanged.



shopping_list = ["apples", "milk", "bananas", "milk", "butter", "cheese"]
print("--- Task 1: Initial Shopping List ---")
print(shopping_list)
print()

print("--- Task 2: List Info ---")
print("Second item:", shopping_list[1])
print("Last item:", shopping_list[-1])
print("Total number of items:", len(shopping_list))
print()

shopping_list.append("eggs")
print("--- Task 3: Inserting Items ---")
print("After adding 'eggs':", shopping_list)

print("What happens to indexes? Inserting 'bread' shifts all elements after it one index to the right.")

shopping_list.insert(1, "bread")
print("After inserting 'bread' as second item:", shopping_list)
print()

print("--- Task 4: Remove 'milk' Once ---")
shopping_list.remove("milk")
print("Updated list:", shopping_list)
print()

print("--- Task 5: Check Existence & Length ---")
print("Does 'milk' still exist in the list?", "milk" in shopping_list)
print("Will 'milk' still exist after removing it once? Yes, because 'milk' was included twice initially.")
print("Does removing an item change the list's length? Yes, it reduces the length by 1.")
print("Number of items remaining:", len(shopping_list))
print()

print("--- Task 6: Loop Through Items ---")
for item in shopping_list:
    print(f"- {item}")
print("Total number of items after loop:", len(shopping_list))
print()

print("--- Task 8: Remove Last Item ---")
removed_item = shopping_list.pop()
print("Removed item:", removed_item)
print("Updated list:", shopping_list)
print()

print("--- Task 9: Sort Alphabetically & Copy ---")
unsorted_copy = shopping_list.copy()
sorted_list = sorted(shopping_list)

print("Unsorted copy (unchanged):", unsorted_copy)
print("Sorted final list:", sorted_list)