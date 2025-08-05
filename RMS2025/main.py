from auth import user_authentication
from menu import display_menu
from order import take_order
from gen_billing import generate_bill

print("\n===== RESTAURANT MANAGEMENT SYSTEM =====")
print("1. User Authentication")
print("2. Show Menu")
print("3. Take Order")
print("4. Generate Bill")
print("5. Book Table")
print("6. Exit")

while(True):
    choice=int(input("Enter your choice:"))

    if choice==1:
        user_authentication()
                   
    elif choice==2:
        display_menu()

    elif choice==3:
        take_order()
    elif choice==4:
        generate_bill(order)
    # elif choice==5:
    elif choice==6:
        break
    