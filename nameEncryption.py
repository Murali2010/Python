s=input("Enter any text")
i=0
while i<len(s):
    ch=s[i]
    print(chr(ord(ch)+3),end='')
    i+=1

#for c in s:
#print(chr(ord(c)+3),end='')
