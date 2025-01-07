def calculate_trip_cost(kilometers, litres_per_km, price_per_liter):
    fuel_required = kilometers * litres_per_km
    total_cost = fuel_required * price_per_liter
    return total_cost

kilometers = float(input("Enter the kms to drive: "))
litres_per_km = float(input("Enter litres per kms usage of the car: "))
price_per_liter = float(input("Enter the price per litre of fuel: "))
trip_cost = calculate_trip_cost(kilometers, litres_per_km, price_per_liter)
print(f"The total cost of the trip is ${trip_cost:.2f}")


def calculate_total_amount(quantity, price_per_item):
    total_cost = quantity * price_per_item
    if quantity > 10:
        discount = total_cost * 0.10
        total_cost -= discount
    return total_cost

quantity = int(input("Enter the quantity of items purchased: "))
price_per_item = float(input("Enter the price per item: "))
total_amount = calculate_total_amount(quantity, price_per_item)
print(f"The total amount is {total_amount:.2f}")