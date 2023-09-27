class father:
    def transport(self):
        print("Cycle")
class son(father):
    def transport(self):
        print("Bike")

obj=son()
obj.transport()
