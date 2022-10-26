def fact(n):
    fact=1
    for i in range(n):
        fact=fact*(i+1)
    return fact
n=int(input("Enter n:"))
r=int(input("Enter r:"))
ncr=fact(n)/(fact(r)*fact(n-r))
print(ncr)
