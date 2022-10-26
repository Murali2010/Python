n=int(input("Enter a number"))
c=0
for i in range(2, (n//2+1)):
    if(n%i==0):
        c+=1
        break
if(c==0):
    print("N is prime")
else:
    print("N is not prime")
