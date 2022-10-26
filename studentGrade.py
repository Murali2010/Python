sub1=int(input("Enter marks in sub1"))
sub2=int(input("Enter marks in sub2"))
sub3=int(input("Enter marks in sub3"))
avg=(sub1+sub2+sub3)/3
if(avg>=75):
    print("Grade A")
elif(avg>=60 and avg<75):
    print("Grade B")
elif(avg>=45 and avg<60):
    print("Grade C")
else:
    print("Grade D")
