import datetime
import random

# Menu dictionary: item number → [name, price]
menu = {
    1: ["🍟 Chips", 10],
    2: ["🥤 Soda", 25],
    3: ["🍫 Chocolate Bar", 15],
    4: ["💧 Water Bottle", 12.20],
    5: ["🍪 Cookies", 13.07],
    6: ["🧃 Juice Box", 12.50]
}

print("✨=== Welcome to the Arat Kilo Vending Machine ===✨")
print("📋 Here's our menu:")
for number, (item, price) in menu.items():
    print(f"{number}. {item:<15} - ${price:.2f}")

# Cart to store selected items
selected_items = {}

while True:
    choice = input("\nEnter the item number to add to your cart (or type 'edit' to modify cart, 'done' to finish): ").strip().lower()

    if choice == "done":
        if not selected_items:
            print("⚠️Your cart is empty. Please add at least one item before finishing.")
            continue
        break

    if choice == "edit":
        if not selected_items:
            print("⚠️Your cart is empty. Nothing to edit.")
            continue

        print("\nYour current cart:")
        for number, qty in selected_items.items():
            print(f"{number}. {menu[number][0]} x {qty}")

        edit_choice = input("Enter the item number you want to edit: ").strip()
        if not edit_choice.isdigit() or int(edit_choice) not in selected_items:
            print("❌Invalid choice. Try again.")
            continue

        edit_choice = int(edit_choice)
        action = input("Type 'update' to change quantity or 'remove' to delete item: ").strip().lower()

        if action == "update":
            new_qty = input(f"Enter new quantity for {menu[edit_choice][0]}: ").strip()
            if new_qty.isdigit() and int(new_qty) > 0:
                selected_items[edit_choice] = int(new_qty)
                print(f"Updated {menu[edit_choice][0]} to {new_qty}.")
            else:
                print("❌Invalid quantity.")
        elif action == "remove":
            del selected_items[edit_choice]
            print(f"Removed {menu[edit_choice][0]} from your cart.")
        else:
            print("❌Invalid action. Please type 'update' or 'remove'.")
        continue

    if not choice.isdigit():
        print("❌Invalid input! Please enter a number from the menu.")
        continue

    choice = int(choice)
    if choice not in menu:
        print("⚠️That item number is not on the menu. Try again.")
        continue

    # Ask for quantity until valid
    while True:
        quantity = input(f"How many {menu[choice][0]} would you like? ").strip()
        if not quantity.isdigit():
            print("❌Invalid quantity! Please enter a number.")
            continue
        quantity = int(quantity)
        if quantity == 0:
            print("⚠️Quantity must be at least 1.")
            continue
        break

    # Add to cart
    if choice in selected_items:
        selected_items[choice] += quantity
    else:
        selected_items[choice] = quantity

    print(f"🛒Added {quantity} x {menu[choice][0]} to your cart.")

# Generate receipt details
now = datetime.datetime.now()
date_time = now.strftime("%Y-%m-%d %H:%M:%S")

# Random 5-digit transaction number
transaction_number = random.randint(10000, 99999)

# Print receipt
print("\n🧾 ===== Receipt ===== 🧾")
print("abcd PLC")
print("Vending Machine 001  Location: Arat Killo Plaza")
print(f"Date & Time: {date_time}")
print(f"Transaction #: {transaction_number}")
print("-------------------------------------------------")
print(f"{'Item':<15}{'Qty':<10}{'Price':<10}{'Line Total'}")
print("-------------------------------------------------")

total = 0
for number, quantity in selected_items.items():
    item, price = menu[number]
    line_total = price * quantity
    print(f"{item:<15}{quantity:<10}${price:<9.2f}${line_total:.2f}")
    total += line_total

print("-------------------------------------------------")
print(f"{'TOTAL':<15}{'':<10}{'':<10}${total:.2f}")
print("=================================================")
# Payment simulation
while True:
    try:
        payment = float(input(f"Please insert payment (Total: ${total:.2f}): "))
        if payment < total:
            print(f"⚠️Insufficient payment! You still owe ${total - payment:.2f}.")
        else:
            change = payment - total
            print(f"✅Payment accepted! Your change is ${change:.2f}")
            break
    except ValueError:
        print("❌Invalid input! Please enter a valid amount.")
print("🎉🎉Thank you for shopping at Arart kilo Vending Machine!🎉🎉")

