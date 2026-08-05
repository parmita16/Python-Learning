#hierarchical inheritence
class A:#parent class
    def __init__(self,pname):
     self.pname = pname
    def display(self):
        return f"Hii i am parent {self.pname}"
class B(A):#child class
    def __init__(self,pname,cname):
        #self.cname = cname
       super(). __init__(pname)
       self.cname = cname
    def display(self):
        p_display = super().display()
        print(p_display)
        return f"Hii i am child {self.cname}"
class C(A):#child class
    def __init__(self,pname,gcname):
        #self.cname = cname
       super(). __init__(pname)
       self.gcname = gcname
    def display(self):
        info = super().display()
        print(info)
        return f"Hii i am grandchild {self.gcname}"