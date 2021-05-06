my_dict = {}


def fib(n):
    if n < 2:
        return n
    else:
        if n in my_dict:
            return my_dict[n]
        my_dict[n] = fib(n-1) + fib(n-2)
        return my_dict[n]


print(fib(200))
