class StockPortfolio:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, symbol, quantity, price):
        """Add a stock to the portfolio."""
        if symbol in self.portfolio:
            self.portfolio[symbol]['quantity'] += quantity
            self.portfolio[symbol]['price'] = price
        else:
            self.portfolio[symbol] = {'quantity': quantity, 'price': price}
        print(f"Added {quantity} of {symbol} at ${price} each.")

    def remove_stock(self, symbol, quantity):
        """Remove a stock or reduce its quantity."""
        if symbol in self.portfolio:
            if quantity >= self.portfolio[symbol]['quantity']:
                del self.portfolio[symbol]
                print(f"Removed all shares of {symbol}.")
            else:
                self.portfolio[symbol]['quantity'] -= quantity
                print(f"Removed {quantity} of {symbol}.")
        else:
            print(f"{symbol} is not in your portfolio.")

    def view_portfolio(self):
        """Display the portfolio."""
        if not self.portfolio:
            print("Your portfolio is empty.")
        else:
            print("Your Portfolio:")
            for symbol, details in self.portfolio.items():
                total_value = details['quantity'] * details['price']
                print(f"{symbol}: {details['quantity']} shares at ${details['price']} each (Total: ${total_value:.2f})")

    def total_value(self):
        """Calculate the total value of the portfolio."""
        total = sum(details['quantity'] * details['price'] for details in self.portfolio.values())
        print(f"Total Portfolio Value: ${total:.2f}")


# Example Usage:
portfolio = StockPortfolio()

while True:
    print("\n1. Add Stock\n2. Remove Stock\n3. View Portfolio\n4. Total Value\n5. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        symbol = input("Enter stock symbol: ").upper()
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price per stock: "))
        portfolio.add_stock(symbol, quantity, price)
    elif choice == '2':
        symbol = input("Enter stock symbol: ").upper()
        quantity = int(input("Enter quantity to remove: "))
        portfolio.remove_stock(symbol, quantity)
    elif choice == '3':
        portfolio.view_portfolio()
    elif choice == '4':
        portfolio.total_value()
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
