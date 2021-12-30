def prime(i):
    res = True
    for n in range(2,i):
        if i%n == 0:
            res = False
    return res
def primes_upto(n):
    primes = []
    for i in range(2, n+1):
        if prime(i):
            primes.append(i)
    return primes 


def Goldbach(n):
    l = []
    x = []
    for i in primes_upto(n):
        l.append(i)
    l.sort()    
    for i in l:
        for j in l:
            if i+j == n and (i<j or i==j):
                x.append((i,j))
    return x
n=int(input())
print(sorted(Goldbach(n)))
