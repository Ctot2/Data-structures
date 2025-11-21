def yes_or_no():
    a = input("")
    if a == "yes":
        return "yes"
    elif a == "no":
        return "no"
    else:
        print("enter yes or no")
        return yes_or_no()

print(yes_or_no())