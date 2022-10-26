li=[]
n=int(input("Enter n"))
for i in range(n):
    a=int(input("Enter an Integer"))
    li.append(a)
print("list",li)
tu=()
for i in li:
    if i>0:
        tu=tu+(i,)
print("Tuple",tu)
