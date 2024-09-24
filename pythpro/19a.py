s=input("Enter the sentence with spaces : ")
a=s.split(' ')
print(a)
d={}
for i in a:
    d.setdefault(i[0],[])
    d[i[0]].append(i)
print(d)