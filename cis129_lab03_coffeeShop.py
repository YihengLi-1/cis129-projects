# Set prices for coffee and muffin
coffee_price = 5
muffin_price = 4
latte_price = 6
cappuccino_price = 7
tax_rate = 0.06

# Ask the user for number of coffees and muffins
num_coffees = int(input("number of coffees bought? "))
num_muffins = int(input("number of muffins bought? "))
num_lattes = int(input("number of lattes bought?"))
num_cappuccinos = int(input("number of cappuccinos bought?"))

# Calculate the subtotal for coffee and muffins
subtotal_coffee = num_coffees * coffee_price
subtotal_muffin = num_muffins * muffin_price
subtotal_latte = num_lattes * latte_price
subtotal_cappuccino = num_cappuccinos * cappuccino_price

# Add the subtotal together
subtotal = subtotal_coffee + subtotal_muffin + subtotal_latte + subtotal_cappuccino

# Calculate the tax and total
tax = subtotal * tax_rate
total = subtotal + tax

# Print the receipt
print("***************************************")
print("My Coffee and Muffin Shop")
print(f"Number of coffees bought? \n {num_coffees}")
print(f"Number of muffins bought? \n {num_muffins}")
print(f"Number of lattes bought? \n {num_lattes}")
print(f"Number of cappuccinos bought? \n {num_cappuccinos}")
print("***************************************")
print("\n\n\n***************************************")
print("My Coffee and Muffin Shop Receipt")
print(f"{num_coffees} Coffee at $5 each: ${subtotal_coffee:.2f}")
print(f"{num_muffins} Muffin at $4 each: ${subtotal_muffin:.2f}")
print(f"{num_lattes} Latte at $6 each: ${subtotal_latte:.2f}")
print(f"{num_cappuccinos} Cappuccino at $7 each: ${subtotal_cappuccino:.2f}")
print(f"6% tax: ${tax:.2f}")
print("---------")
print(f"Total:${total:.2f}")
print("***************************************")

# Thanks the user
print("Thank you for visiting My Coffee and Muffin Shop! We hope to see you again!")
      
