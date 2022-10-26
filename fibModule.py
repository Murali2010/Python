def fib(n):
    a=0
    b=1
    print('%d' %a)
    print('%d' %b)
    for i in range(3, n+1):
        c=a+b
        print('%d' %c)
        a=b
        b=c
        
def fibRec(n):
    if n<0:
        print("Incorrect input")
    elif n==0 or n==1:
        return n
    else:
        return fibRec(n-1)+fibRec(n-2)
