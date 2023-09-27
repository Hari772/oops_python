class father:
    def fdisplay(self):
        print("Father")
class mother:
    def mdisplay(self):
        print("Mother")
class child(father,mother):
    def cdisplay(self):
        print("Child")
c1=child()
c1.mdisplay()
c1.cdisplay()
c1.fdisplay()
