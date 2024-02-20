bill = float(input("What was the total bill? "))
percent = float(input("What percentage tip would you like to give: 10, 12, or 15? "))
people = int(input("How many people split the bill? "))

tip_amount = bill * (percent / 100)
total_bill = bill + tip_amount
split_amount = total_bill / people
rounded_split_amount = round(split_amount, 2)

print(f"Each person should pay: ${rounded_split_amount}")