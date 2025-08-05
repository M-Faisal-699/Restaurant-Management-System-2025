from order_processing import order




def generate_bill(order):
    print("\n--- BILL ---")
    total = 0
    for item, qty_type, qty, price in order:
        item_total = qty * price
        print(f"{item} {qty_type}X{qty}=₹{item_total}")
        total += item_total

    gst_rate = 5 / 100
    discount_rate = 10 / 100
    gst = total * gst_rate

    apply_discount = input("Apply 10% discount? (y/n)").lower()
    if apply_discount == "y":
        discount = total * discount_rate
    else:
        discount = 0

    final_total = total + gst - discount
    print(f"\nSubtotal:{total}")
    print(f"GST (5%): ₹{gst}")
    print(f"Total to pay: ₹{final_total}")
    return final_total





