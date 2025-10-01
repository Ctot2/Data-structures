x = list(input("write word here: "))
y = ["a", "e", "i", "o", "u"]
z = 0
def vowels(x, y, z):
    for i in range(len(x)):
        for n in range (0, 5):
            if x[i-1] == y[n]:
                z = z+1
    return(z)


if __name__ == "__main__":
    vowels(x, y, z)