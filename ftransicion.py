class Ftransicion:
    def __init__(self, izquierda,derecha):
        self.iz = izquierda 
        self.der = derecha
    def to_string(self):
        print self.iz+" -> "+self.der
    def __str__(self):
        return self.iz+" -> "+self.der
    def __repr__(self):
        return self.iz+" -> "+self.der
    def right(self):
        return str(self.der)
    def left(self):
        return self.iz

