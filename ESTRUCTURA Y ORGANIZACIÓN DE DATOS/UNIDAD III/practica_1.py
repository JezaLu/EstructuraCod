#1 factorial de un numero
def factorial(x):
    if x==0 or x==1: 
        return 1
    return x*factorial(x-1)
print(factorial(10))

#2.- sumna de una lista
def suma_lista(lista):
    if not lista:
        return 0
    return lista[0] + suma_lista(lista[1:])
print(suma_lista([1,2,3,4,5]))

#3.- resta de una lista
def resta(lista):
   if not lista:
      return 0
   return lista[0] - resta(lista[1:])
print(resta ([10,20]))

#4-. invertir una cadena de texto
def invertir_cadena(cadena):
    if len(cadena)==0: 
        return "" 
    return cadena[-1]+invertir_cadena(cadena[:-1]) 
print(invertir_cadena("")) 

#5.- potencia de un numero
def potencia(base,elevado):
    if elevado==0:
        return 1
    return base * potencia(base, elevado -1)
print (potencia(5,3))

#6.- serie de fibonacci
def fibonacci(x):
    if x<=1:
        return x
    return fibonacci(x-1) + fibonacci (x-2)
print(fibonacci(6))

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
piramide(10)

#9.- contar elementos en una lista(saber cuantos elementos hay en una lista)
def contar(lista):
    if not lista:
        return 0
    else:
        return 1 + contar(lista[1:])#1: para definir que hay un consiguiente de la lista
print(contar([1,2,3,4,5]))

#10.- maximo comun divisor
def comun_divisor(a,b):
    if b==0:
        return a
    else:
        return comun_divisor(b, a % b)#% es como la division de los elementos
print(comun_divisor(48,18))

#11.- palabras palindromos
def palindromo(palabra):
    if len(palabra)<=1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return palindromo(palabra[1:-1])
print(palindromo("ojo"))
print(palindromo("python"))
print(palindromo("reconocer"))

#12.- espiral de llamadas
def espiral(x):
    if x==0:
        return
    print(f"Llamada numero {x}")
    espiral(x-1)
espiral(5)

#suma de digitos
def suma_digitos(n):
    if n<10:
        return n
    else:
        return n%10+suma_digitos(n//10)
print(suma_digitos(12345))

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
            print(factorial(10))

        elif opcion =="2":
            print(suma_lista([1,2,3,4,5]))

        elif opcion == "3":
            print(resta ([10,20]))
        
        elif opcion == "4":
            print(invertir_cadena("Hospital")) 

        elif opcion == "5":
            print (potencia(5,3))
        
        elif opcion == "6":
            print(fibonacci(6))
        
        elif opcion == "7":
            print(cuenta_regresiva(5))
        
        elif opcion == "8":
            piramide(10)

        elif opcion == "9":
            print(contar([1,2,3,4,5]))

        elif opcion == "10":
            print(comun_divisor(48,18))

        elif opcion == "11":
            print(palindromo("ojo"))
            print(palindromo("python"))
            print(palindromo("reconocer"))

        elif opcion == "12":
            espiral(5)
        
        elif opcion == "13":
            print(suma_digitos(12345))

        elif opcion == "14":
            print("Salirse del programa")
            break
        else:
            print("Ingresaste un dato inválido")

if __name__ == "__main__":
    menu()