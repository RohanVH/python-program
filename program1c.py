#evaluate 1/2+2/3+3/4....+n/n+1
#read n value
n=int(input("enter the value\t"))
eval=0
for i in range(1,n+1):
    eval+=i/i+1
    print(f"{i}/{i+1}+")
print(eval)