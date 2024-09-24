import re
s=input("Enter the IP address: ")
f=0
k=r'\b[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\b'
if re.search(k,s):
    a=s.split('.')
    for i in a:
        if int(i)>=0 and int(i)<=255:
            f=1
        else:
            print("Invalid IP address")
            break
else:
    print("Invalid IP address")
if f==1:
    print("Valid IP address")