menu = {
    "Breakfast": {
        "Idli": {"half": 30.00, "full": 50.00},
        "Dosa": {"half": 40.00, "full": 70.00},
        "Omelette": {"half": 15.00, "full": 25.00},
    },
    "Lunch": {
        "Veg Thali": {"half": 70.00, "full": 120.00},
        "Chicken Biryani": {"half": 100.00, "full": 180.00},
        "Shahi Paneer": {"half": 80.00, "full": 150.00},
    },
    "Dinner": {
        "Chicken Curry": {"half": 50.00, "full": 90.00},
        "Fish Curry": {"half": 120.00, "full": 220.00},
        "Dal Tadka": {"half": 40.00, "full": 70.00},
    },
    "Snacks": {
        "Samosa": {"half": 25.00, "full": 40.00},
        "Chaat": {"half": 30.00, "full": 50.0},
        "Pakora": {"half": 20.00, "full": 30.00},
    },
    "Dessert": {
        "Gulab Jamun": {"half": 25.00, "full": 40.00},
        "Ice Cream": {"half": 40.00, "full": 70.00},
        "Kheer": {"half": 50.00, "full": 90.00},
    },
    "Drinks": {
        "Tea": {"half": 15.00, "full": 25.00},
        "Coffee": {"half": 20.00, "full": 30.00},
        "Fresh Juice": {"half": 40.00, "full": 70.00},
        "Water Bottle": {"half": 15.00, "full": 20.00},
    }
}

def display_menu():
    print("\n=====RESTAURANT MENU=====")
    for category,item in menu.items():
        print(f"\n--{category}--")
        for item,price in item.items():
            print(f"{item:<20} | Half:₹{price["half"]:<5} | Full:₹{price["full"]:<5}")
