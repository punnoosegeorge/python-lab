s="onionooo"
print(s)
#words=s.split()
#z=set(words)
#print(words)
#print(z)
flag=1
for i in s :
    if i in s[1:8]:
        flag=0
        break
print(s[0]+s[1:8].replace("o","$"))


  #      print(f"{i}={words.count(i)}")
