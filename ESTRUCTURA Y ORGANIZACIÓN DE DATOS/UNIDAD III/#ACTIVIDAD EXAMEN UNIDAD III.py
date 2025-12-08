#ACTIVIDAD EXAMEN
#metodo de elevado al cuadrado
#elevado al cubo
#que me diga si es mayor o menor de edad
#en menu con input
def cuadrado(base, elevado): #
    if elevado==0:
        return 1
    return base * cuadrado(base,elevado -1)

#elevacion al cubo de cualquier numero
def cubo(base, elevado): #
    if elevado==0:
        return 1
    return base * cubo(base,elevado -1)

def edad(x):
    if x >= 18:
        print("Eres mayor de edad")
    else:
        print("Eres menor de edad")

def menu():
    while True:
        print("MENU DEL PROGRAMA")
        print("1. Elevar un numero al cuadrado")
        print("2. Elevar un numero al cubo")
        print("3. Mayor o menor de edad")
        print("4. Salir")
    
        opcion = input("Selecciona una opción(1 al 7): ")

        if opcion == "1":
            base=int(input("ingresa la base: "))
            elevado=int(2)
            print("el resultado es:", cuadrado(base,elevado))

        elif opcion == "2":
            base=int(input("ingresa la base: "))
            elevado=int(3)
            print("el resultado es:", cubo(base,elevado))

        elif opcion =="3":
            x = int(input("Ingrese su edad: "))
            edad(x)

        elif opcion == "4":
            print("Salirse del programa")
            break
        else:
            print("Ingresaste un dato inválido")

if __name__ == "__main__":
 menu()