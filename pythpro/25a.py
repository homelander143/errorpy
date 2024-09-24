class student:
    scn="bvvs"
    def __init__(self,a,b,c):
        self.name=a
        self.usn=b
        self.cgpa=c
    def display(self,us):
        if self.usn==us:
            print("Student details\n")
            print("Name:",self.name)
            print("USN:",self.usn)
            print("CGPA:",self.cgpa)
    def cgp(self,us):
        if self.usn==us:
            if self.cgpa>=9:
                print("O grade")
            elif self.cgpa>=8:
                print("A grade")
            elif self.cgpa>=7:
                print("B grade")
            elif self.cgpa>=6:
                print("C grade")
            elif self.cgpa>=4:
                print("D grade")
            else:
                print("F grade")
    def deletee(self,us):
        if self.usn==us:
            self.name=None
            self.usn=None
            self.cgpa=None
        else:
            print("Student doesn't exist")
    def updatee(self,us,cg):
        if self.usn==us:
            self.cgpa=cg
        else:
            print("Student doesn't exist")

n=int(input("Enter the number of students details you want to store : "))
l=[]
for i in range(n):
    a=input("Enter the student name : ")
    b=float(input("Enter the student cgpa : "))
    s=student(a,i+1,b)
    l.append(s)
while True:
    ch=input("Enter your choice : ")
    if ch=='display':
        x=int(input("Enter the USN of the student to display its details : "))
        l[x-1].display(x)
    elif ch=='cgpa':
        x=int(input("Enter the USN of the student to display his cgpa : "))
        l[x-1].cgp(x)
    elif ch=='delete':
        x=int(input("Enter the USN of the student to delete his information : "))
        l[x-1].deletee(x)
    elif ch=='update':
        x=int(input("Enter the USN of the student to update his information : "))
        z=input("Enter the new CGPA : ")
        l[x-1].updatee(x,z)
    else:
        break