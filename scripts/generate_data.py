from extract import (
    generate_products,
    generate_warehouses,
    generate_customers,
    generate_sales,
    generate_inventory
)

from transform import calculate_sales_amounts

from load import (
    get_connection,
    load_products,
    load_warehouses,
    load_customers,
    get_product_prices,
    load_sales,
    load_inventory
)


conn = get_connection()
cur = conn.cursor()

products = generate_products()
warehouses = generate_warehouses()
customers = generate_customers()
sales = generate_sales()
inventory = generate_inventory()

load_products(cur, products)
load_warehouses(cur, warehouses)
load_customers(cur, customers)

conn.commit()

product_prices = get_product_prices(cur)
sales = calculate_sales_amounts(sales, product_prices)

load_sales(cur, sales)
load_inventory(cur, inventory)

conn.commit()

cur.close()
conn.close()

print("ETL pipeline completed successfully.")