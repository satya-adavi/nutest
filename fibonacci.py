# def fibonacci(n):
#     if n <= 0:
#         return []
#     elif n == 1:
#         return [0]
#     elif n == 2:
#         return [0, 1]
#     else:
#         fib = [0, 1]
#         for i in range(2, n):
#             fib.append(fib[i - 1] + fib[i - 2])
#         return fib

# # print(fibo(0,1,0,5))
def fibo(a, b, start, end):
    if a==0:
        print(a)
        print(b)
    c = a + b

    print(c)
    if start < end:
        a, b = b, c
        start = start + 1
        return fibo(a, b,start,end)
    else:
        return c
fibo(0,1,1,6)
