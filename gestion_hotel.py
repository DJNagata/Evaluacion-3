
import csv
from datetime import date

def reservar_habitacion(lista):
    try:
        habitacion = int(input("Ingrese en que habitacion desea reservar \n"))
        nombre = input("Ingrese nombre de la persona")
        apellido = input("Ingrese apellido de la persona")
        rut = input("Ingrese rut de la persona")
        fecha_entrada = input("Ingrese la hora de entrada")
        fecha_salida = input("Ingrese la hora de entrada")
        for pisos in lista:        
            if pisos[0] == habitacion:
                pisos[2] = "RESERVADO"
                pisos[3] = nombre
                pisos[4] = apellido
                pisos[5] = rut
                pisos[6] = fecha_entrada
                pisos[7] = fecha_salida
    except ValueError:
        print("Valor no valido")

def buscar_habitacion(lista):
    habitacion = int(input("Ingrese en que habitacion desea ver \n"))
    for pisos in lista:
        if pisos[0] == habitacion:
            print(pisos)

def ver_estado(lista):
    for pisos in hotel_reserva:
        print(pisos)

def guardar(lista):
    with open("habitaciones.csv","w",newline="") as archivo_csv:
        writer = csv.writer(archivo_csv)
        for habitaciones in lista:
            writer.writerow(habitaciones)

def ventas_diaras(lista):
    total = 0
    for pisos in lista:
        if pisos[1] == "RESERVADO":
            total = pisos[2] + total:


hotel_reserva = []
lista_piso = []
c = 101
for habitaciones in range (0,40): 
    lista_piso.append(c)
    c = c + 1
    if(c == 109):
        c = 201
    if(c == 209):
        c = 301
    if(c == 309):
        c = 401
    if(c == 409):
        c = 501 
    lista_piso.append("Libre")
    if (c<400):
        lista_piso.append(30000)
    elif (c<500):
        lista_piso.append(60000)
    elif (c<600):
        lista_piso.append(100000)
    lista_piso.append("Nombre")
    lista_piso.append("Apellido")
    lista_piso.append("RUT")
    lista_piso.append("Fecha entrada")
    lista_piso.append("Fecha entrada")


    
    #print(lista_piso)
    
    hotel_reserva.append(lista_piso)
    lista_piso = []
    #c = c + 94

#for pisos in hotel_reserva:
#    print(pisos)

#print(hotel_reserva)

ciclo = True
while(ciclo):
    opcion = int(input("Ingrese la opcion: \n1.reservar habitacion \n2.Buscar Habitacion \n3.Ver estado \n4.ventas diaras\n5.Guardar\n6.salir\n"))
    match opcion:
        case 1:
            reservar_habitacion(hotel_reserva)
        case 2:
            buscar_habitacion(hotel_reserva)
        case 3:
            ver_estado(hotel_reserva)
        case 4:
            ventas_diaras(hotel_reserva)
        case 5:
            guardar(hotel_reserva)
        case 6:
            print("Saliendo del programa")
            ciclo = False
        case _:
            print("Ingrese un valor valido")