#ordenamiento con input
#list forma de ordenar todos los valores
lista=input("Ingresa numeros separados por espacios")
lista=list(map(int, lista.split()))

for x in range (len(lista)):
    for i in range (len(lista)-1):
        if lista[i] > lista[i + 1]:
            lista[i], lista[i+1] = lista[i+1], lista[i]
print("La lista ordenada es: ", lista)

#metodo seleccion
#lista1=[5,2,8,7]
def seleccion(lista1):
    for i in range(len(lista1)):
        menor=i
        for j in range(i+1, len(lista1)):
            if lista1[j] < lista1[menor]:
                menor=j
                lista1[i], lista1[menor]= lista1[menor], lista1[i]
    return lista1

#metodo inserción(va a mover todos los numeros hacia atrás hasta que quede ordenado)
#lista2=[3,1,2,5,6,9]
def insercion(lista2):
    for i in range (1, len(lista2)):
        valor = lista2[i]
        j=i - 1
        while j >= 0 and lista2[j]>valor:
            lista2[j+1] = lista2[j]
            j -= 1
            lista2[j+1] = valor
    return lista2

#metodo mezcla (divide todos los valores entre sí y al final hace el ordenamiento)
def mezcla(lista3):
    if len(lista3) <= 1:
        return lista3
    
    medio= len(lista3)//2
    izquierda = mezcla(lista3[:medio])
    derecha= mezcla(lista3[medio:])

    resultado=[]
    while izquierda and derecha:
        if izquierda[0]< derecha[0]:
            resultado.append(izquierda.pop(0))
        else:
            resultado.append(derecha.pop(0))
    return resultado + izquierda + derecha

#rapido de ordenamiento(sirve para cualquier tipo de dato)
def rapido (lista4):
    if len (lista4)<=1:
        return lista4
    pivote = lista4[0]
    menores = [x for x in lista4[1:] if x < pivote]
    mayores = [x for x in lista4[1:] if x >= pivote]
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
            print(burbuja([3,5,2,8]))
        elif opcion=="2":
            print(seleccion([5,2,8,7]))

        elif opcion=="3":
            print(insercion([3,1,2]))

        elif opcion=="4":
            print(mezcla([5,7,2,4]))

        elif opcion=="5":
            print(rapido([4,2,7,9,1]))

        elif opcion == "6":
            print("Saliste del programa")
            break
        else:
            print("Ingresaste un dato inválido")
            
if __name__ == "__main__":
 menu()
