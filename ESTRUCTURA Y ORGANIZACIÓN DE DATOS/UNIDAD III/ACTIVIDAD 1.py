def suma(x, y):
    if y==0:
        return x
    if y > 0:
        return x + y
                                    
def resta(x, y):
    if y==0:
        return x
    if y > 0:
        return x - y

def multiplicacion(x, y):
   if y==0:
        return 0
   if y > 0:
        return x * y
   
def division(x, y):
   if y==0:
        return "Error, no se puede dividir entre cero"
   return x / y

def menu():
    while True:
        print("Menu del codigo: ")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")
        
        opcion=input("Selecciona una opcion:(1-5)")
        
        if opcion=="1":
            x=int(input("Ingresa un numero entero"))
            y=int(input("Ingresa un segundo numero"))
            print(suma(x,y))

        elif opcion =="2":
            x=int(input("Ingresa un numero: "))
            y=int(input("Ingresa el segundo numero a restar"))
            print(resta(x,y))
    
        elif opcion == "3":
            x=int(input("Ingresa un numero: "))
            y=int(input("Ingresa el numero a multiplicar"))
            print(multiplicacion(x,y))
        
        elif opcion == "4":
            x=int(input("Ingresa el divisor"))
            y=int(input("Ingresa el dividendo"))
            print(division(x,y))

        elif opcion == "5":
            print("Salirse del programa")
            break
        else:
            print("Ingresaste un dato inválido")

if __name__ == "__main__":
    menu()