from bot.logging_config import logger

def place_order(client, symbol, side, order_type, quantity, price=None):
    try:
        params = {
            "symbol": symbol.upper(),
            "side": side,
            "type": order_type,
            "quantity": quantity,
        }

        if order_type == "LIMIT":
            params["price"] = price
            params["timeInForce"] = "GTC"

        logger.info(f"Order Request: {params}")

        response = client.create_order(**params)

        logger.info(f"Order Response: {response}")

        return response

    except Exception as e:
        logger.error(f"Order Failed: {str(e)}")
        raise