import pandas as pd
import os.path


Almacenamiento_Alumnos = {}
Almacenamiento_Calificaciones = {}

i = 1
while i > 0:
    Menu = int(input("-- BIENVENIDO AL MENU DEL SISTEMA -- \n [1] Ingresar Alumnos \n [2] Ingresar Calificaciones \n [3] Asignaturas con desempeño más bajo \n [4] Estudiantes reprobados \n [5] Salir \n "))
    
    if Menu == 1:
        ID = int(input("Ingrese la matricula del nuevo alumno: "))
        Nombre = input("Ingrese el nombre del alumno: ")
        
        if ID not in (Almacenamiento_Alumnos.keys()):
            Almacenamiento_Alumnos[ID] = [Nombre]
            print("\n ALUMNO AGREGADO EXITOSAMENTE \n")
        else:
            print("\n Esta matricula YA ESTA EN USO, no se permiten matriculas duplicadas.")
            print("Lista de alumnos registrados:")
            
        print(Almacenamiento_Alumnos)
        print("\n")
    
    elif Menu == 2:
        
        Matricula = int(input("Ingrese la matricula del amuno al que desaes calificar: "))
        Name = (input("Ingrese el nombre del alumno a calificar: "))
        
        if Matricula in (Almacenamiento_Alumnos.keys()):
            EstDes = int(input("Ingresar la calificacion de Estadistica Descriptiva: "))
            EstData = int(input("Ingresar la calificacion de Estructura de Datos: "))
            PrBD = int(input("Ingresar la calificacion de Programacion a Base de Datos: "))
            ConAdm = int(input("Ingresar la calificacion de Contabilidad Administrativa: "))
            Macro = int(input("Ingresar la calificacion de Macroeconomia: "))
            if EstDes <= 100 and EstData <= 100 and PrBD <= 100 and ConAdm <= 100 and Macro <= 100:
                Almacenamiento_Calificaciones[ID] = [[Nombre], EstDes , EstData, PrBD, ConAdm , Macro]
            else:
                print("Calificaion invalida")
        else:
            print("Ese alumno no existe en el registro \n")
        print("Listado de alumnos: \n")
        print(Almacenamiento_Alumnos)
        print()

    elif Menu == 3:
        Calificaciones = pd.DataFrame(Almacenamiento_Calificaciones)
        
        Calificaciones.index = ["Nombre","Estadistica Descriptiva","Estructura de Datos","Programacion a Base de Datos","Contabilidad Administrativa","Macroeconomia"]
        
        Busqueda = int(input("1.- Si requiere el promedio de alumnos   2.- Si requiere el promedio de materias \n"))
    
        if Busqueda == 2:
                print("Promedio de materias")
                print(Calificaciones.T.mean(axis = 0))
                print(Calificaciones.describe())
                
                Almacenamiento = open("PromedioMateria.txt", "w")
                Almacenamiento.write("%s" %Calificaciones.T.mean())
                Almacenamiento.close()
                
        else:
                print("Promedio de alumnos")
                print(Calificaciones[1:6].mean(axis = 0))
                print(Calificaciones.describe())
                
                Almacenamiento2 = open("PromedioAlumno.txt", "w")
                Almacenamiento2.write("%s" %Calificaciones[1:6].mean())
                Almacenamiento2.close()
                
    elif opcion == 4:
        
            Calificaciones = pd.DataFrame(Almacenamiento_Calificaciones)
            Calificaciones.index = ["Nombre","Estadistica Descriptiva","Estructura de Datos","Programacion a Base de Datos","Contabilidad Administrativa","Macroeconomia"]
                
            print("Calificaciones reprobadas que tiene el alumno ")
                
            MateriasReprobadas = Calificaciones[Calificaciones[1:6] < 70]
                
            print(MateriasReprobadas.T)    