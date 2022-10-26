sales=int(input("Enter the sales"))
if(sales<=10000):
    print("Commision is 500")
elif(sales>=10000 and sales<15000):
    print("Commision is "+str((sales*15)/100))
elif(sales>=15000 and sales<25000):
    print("The commision is"+str((sales*20)/100))
else:
    print("The commision is"+str((sales*30)/100))
