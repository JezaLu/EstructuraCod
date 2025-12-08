#listas
#in
def listain():#----------------------COMPLETADO-------------------
    n=[1,2,3,4,5]
    print(n)
    n1=int(input("Ingrese el numero quequieres buscar"))
    print(n1 in n)
listain()

#index
def listaindex():#------------------COMPLETADO---------------------
    m=[2,4,6,8]
    print(m)  #devuelve la posicion del valor en la lista  
    l1=int(input("Ingrese el numero a buscar"))
    print(l1 in m)  #devuelve la posicion del valor en la lista
listaindex()

#1.busqueda de cadenas
def find():#--------------------COMPLETADO-------------------------------
    n="python es el mejor"
    print(n)#para imprimir primero toda la oracion
    buscar=input("Ingresa la palabra que quieres encontrar conforme a la oración: ")
    print(n.find(buscar))#buscar mediante consola la palabra
find()

#.index()=es lo mismo que el find pero si no existe una palabra marca error(desde antes de iniciar la letra de la palabra)
def index():#---------------------------COMPLETADO-----------------------------
    m="hola mundo"
    print(m)
    buscar1=input("Ingresa la palabra que quieres encontrar")
    print(m.index(buscar1))
index()

#startswith y endswith
def start():#------------------------COMPLETADO-------------------------
    j="El monte Everest"
    print(j)
    buscar5=input("Ingrese las primeras letras de la oracion")
    print(j.startswith(buscar5))
start()

def end():#---------------------COMPLETADO----------------------------
    k="El cerro San Vicente"
    print(k)
    buscar6=input("Ingrese las ultimas letras de la oracion")
    print(k.endswith(buscar6))
end()

#metodo de busqueda avanzada
#con def
#busqueda binaria(bissect)
import bisect #------------------COMPLETADO-----------
def bs():
    lista1=[1,2,3,4,5,6,7]
    print(lista1)
    k1=int(input("Ingrese el valor que desea buscar"))
    pos=bisect.bisect_left(lista1, k1) #indica la posicion del numero
    print(pos)
bs()
