#ACTIVIDAD 3
#meter el input al programa de anchura y profundidad, crear un menu para seleccionar

class grafo:
    def __init__(self):
        self.grafo = {}

def menu(g = grafo()):

    while True:
        print("Menu del codigo: ")
        print("1. Agregar vertices")
        print("2. Agregar aristas")
        print("3. Mostrar grafo")
        print("4. Recorrido por anchura")
        print("5. Recorrido por profundidad")
        print("6. Salir del programa")

        opcion=input("Selecciona una opcion:(1-6)")

        if opcion== "1":
        
            n= int(input("Agrega el numero de vertices"))
            for i in range (n):
                vertice= int(input(f"Ingresa el numero de vertices, #{i+1}:"))
                g.agregar_vertice(vertice) #agrega vertices directamente

        if opcion == "2":
            m= int(input("Agrega el numero de aristas"))
            for i in range (m):
                print(f"Aristas, #{i+1}:")
                v1=input("Agrega la primera arista")
                v2=input("Agrega la segunda arista")
                g.agregar_arista(v1,v2)

        if opcion == "3":
            print("Recorrido por anchura")
            g.bfs()

        if opcion == "4":
            print("Recorrido por profundidad")
            g.dfs()

        if opcion == "5":
            print("Recorrido por anchura")
            g.bfs()

        elif opcion == "6":
            print("Salirse del programa")
            break
        else:
            print("Ingresaste un dato inválido")

if __name__ == "__main__":
  menu()

def agregar_vertice(self,vertice):
    if vertice not in self.grafo:
        self.grafo[vertice] = []

    else:
        print("El grafo ya existe")
#unir login con formulario, y formulario con calculadora y un boton de cerrar sesión
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

#recorridos por anchura y produndidad
    def bfs(self, inicio): #bfs representa directamente anchura
        visitados= set()
        cola=[inicio]

        while cola:
            vertice=cola.pop(0)
            if vertice not in visitados:
                print(vertice, end=" ")
                visitados.add(vertice) #add: para agregar la variable vertice a visitados
                for vec in self.grafo[vertice]:
                    cola.append(vec)

    def dfs(self, inicio, visitados=None): #dfs representa produndidad
        if visitados is None:
            visitados=[]
            print(inicio, end=" ")
            visitados.append(inicio)
            for vec in self.grafo[inicio]:
                if vec not in visitados:
                    self.dfs(vec,visitados)
