n = 0
def factorial(n):
    n = 5
    x = 1

    for i in range(n):
        x = x * (n - i)
        print(x)

    return(x)

if __name__ == "__main__":
    factorial(n)