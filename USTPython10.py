import time
import random

def stock_price_manipulator(base_price, volatility, steps):
    price = base_price
    for _ in range(steps):
        change_percent = random.uniform(-volatility, volatility)
        price += price * change_percent  # Apply the percentage change
        print(f"Stock Price: {price:.2f}")
        time.sleep(1)

# Example usage
stock_price_manipulator(200, 0.03, 10)
