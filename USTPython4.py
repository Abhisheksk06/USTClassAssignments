kilometers = float(input("Enter the kms to drive: "))
litres_per_km = float(input("Enter litres per kms usage of the car: "))
price_per_liter = float(input("Enter the price per litre of fuel: "))

fuel_required = kilometers * litres_per_km
total_cost = fuel_required * price_per_liter

print(f"The total cost of the trip is {total_cost:.2f}")


quantity = int(input("Enter the quantity of items purchased: "))
price_per_item = float(input("Enter the price per item: "))
total_cost = quantity * price_per_item

if quantity > 10:
    discount = total_cost * 0.10
    total_cost -= discount

print(f"The total amount is {total_cost:.2f}")