s=input("Enter the string : ")
f=0
alp="abcdefghijklmnopqrstuvwxyz"
for i in s:
    if i not in alp:
        f=1
        break
    else:
        f=0
if f==1:
    print("String is not panagram")
else:
    print("String is panagram")