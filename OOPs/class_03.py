class student:
    name="hari"

s1=student()
s2=student()
s3=student()
s1.age=40
print("Name:",s1.name)#hari
print("Age:",s1.age)#21
s2.age=100
s2.name="harry"
del s2.age
print("name:",s2.name)
#print("age:",s2.age)
# now i delete object s3
# del s3
# print(s3)