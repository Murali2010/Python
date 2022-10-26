n= int(input('Enter n: '))

i = 2
while(i<=n):
   if(i>1):
      j = 2
      while(j <= (i/j)):
         if(i%j)==0:
            break
         j=j+1
      else:
         print(i)
   i=i+1    
   
