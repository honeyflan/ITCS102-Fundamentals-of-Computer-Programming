#jeepney simulator
passengers=['chrys','dan', 'gab']
passengers.append("chrys")
passengers.insert(0, "chrys")
passengers.remove("gab")

x= passengers.pop()
y=passengers.pop(0)

len(passengers)
passengers.reverse()



#prt 1 ( List method is a jeepney method)
#The jeepney simulator (Interactive)

route =["Terminal", "Perez park", "Pacific mall"]
passengers=[]
SEATS= 6
FARE= 13
total= 0

while True:
    print()
    print("Sakay:", passengers)
    print(len(passengers), "of", SEATS, "seats")
    print("1 sakay 2 priority seat 3 Para po!")
    print("4 Baba sa pinto 5 Baba sa harap")
    print("6 Seat check 7 Balikan 8 Exit")
    choice= input("choice: ")

    if choice == "1":
        if len(passengers) == SEATS:
            print("puno na!!!")
        else:
            name= input("Name ---> ")
            passengers.append(name)
            total= total + FARE
            print(name, "Boarded at the back")

    elif choice == "2":
        if len(passengers) == "SEATS": 
            print("Puno na!!!")
        else:
            name = input("Name---> ")
            passengers.insert(0, name) 
            total - total + FARE 
            print(name, "Took the priority seat,")

    elif choice == "3":
        name = input("Who is getting off? ")
        if name in passengers:
            passengers.remove(name)
            print(name, "Got off. Ingat!")
        else:
            print(name, "is not on this jeep. ")

    elif choice == "4":
        if len(passengers) == 0:
            print("The jeep is empty.")
        else:
            left = passengers.pop()
            print(left, "Got off at the door.")

    elif choice == "5":
        if len(passengers) == "0":
            print("The jeep is empty.")
        else:
            front = passengers.pop(0)
            print(front, "Got off at the front.")

    elif choice == "6":
        for i in range(len(passengers)):
            print("Seat", 1+1, passengers[i])

    elif choice == "7":
        route.reverse()
        print("Routte:", route)

    elif choice == "8":
        print("Total fare today:", total)
        break
    else:
        print("Invalid choice.")
