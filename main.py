products = [
    {"name": "leather", "unit_price": 1100, "gst_percentage": 18, "quantity": 1, "eligible_for_discount": True},
    {"name": "umbrella", "unit_price": 900, "gst_percentage": 12, "quantity": 4, "eligible_for_discount": True},
    {"name": "cigarette", "unit_price": 200, "gst_percentage": 28, "quantity": 3, "eligible_for_discount": False},
    {"name": "honey", "unit_price": 100, "gst_percentage": 0, "quantity": 2, "eligible_for_discount": False},
]

total_amount = 0

for product in products:
    unit_price = product["unit_price"]
    gst_percentage = product["gst_percentage"]
    quantity = product["quantity"]
    eligible_for_discount = product["eligible_for_discount"]
    total_product_amount = unit_price * (1 + gst_percentage / 100) * quantity
    if eligible_for_discount and unit_price >= 500:
        total_product_amount *= 0.95

    total_amount += total_product_amount

print(f"Total amount to be paid: Rs {total_amount:.2f}")


