
# ============================
# PRACTICE SHEET: TUPLE
# ============================

# Task 1: STUDENT REGISTRATION
# A university stores student information:
# ("Dara", 20, "Computer Science", "Year 3")

# 1. Create a tuple named student.
# 2. Print the student's name and major.
# 3. Print the total number of items.
# 4. Print the student's year using negative indexing.



# Task 2: COURSE ENROLLMENT
# A student enrolls in the following courses:
# ("Python", "Database", "Networking", "Python", "Web Development")

# 1. Create a tuple named courses.
# 2. Count how many times "Python" appears.
# 3. Find the index position of "Networking".
# 4. Use a for loop to print each course separately.



# Task 3: UPDATING STUDENT COURSES
# A student initially registers for:
# ("Python", "Database", "Networking")

# 1. Create a tuple named registered_courses.
# 2. Convert the tuple into a list.
# 3. Add "Cloud Computing" to the list.
# 4. Convert the list back into a tuple.
# 5. Print the updated course registration.

student = ("Dara", 20, "Computer Science", "Year 3")
print("--- Task 1: Student Registration ---")

print("Student Name:", student[0])
print("Major:", student[2])

print("Total number of items:", len(student))

print("Student Year (negative indexing):", student[-1])
print()


courses = ("Python", "Database", "Networking", "Python", "Web Development")
print("--- Task 2: Course Enrollment ---")

print("'Python' appears:", courses.count("Python"), "times")

print("Index position of 'Networking':", courses.index("Networking"))

print("Courses list:")
for course in courses:
    print(f"- {course}")
print()


registered_courses = ("Python", "Database", "Networking")
print("--- Task 3: Updating Student Courses ---")
print("Initial tuple:", registered_courses)

courses_list = list(registered_courses)

courses_list.append("Cloud Computing")

registered_courses = tuple(courses_list)

print("Updated registered_courses tuple:", registered_courses)