# Menu de opciones
# 1 suma
# 2 Resta
# 3 Multiplicacion
import os

class Operaciones():

    a = 0
    b = 0

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def suma(self):
        return self.a + self.b

    def resta(self):
        return self.a - self.b

    def multiplicacion(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b

def main():
    while True:
        os.system('clear')
        print("Elije una opcion")
        print("1. Sumar")
        print("2. Resta")
        print("3. Multiplicacion")
        print("4. Division")
        print("5. Salir")
        option = input()

        if option == '5':
            break

        if option == '1':
            os.system('clear')
            num1 = float(input('Ingresa el numero 1: '))
            num2 = float(input('Ingresa el numero 2: '))
            operaciones = Operaciones(num1, num2)
            print(f"El resultado de la suma es: {operaciones.suma()}")
        elif option == '2':
            os.system('clear')
            num1 = float(input('Ingresa el numero 1: '))
            num2 = float(input('Ingresa el numero 2: '))
            operaciones = Operaciones(num1, num2)
            print(f"El resultado de la resta es: {operaciones.resta()}")
        elif option == '3':
            os.system('clear')
            num1 = float(input('Ingresa el numero 1: '))
            num2 = float(input('Ingresa el numero 2: '))
            operaciones = Operaciones(num1, num2)
            print(f"El resultado de la resta es: {operaciones.multiplicacion()}")
        elif option == '4':
            os.system('clear')
            num1 = float(input('Ingresa el numero 1: '))
            num2 = float(input('Ingresa el numero 2: '))
            operaciones = Operaciones(num1, num2)
            print(f"El resultado de la resta es: {operaciones.division()}")
        else:
            os.system('clear')
            print("Opcion invalida")
        input("Presiona una tecla para continuar")
        

if __name__ == '__main__' :
    main()