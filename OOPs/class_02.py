class student:
    age=40
    def myself(self):
        print("age=",self.age)
        self.name="Hari"
        self.age=20
        print("My name is",self.name)
        print("My age is :",self.age)
s1=student()
s1.myself()