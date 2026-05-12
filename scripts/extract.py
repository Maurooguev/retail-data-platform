from faker import Faker
import random
from datetime import datetime

fake = Faker()


def generate_products():
    return [
        ("Coca Cola 500ml", "Beverages", 2.50),
        ("Sprite 500ml", "Beverages", 2.30),
        ("Fanta 500ml", "Beverages", 2.20),
        ("Water 1L", "Beverages", 1.50),
        ("Energy Drink", "Beverages", 3.00)
    ]


def generate_warehouses():
    return [
        ("Berlin Warehouse", "Berlin"),
        ("Munich Warehouse", "Munich"),
        ("Hamburg Warehouse", "Hamburg")
    ]


def generate_customers(quantity=20):
    customers = []

    for _ in range(quantity):
        customers.append(
            (fake.name(), fake.city())
        )

    return customers


def generate_sales(quantity=100):
    sales = []

    for _ in range(quantity):
        sales.append({
            "product_id": random.randint(1, 5),
            "customer_id": random.randint(1, 20),
            "warehouse_id": random.randint(1, 3),
            "quantity": random.randint(1, 20),
            "sale_date": datetime.now()
        })

    return sales


def generate_inventory():
    inventory = []

    for product_id in range(1, 6):
        for warehouse_id in range(1, 4):
            inventory.append({
                "product_id": product_id,
                "warehouse_id": warehouse_id,
                "stock_quantity": random.randint(50, 500),
                "updated_at": datetime.now()
            })

    return inventory