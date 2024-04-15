import json
import config

class RealTimeTradingAlgorithm:
    def __init__(self, symbol, buy_condition, sell_condition):
        self.symbol = symbol
        self.buy_condition = buy_condition
        self.sell_condition = sell_condition

    def process_real_time_data(self, data):
        try:
            symbol = data['S']
            bid_price = data['bp']
            ask_price = data['ap']
            print(f"Received data for {symbol}: Bid Price = {bid_price}, Ask Price = {ask_price}")

            # Execute trading logic based on user input and real-time data
            if symbol == self.symbol and bid_price <= self.buy_condition:
                print("Executing buy order...")
                # Implement code to execute buy order

            if symbol == self.symbol and ask_price >= self.sell_condition:
                print("Executing sell order...")
                # Implement code to execute sell order

        except Exception as e:
            print("Error processing real-time data:", e)
