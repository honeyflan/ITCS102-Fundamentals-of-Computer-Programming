#Boolean while looping

while True:

    question= input(" Do you want to continue? (yes/no)")

    if question == "yes" or question == "Yes":
        print("Yes success")
    else:
        print(" Ok im sad :( ")
        break
