def sum_list(n):
   if len(n) == 0:
       return 0
   else:
       return n[0] + sum_list(n[1:])

def count_x(x):
    print(x)
    if x == "":
        return 0
    else:
        if x[0] == "x":
            return 1 + count_x(x[1:])
        else:
            return 0 + count_x(x[1:])

def replace_x(t):
    z = list(t)
    if len(z) == 0:
        return ""
    if z[0] == "x":
        return "y" + replace_x(t[1:])
    else:
        return t[0] + replace_x(t[1:])

def harmonic_sum(a):
    if a == 0:
        return 0
    else:
        return 1/a + harmonic_sum(a-1)

def recursive_search(item, my_list):
    if len(my_list) == 0:
        return False
    else:
        if my_list[0] == item:
            return True
        else:
            return recursive_search(item, my_list[1:])

def better_fib_helper(n, a, b):
    if n == 1:
        return a
    if n == 2:
        return b
    return better_fib_helper(n - 1, b, a + b)

def better_fib(n):
    return better_fib_helper(n, 1, 1)

print("Enter an integer:")
n = int(input())
print(better_fib(n))
