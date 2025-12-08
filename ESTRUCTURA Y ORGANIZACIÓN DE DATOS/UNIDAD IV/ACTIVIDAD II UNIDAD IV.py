#listas-convertir cel int con input y con def, index con input y def, bucle con input y con def, comprension con input y con def
#cadenas=find con input y def, index, starwith, endswith
#metodos de busqueda avanzada: binaria a input y def, grafos a input
#con menú

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

#bucles
def bucles(): #-----------------------------completar------------------
    nums=[1,2,3,4,5]
    print(nums)
    for n in nums:
        if n==nums:
            print("numero encontrado:")

#busqueda con comprension
def comprension(): #-------------------------completar------------------
    lista0=[2,4,6,8,9,5]
    print(lista0)
    posicion=int(input("Ingrese el valor que quiere buscar"))
    posicion=[i for i, x in enumerate(lista0) if x==4]  #devuelve la posicion del valor que cumple la condicion si queremos la posicion de todos los valore agregamos la condicional de x>o y mostrara todos las posciciones de los valores que cumplen la condicion
    print("oye esta es la posicion del numero que buscas: ",posicion)  #devuelve la posicion del valor que cumple la condicion
comprension()

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

#2.- busqueda por diccionarios
    #busqueda por claves
def claves():#-----------------completar--------------
    d= {"a":1, "b":2, "c":3, "d":4}
    print(d)
    d1=int(input("Ingrese el valor a buscar"))
    print(d1 in d)#imprime true porque está en la lista
claves()

#3.- busqueda por valores
def valores():#-----------------completar---------------
    c1={"x":10, "y":20, "z":30, "g":40}
    print(c1)
    c1=input("Ingrese el valor que desea buscar")
    buscar5=[k for k, v in c1.items() if v == c1]
    print(buscar5)#imprime y que es el valor de 20
valores()

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

#6.-grafos y arboles
grafo={
    "A":["B", ""],
    "B":["D"],
    "C":[],
    "D":[]
}
def dfs(nodo):
    print(nodo)
    for vecino in grafo[nodo]:
        dfs(vecino)
dfs("A")
