# program on sum the given digits
print("to print sum of the given digits")
num=int(input("enter the number\t"))
result=0
hold=num
while num>0:
    rem=num%10
    result=result+rem
    num=int(num/10)
print(f"sum of {hold}=\t{result}")