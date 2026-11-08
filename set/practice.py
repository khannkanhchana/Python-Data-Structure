# ============================
# PRACTICE SHEET: SET
# ============================

# Scenario: A backup tool compares the files in a folder from yesterday
# and today to find out what changed.
#
#   yesterday = {"a.txt", "b.txt", "c.txt"}
#   today     = {"b.txt", "c.txt", "d.txt"}


# TASK 1: SETUP
# Create the two sets, yesterday and today, with the files above.


# TASK 2: NEW AND DELETED FILES
# Find the files that exist today but did not exist yesterday.
# Then find the files that existed yesterday but are gone today.
# Print both results.


# TASK 3: UNCHANGED FILES
# Find the files that exist on both days.
# Print them.


# TASK 4: ALL CHANGES
# Find every file that was either added or deleted.


# TASK 5: ALL FILES EVER SEEN
# Build one set containing every file that appeared on either day.
# Print it.


yesterday = {"a.txt", "b.txt", "c.txt"}
today = {"b.txt", "c.txt", "d.txt"}

print("--- TASK 1: SETUP ---")
print("Yesterday's files:", yesterday)
print("Today's files:", today)
print()


new_files = today - yesterday
deleted_files = yesterday - today

print("--- TASK 2: NEW AND DELETED FILES ---")
print("New files added today:", new_files)
print("Files deleted since yesterday:", deleted_files)
print()


unchanged_files = yesterday & today

print("--- TASK 3: UNCHANGED FILES ---")
print("Unchanged files (on both days):", unchanged_files)
print()


changed_files = yesterday ^ today

print("--- TASK 4: ALL CHANGES ---")
print("Files added or deleted (changed files):", changed_files)
print()


all_files = yesterday | today

print("--- TASK 5: ALL FILES EVER SEEN ---")
print("All files seen across both days:", all_files)