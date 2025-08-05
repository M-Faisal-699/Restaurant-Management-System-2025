from menu import display_menu




def take_order():
    order=[]
    while(True):
         category_input=input("\nEnter category name(or type done to finish):").title()
         if category_input.lower()=="done":
            break
         if category_input not in menu:
            print("Invalid category")
            continue
         
         print(f"\nAvailable items in {category_input}:")
         for item in menu[category_input]:
            print(f"{item}")
        
         item_name=input("\nEnter item name:").title()
         if item_name not in menu[category_input]:
             print("Invalid Try again.")
             continue
         
         qty_type=input("Half or 'Full?:").lower()
         if qty_type not in ["half","full"]:
             print("Please enter 'half' or 'full'.")
             continue
         
         qty=int(input("Quantity:"))
         
         price = menu[category_input][item_name][qty_type]
         order.append((item,qty_type,qty,price))
         print(f"Added:{qty}x{item} {qty_type.title()}")
         print(f"Price: ₹{price} each")
    return order
