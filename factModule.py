def fact(n):
    fact=1
    for i in range(n):
        fact=fact*(i+1)
    return fact

def rec_fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*rec_fact(n-1)

