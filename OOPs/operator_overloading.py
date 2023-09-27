print("operator overloading:10")
def operator(a,b):
    return a+b
c=operator(a=eval(input("Enter the number:")),b=eval(input("Enter the number:")))
d=operator(a=input("Enter the string:"),b=input("Enter the string:"))
print("Addition:",c)
print("Concatentation:",d)