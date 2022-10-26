n=int(input('Enter number of elements you would like as input'))
list=[]
for i in range(n):
    ele=int(input('Enter the {} element'.format(i)))
    list.append(ele)
print('list is',list)
temp=[]
for i in list:
    if i not in temp:
        temp.append(i)
#list=temp
print('List with no duplicates',temp)                  
