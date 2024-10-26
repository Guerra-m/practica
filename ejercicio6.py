cantidad = int(input("cuantos números desea ingresar?:"))
numeros = []

for i in range(cantidad):
    numeros.append(int(input(f"Ingrese el {i+1}°n: ")))
    
conjuntoSinRepetidos =set(numeros)
print(conjuntoSinRepetidos)
        