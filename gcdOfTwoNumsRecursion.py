def rec_gcd(a,b):
    if b==0:
        return a
    else:
        return rec_gcd(b, a%b)

a=int(input("Enter a "))
b=int(input("Enter b "))
if a>b:
    print("The Gcd of ",a,"and",b,"is ",rec_gcd(a,b))
if b>a:
    print("The Gcd of ",a,"and",b,"is ",rec_gcd(a,b))
