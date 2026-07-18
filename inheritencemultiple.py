class Father:
    def money(self):
        print("Father has money")

class Mother:
    def love(self):
        print("Mother gives love")

class Child(Father, Mother):
    pass

c = Child()
c.money()
c.love()