print("Welcome to Bank loan")
#input
owner_age=int(input("Enter your age --->"))
cc=int(input("What is your credit score history?"))
yrs_b=float(input("How many years are you in business?"))
month_rev=float(input("What is your monthly revenue?"))
collateral_name=input("What is your collateral?")

#Records of bankruptcy
has_defaults=bool(input("Do you have bankruptcy records? (True/False): ")) == False

#Collateral value
collateral_val=float(input("What is the value of your collateral?"))

base_rate= 0.0
max_loan= 0

#Business rules
if owner_age >= 21 and yrs_b >= 2 and has_defaults == False:
      print("You are Accepted! eligible Owner")
    if cc >= 720: 
        max_loan= month_rev * 3
        print("max_loan for high credit is," max_loan)
        print("High Credit Score of 720")
    #Conditions for monthly rev
        if month_rev >= 50000:
             base_rate= month_rev * 0.015
             print("base fee rate is," base_rate)
        else:
            base_rate= month_rev * 0.025
            print("base fee rate is," base_rate)
else:
      print("You are Rejected! Ineligible Owner")          
#Tier 2:
