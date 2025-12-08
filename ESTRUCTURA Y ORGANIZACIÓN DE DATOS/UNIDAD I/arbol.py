class Nodo:
    def __init__(self,valor):
        self.valor=valor
        self.izquierda=None
        self.derecha=None

raiz=Nodo("Pedro")
raiz.izquierda=Nodo("Maria")
raiz.derecha=Nodo("Juan")

print("Papá",raiz.valor)
print("Hija mayor",raiz.izquierda.valor)
print("Hijo menor",raiz.derecha.valor)