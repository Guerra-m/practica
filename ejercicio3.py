cantidad = int(input("Cuantós números desea ingresar?: "))
lista = []
for i in range(cantidad):
    lista.append(int(input(f"Ingrese el {i+1}°n: ")))

listainvertida = []
for i in range(cantidad-1, -1, -1):
    listainvertida.append(lista[i])
    
print(f"lista: {lista}")
print(f"lista invertida: {listainvertida}")