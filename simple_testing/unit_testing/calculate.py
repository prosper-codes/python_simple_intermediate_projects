
class Calculate:

    def add (self,a,b):
        return a+b

    def subt(self,a,b):
        return a-b

    def mult(self,a,b):
        return a*b

    def div(self,a,b):
        if b == 0:
            raise ValueError("cannot divide by zero")
        
        return a/b
        
            


    