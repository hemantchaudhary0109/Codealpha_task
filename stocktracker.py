# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 420,
    "AMZN": 185
}

portfolio = {}
total_investment = 0

print("=" * 50)
print("        STOCK PORTFOLIO TRACKER")
print("=" * 50)

print("\nAvailable Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock} : ${price}")

print("\nEnter 'done' when you finish adding stocks.\n")

while True:

    stock = input("Enter stock name: ").upper().strip()

    # Stop taking input
    if stock == "DONE":
        break

    # Check stock availability
    if stock not in stock_prices:
        print("Stock not available. Please choose from the list.")
        continue

    # Take quantity
    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

    except ValueError:
        print("Please enter a valid quantity.")
        continue

    # Calculate investment
    price = stock_prices[stock]
    investment = price * quantity

    # Store in portfolio
    if stock in portfolio:
        portfolio[stock] += quantity
    else:
        portfolio[stock] = quantity

    total_investment += investment

    print(f"{quantity} shares of {stock} added successfully.")
    print(f"Investment for {stock}: ${investment}")
    print()

# Display portfolio
print("\n" + "=" * 60)
print("                 PORTFOLIO SUMMARY")
print("=" * 60)

if len(portfolio) == 0:
    print("No stocks were added.")

else:
    print(f"{'Stock':<10}{'Quantity':<12}{'Price':<12}{'Investment':<15}")
    print("-" * 60)

    for stock, quantity in portfolio.items():

        price = stock_prices[stock]
        investment = price * quantity

        print(
            f"{stock:<10}"
            f"{quantity:<12}"
            f"${price:<11}"
            f"${investment:<14}"
        )

    print("-" * 60)
    print(f"Total Investment: ${total_investment:.2f}")

# Save result to text file
save = input("\nDo you want to save the result? (yes/no): ").lower()

if save == "yes":

    with open("portfolio.txt", "w") as file:

        file.write("STOCK PORTFOLIO REPORT\n")
        file.write("=" * 50 + "\n\n")

        for stock, quantity in portfolio.items():

            price = stock_prices[stock]
            investment = price * quantity

            file.write(
                f"Stock: {stock}\n"
                f"Quantity: {quantity}\n"
                f"Price: ${price}\n"
                f"Investment: ${investment}\n"
                f"{'-' * 30}\n"
            )

        file.write(
            f"\nTotal Investment: ${total_investment:.2f}\n"
        )

    print("Portfolio saved successfully in portfolio.txt")

print("\nThank you for using Stock Portfolio Tracker!")