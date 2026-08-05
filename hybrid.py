#hybrid inheritence 1
class A:
    def __init__(self, pname):
        self.pname = pname
    def display(self):
        return f"Hii I am parent {self.pname}"
class B(A):
    def __init__(self, pname, cname):
        A.__init__(self, pname)
        self.cname = cname
    def display(self):
        print(A.display(self))
        return f"Hii I am child of A = {self.cname}"
class C(A):
    def __init__(self, pname, gcname):
        A.__init__(self, pname)
        self.gcname = gcname
    def display(self):
        print(A.display(self))
        return f"Hii I am another child of A = {self.gcname}"
class D(B, C):
    def __init__(self, pname, cname, gcname, dname):
        B.__init__(self, pname, cname)
        C.__init__(self, pname, gcname)
        self.dname = dname
    def display(self):
        print(B.display(self))
        print(C.display(self))
        return f"Hii I am grandchild {self.dname}"
print(D.mro())