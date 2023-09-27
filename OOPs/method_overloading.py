class Hari:
    def display(self,a=None,b=None):
        print(a,b)
        print("a=",type(a))
        print("b=",type(b))
h1=Hari()
h1.display(10,None)
h1.display(None,40)
h1.display(772,546)
