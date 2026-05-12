import psycopg2


def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="retail_db",
        user="admin",
        password="admin",
        port="5432"
    )


def load_products(cur, products):
    for name, category, price in products:
        cur.execute(
            """
            INSERT INTO products (product_name, category, unit_price)
            VALUES (%s, %s, %s)
            """,
            (name, category, price)
        )


def load_warehouses(cur, warehouses):
    for name, city in warehouses:
        cur.execute(
            """
            INSERT INTO warehouses (warehouse_name, city)
            VALUES (%s, %s)
            """,
            (name, city)
        )


def load_customers(cur, customers):
    for name, city in customers:
        cur.execute(
            """
            INSERT INTO customers (customer_name, city)
            VALUES (%s, %s)
            """,
            (name, city)
        )


def get_product_prices(cur):
    cur.execute("SELECT product_id, unit_price FROM products")

    rows = cur.fetchall()

    return {
        product_id: unit_price
        for product_id, unit_price in rows
    }


def load_sales(cur, sales):
    for sale in sales:
        cur.execute(
            """
            INSERT INTO sales
            (product_id, customer_id, warehouse_id, quantity, sale_date, total_amount)
            VALUES (%s, %s, %s, %s, %s, %s)
            """,
            (
                sale["product_id"],
                sale["customer_id"],
                sale["warehouse_id"],
                sale["quantity"],
                sale["sale_date"],
                sale["total_amount"]
            )
        )


def load_inventory(cur, inventory):
    for item in inventory:
        cur.execute(
            """
            INSERT INTO inventory
            (product_id, warehouse_id, stock_quantity, updated_at)
            VALUES (%s, %s, %s, %s)
            """,
            (
                item["product_id"],
                item["warehouse_id"],
                item["stock_quantity"],
                item["updated_at"]
            )
        )