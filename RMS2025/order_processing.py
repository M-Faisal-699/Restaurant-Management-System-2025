from menu import menudata
import json

def take_order():
    order=[]
    while(True):
         category_input=input("Enter category name(or type done to finish):").title()
         if category_input.lower()=="done":
            break
         if category_input not in menudata:
            print("Invalid category")
            continue
         
         print(f"\nAvailable items in {category_input}:")
         for item in menudata[category_input]:
            print(f"{item}")
        
         item_name=input("\nEnter item name:").title()
         if item_name not in menudata[category_input]:
             print("Invalid Try again.")
             continue
         
         qty_type=input("Half or 'Full?:").lower()
         if qty_type not in ["half","full"]:
             print("Please enter 'half' or 'full'.")
             continue
         
         qty=int(input("Quantity:"))
         
         price = menudata[category_input][item_name][qty_type]
         order.append((item,qty_type,qty,price))
         print(f"Added:{qty}x{item} {qty_type.title()}")
         print(f"Price: ₹{price} each")
    return order

with open("order.json", "w") as file:
    order_data = take_order()
    file.write(json.dumps(order_data, indent=4))   



