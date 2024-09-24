import re
s=input("Enter passport number : ")
if len(s)==8:
    k=r'\b[A-Z]{1}[1-9]{1}[0-9]{1}[0-9]{4}[1-9]{1}\b'
    if re.search(k,s):
        print("Valid passport number")
    else:
        print("Invalid passport number")
else:
    print("Invalid passport number")

