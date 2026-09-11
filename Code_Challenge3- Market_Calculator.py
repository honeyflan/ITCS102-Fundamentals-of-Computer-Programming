#Global freight calculator

print("\n__________________________________________________________________\n")
print("Welcome to the Global Freight Calculator")



Sender_Name= input("Enter your name ---> ")
Type_of_item= input("Enter the type of item you want to ship ---> ")
weight= float(input("Enter the weight of the item in kg --->"))              
distance= float(input("Enter the distance in km --->  "))
is_express= input("Do you want express shipping? (True/False) ---> ").lower
is_international= input("Is this an international shipment? (True/False) ---> ").lower
is_fragile= input("Is the item fragile? (True/False) ---> ").lower
print("\n__________________________________________________________________\n")

base_cost= (" weight * 2.50 + distance * 0.15")

if weight <= 2.0 and distance <= 100 and is_express == "False" and is_international == "False" and is_fragile == "False":
    total_cost= 0.00   
    total = round(total_cost, 2)
    print("Hi", Sender_Name, "the total cost of shipping your", Type_of_item, "is $", total)
elif is_international and is_express:
    total= (base_cost * 1.40) + 50
elif is_express or(is_international and weight > 20):
    total= (base_cost * 1.20) + 25
elif weight > 30 or distance > 1000:
    total= base_cost + 30
else:
    total= base_cost
    tier = "Standard rate"

total = round(total, 2)

print("Hi", Sender_Name, "the total cost of shipping your", Type_of_item, "is $", total)
""





