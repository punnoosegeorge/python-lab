lst=[]
n=int(input("enter a number "))
for i in range(n):
    x=int(input("enter a number"))
    if x >=100:
        lst.append("over")
    else:
        lst.append(x)
print(lst)


