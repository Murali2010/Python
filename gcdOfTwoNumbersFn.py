def gcd(x,y):
    rem=x%y
    while rem!=0:
        x=y
        y=rem
        rem=x%y
    return y
m=int(input("Enter first number"))
n=int(input("Enter second number"))
print(gcd(m,n))
