# Inputs
sender_name = input("Enter your Name: ")
type_of_item = input("Enter the type of item you want to ship: ")

# Standard string inputs for booleans
is_fragile = input("Is the item fragile? (True/False): ") == "True"
weight = float(input("Enter the weight in kg: "))
distance = float(input("Enter the distance in km: "))
is_express = input("Do you want express shipping? (True/False): ") == "True"
is_international = input("Is this an international shipment? (True/False): ") == "True"

# 1. Calculate Base Cost
base_cost = (weight * 2.50) + (distance * 0.15)

# 2. Evaluate Pricing Tiers
if weight <= 2.0 and distance <= 100 and not is_express and not is_international:
    total = 0.00
elif is_international and is_express:
    total = (base_cost * 1.40) + 50
elif is_express or (is_international and weight > 20):
    total = (base_cost * 1.20) + 25
elif weight > 30 or distance > 1000:
    total = base_cost + 30
else:
    total = base_cost

total = round(total, 2)

print("\t________________________________________________________________________________________________\n")
print("\t\t\t\t\tGlobal Freight Calculator")
print("\t________________________________________________________________________________________________\n")
print("\tSender Name: ", sender_name)
print("\tType of Item: ", type_of_item)
print("\tWeight (kg): ", weight)
print("\tDistance (km): ", distance) 
print("\tTotal Cost: $", total)
print("\t________________________________________________________________________________________________\n")