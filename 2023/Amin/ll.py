
class Number:  # blueprint, pattern, type
    _x = 0  # class attr
    
    def __init__(self, num):
        self.num = num  # instance attr
        self.msg = "hello world"
        #print("Before chanege.")
        #print("Number: ", Number.x)
        #print("Self.x: ", self.x)
        #print('-----------')
        #print("After change.")
        self._x = 200
        #Number.x = 10
        #print("Number: ", Number.x)
        #print("Self.x: ", self.x)
    
    # instance (object) method
    def iseven(self):
        if self.isint():
            return "even" if self.num % 2 == 0 else "odd"
        
        return "Error: x must be int."

    # instance (object) method
    @classmethod
    def isint(cls, value=None):
        if value is not None:
            if isinstance(value, int):
                return True
            return False
        
##        if isinstance(self.num, int):
##            return True
##        return False
    @staticmethod
    def hello():
        return "hello world"

def main():
    n = Number(15)

    print(n.hello())
    print(Number.hello())


class Runner:
    def start(self):
        pass

    @staticmethod
    def execuate():
        runner = Runner()
        runner.start()



def execuate():
        runner = Runner()
        runner.start()

execuate()



    
class Rectangle:
    
    def area(w, h):
        return w * h

    def priemeter(w, h):
        return 2 + (w * h)

    

main()
