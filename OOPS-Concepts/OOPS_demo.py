class Caluclator:
    num = 100


    def __init__(self,a,b):
        self.firstnum = a
        self.secnum = b
        print("parent constructor")


    def getdata(self):
        print("I am now executing as method in class")

    def summatino(self):
        return self.firstnum + self.secnum + Caluclator.num






