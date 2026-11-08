
# ============================
# PRACTICE SHEET: DICTIONARY
# ============================

# 1. Create a dictionary called inventory with 3 products and their stock numbers.
# 2. Use get() to check the stock of a product that may not exist.
# 3. Use update() to add 2 new products and change one stock number.
# 4. Use items() to print every product and its stock.
# 5. Use pop() to remove a product that is sold out.
# 6. Use setdefault() to add a new product only if it is not already there.
# 7. Use values() and sum() to print the total number of items in stock.
# 8. Use copy() to save a backup, then clear() the original.

inventory = {
    "laptop": 15,
    "mouse": 50,
    "keyboard": 30
}
print("--- 1. Initial Inventory ---")
print(inventory)
print()

print("--- 2. Check Stock with get() ---")
monitor_stock = inventory.get("monitor", 0)  
print("Stock for 'monitor':", monitor_stock)
print()

print("--- 3. Update Inventory ---")
inventory.update({
    "headset": 20,  
    "webcam": 12,  
    "mouse": 45     
})
print("Updated inventory:", inventory)
print()

print("--- 4. Iterate using items() ---")
for product, stock in inventory.items():
    print(f"- {product}: {stock} units")
print()

print("--- 5. Remove Product with pop() ---")
removed_stock = inventory.pop("headset")
print(f"Removed 'headset' (had {removed_stock} units)")
print("Inventory after pop:", inventory)
print()

print("--- 6. Add Product with setdefault() ---")
inventory.setdefault("speaker", 25)
inventory.setdefault("laptop", 100)
print("Inventory after setdefault:", inventory)
print()

print("--- 7. Total Stock using values() & sum() ---")
total_stock = sum(inventory.values())
print("Total number of items in stock:", total_stock)
print()

print("--- 8. Backup and Clear ---")
inventory_backup = inventory.copy()
inventory.clear()

print("Original inventory after clear():", inventory)
print("Backup inventory:", inventory_backup)