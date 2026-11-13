#Loan maker 

amount = float(input("Please enter your loan amount ---> "))
years= int(input("Input years to pay --->"))
m= years * 12
principal= amount / m
rem_bal= amount #amount initially
#interest=
#paymemt=

for count in range( 1, m + 1):
    rem_bal -= principal
    interest = rem_bal * 0.00256
    payment = interest + principal
    #print( count,round(rem_bal, 2), round(principal, 2)
    
    #string format
print(f"| ,
