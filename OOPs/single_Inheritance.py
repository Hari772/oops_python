class parent:
    def pdisplay(self):
        print("Parent")
class child(parent):
    def cdisplay(self):
        print("Child")
p1=parent()
c1=child()
c1.pdisplay()
c1.cdisplay()
