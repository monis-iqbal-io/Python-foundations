# Display the program title
print("Here is your Tip Calculator")

# Take the total bill amount as input and convert it to float
Bill = float(input("What was your Bill?\n"))

# Take the tip percentage as input and convert it to integer
Tip = int(input("How much Percent of the bill you want to give as Tip? 10% 12% 14%\n"))

# Take the number of people to split the bill
Persons = int(input("How many people to split the bill ?\n"))

# Calculate the amount each person should pay
Amount = float(Bill * Tip / 100) / Persons

# Display the calculation process
print("Each Person Should Pay:")
print(f"({Bill}*{Tip}/{100})/{Persons}")

# Print the calculated amount per person
print(Amount)

# Display the formatted result rounded to two decimal places
print("After formatting the result to 2 decimal Places=")
print(round(Amount, 2))
