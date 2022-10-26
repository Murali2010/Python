li=[]
for i in range(1,11):
    li.append(i)
print("List of 1-10 numbers")
print(li)
for i in li:
    if i%2==0:
        li.remove(i)
print("List of odd numbers from 1-10")
print(li)
