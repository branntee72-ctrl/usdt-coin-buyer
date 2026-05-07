from binance.client import Client
import config

# Initialize the Binance Client
client = Client(config.api_key, config.api_secret)

def buy_low_value_coin(symbol, usdt_amount):
    """
    Buys a specified amount of a coin using USDT.
    Example symbol: 'DOGEUSDT' or 'SHIBUSDT'
    """
    try:
        # Get latest price for the coin
        ticker = client.get_symbol_ticker(symbol=symbol)
        print(f"Current price for {symbol}: {ticker['price']}")

        # Place a market buy order
        order = client.order_market_buy(
            symbol=symbol,
            quoteOrderQty=usdt_amount
        )
        print("Success! Order details:", order)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    # Change these to your target coin and USDT amount
    TARGET_COIN = "PEPEUSDT"
    SPEND_AMOUNT = 10  # 10 USDT
    buy_low_value_coin(TARGET_COIN, SPEND_AMOUNT)
