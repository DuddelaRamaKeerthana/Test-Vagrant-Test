products = [
    {'product_name': 'leather', 'unit_price': 1100, 'gst_percentage': 18, 'quantity': 1, 'discount_eligible': True},
    {'product_name': 'umbrella', 'unit_price': 900, 'gst_percentage': 12, 'quantity': 4, 'discount_eligible': True},
    {'product_name': 'cigarette', 'unit_price': 200, 'gst_percentage': 28, 'quantity': 3, 'discount_eligible': False},
    {'product_name': 'honey', 'unit_price': 100, 'gst_percentage': 0, 'quantity': 2, 'discount_eligible': False},
]
for product in products:
    product['total_amount'] = product['unit_price'] * product['quantity']
    product['discount_amount'] = 0
    if product['discount_eligible'] and product['unit_price'] >= 500:
        product['discount_amount'] = 0.05 * product['total_amount']

    product['gst_amount'] = (product['total_amount'] - product['discount_amount']) * (product['gst_percentage'] / 100)
max_gst_product = max(products, key=lambda x: x['gst_amount'])
print(f"The product with the maximum GST amount is {max_gst_product['product_name']} with GST amount: {max_gst_product['gst_amount']} rupees.")

