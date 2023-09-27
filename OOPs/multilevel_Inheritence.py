class grand_parent:
    def gdisplay(self):
        print("grand parent")

class parent(grand_parent):
    def pdisplay(self):
        print("Parent")
class child(parent):
    def cdisplay(self):
        print("child")
c1=child()
p1=parent()
c1.cdisplay()
c1.pdisplay()
c1.gdisplay()
p1.pdisplay()
p1.gdisplay()
