import subprocess
subprocess.run("cls", shell=True)

# -----------------------------------------------------
# 1. get(): Accessing a value safely
# Returns the value associated with a specified key.
# If the key does not exist, it returns None (or a default value).
# Unlike dictionary[key], it does not raise a KeyError when the key is missing
# -----------------------------------------------------
# Scenario: Your app receives user data from a server.
# Some fields may be missing, and the program must not crash.

# Create a dictionary called user_response with the keys:
# "id" = 101, "username" = "dara_it", "country" = "Cambodia"

# user_response = {
#     "id" : 101,
#     "username" : "dara_it",
#     "country": "cambodia"
# }


# Print the username using get().

# print(user_response.get("country"))

# Try to read the key "phone" using get().
# If it is missing, print "Phone not provided".
# print(user_response.get("phone"))
# print(user_response.get("phone", "Phone not provided"))

# Get value by accessing the key directly. if the key does not exist, it will raise a KeyError.
# if user_response["phone"] in user_response:
#     print(user_response["phone"])
# else:
#     print("Phone not provided")


# -----------------------------------------------------
# 2. keys(): Getting all dictionary keys
# Returns a view containing all keys in the dictionary.
# Useful for checking whether a specific key exists.
# -----------------------------------------------------
# Scenario: Before saving a registration form, check that the
# required fields exist.

# Create a dictionary called form_data with: "name", "email", "password".

user_info = {
    "name": "dara",
    "email": "dara@gmail.com",
    "password": "1232143"
}


# Print all keys using keys().

# print(user_info.keys())


# Create a list called required_fields = ["name", "email", "password", "phone"].
# Loop through required_fields and print "Missing: <field>"
# for every field that is NOT in form_data.keys().

# required_keys = ["name", "email", "password", "phone"]

# for i in required_keys:
#     if i in user_info.keys():
#         print(i)
#     else:
#         print(f"Missing: {i}")

# -----------------------------------------------------
# 3. values(): Getting all dictionary values
# Returns a view containing all values in the dictionary.
# Useful for calculations such as sum(), max(), and min().
# -----------------------------------------------------
# Scenario: A shop keeps the sales of each day in a dictionary.

# Create a dictionary called daily_sales:
# "Mon" = 120, "Tue" = 95, "Wed" = 150, "Thu" = 80, "Fri" = 200

daily_sales = {
    "Mon": 120, 
    "Tue": 95, 
    "Wed": 150, 
    "Thu": 80, 
    "Fri": 200
}

# Print all values using values().

# print(daily_sales.values())

# # Use sum() on the values to print the total sales of the week.

# print(f"Total sales of the week: {sum(daily_sales.values())}")

# Use max() on the values to print the best day's sales.

# print(f"Best day's sales: {max(daily_sales.values())}")

# -----------------------------------------------------
# 4. items(): Getting key-value pairs
# Returns a view containing all key-value pairs as tuples.
# Useful for looping through both keys and values at the same time.
# -----------------------------------------------------
# Scenario: Print a price list for a cafe menu.

# Create a dictionary called menu:
# "Coffee" = 2.50, "Tea" = 1.75, "Juice" = 3.00

menu = {
    "Coffee": 2.50, 
    "Tea": 1.75, 
    "Juice": 3.00
}

# Print all key-value pairs using items().

# print(menu.items())
# print(type(menu.items()))

# Loop through items() and print each line in this format:
# Coffee costs $2.50

# for key, value in menu.items():
#     print(f"{key} costs {value} ")

# Bonus: inside the loop, print only the items that cost more than $2.

# print("*"*30)

# for key, value in menu.items():
#     if(value > 2):
#         print(f"{key} costs {value} ")


# -----------------------------------------------------
# 5. update(): Adding or updating dictionary items
# Adds new key-value pairs or updates existing keys.
# If a key already exists, its value will be replaced.
# -----------------------------------------------------
# Scenario: A user edits their profile settings in an app.

# Create a dictionary called profile:
# "username" = "sokha", "theme" = "light", "language" = "en"

# profile = {
#    "username": "sokha",
#     "theme": "light",
#     "language": "en"
# }

# Create a second dictionary called changes:
# "theme" = "dark", "notifications" = True

# change = {
#     "theme": "dark",
#     "notifications": True
# }

# Use update() to merge changes into profile.

# profile.update(change)

# Print profile. Which key was changed? Which key was added?

# print(profile)

# -----------------------------------------------------
# 6. pop(): Removing an item by key
# Removes the specified key and returns its value.
# If the key does not exist, it raises a KeyError unless a default value is provided.
# -----------------------------------------------------
# Scenario: Before sending user data to the frontend, remove
# the password but keep a copy of it for checking.

# Create a dictionary called account:
# "username" = "dara", "password" = "12345", "role" = "admin"

account = {
    "username": "dara",
    "password" : "12345",
    "role" : "admin"
}

# Use pop() to remove "password" and store it in a variable called removed_password.

# removed_password = account.pop("password")

# Print removed_password and the updated account.

# print('removed_password: ',removed_password)


# Try pop("email") on the same dictionary.
# What happens? Then fix it by giving pop() a default value of None.

# account.pop("email", None)

# -----------------------------------------------------
# 7. copy(): Creating a dictionary copy
# Creates a shallow copy of the dictionary.
# Changes to the original dictionary do not affect the copied dictionary's top-level values.
# -----------------------------------------------------
# Scenario: Save the original settings before the user edits them, so you can reset them later.

# Create a dictionary called settings:
# "volume" = 50, "brightness" = 70

settings = {
    "volume" : 50,
    "brightness" : 70
}
# print("Original Setting: ", settings)
# # Create a backup using copy().

# backup = settings.copy()
# print("backup Setting: ", backup)

# Change settings["volume"] to 90.

settings["volume"] = 90

# Print both dictionaries. Does the backup change too?

# print("Original Setting: ", settings)
# print("backup Setting: ", backup)

# Then write one line to reset settings back to the backup values.

# settings = backup.copy()

# why settings = backup is not correct in this sense, you just point both variable to same dictionary, not make it to separate dicts. which could lead to reset when the user change the value. 

# -----------------------------------------------------
# 8. clear(): Removing all dictionary items
# Removes all key-value pairs from the dictionary.
# The dictionary becomes empty but still exists.
# -----------------------------------------------------
# Scenario: After a customer checks out, their shopping cart must be emptied.

# Create a dictionary called cart:
# "Notebook" = 2, "Pen" = 5, "Ruler" = 1

cart = {
    "Notebook" : 2, 
    "Pen" : 5, 
    "Ruler" : 1
}

# Print the cart.

print(cart)

# Use clear() to empty it, then print the cart again.

# cart.clear()
# print(cart)

# -----------------------------------------------------
# 9. popitem(): Removing the last inserted item
# Removes and returns the last inserted key-value pair as a tuple.
# Raises a KeyError if the dictionary is empty.
# -----------------------------------------------------
# Scenario: A simple "undo" feature that removes the most
# recently added item from an order.

# Create an empty dictionary called order.

order = {}

# Add three items one by one: "Burger" = 3.50, "Fries" = 1.50, "Cola" = 1.00

order.update({
    "Burger" : 3.50, 
    "Fries" : 1.50, 
    "Cola" : 1.00
})

# print(order)
# # Use popitem() to remove the last item and store it in removed_item.

# removed_item = order.popitem()

# # Print removed_item and the remaining order.

# print(f"remove item: ",removed_item)
# print(type(removed_item))
# print(order)

# Think: what type of value does popitem() return?
#tuple

# -----------------------------------------------------
# 10. setdefault(): Getting or creating a default value
# Returns the value of the specified key if it exists.
# If the key does not exist, it creates the key with the given default value.
# Useful for initializing dictionary values without overwriting existing ones.
# -----------------------------------------------------
# Scenario A: Give a new user default settings without
# overwriting values they already chose.

# Create a dictionary called user_settings with only "theme" = "dark".

user_settings = {
    "theme": "dark"
}

# Use setdefault() to make sure "language" exists with the value "en".

user_settings.setdefault("language", "en")
print(user_settings)

# Use setdefault() again on "theme" with the value "light".
# Print the result. Did the theme change?

user_settings.setdefault("theme", "light")

print(user_settings)


# -----------------------------------------------------
# 11. fromkeys(): Creating a dictionary from keys
# Creates a new dictionary using the given keys.
# All keys are assigned the same initial value.
# If no value is specified, the default value is None.
# -----------------------------------------------------
# Scenario A: Start a quiz game where every player begins with 0 points.

# Create a list called players = ["Dara", "Sokha", "Vanna"].

players = ["Dara", "Sokha", "Vanna"]

# Use fromkeys() to create a dictionary called scores where every player has 0.

scores = dict.fromkeys(players,0)
print(scores)

# Update one player's score and print scores.

scores.update({
    "Sokha": 5
})

print(scores)