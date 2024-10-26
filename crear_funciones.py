def sumar(num1, num2):
    resultado = num1 + num2
    return resultado


def saludar(nombre):
    print(f"Hola {nombre}")


nombre= input("hola Dime tu nombre: ")
saludar(nombre)

num1 = int(input("Dime el primer numero: "))
num2 = int(input("Dime el segundo numero: "))

print(f"El resultado de tu suma es:{sumar(num1, num2)} ")