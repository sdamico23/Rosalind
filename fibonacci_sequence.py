def fib(n):
    if n == 0:
        return 0
    terms = []
    terms.append(0)
    terms.append(1)
    for i in range(2, n+1):
        terms.append(terms[i-1] + terms[i-2])
    return terms[n]


print(fib(22))
