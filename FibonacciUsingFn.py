def fib(num):
    a=0
    b=1
    print('%d' %a)
    print('%d' %b)
    for i in range(3, num+1):
        c=a+b
        print('%d' %c)
        a=b
        b=c
n=int(input("Enter n"))
fib(n)
