def number_addition():
    x = []
    total = 0
    for i in range (5):
        y = int(input("chose a number: "))
        x.append(y)
        total = total + y
        print(x)

    return(total)


print(number_addition())