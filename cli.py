import click
from bot.client import BinanceClient
from bot.orders import place_order
from bot.validators import *
from bot.logging_config import logger


@click.command()
@click.option("--symbol", prompt="Enter Symbol (e.g., BTCUSDT)")
@click.option("--side", prompt="Enter Side (BUY/SELL)")
@click.option("--order_type", prompt="Enter Order Type (MARKET/LIMIT)")
@click.option("--quantity", prompt="Enter Quantity", type=float)
@click.option("--price", prompt="Enter Price (required for LIMIT)", default=None, type=float)
def run(symbol, side, order_type, quantity, price):

    try:
        # Validation
        validate_side(side)
        validate_order_type(order_type)
        validate_quantity(quantity)
        if order_type == "LIMIT" and price is None:
            price = float(input("Enter Price (required for LIMIT): "))

        client = BinanceClient()

        print("\n Order Summary")
        print(f"Symbol: {symbol}")
        print(f"Side: {side}")
        print(f"Type: {order_type}")
        print(f"Quantity: {quantity}")
        if price:
            print(f"Price: {price}")

        response = place_order(client, symbol, side, order_type, quantity, price)

        print("\n Order Placed Successfully!")
        print("Order ID:", response.get("orderId"))
        print("Status:", response.get("status"))
        print("Executed Qty:", response.get("executedQty"))
        print("Avg Price:", response.get("avgPrice", "N/A"))

    except Exception as e:
        print("\n Error:", str(e))
        logger.error(str(e))


if __name__ == "__main__":
    run()