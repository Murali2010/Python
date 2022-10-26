n=int(input("Enter number of elements"))
list=[]
sum=0
for i in range(n):
    ele=int(input('Enter the {} element'.format(i)))
    list.append(ele)
    sum+=list[i]
print('list is: ',list)
print('Sum of elements is :',sum)
