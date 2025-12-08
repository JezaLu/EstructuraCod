# 1.-busqueda de listas (in, index, bucles, busquedas con comprension)
num=[1,2,3,4,5,6,7,8,9,10]
print(3 in num)  #devuelve True si el valor esta en la lista
print(0 in num)  #devuelve False si el valor no esta en la lista

numA=["rosa","azul","verde","amarillo"]
print("azul" in numA)  #devuelve True si el valor esta en la lista
print("negro" in numA)  #devuelve False si el valor no esta en la lista

#index
lista1=[10,20,30,40,50]
print(lista1.index(30))  #devuelve la posicion del valor en la lista
print(lista1.index(10))  #devuelve la posicion del valor en la lista

lista2=["manzana","banana","cereza","durazno"]
print(lista2.index("cereza"))

lista3=[4,5,"ojo","luz",7]
print(lista3.index("ojo"))


#bucles
nums=[1,2,3,4,5]
for n in nums:
    if n==5:
        print("numero encontrado:")
 #   else:     se le puede agregar un else para que muestre un mensaje si no encuentra el numero pero no es necesario en este metodo
       # print("numero no encontrado:")
       # break

nums=[1,2,3,"rosi",5,"gato"]  #se combina con diferentes tipos de datos
for n in nums:
    if n=="gato":
        print("numero encontrado:")

#busqueda con comprension
lista0=[2,4,6,8,9,5]
posicion=[i for i, x in enumerate(lista0) if x==4]  #devuelve la posicion del valor que cumple la condicion si queremos la posicion de todos los valore agregamos la condicional de x>o y mostrara todos las posciciones de los valores que cumplen la condicion
print("oye esta es la posicion del numero que buscas: ",posicion)  #devuelve la posicion del valor que cumple la condicion

listaA0=[1,"arbol",3,"flor",5]  #ahora con diferentes tipos de datos
posicionA=[i for i, x in enumerate(listaA0) if x= "flor"]
print("oye esta es la posicion del valor que buscas: ",posicionA)  #devuelve la posicion del valor que cumple la condicion

# 2.- busquedas de cadenas
#1.busqueda de cadenas
#.find()=buscar mediante posiciones el ino de una palabra
s="python es el mejor en programacion xd"
print(s.find("xd"))
#con input
n="python es el mejor"
buscar=input("Ingresa la palabra que quieres encontrar conforme a la oración: ")
print(n)#para imprimir primero toda la oracion
print(n.find(buscar))#buscar mediante consola la palabra

#con def
def find():
    n="python es el mejor"
    buscar=input("Ingresa la palabra que quieres encontrar conforme a la oración: ")
    print(n)#para imprimir primero toda la oracion
    print(n.find(buscar))#buscar mediante consola la palabra
find()

#.index()=es lo mismo que el find pero si no existe una palabra marca error(desde antes de iniciar la letra de la palabra)
l="hola mundo"
print(l.index("mundo"))

#con input
m="hola mundo"
buscar1=input("Ingressa la palabra que quieres encontrar")
print(m.index(buscar1))

#con def
def index():
    m="hola mundo"
    buscar1=input("Ingressa la palabra que quieres encontrar")
    print(m.index(buscar1))
index()

#.startswith // .endswith=parta poder separar palabras y buscar mediante letras si está en la oracion
"programar".startswith("pro")#depende de la version de python para poder imprimir

m1="programar es estresante"
print(m1.startswith("pro"))#toma las primeras letras de la oración

m2="programar es relajante"
print(m2.endswith(("te")))#toma las ultimas letras de la oracion

m3="programar es mi pasion"
buscar3=input("Ingresa las primeras letras de la oracion: ")
print(m3.startswith(buscar3))

m4="programar es mi pasion"
buscar4=input("Ingresa las ultimas letras de la oracion: ")
print(m4.endswith(buscar4))

#2.- busqueda por diccionarios
    #busqueda por claves
d= {"a":1, "b":2}
print("a" in d)#imprime true porque está en la lista
print(d.get("b"))#.get es un metodo para determinar los valores de las claves

#3.- busqueda por valores
d1={"x":10, "y":20}
buscar5=[k for k, v in d1.items() if v == 20]
print(buscar5)#imprime y que es el valor de 20

#4.- metodo de busqueda avanzada
    #busqueda binaria(bissect)
import bisect
lista1=[1,2,3,4,5,6,7]
pos=bisect.bisect_left(lista1, 7) #indica la posicion del numero
print(pos)

#con def
import bisect
def bs():
    lista1=[1,2,3,4,5,6,7]
    pos=bisect.bisect_left(lista1, 7) #indica la posicion del numero
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
