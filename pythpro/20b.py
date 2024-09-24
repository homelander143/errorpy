def CONVERT_STR_DICT(a):
    d={}
    b=a.split(" ")
    for i in b:
        c=i.split("-")
        d[c[0]]=int(c[1])
    return d

def CONVERT_DICT_STR(s):
    st=""
    for i in s:
        st=st+i+"-"+str(s[i])+" "
    return st.rstrip()

x=eval(input("Enter the dictionary : "))
y=input("Enter the string : ")
print(CONVERT_DICT_STR(x))
print(CONVERT_STR_DICT(y))