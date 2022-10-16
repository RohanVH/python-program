# program to find the average of a given number
def sum(*x):
    s=0
    for i in x:
        s+=i
    print(f"average={s/len(x)}")
sum(2,5,5,4)