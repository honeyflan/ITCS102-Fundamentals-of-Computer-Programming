#import Neleto
import getpass #folder

username= "Neleto"
password= "Butchi22"

u= input("Input USERNAME ---> ")
p= getpass.getpass("Input PASSWORD ---> ")

if u == username:
	print("username correct")

else: 
	print("incorrect username")

if u == password:
	print("password correct")

else: 
	print("incorrect password")

if not u == username and p == password:
	print("username or password")

else:
	print("Invalid")