def calculate_sales_amounts(sales, product_prices):
    transformed_sales = []

    for sale in sales:
        unit_price = product_prices[sale["product_id"]]
        total_amount = sale["quantity"] * float(unit_price)

        sale["total_amount"] = total_amount
        transformed_sales.append(sale)

    return transformed_sales