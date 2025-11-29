def fib(n):
    ls = [0, 1]
    if n < 2:
        return ls[n]
    for i in range(2, n + 1):
        ls.append(ls[i - 2] + ls[i - 1])
    print(ls)
    return ls[n]
