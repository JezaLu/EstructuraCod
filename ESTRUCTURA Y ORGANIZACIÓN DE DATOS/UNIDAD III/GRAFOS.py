class grafo:
    def __init__(self):
        self.grafo = {} #un diccionario se representa mediante llaves {}

    def agregar_vertice(self,vertice):
        if vertice not in self.grafo:
            self.grafo[vertice] = []

        else:
            print("El grafo ya existe")

    def agregar_arista(self, v1, v2):
        if v1 in self.grafo and v2 in self.grafo:
            self.grafo[v1].append(v2)
            self.grafo[v2].append(v1)
        else:
            print("El vertice no existe")
    
    def mostrar(self):
        for vertice in self.grafo:
            print(vertice, "->", self.grafo[vertice])

if __name__ == "__main__":
    g = grafo()

    n= int(input("Agrega el numero de vertices"))
    for i in range (n):
        vertice= int(input(f"Ingresa el numero de vertices, #{i+1}:"))
        g.agregar_vertice(vertice) #agrega vertices directamente
        
    #agregar aristas
    m= int(input("Agrega el numero de aristas"))
    for i in range (m):
        print(f"Aristas, #{i+1}:")
        v1=input("Agrega la primera arista")
        v2=input("Agrega la segunda arista")
        g.agregar_arista(v1,v2)

        g.mostrar()
        #meter el input al programa de anchura y profundidad, crear un menu para seleccionar
        