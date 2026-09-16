import getpass

#The Bank Loan & Interest Rate Approver

#inputs
#age
#is_employed
#credit_score
#annual_income
#has_collateral

#Login
print("\t____________________________________________________________")
print("\tWELCOME TO BANK LOAN! PLEASE ENTER YOUR PROFILE INFORMATION")
username ="Venn mark_11"
password ="butchi22"
print("\t____________________________________________________________")

username= input("Please enter your username --->:")
password= input("Please enter your password --->:")

      
#Username description
if username ==  username and password == password:
    print("\nYour username and password is correct! you may proceed")
    Full_name= input("Please enter your Full name--->")
    age= int(input("Enter your age --->"))
    is_employed= input("Are you employed? (True/false):")
    Job_description=("Enter your job description:")
    credit_score= int(input("What is your credit_score history?"))
    annual_income= eval(input("How much is your annual income? --->"))

    base_rate= 0.0
    #Tier 1 (High credit)
    if age >= 21 and is_employed == True:
        print("You are eligible to loan")
        if credit_score >= 750:
            if annual_income >= 100000:
                base_rate= 4.5
        else:
            base_rate= 5.0
            print("Your interest_rate is", base_rate)
#tier 2 (Fair credit)
    elif credit_score >= 600 and credit_score < 750:
            collateral_desc= input("Enter the description of collateral---> (e.g, motorcycle, land, house):")
            collateral_value= eval(input("Enter the collateral value --->"))
            has_collateral= collateral_value>= 30000

            if not has_collateral:
                print("NOTICE: The collateral you entered did not satisfy the specifications. (Under 30000 value is invalid)")
            if has_collateral == True:
                base_rate= 7.0
                print("Your interest rate is", base_rate)
            elif annual_income < 40000:
                base_rate= 9.5
                print("Your interest rate is", base_rate)   
            else:
                base_rate= 8.0
                print("Your interest rate is", base_rate)
else:print("Your access is denied. Please enter the correct description")       
