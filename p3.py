class MaquinaTuring:
  def __init__(self,estadoInicial,estadosFinales,funcionesTransicion,contenidoCinta,posInicial):
    self.estadoInicial=estadoInicial #estado inicial de la maquina
    self.estadosFinales=estadosFinales #lista con estados finales
    self.funcionesTransicion=funcionesTransicion #lista con funciones de transicion del tipo (estado,contPila -> estado,escribirpila,movimiento)
    self.cinta=Cinta(contenidoCinta,posInicial)
    self.estadoActual=estadoInicial #estado en un momento concreto
    self.trace=True #imprimir estado de la cinta a cada paso 
    self.trace2=False

  def printState(self):
    izquierda,derecha=self.cinta.getPilas()
    #falta reverse de izquierda
    izquierda =self.reverse(izquierda)
    print izquierda+"#"+self.estadoActual+"#"+derecha

  def reverse(self,text):
    if len(text) <= 1:
      return text
    return self.reverse(text[1:]) + text[0]

  def run(self):
    while(self.estadoActual not in self.estadosFinales):
      self.siguienteEstado()
      if self.trace:
        self.printState()

  def siguienteEstado(self):
    cinta=self.cinta.getActual()
    for transicion in self.funcionesTransicion:
      if transicion.iz[0] == self.estadoActual and cinta==transicion.iz[1]:
        aplicar=transicion.der
        break
    ## usar copy.deepcopy para copiar las maquinas de turing
    if self.trace2:
        print "apply --> "+self.estadoActual+","+cinta+"-> "+aplicar[0],aplicar[1],aplicar[2]
    self.estadoActual=aplicar[0]
    self.cinta.insertarCinta(aplicar[1],aplicar[2])
    

  
class Cinta:
  def __init__(self,contenidoCinta,posCabeza):
    self.izquierda=contenidoCinta[:posCabeza]
    self.derecha=contenidoCinta[posCabeza:]

  def insertarCinta(self,simbolo,movimiento):
    self.derecha=simbolo+self.derecha[1:]
    if movimiento=="R":
      self.moverDerecha()
    if movimiento=="L":
      self.moverIzquierda()
    if movimiento=="N":
      pass
  def reverse(self,text):
    if len(text) <= 1:
      return text
    return self.reverse(text[1:]) + text[0]

  def getPilas(self):
    return self.izquierda,self.derecha

  def moverDerecha(self):
    self.izquierda=self.derecha[0]+self.izquierda
    self.derecha=self.derecha[1:]

  def moverIzquierda(self):
    self.derecha=self.izquierda[0]+self.derecha
    self.izquierda=self.izquierda[1:]

  def getActual(self):
    if len(self.derecha)==0:
      return "_"
    return self.derecha[0]
