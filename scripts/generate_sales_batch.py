import logging
from extract import generate_sales
from transform import calculate_sales_amounts
from load import get_connection, get_product_prices, load_sales


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def main():
    conn = None
    cur = None

    try:
        logging.info("Starting sales batch pipeline...")

        conn = get_connection()
        cur = conn.cursor()

        sales = generate_sales(quantity=20)
        logging.info(f"Generated {len(sales)} new sales.")

        product_prices = get_product_prices(cur)
        sales = calculate_sales_amounts(sales, product_prices)

        load_sales(cur, sales)
        conn.commit()

        logging.info("Sales batch loaded successfully.")

    except Exception as error:
        logging.error(f"Pipeline failed: {error}")

        if conn:
            conn.rollback()
            logging.info("Database transaction rolled back.")

    finally:
        if cur:
            cur.close()

        if conn:
            conn.close()

        logging.info("Database connection closed.")


if __name__ == "__main__":
    main()