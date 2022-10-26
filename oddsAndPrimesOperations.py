o=set()
p=set()
for i in range(20):
    if(i%2!=0):
        o.add(i)
print(o)
for i in range(2, 20):
    c=0
    j=1
    while(j<=i):
        if(i%j==0):
            c+=1
        j+=1
    if(c==2):
        p.add(i)
print(p)
print("Union: ",p.union(o))
print("Intersection: ",p.intersection(o))
print("Difference: ",p.difference(o))
print("Symmetric Difference: ",p.symmetric_difference(o))
       
