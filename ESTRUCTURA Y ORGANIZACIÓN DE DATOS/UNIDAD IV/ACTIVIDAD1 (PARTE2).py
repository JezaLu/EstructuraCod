lista=input("Ingresa numeros separados por espacios")
lista=list(map(int, lista.split()))

#metodo burbuja
def burbuja(lista):
    for x in range (len(lista)):
        for i in range (len(lista)-1):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
    return lista

#metodo seleccion
def seleccion(lista):
    for i in range(len(lista)):
        menor=i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[menor]:
                menor=j
                lista[i], lista[menor]= lista[menor], lista[i]
    return lista

#metodo inserción
def insercion(lista):
    for i in range (1, len(lista)):
        valor = lista[i]
        j=i - 1
        while j >= 0 and lista[j]>valor:
            lista[j+1] = lista[j]
            j -= 1
            lista[j+1] = valor
    return lista

#metodo mezcla
def mezcla(lista):
    if len(lista) <= 1:
        return lista
    
    medio= len(lista)//2
    izquierda = mezcla(lista[:medio])
    derecha= mezcla(lista[medio:])

    resultado=[]
    while izquierda and derecha:
        if izquierda[0]< derecha[0]:
            resultado.append(izquierda.pop(0))
        else:
            resultado.append(derecha.pop(0))
    return resultado + izquierda + derecha

#metodo rapido de ordenamiento
def rapido (lista):
    if len (lista)<=1:
        return lista
    pivote = lista[0]
    menores = [x for x in lista[1:] if x < pivote]
    mayores = [x for x in lista[1:] if x >= pivote]
    return rapido(menores) + [pivote] + rapido(mayores)

def menu():
    while True:
        print("Menu del codigo: ")
        print("1. Método burbuja")
        print("2. Método selección")
        print("3. Método inserción")
        print("4. Método mezcla")
        print("5. Método rápido de ordenamiento")
        print("6. Salir")

        opcion=input("Selecciona una opcion:(1-6)")
        
        if opcion=="1":
            print("La lista ordenada por el metodo burbuja es: ", burbuja(lista))

        elif opcion=="2":
            print("La lista ordenada por el metodo seleccion es: ", seleccion(lista))

        elif opcion=="3":
            print("La lista ordenada por el metodo insercion es: ", insercion(lista))

        elif opcion=="4":
            print("La lista ordenada por el metodo mezcla es: ", mezcla(lista))
 
        elif opcion=="5":
            print("La lista ordenada por el metodo rapido de ordenamiento es: ", rapido(lista))

        elif opcion == "6":
            print("Saliste del programa")
            break
        else:
            print("Ingresaste un dato inválido")
            
if __name__ == "__main__":
 menu()
