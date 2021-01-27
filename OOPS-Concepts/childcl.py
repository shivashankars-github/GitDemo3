
from OOPS_demo import Caluclator


class childexample(Caluclator):
    num2 = 200

    def __init__(self):
        Caluclator.__init__(self,2,10)

    def getcompletedata(self):
        return self.num2 + self.num + self.summatino()


obj2 = childexample()

print(obj2.getcompletedata())
