class parent:
    def pdisplay(self):
        print("parent")
class child1(parent):
    def c1display(self):
        print("Child 1")
class child2(parent):
    def c2display(self):
        print("Child 2")

c1=child1()
c2=child2()
c1.c1display()
c1.pdisplay()
c2.pdisplay()
c2.c2display()