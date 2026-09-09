#Breakdown fix money value to peso
# 100, 500, 200, 100, 50, 10, 5,1

money= eval(input("Enter the money to deposit --->"))
# in(), Eval(), type()
#print(type(money))

print("================================PH BANK BREAKDOWN================================")
print(" MONEY TO DEPOSIT ------>", money, "php")


a=19863
T=0
fiveH=0
twoH=0
H=0
F=0
ty=0
ten=0
one=0

print("My current money is", a)
T=a//1000 
a=a%1000
print("thousand:", T)
fiveH=a//500
a=a%500
print("Fivehundred:", fiveH)
twoH=a//200
a=a%200
print("twohundred:", twoH)
H=a//100
a=a%100
print("Hundred:", H)
F=a//50
a=a%50
print("Fifthy:", F)
ty=a//20
a=a%20
print("Twenty:", ty)
ten=a//10
a=a%10
print("tenth:", ten)
one=a//1
a=a%1
print("ones:", one)
print("ones:", one)
