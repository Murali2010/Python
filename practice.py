def fact(n):
    i=1
    f=1
    while(i<=n):
        f*=i
        i+=1
    print(f)
n=int(input("n"))
fact(n)
