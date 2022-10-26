slabs=int(input("Enter slabs in units"))
if(slabs<=100 and slabs>0):
    print("Your electricity bill is "+str(slabs*1.25))
elif(slabs>=101 and slabs<=200):
    print("Your electricity bill is "+str(slabs*2.25))
elif(slabs>=201 and slabs<=250):
    print("Your electricity bill is "+str(slabs*3.50))
else:
    print("Your electricity bill is "+str(slabs*6.75))
    
    
