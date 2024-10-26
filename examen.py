#Lista golinas
golosinas =[
    [1, "KitKat",             20], 
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
golosinas2 =[ #lista para funcion RegistrarGolosinas
    [1, "KitKat",             0], 
    [2, "Chicles",            0],
    [3 , "Caramelos de Menta",0], 
    [4 ,"Huevo Kinder",       0],
    [5 ,"Chetoos" ,           0], 
    [6 ,"Twix" ,              0],
    [7 ,"M&M'S" ,             0], 
    [8,"Papas Lays",           0],
    [9,"Milkybar",            0],
    [10, "Alfajor Tofi",       0], 
    [11,"Lata Coca",          0], 
    [12,"Chitos",            0 ]
]

#Lista empleados
empleados ={
    "1100": "José Alonso",
    "1200": "Federico Pacheco",
    "1300": "Nelson Pereyra",
    "1400": "Osvaldo Tejada",
    "1500": "Gastón García"
}

#tupla
clavesTecnico = ("admin", "CCCDDD", "2020")
#golosinas Pedidas
golosinasPedidas =[["Código golosina", "Denominación golosina", "Cantidad total pedida"]
                   ]


def validarLegajo(legajo,empleados): #Lo utilizo en case 1
    if legajo in empleados:
        return True
    else:
        return False

def pedirGolosinas(golosinas, indice): #Lo utilizo en case 1
    indice=indice-1
    for fila in golosinas:
        if golosinas.index(fila) ==indice:
            golosinas[golosinas.index(fila)][2] =golosinas[golosinas.index(fila)][2]-1
def verificarStock(golosinas, indice):  #Lo utilizo en case 1
    indice = indice-1
    for fila in golosinas:
        if golosinas.index(fila) ==indice:
            if (golosinas[indice][2] >0):
                return True
            else:
                return False
mem =[] #Creo la variable mem para guardar los indices de las filas que inserte en golosinasPedidas
def RegistrarGolosinas(golosinasPedidas, golosinas2, indice): #Lo utilizo en case 1
    if indice in mem:
        golosinas2[indice-1][2] +=1
    else:
        golosinas2[indice-1][2] +=1
        golosinasPedidas.append(golosinas2[indice-1]) #Añado la lista fila de la golosina pedida
        mem.append(indice)


def mostrarGolosinas(golosinas): #Lo utilizo en case 2
    for fila in golosinas:
        print(fila)

def validarContrasenia(clavesTecnico):#Lo utilizo en case 3
    clave1 =input("Ingrese la contraseña de 3 pasos: ")
    clave2 =input()
    clave3 =input()
    if clave1 in clavesTecnico and clave2 in clavesTecnico and clave3 in clavesTecnico:
        return True
    else:
        return False

def rellenarGolosinas(golosinas, recargar, indiceRecargar): #Lo utilizo en case 3
    golosinas[indiceRecargar-1][2] += recargar

def calcularTotal(golosinasPedidas): #Lo utilizo en case 4:
    longitud = len(golosinasPedidas)
    total= 0
    for i in range(1,longitud):
        total+= golosinasPedidas[i][2]
    return total
        
#======================================================================================================================
 
        
#Martín Guerra                                                Parcial n°1 Python  
opcionmenu = 0
salir=False
while (salir ==False):
    print("=====Menú========")
    print("Elija una opción.")
    print("(1) Pedir golosinas.")
    print("(2) Mostrar golosinas.")
    print("(3) Rellenar golosinas.")
    print("(4) Apagar máquina.")
    print("==================")
    opcionmenu=int(input())
    match opcionmenu:
        case 1:
            print("Ingrese su legajo:")
            legajo =input()
            print("validando legajo...")
            if validarLegajo(legajo, empleados) == True:
                print("Legajo verificado.")
                continuar = True
                while(continuar==True):
                    indice=int(input("Ingrese el código de la golosina:"))
                    if indice>=0 & indice<=12:
                        if verificarStock(golosinas, indice)==True:  
                            pedirGolosinas(golosinas, indice)
                            RegistrarGolosinas(golosinasPedidas, golosinas2, indice) 
                            continuar = False
                            print("Operación exitosa.")
                            input("Presione enter para continuar...")
                        else:
                            print(f"Lo sentimos la golosina {golosinas[indice-1][1]} no se encuentra disponible.")
                            continuarcase1 = input("Ingrese (1) para ingresar otra golosina, de lo contrario otro numero para salir")
                            match continuarcase1:
                                case 1: 
                                    continuar = True
                                case _: 
                                    continuar = False
                    else: 
                        print("Código de la Golosina no disponible")
            else: 
                print("Usted no es un empleado de la empresa.")
                input("Presione enter para continuar...")
        case 2:
            mostrarGolosinas(golosinas)
            input("Presiona enter para continuar...")
        case 3:
            if (validarContrasenia(clavesTecnico) ==True):
                print("Contraseña Correcta")
                golosinacodCorrecto = False
                while golosinacodCorrecto == False:
                    IndiceRecargar=int(input("Ingrese el código de la golosina a recargar: "))
                    if(IndiceRecargar>0 and IndiceRecargar<13):
                        golosinacodCorrecto = True
                    else:
                        golosinacodCorrecto = False
                        print("Ingrese un código entre 1 y 12")
                mayorAcero =False
                while mayorAcero==False:
                    
                    print("Ingrese la cantidad a recargar:")
                    recargar = int(input())
                    if(recargar>0):
                        mayorAcero = True 
                        rellenarGolosinas(golosinas, recargar, IndiceRecargar)
                        print("Operación exitosa.")
                        input("Presione enter para continuar...")
                    else:
                        print("Ingrese una cantidad mayor a cero")
                        mayorAcero = False
            else:
                print("No tiene permiso para ejecutar la función de recarga.")
        case 4: 
            print("Lista de golosinas pedidas")
            for fila in golosinasPedidas:
                print(fila)
            print(f"El total de golosinas pedidas es: {calcularTotal(golosinasPedidas)}")
            salir = True

