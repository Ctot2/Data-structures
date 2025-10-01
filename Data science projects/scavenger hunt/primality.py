

def primality():
    input_number = int(input('input a number here: '))
    for d in range (input_number - 1):
        if input_number % d == 0:
            print("not prime")
            return False
        else:
            print("prime!")
            return True

if __name__ == "__main__":
    primality()

