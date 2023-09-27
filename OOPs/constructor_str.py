class person:
    def __int__(self,name,age):
        self.name =name
        self.age=age

    def __str__(self):#-->return the value in the form of string
        return f"{self.name}({self.age})"



p1=person("Hari","40")
# print(p1.age)
# print(p1.name)
print(p1)