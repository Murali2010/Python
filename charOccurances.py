c=0
my_string=input("Enter a sentence: ")
s=input("Enter the char to find occurances")
for ch in my_string:
    if ch==s:
        c=c+1
print("The char {} appears {} times.".format(s,c))
