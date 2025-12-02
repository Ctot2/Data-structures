def yes_or_no():
    a = input("input here: ")
    if a == "yes":
        return True
    elif a == "no":
        return False
    else:
        print("enter yes or no")
        return yes_or_no()
