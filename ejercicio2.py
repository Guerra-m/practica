lista= []
print("cuantos numeros desea ingresar?")
cantidad = int(input())

print("Ingrese los números:") #Ingrese los números en una lista
for i in range(cantidad):
    lista.append(int(input()))

mayor = lista[0]
menor = lista[0]
for i in range(cantidad):
    if(lista[i]>mayor):
        mayor = lista[i]
    elif(lista[i]<menor):
        menor = lista[i]

print(f"mayor: {mayor}")
print(f"menor: {menor}")
         