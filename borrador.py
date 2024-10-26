golosinas =[
    [1, "KitKat",             0], 
    [2, "Chicles",            50],
    [3 , "Caramelos de Menta",50], 
    [4 ,"Huevo Kinder",       10],
    [5 ,"Chetoos" ,           10], 
    [6 ,"Twix" ,              10],
    [7 ,"M&M'S" ,             10], 
    [8,"Papas Lays",           2],
    [9,"Milkybar",            10],
    [10, "Alfajor Tofi",       15], 
    [11,"Lata Coca",          20], 
    [12,"Chitos",            10 ]
]

# def pedirGolosinas(golosinas, indice):
#     indice=indice-1
#     for fila in golosinas:
#         if golosinas.index(fila) ==indice:
#             golosinas[golosinas.index(fila)][2] =golosinas[golosinas.index(fila)][2]-1
#             print("disminuyendo")
            
def verificarStock(golosinas, indice):
    indice = indice-1
    for fila in golosinas:
        if golosinas.index(fila) ==indice:
            if (golosinas[indice][2] >0):
                return True
            else:
                return False

# pedirGolosinas(golosinas, 1)
print(f"Stock: {verificarStock(golosinas, 1)}")
