cantidad =int(input("cuántos números desea ingresar?: "))
lista = []

for i in range(cantidad):
    lista.append(int(input(f"Ingrese el {i+1}°n")))
    
b = int(input("Por cuanto desea multiplicar cada elemento?"))
    
for num in lista:
    print(num*b)
    