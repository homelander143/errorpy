class cart:
    def __init__(self):
        self.li=[]
    def add(self,x,y):
        self.li.append([x,y])
        print("item added")
    def remove(self,x):
        for i in self.li:
            if i[0]==x:
                self.li.remove[i]
                print("not found")
            else:
                print("not found")
    def cal(self):
        p=0
        for i in self.li:
            p+=i[1]
        return p
c=cart()
while True:
    ch=input("add remove price")
    if ch=="add":
        x=input("item=")
        y=int(input("price="))
        c.add(x,y)
    elif ch=="remove":
        x=input("enter item to remove")
        c.remove(x)
    else:
        total=c.cal()
        print("price=",total)