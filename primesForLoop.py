n=int(input("Enter a number"))
c=0
for i in range(2, n):
    if(n%i==0):
        c+=1
        
print(c)        
