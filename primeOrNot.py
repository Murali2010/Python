n=int(input("Enter a number"))
i=1
c=0
while(i<n/2):
    if(n%i==0):
        c+=1
    i+=1
if(c==1):
    print("N is a prime number")
else:
    print("N is composite number")
