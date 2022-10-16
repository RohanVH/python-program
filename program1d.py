# generate prime numbers between a and b
# sum of the list
def prime(n):
    isprime=True
    if n<2:
        isprime=False
    else:
        for i in range(2,n):
            if n%i==0:
                isprime=False
                break
    return isprime

a,b=map(int,input("enter the start and the end range:\t").split())
print(a,b)
lst=[i for i in range(a,b+1) if prime(i)]
print(f"Prime numbers between ={lst}")
print(f"sum={sum(lst)}")