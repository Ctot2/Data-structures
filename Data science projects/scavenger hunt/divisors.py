def divisors():
    divisors_list = []
    input_number = int(input('input a number here: '))
    for i in range (1, input_number):
        if input_number %  i == 0:
            divisors_list.append(i)
    return divisors_list

if __name__ == "__main__":
    divisors()







