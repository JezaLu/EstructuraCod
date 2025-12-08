#examen unidad III
#1.- elevacion al cuadrado
def cuadrado(elevado):
    elevado= float(input("Ingresa un numero: "))
    cuadrado = elevado ** 2
    print("El numero elevado al cuadrado es: ", cuadrado)

#2.- elevacion al cubo
def cubo(elevado):
    elevado= float (input("Ingrese un numero: "))
    cubo = elevado ** 3
    print("El numero elevado al cubo es: ", cubo)

#3.- cuenta rgresiva
def cuenta_regresiva(n):
    n = int(input("¿Desde donde inicia el conteo?"))
    for i in range (n, 0, -1):
        print(i)
    print("¡GO!")
    
#4.- factorial de un numero decimal
def factorial_decimal(x):
    x = float(input("Ingrese un numero decimal: "))
    if x==0 or x==1: 
        return 1
    return x*factorial_decimal(x-1)


#5.- palindromos
def palindromo(palabra):
    palabra = int(input ("Ingrese una palabra:"))
    if len(palabra)<=1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return palindromo(palabra[1:-1])

#6.- sumar 4 numeros
def suma_promedio(m):
    m = []
    for i in range(1,4):
        m = float(input(f"Ingrese el numero {i}: "))
        m.append(m)

        suma = sum(m)
        promedio = suma /4
    print("La suma es: ", suma)
    print("El promedio es: ", promedio)

#menu
def menu():
    while True:
        print("Menu del codigo: ")
        print("1.- Elevacion al cuadrado")
        print("2.- Elevacion al cubo")
        print("3.- Cuenta regresiva")
        print("4.- Factorial de un numero decimal")
        print("5.- Palindromo")
        print("6.- Sumar 4 numeros")
        print("7.- Salirse del programa")

        opcion=input("Selecciona una opcion:(1-7)")
        
        if opcion=="1":
            num = float(input("Ingresa un numero: "))
            print("Resultado: ", num ** 2)

        elif opcion =="2":
            num = float(input("Ingrese un numero: ", num ** 3))
            print("El resultadp es: ", num ** 3)

        elif opcion == "3":
            n = int (input("¿Desde donde quiere iniciar el conteo?"))
            print(n)

        elif opcion == "4":
            x = int (input("Ingrese un numero decimal"))
            print(x)

        elif opcion == "5":
            palabra = int( input ("Ingresa una palabra"))
            print (palindromo(palabra))
        
        elif opcion == "6":
            numeros = int (input("Ingrese los 4 numeros a sumar: "))
            print(suma_promedio(numeros))
        
        elif opcion == "7":
            print("Salirse del programa")
            break
        else:
            print("Ingresaste un dato inválido")

if __name__ == "__main__":
    menu()