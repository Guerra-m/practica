cantidad = int(input("cuantos números desea ingresar?: "))
numeros = []

for i in range(cantidad):
    numeros.append(int(input(f"Ingrese el {i+1}°n. ")))
    
#recorremos lista
pares = 0
impares = 0
for num in numeros:
    if(num%2==0):
        pares = pares+1
    else:
        impares = impares+1

print(f"{pares} números son pares.")
print(f"{impares} números son impares.")