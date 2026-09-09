#multiple if and elif conditions

#Create a python program that would capture age group

name = input("Please input your name ---> ")

age= int(input("Please input your age ---> "))


if age >=0 and age >= 5 :
	print("That age is considered as INFANT ")

elif age >0 and age <=5 :
	print("That age is considered an INFANT ")
else:
	print("age invalid")
