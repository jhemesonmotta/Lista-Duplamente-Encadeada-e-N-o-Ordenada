class No():
    def __init__ (self,anterior = None, valor = None, proximo = None):
        self.info = valor
        self.prox = proximo
        self.ant = anterior

class Ldde():
    def __init__ (self):
        self.prim = None
        self.ult = None
        self.quant = 0

    def inserirInicio(self,valor):
        if self.quant == 0:
            self.prim = self.ult = No(None, valor, None)
        else:
            self.prim = No(None, valor, self.prim)
            self.prim.prox.ant = self.prim
        self.quant+=1
        """if self.quant == 0:
            self.prim = self.ult = No (valor,None)
        else:
            self.prim = No(valor, self.prim)
        self.quant += 1"""

    def inserirFim(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(None, valor, None)
        else:
            self.ult = No(self.ult, valor, None)
            self.ult.ant.prox = self.ult
        self.quant += 1

    def removerInicio(self):


    def imprimir (self):
        aux = self.prim
        while aux != None:
            print(aux.info)
            aux = aux.prox

    def inserirFim (self,valor):
        if self.quant == 0:
            self.prim = self.ult=No(valor,None)
        else:
            self.ult.prox = self.ult=No(valor,None)
        self.quant += 1

    def removerInicio (self):
        if self.quant==1:
            self.prim=self.ult=None
        else:
            self.prim=self.prim.prox
            self.prim.ant=None
        self.quant-=1
        """if self.quant == 1:
            self.print = self.ult = None
        else:
            self.prim = self.prim.prox
        self.quant -= 1"""

    def estaVazia(self):
        returnself.quant=0

    def getPrim(self):
        return self.prim.info

    def removerFim(self):
        if self.quant==1:
            self.prim=self.ult=None
        else:
            self.ult=self.ult.ant
            self.ult.prox=None
        self.quant-=1
        """if self.quant==1:
            self.prim=self.ult=None
        else:
            aux=self.prim
            while aux.prox != self.ult:
                aux=aux.prox
            self.ult=aux
            self.ult.prox=None
        self.quant-=1"""

    def getUlt(self):
        return self.ult.info