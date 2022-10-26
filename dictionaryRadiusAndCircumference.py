di={}
r=0
n=int(input("Enter number of radii"))
i=0
while(i<n):
    r=float(input("Enter radius"))
    di.update(dict([(r, 2*3.14*r)]))
    i=i+1
print(di)
