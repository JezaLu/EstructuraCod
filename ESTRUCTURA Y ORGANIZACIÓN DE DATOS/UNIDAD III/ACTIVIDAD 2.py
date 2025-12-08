#altura de un arbol, actividad 2: crear un metodo que tendrá input para agregar desde consola parte, 
# deberá tener una igualación, un print y un menu desde consola
def altura(nodo):
    if nodo is None:
        return 0
    return 1 + max(altura (nodo.izquierda),altura(nodo.derecha))

def crear_arbol():
    valor=int(input("Ingresa los valores separados por espacios:"))
    if valor=="":
        return None
    
    nodo=nodo(valor)
    print(f"nodo izquierda de {valor}---")
    nodo.izquierda=crear_arbol()
    print(f"nodo derecha de {valor}---")
    nodo.derecha=crear_arbol()

    return nodo

def calcular_altura():
    print("crear arbol binario")
    raiz=crear_arbol()
    print("Calcular altura")
    a=altura(raiz)
    print(f"La altura del arbol es: {a}")

def menu():
    while True:
        print("Menu del codigo: ")
        print("1. Crear y calcular la altura de un arbol")
        print("2. Salir del programa")

        opcion=input("Selecciona una opcion:(1-2)")
        
        if opcion=="1":
            calcular_altura()

        elif opcion == "2":
            print("Salirse del programa")
            break
        else:
            print("Ingresaste un dato inválido")
            
if __name__ == "__main__":
 menu()
