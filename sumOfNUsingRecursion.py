def rec_sum(n):
    if n==0 or n==1:
        return n
    else:
        return n+rec_sum(n-1)
n=int(input("enter a number"))
print("The sum of ", n,"numbers is ",rec_sum(n))
