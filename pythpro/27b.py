class triangle:
    def __init__(self,a,b):
        self.p=a
        self.q=b
    def __gt__(self,t1):
        if 0.5*self.p*self.q>0.5*t1.p*t1.q:
            return "Area of 1st triangle is greater than 2nd triangle"
        else:
            return "Area of 2nd triangle is greater than 1st triangle"

m=int(input("Enter the length of 1st triangle : "))
n=int(input("Enter the breadth of 1st triangle : ")) 
t=triangle(m,n)
x=int(input("Enter the length of 2nd triangle : "))
y=int(input("Enter the breadth of 2nd triangle : ")) 
t1=triangle(x,y)
k=t>t1
print(k)