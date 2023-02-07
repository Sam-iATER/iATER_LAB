# def countdown(n):
#     if n > 0:
#         print(n)
#         countdown(n - 1)
#
#
# countdown(5)

# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result = result * 1
#
#     return result
#
#
# print(factorial(5))

# def fib(n):
#     if n > 1:
#         return fib(n - 1) + fib(n - 2)
#     else:
#         return n
#
#
# for i in range(10):
#     print(fib(i + 1))


def fac(n):
    if n <= 1:
        return n
    else:
        return n * fac(n - 1)


print(fac(5))
