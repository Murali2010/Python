import os
fp=open("Student.txt", "w")
fp.write("Hello")
fp.close()
fp=open("Student.txt", "r")
print(fp.read())
fp.close()
os.rename("Student.txt", "Stud.txt")
