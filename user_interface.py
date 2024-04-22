import tkinter as tk


class ParameterParser:
    @staticmethod
    def paraser_user_input(symbol,buy_condition,sell_condition):
        if not symbol:
            raise ValueError("Symbol cannot be empty")
        try:
            buy_condition = float(buy_condition)
        except ValueError:
            raise ValueError("Buy condition must be valid number")
      
        try:
            sell_condition = float(sell_condition)  
        except ValueError:
            raise ValueError("Sell condition must be valid number")
        
        return{
            'symbol' : symbol,
            'buy_condition' : buy_condition,
            'sell_condition' : sell_condition
        }

def get_user_input():
    window = tk.Tk()

    window.title("Trade Bot User Input")
    tk.Label(window, text = "Enter Symbol:").grid(row=0, column=0)
    symbol_entry = tk.Entry(window)
    symbol_entry.grid(row=0, column=1)

    tk.Label(window,text = "Enter the buy condition").grid(row=1, column=0)
    buy_condition_entry = tk.Entry(window)
    buy_condition_entry.grid(row=1, column=1)

    tk.Label(window, text= "Enter the sell condition").grid(row=2, column=0)
    sell_condition_entry = tk.Entry(window)
    sell_condition_entry.grid(row=2, column=1)

    error_label = tk.Label(window, text="", fg="red")
    error_label.grid(row=3, columnspan=2)
    #Function to retrieve user input when the button is clicked
    
    def get_input():
        symbol = symbol_entry.get()
        buy_condition = buy_condition_entry.get()
        sell_condition = sell_condition_entry.get()

        try:
            user_input = ParameterParser.paraser_user_input(symbol,buy_condition, sell_condition)
            window.destroy()
            return user_input

        except ValueError as e:
            error_label.config(text = str(e))

    submit_button = tk.Button(window, text = "Submit", command = get_input)
    submit_button.grid(row=4, columnspan = 2)

    window.mainloop()

user_input = get_user_input()

if user_input:
    print("User input:", user_input)



