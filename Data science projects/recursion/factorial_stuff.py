def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result


print(factorial(5))


def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


print(fact(5))

def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n-1)

print(sum(10))


def fib(n):
   if n == 1:
       return 1
   if n == 2:
       return 1
   else:
       return fib(n-1) + fib(n-2)


print(fib(25))
print(fib(30))
print(fib(35))
print(fib(40))