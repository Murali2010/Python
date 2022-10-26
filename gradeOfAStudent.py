sub1=int(input("Enter sub1 marks: "))
sub2=int(input("Enter sub2 marks: "))
sub3=int(input("Enter sub3 marks: "))
avg=(int)(sub1+sub2+sub3)/3
if(avg>=75):
    print("Grade A")
elif(avg>60&avg<75):
    print("Grade B")
else:
    print("Grade c")
