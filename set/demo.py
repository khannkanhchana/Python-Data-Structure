import subprocess
subprocess.run("cls", shell=True)

# =============================================================================
# PART 1: CREATING SETS      my_set = {1, 3, 5}      my_set = set([1, 3, 5])
# =============================================================================

# A blog has a fixed list of allowed post categories.
# TASK: Create a set called categories with "tech", "food", "travel".

categories = {"tech", "food", "travel"}
print(categories)

# categories = set(["tech", "food", "travel"])
# print(categories)

# TASK: Create an empty set called empty_set and print it.

# empty_set = set()
# print(empty_set)


# =============================================================================
# PART 2: ADDING ELEMENTS      my_set.add(7)      my_set.update([7, 8])
# =============================================================================

# A shopping cart stores unique product IDs.
# TASK: cart = {"P1", "P2"}. The customer adds "P3". Print the cart.

# cart = {"P1", "P2"}
# cart.add("P3")
# print(cart)

# The customer clicks "add" on "P2" again by mistake.
# TASK: Add "P2" to the cart again and print it. What happens to the
#       duplicate?

# cart.add("P2")
# print(cart)

# The customer adds several products at once.
# TASK: Add "P4", "P5" and "P2" to the cart in one go and print it.

# cart.update(["P4", "P5", "P2"])
# print(cart)

# cart |= {"P6"}
# print(cart)


# =============================================================================
# PART 3: REMOVING ELEMENTS      my_set.remove(3)      my_set.discard(3)
# =============================================================================

# A customer removes an item from their cart.
# TASK: cart = {"P1", "P2", "P3"}. Remove "P2" and print the cart.

# cart = {"P1", "P2", "P3"}
# cart.remove("P2")
# print("After removed P2: ", cart)

# The customer removes "P2" again, but it is already gone.
# TASK: Remove "P2" without getting an error, then remove "P3" and print the cart.

# cart.discard("P2")
# cart.discard("P3")
# print("After discard: ", cart)


# =============================================================================
# PART 4: SET OPERATIONS
# =============================================================================

# python_students = {"Ann", "Ben", "Cara", "Dev"}
# sql_students    = {"Cara", "Dev", "Eli", "Fay"}

# UNION   a | b   a.union(b)
# Send a newsletter to everyone enrolled in EITHER course, without anyone
# receiving it twice.
# TASK: Build the recipient set and print it.

# recipients = python_students | sql_students
# print(recipients)

# recipients = python_students.union(sql_students)
# print(recipients)


# INTERSECTION   a & b   a.intersection(b)
# Give a "full stack" certificate to students taking BOTH courses.
# TASK: Find who is eligible and print it.

# eligible = python_students & sql_students
# print(eligible)

# eligible = python_students.intersection(sql_students)
# print(eligible)


# DIFFERENCE   a - b   a.difference(b)
# Offer a SQL discount to Python students who have NOT joined the SQL course yet.
# TASK: Find them and print the result.

# discount = python_students - sql_students
# print(discount)

# discount = python_students.difference(sql_students)
# print(discount)

# Who is in SQL but not in Python? (swap the sides: b - a)

# bonus = sql_students - python_students
# print(bonus)

# bonus = sql_students.difference(python_students)
# print(bonus)


# SYMMETRIC DIFFERENCE   a ^ b   a.symmetric_difference(b)
# Returns the items that are in a or in b, but NOT in both.
# It is the union without the overlap. Returns a new set.
# Invite students who are in EXACTLY ONE course (not both) to a
# "try the other course" workshop.
# TASK: Find them and print the result.

# one_course_only = python_students ^ sql_students
# print(one_course_only)

# one_course_only = python_students.symmetric_difference(sql_students)
# print(one_course_only)

# one_course_only = (python_students - sql_students) | (sql_students - python_students)
# print(one_course_only)


# SYMMETRIC DIFFERENCE UPDATE   a ^= b   a.symmetric_difference_update(b)
# Same as symmetric difference, but it changes set a itself instead of returning a new set. Returns None.
# TASK: Make a copy of python_students called workshop_list, update it so it
#       holds the students in exactly one course, then print it.

# workshop_list = python_students.copy()
# workshop_list ^= sql_students
# print(workshop_list)

# workshop_list = python_students.copy()
# workshop_list.symmetric_difference_update(sql_students)
# print(workshop_list)

# print(python_students)