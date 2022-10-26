def fib(n):
    if n<0:
        print("Incorrect input")
    elif n==0 or n==1:
        return n
    else:
        return fib(n-1)+fib(n-2)

n=int(input("Enter n"))
for num in range(0, n):
    print(fib(num), end=' ')
