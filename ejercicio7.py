cantidad = int(input("Cuántos números desea ingresar?: "))
numeros =[]
for i in range(cantidad):
    numeros.append(int(input(f"Ingrese el {i+1}°n: ")))
suma = 0
#sumo los elementos
for i in range(cantidad):
    suma = suma + numeros[i]

promedio = suma / cantidad

print(f"Promedio: {promedio}") 