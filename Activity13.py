#The Bank Loan & Interest Rate Approver

#inputs
#age
#is_employed
#credit_score
#annual_income
#has_collateral
print("Welcome to the Bank Loan ")
print("_________________________________")
age= int(input("Enter your age --->  "))
is_employed= bool(input("Are you employed? --->"))
credit_score= eval(input("What's your credit score history? --->"))
annual_income= eval(input("How much is your annual income? --->"))
has_collateral= bool(input("Do you have any collateral? --->"))
print("_________________________________")

base_rate= 0.0
#Tier 1(High credit)
if age >= 21 and is_employed == True:
    print("You are now eligible to loan")
    if credit_score >=750:
        base_rate= 4.5
    if annual_income >=100000:
        base_rate=4.5
        print("Your interest rate is", base_rate)
    else:
        base_rate= 5.0
        print("Your interest rate is", base_rate)
#tier 2 (Fair credit)
elif credit_score >= 600 and credit_score < 750:
    if has_collateral == "True":
        base_rate= 7.0
        print("Your interest rate is", base_rate)
    elif annual_income < 40000:
        base_rate= 9.5
        print("Your interest rate is", base_rate)   
    else:
        base_rate= 8.0
        print("Your interest rate is", base_rate)
#tier 3 (Low credit)
    if credit_score < 600:
        print("You are not eligible to loan")
        
else:
    print("Rejected, you are not eligible to loan")
