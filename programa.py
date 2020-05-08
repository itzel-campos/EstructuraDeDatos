import pandas as pd
import json
import os.path
import time



Almacenamiento_Alumnos = {}
Almacenamiento_Calificaciones = {}

opciones = (1,2,3,4,5,6)
salir = 1


while salir == 1:
    
    print("-- BIENVENIDO AL MENU DEL SISTEMA -- \n\n Opciones:\n\n [1] Ingresar Alumnos \n [2] Ingresar Calificaciones \n [3] Reporte de asignaturas \n [4] Estudiantes reprobados \n [5] Exportar calificaciones \n [6] Terminar\n")
    Menu = int(input("Ingresa una opcion: "))

   
    if Menu in opciones:
        
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
            time.sleep(4)
    
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
                    print("\nCalificaciones guardadas\n")
                    print("Listado de alumnos: \n")
                    print(Almacenamiento_Alumnos)
                    print()
                else:
                    print("\nCalificaion invalida")

            else:
                print("\nEse alumno no existe en el registro \n")
            
            time.sleep(4)

        elif Menu == 3:
            Calificaciones = pd.DataFrame(Almacenamiento_Calificaciones)
        
            Calificaciones.index = ["Nombre","Estadistica Descriptiva","Estructura de Datos","Programacion a Base de Datos","Contabilidad Administrativa","Macroeconomia"]
        
            Busqueda = int(input("1.- Si requiere el promedio de alumnos   2.- Si requiere el promedio de materias \n")) 
    
            if Busqueda == 2:
                    print("Promedio de materias: \n")
                    print(Calificaciones.T.mean(axis = 0))
                    print(Calificaciones.count())
                    print(Calificaciones.std())
                    print(Calificaciones.min())
                    print(Calificaciones.max())
                    
                    respuesta=int(input("\n¿Deseas guardar el reporte en un archivo de texto plano?\n   1.- Si     2.- No \n"))
                    if respuesta == 1:
                        Almacenamiento = open("PromedioMateria.txt", "w")
                        Almacenamiento.write("%s" %Calificaciones.T.mean())
                        Almacenamiento.close()
                        print("***Guardado***")
                
            else:
                    print("Promedio de alumnos: ")
                    print(Calificaciones[1:6].mean(axis = 0))
                    print("Calificaciones registradas: ")
                    print(Calificaciones[1:6].count())
                    print("Desviacion estandar: ")
                    print(Calificaciones[1:6].std())
                    print("Calificación mas baja")
                    print(Calificaciones[1:6].min())
                    print("Calificacion mas alta")
                    print(Calificaciones[1:6].max())
                    
                    respuesta=int(input("\n¿Deseas guardar el reporte en un archivo de texto plano?\n   1.- Si     2.- No \n"))
                    
                    if respuesta == 1:
                        Almacenamiento2 = open("PromedioAlumno.txt", "w")
                        Almacenamiento2.write("%s" %Calificaciones[1:6].mean())
                        Almacenamiento2.close()
                        print("***Guardado***")
            time.sleep(4)
            
        elif Menu == 4:
        
                Calificaciones = pd.DataFrame(Almacenamiento_Calificaciones)
                Calificaciones.index = ["Nombre","Estadistica Descriptiva","Estructura de Datos","Programacion a Base de Datos","Contabilidad Administrativa","Macroeconomia"]
                
                print("Calificaciones reprobadas que tiene el alumno ")
                
                MateriasReprobadas = Calificaciones[Calificaciones[1:6] < 70]
                
                print(MateriasReprobadas.T)
                time.sleep(5)
    
        elif Menu == 5:
             Opciones_de_guardado = int(input(" Exportar calificaciones mediante: \n [1] Opcion de guardado en CSV \n [2] Opcion de guardado en JSON\n"))
            
             if Opciones_de_guardado == 1:
                    Calificaciones.to_csv(r'Calificaciones_csv', index = True, header = True)
                    print("Calificaciones guardadas exitosamente en CSV\n")
    
             elif Opciones_de_guardado == 2:
                    Calificaciones.T.to_json(r'Calificacionesjson.json', index = True, header = True)
                    print("Calificaciones guardadas exitosamente en JSON\n")
             time.sleep(4)
             
        elif Menu == 6:
             
             salir = 2
            
            
    else:
        print("***Introduce una opcion valida***\n")
        time.sleep(4)
        
print("Saliste")
        