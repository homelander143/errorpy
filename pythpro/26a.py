class employee:
    org="State bank of india"
    def __init__(self):
        self.id=int(input("Enter the employee ID : "))
        self.name=input("Enter employee name : ")
        self.__sal=float(input("Enter the employee salary : "))
        self.des=input("Enter employee designation : ")

    def getId(self):
        return self.id
    def getName(self):
        return self.name
    def setName(self,nname):
        self.name=nname
    def getSal(self):
        return self.__sal
    def getDes(self):
        return self.des
    
    def disp(emp):
        print("ID : ",emp.getId(),"\nName : ",emp.getName(),"\nSalary : ",emp.getSal(),"\nDesignation : ",emp.getDes())
    def search(l,id):
        for i in l:
             if i.getId()==id:
                 s.disp(i)
                 return
        print("ID doesn't exist")
    def countDes(l,des):
        c=0
        for i in l:
            if i.getDes()==des:
                c+=1
        return c
    def deletee(l,id):
        for i in l:
            if i.getId()==id:
                l.remove(i)
                return
        print("ID doesn't exist")
    def updatee(l,id,nname):
        for j in l:
            if j.getId()==id:
                j.setname(nname)
                return
        print("ID doesn't exist")
    
n=int(input("Enter the number of employee details to store : "))
l=[]
for i in range(n):
    s=employee()
    l.append(s)
while(True):
    ch=input("Enter your choice : ")
    if ch=='search':
        x=int(input("Enter the employee ID to search : "))
        employee.search(l,x)
    elif ch=='countdes':
        x=input("Enter the designation to count no. of same designation : ")
        res=employee.countDes(l,x)
        print("No. of designation is ",res)
    elif ch=='delete':
        x=int(input("Enter the employee ID to delete : "))
        employee.deletee(l,x)
    elif ch=='update':
        x=int(input("Enter the employee ID to update his name : "))
        z=input("Enter the new name : ")
        employee.updatee(l,x,z)
    else:
        break