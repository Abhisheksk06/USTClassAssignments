items = ['Bread', 'Cookies', 'Butter', 'Cheese', 'Yoghurt']
prices = [40, 80, 120, 180, 60]

cart = []

while True:
    print("What do you want to do?")
    print("1 - View items")
    print("2 - Add items to cart")
    print("3 - Update items in cart")
    print("4 - Remove items from cart")
    print("5 - Print bill")
    print("6 - Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        for i in range(len(items)):
            print(f"Name: {items[i]} - Price: {prices[i]}")
    
    elif choice == 2:
        # Add items to the cart
        item_name = input("Enter the item name: ")
        if item_name in items:
            index = items.index(item_name)  # Find the index of the item in the list
            quantity = int(input("Enter the quantity: "))
            cart.append([item_name, quantity, prices[index], prices[index] * quantity])
    
    elif choice == 3:
        # Update quantity of items in cart
        item_name = input("Enter the item to update: ")
        
        # Check if the item is in the cart
        item_found = False
        for item in cart:
            if item[0] == item_name:
                item_found = True
                new_quantity = int(input("Enter the new quantity: "))
                item[1] = new_quantity  # Update the quantity
                item[3] = new_quantity * item[2]  # Update the total cost based on the new quantity
                print(f"{item_name} quantity updated.")
                break
        
        if not item_found:
            print(f"{item_name} not found in the cart.")
    
    elif choice == 4:
        # Remove item from cart
        item_name = input("Which item to remove: ")
        
        item_found = False
        for item in cart:
            if item[0] == item_name:
                cart.remove(item)  # Remove the item from the cart
                item_found = True
                print(f"{item_name} removed from the cart.")
                break
        
        if not item_found:
            print(f"{item_name} not found in the cart.")
    
    elif choice == 5:
        # Print the bill
        print("Item, Quantity, Price, Total")
        total = 0
        for item in cart:
            print(f"{item[0]}, {item[1]}, {item[2]}, {item[3]}")
            total += item[3]  # Add total cost
        print(f"Total amount: {total}")
    
    elif choice == 6:
        break
    
    else:
        print("Invalid choice! Please try again.")
