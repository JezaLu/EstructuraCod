#1 factorial de un numero
def factorial(x):
    if x==0 or x==1: 
        return 1
    return x*factorial(x-1)

#2.- sumna de una lista
def suma_lista(lista):
    if not lista:
        return 0
    return lista[0] + suma_lista(lista[1:])

#3.- resta de una lista
def resta(lista1):
   if not lista1:
      return 0
   return lista1[0] - resta(lista1[1:])


#4-. invertir una cadena de texto
def invertir_cadena(cadena):
    if len(cadena)==0: 
        return "" 
    return cadena[-1]+invertir_cadena(cadena[:-1]) 

#5.- potencia de un numero
def potencia(base,elevado):
    if elevado==0:
        return 1
    return base * potencia(base, elevado -1)

#6.- serie de fibonacci
def fibonacci(x):
    if x<=1:
        return x
    return fibonacci(x-1) + fibonacci (x-2)

#7.- cuenta regresiva
def cuenta_regresiva(n):
    if n<0:
        print("Go!")
        return
    print(n)
    cuenta_regresiva(n-1)

#23/10/2025
#8.- pirámide con *
def piramide(n):
    if n ==0: #se iguala poque no tieneu un valor en específico
        return
    piramide(n-1) #n-1 porque se reduce menos uno
    print("*"*n)

#9.- contar elementos en una lista(saber cuantos elementos hay en una lista)
def contar(lista):
    if not lista:
        return 0
    else:
        return 1 + contar(lista[1:])#1: para definir que hay un consiguiente de la lista

#10.- maximo comun divisor
def comun_divisor(a,b):
    if b==0:
        return a
    else:
        return comun_divisor(b, a % b)#% es como la division de los elementos

#11.- palabras palindromos
def palindromo(palabra):
    if len(palabra)<=1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return palindromo(palabra[1:-1])

#12.- espiral de llamadas
def espiral(x):
    if x==0:
        return
    print(f"Llamada numero {x}")
    espiral(x-1)

#suma de digitos
def suma_digitos(n):
    if n<10:
        return n
    else:
        return n%10+suma_digitos(n//10)

def menu():
    while True:
        print("Menu del codigo: ")
        print("1. Factorial de un numero")
        print("2. Suma de una lista")
        print("3. Resta de 2 numeros")
        print("4. Invertir una cadena de texto")
        print("5. Potencia de un numero")
        print("6. Serie de fibonacci")
        print("7. Cuenta regresiva")
        print("8. Pirámide con *")
        print("9. Contar elementos de una lista")
        print("10. Maximo comun divisor")
        print("11. Palabras palindromos")
        print("12. Espiral de llamadas")
        print("13. Suma de digitos")
        print("14. Salir de programas")

        opcion=input("Selecciona una opcion:(1-8)")
        
        if opcion=="1":
            x=int(input("Ingresa un numero entero"))
            print(factorial(x))

        elif opcion =="2":
            lista=list(map(int,input("Ingresa numeros separados por un espacio").split))
            print ("la suma es:", suma_lista(lista))
    
        elif opcion == "3":
            lista1=list(map(int,input("Ingresa dos numeros separados por un espacio").split))
            print("La resta es", resta(lista1))
        
        elif opcion == "4":
            invertir_cadena=input("Ingresa cadena de texto")
            print("La cadena invertida es", invertir_cadena(invertir_cadena))
            
        elif opcion == "5":
            base=(input("Ingresa la base"))
            elevado=(input("Ingresa el exponente"))
            print("El resultado es: ",potencia(base,elevado))
        
        elif opcion == "6":
            n=int(input("Ingresa un numero"))
            print("El resultado es: ",fibonacci(n))
        
        elif opcion == "7":
            n=int(input("Ingresa desde que numero quieres contar hacia atrás"))
            cuenta_regresiva(n)
        
        elif opcion == "8":
            n=int(input("Ingresa un numero base de la prirámide"))
            piramide(n)

        elif opcion == "9":
            lista=list(map(int,input("Ingresa numeros separados por espacio".split())))
            print(contar([1,2,3,4,5]))

        elif opcion == "10":
            a=int(input("Ingresa un numero entero"))
            b=int(input("Ingresa otro numero"))
            print(comun_divisor(a,b))

        elif opcion == "11":
            palabra=input("Ingresa una palabra")
            print(palindromo(palabra))

        elif opcion == "12":
            x=int(input("Ingresa el numero de llamadas"))
            print(espiral(x))
        
        elif opcion == "13":
            n=int(input("Ingresa un numero de varios digitos"))
            print(suma_digitos(n))

        elif opcion == "14":
            print("Salirse del programa")
            break
        else:
            print("Ingresaste un dato inválido")

if __name__ == "__main__":
  menu()