from alpaca_trade_api.stream import Stream
import websocket
import json
import config

#from trading_algorithm import RealTimeTradingAlgorithm  # Importing the algorithm class

def on_open(ws):
    print("opened")
    auth_data = {
        "action": "auth",
        "key": config.API_key,
        "secret": config.API_secret_key
    }

    ws.send(json.dumps(auth_data))

    listen_message = {"action": "subscribe", "quotes": ["ETH/USD"]}

    ws.send(json.dumps(listen_message)) 

def on_message(ws, message):
    print("received a message")
    print(message)

def on_close(ws):
    print("closed connection")

# Get user input from the user interface file
# For example, if the user interface file is user_interface.py:
from user_interface import get_user_input

# Get user input
symbol, buy_condition, sell_condition = get_user_input()

# Initialize AlgorithmicTradingLogic object with user input
algorithm = RealTimeTradingAlgorithm(symbol, buy_condition, sell_condition)

# Connect to WebSocket for real-time data
ws = websocket.WebSocketApp('wss://stream.data.alpaca.markets/v1beta3/crypto/us', on_open=on_open, on_message=on_message, on_close=on_close)
ws.run_forever()
