#Importacion de librerias

import os.path
import time
import sys
import sqlite3
from sqlite3 import Error



#Definicion de funciones para registrar

def menu():
    print("\n-- BIENVENIDO AL MENU DEL SISTEMA -- \n\n Opciones:\n\n [1] Opciones de registro\n [2] Opciones de consulta\n [3] Actualizar o eliminar datos\n [4] Salir\n")

def registro_alumno(idalumno, nombre):
    try:
        with sqlite3.connect("acm.db") as conn:
            cursor = conn.cursor()
            datos = {"idalumno":idalumno, "nombre":nombre}
            cursor.execute("INSERT INTO alumnos VALUES(:idalumno,:nombre)", datos)
            print("\n*** Se ha registrado el alumno ***\n")
            print("")
    except Error as e:
        print (e)
    except:
        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
    finally:
        conn.close()
        
def registro_materia(idmateria, nombre):
    try:
        with sqlite3.connect("acm.db") as conn:
            cursor = conn.cursor()
            datos_materias = {"idmateria":idmateria, "nombre":nombre}
            cursor.execute("INSERT INTO materias VALUES(:idmateria,:nombre)", datos_materias)
            print("*** Se ha registrado la materia ***")
            print("")
    except Error as e:
        print (e)
    except:
        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
    finally:
        conn.close()
        
def registro_calificacion(idcalificacion, idalumno, idmateria, calificacion):
    try:
        with sqlite3.connect("acm.db") as conn:
            cursor = conn.cursor()
            datos_calificaciones = {"idcalificacion":idcalificacion, "idalumno":idalumno, "idmateria":idmateria, "calificacion":calificacion}
            cursor.execute("INSERT INTO calificaciones VALUES(:idcalificacion,:idalumno,:idmateria,:calificacion)", datos_calificaciones)
            print("\n*** Se ha registrado la calificacion ***\n")
            print("")
    except Error as e:
        print (e)
    except:
        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
    finally:
        conn.close()
        

#Creacion de tablas y relaciones de la base de datos

try:
    with sqlite3.connect("acm.db") as conn:
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS alumnos (idalumno INTEGER PRIMARY KEY, nombre varchar2(50) NOT NULL);")
        c.execute("CREATE TABLE IF NOT EXISTS materias (idmateria INTEGER PRIMARY KEY, nombre varchar2(50) NOT NULL);")
        c.execute("CREATE TABLE IF NOT EXISTS calificaciones (idcalificacion INTEGER PRIMARY KEY, idalumno integer not null, idmateria integer not null, calificacion integer, FOREIGN KEY(idalumno) REFERENCES alumnos(idalumno), FOREIGN KEY(idmateria) references materias(idmateria));")
except Error as e:
    print (e)
except:
    print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
finally:
    conn.close()



#logica e interfaz

salir = 1
while salir == 1:    
    menu()
    opcion = int(input("Ingresa una opcion: "))

    if opcion == 1: #registro de datos 
        continuar1 = True
        while continuar1:
            
            print("\n--OPCIONES DE REGISTRO--\n\n [1] Registrar alumnos\n [2] Registrar materias\n [3] Registrar calificaciones\n [4] Regresar\n")
            opcion_registro = int(input("Introduce una opcion: "))
            
            if opcion_registro == 4: 
                continuar1 = False
            elif opcion_registro == 1:
                continuar= True
                
                while continuar:   
                    print("\n--REGISTRO ALUMNOS--\n\nIngresa la matricula y el nombre.\n*Teclea la matricula '0' para finalizar*\n")
                    idalumno = int(input("Ingrese la matricula del alumno: "))
                    if idalumno == 0:
                        continuar=False
                    else:
                        nombre = input("Ingrese el nombre del alumno: ")
                        registro_alumno(idalumno, nombre)    
    
            elif opcion_registro == 2: #registrar materias    
                continuar=True
                while continuar:
                    print("\n--REGISTRO MATERIAS--\n\n Ingresa la clave y el nombre\n*Teclea la clave '0' para finalizar*\n")
                    idmateria = int(input("Ingresa la clave de la materia: "))
                    if idmateria == 0:
                        continuar = False
                    else:
                        nombre = input("Ingresa el nombre: ")
                        registro_materia(idmateria, nombre)
            
            elif opcion_registro == 3:  #registrar calificaciones     
                continuar=True
                while continuar:
                    print("\n--REGISTRO CALIFICACIONES--\n\n Ingresa la matricula y el nombre.\n*Teclea la matricula '0' para finalizar*\n")
                    idalumno = int(input("Ingrese la matricula del amuno al que desaes calificar: "))   
                    if idalumno == 0:
                        continuar=False
                    else:
                        idcalificacion = int(input("\nIngresa el folio de la calificacion\n (ultimos 3 digitos de la matricula del alumno + la clave de la materia): "))
                        idmateria = int(input("Ingresa la clave de la materia: "))
                        calificacion = int(input("Ingresa la calificacion: "))
                        registro_calificacion(idcalificacion, idalumno, idmateria, calificacion)
                        
            else:
                print("Ingresa una opcion valida")
                       
    elif opcion == 2:  #opciones de consulta
        
        continuar2 = True
        while continuar2: 
            print("\n--OPCIONES DE CONSULTA--\n\n [1] Consultar los alumnos registrados\n [2] Consultar las materias y sus claves\n [3] Consultar calificaciones\n [4] Alumnos reprobados\n [5] Reporte estadistico\n [6] Regresar\n")
            opcion_registro = int(input("Ingresa una opcion: ")) 
            if opcion_registro == 6:    
                continuar2 = False
       
            elif opcion_registro == 1: #consultar todos los alumnos 
                try:
                    with sqlite3.connect("acm.db") as conn:
                         cursor = conn.cursor()
                         cursor.execute("select * from alumnos;")
                         alumnos = cursor.fetchall()
                         print("\n*******************************")
                         print("Matricula    Nombre\n")
                         for alumno in alumnos:
                             print(alumno)
                         print("********************************")
                         print("")            
                except Error as e:
                    print (e)
                except:
                    print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
                finally:
                    conn.close()
            
            elif opcion_registro == 2: #consultar todas las materias   
                 try:
                    with sqlite3.connect("acm.db") as conn:
                         cursor = conn.cursor()
                         cursor.execute("select * from materias;")
                         materias = cursor.fetchall()
                         print("\n*******************************")
                         print("Clave    Materia\n")
                         for materia in materias:
                             print(materia)
                         print("\n********************************")
                         print("")        
                 except Error as e:
                     print (e)
                 except:
                     print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
                 finally:
                     conn.close()

            elif opcion_registro == 3: #consultar calificaciones 
                print("\n¿Deseas hacer la consulta por alumno o por materia?\n\n [1] Por alumno\n [2] Por materia\n")
                opcion_cali = int(input("Ingresa una opcion: "))
                
                if opcion_cali == 1: #por alumno         
                                matricula = int(input("Ingresa la matricula del alumno del que deseas consultar la calificacion: "))
                                try:
                                    with sqlite3.connect("acm.db") as conn:
                                        cursor = conn.cursor()
                                        cursor.execute(f"select idmateria, calificacion from calificaciones WHERE idalumno = {matricula}")
                                        calificacion = cursor.fetchall()
                                        print("\n*******************************")
                                        print(f"Clave materia      Calificacion")
                                        for materia in calificacion:
                                            print(materia)
                                        print("\n********************************")
                                        print("")
                                except Error as e:
                                          print (e)
                                except:
                                          print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
                                finally:
                                          conn.close()
                
                if opcion_cali == 2: #por materia
                    clave = int(input("\nIngresa la clave de la materia: "))
                    try:
                        with sqlite3.connect("acm.db") as conn:
                            cursor = conn.cursor()
                            cursor.execute(f"select idalumno, idmateria, calificacion from calificaciones WHERE idmateria = {clave}")
                            calificacion = cursor.fetchall()
                            print("\n*******************************")
                            print(f"Matricula    Materia    Calificacion\n")
                            for materia in calificacion:
                                print(materia)
                            print("\n********************************")
                            print("")   
                    except Error as e:
                                print (e)
                    except:
                                print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
                    finally:
                                conn.close()
                                
            elif opcion_registro == 4: #alumnos reprobados
                    print("\nALUMNOS REPROBADOS\n")
                    print("Materias:\n [1] Estadistica\n [2] Programacion\n [3] Base de datos\n [4] Contabilidad\n [5] Macroeconomia\n Introduce la clave de la materia: ")
                    try:
                        with sqlite3.connect("acm.db") as conn:
                            cursor = conn.cursor()
                            cursor.execute(f"select idalumno, idmateria, calificacion from calificaciones WHERE calificacion < 71 order by idalumno")
                            calificacion = cursor.fetchall()
                            print("\n*******************************")
                            print(f"Matricula  Materia  Calificacion\n")
                            for materia in calificacion:
                                print(materia)
                            print("\n********************************")
                            print("")
                    except Error as e:
                                print (e)
                    except:
                                print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
                    finally:
                                conn.close()
            
            elif opcion_registro == 5: #reporte estadistico
                
                    continuar = True
                    while continuar:
                        
                        print("\nREPORTE ESTADISTICO\n\n [1] Reporte de alumno\n [2] Reporte de materia\n [3] Regresar\n")
                        opcion_reporte = int(input("\nIngresa una opcion: "))
                    
                        if opcion_reporte == 1: #por alumno
                        
                            idalumno = int(input("\nIngresa la matricula del alumno: "))
                        
                            try:
                                with sqlite3.connect("acm.db") as conn:
                                
                                    cursor = conn.cursor()
                                    cursor.execute(f"select idalumno, count(calificacion) from calificaciones WHERE idalumno = {idalumno};")
                                    contador = cursor.fetchall()
                                    print("\n*******************************")
                                    print(f"Matricula  Calificaciones registradas")
                                    print(contador)
                                    print("********************************")
                                
                                    cursor = conn.cursor()
                                    cursor.execute(f"select idalumno, idmateria, min(calificacion) from calificaciones WHERE idalumno = {idalumno};")
                                    minimo = cursor.fetchall()
                                    print("*******************************")
                                    print(f"Matricula  Materia  Calificacion mas baja")
                                    print(minimo)
                                
                                    cursor.execute(f"select idalumno, idmateria, max(calificacion) from calificaciones WHERE idalumno = {idalumno};")
                                    maximo = cursor.fetchall()
                                    print("*******************************")
                                    print(f"Matricula  Materia  Calificacion mas alta")
                                    print(maximo)
                                
                                    cursor.execute(f"select idalumno, avg(calificacion) from calificaciones WHERE idalumno = {idalumno};")
                                    promedio = cursor.fetchall()
                                    print("*******************************")
                                    print(f"Matricula  Promedio del alumno")
                                    print(promedio)
                                    print("********************************")
                                
                                    cursor.execute(f"select idalumno, sum(calificacion) from calificaciones WHERE idalumno = {idalumno};")
                                    suma = cursor.fetchall()
                                    print("*******************************")
                                    print(f"Matricula  Suma de calificaciones")
                                    print(suma)
                                    print("********************************")
                                    
                                    datos = [contador, minimo, maximo, promedio, suma]
                                    respuesta=int(input("\n¿Deseas guardar el reporte en un archivo de texto plano?\n   1.- Si     2.- No \n"))
                                    if respuesta == 1:
                                        Almacenamiento = open("Reporte_alumno.txt", "w")
                                        Almacenamiento.write("%s" %datos)
                                        Almacenamiento.close()
                                        print("***Guardado***")
                                
                            except Error as e:
                                    print (e)
                            except:
                                    print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
                            finally:
                                    conn.close()
                    
                        elif opcion_reporte == 2: #por materia
                            print("")
                            print("*" * 20)
                            print("MATERIAS:\n\n [1] Estadistica\n [2] Programacion\n [3] Base de datos\n [4] Contabilidad\n [5] Macroeconomia")
                            print("*" * 20)
                            idmateria = int(input("\nIngresa la clave de la materia: "))
                        
                            try:
                                with sqlite3.connect("acm.db") as conn:
                                
                                    cursor = conn.cursor()
                                    cursor.execute(f"select idmateria, count(calificacion) from calificaciones WHERE idmateria = {idmateria};")
                                    contador = cursor.fetchall()
                                    print("\n*******************************")
                                    print(f"Materia  Calificaciones registradas")
                                    print(contador)
                                
                                    cursor = conn.cursor()
                                    cursor.execute(f"select idmateria, min(calificacion), idalumno from calificaciones WHERE idmateria = {idmateria};")
                                    minimo = cursor.fetchall()
                                    print("*******************************")
                                    print(f"Materia  Calificacion mas baja  Matricula")
                                    print(minimo)
                                
                                    cursor.execute(f"select idmateria, max(calificacion), idalumno from calificaciones WHERE idmateria = {idmateria};")
                                    maximo = cursor.fetchall()
                                    print("*******************************")
                                    print(f"Materia  Calificacion mas alta  Matricula")
                                    print(maximo)
                                
                                    cursor.execute(f"select idmateria, avg(calificacion) from calificaciones WHERE idmateria = {idmateria};")
                                    promedio = cursor.fetchall()
                                    print("*******************************")
                                    print(f"Materia  Promedio de calificaciones")
                                    print(promedio)
                                
                                    cursor.execute(f"select idmateria, sum(calificacion) from calificaciones WHERE idmateria = {idmateria};")
                                    suma = cursor.fetchall()
                                    print("*******************************")
                                    print(f"Materia  Suma de calificaciones")
                                    print(suma)
                                    print("********************************")
                                    
                                    datos = [contador, minimo, maximo, promedio, suma]
                                    respuesta=int(input("\n¿Deseas guardar el reporte en un archivo de texto plano?\n   1.- Si     2.- No \n"))
                                    if respuesta == 1:
                                        Almacenamiento = open("Reporte_materia.txt", "w")
                                        Almacenamiento.write("%s" %datos)
                                        Almacenamiento.close()
                                        print("***Guardado***")
                                    
                                   
                                
                            except Error as e:
                                    print (e)
                            except:
                                    print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
                            finally:
                                    conn.close()
                                    
                        elif opcion_reporte == 3:
                             continuar = False
                            
                        else:
                            print("\n******Introduce una opcion valida*****\n")
                            
                        
                                         
                                         
                
                                                               
    elif opcion == 3: #modificar y actualizar datos
        
        continuar3 = True
        while continuar3:
            print("\n--ACTUALIZAR DATOS--\n\n [1] Actualizar alumno\n [2] Dar de baja alumno\n [3] Actualizar calificacion\n [4] Eliminar calificacion\n [5] Regresar\n")
            opcion_actualizar = (int(input("Ingresa una opcion: ")))
            if opcion_actualizar == 5:
                continuar3 = False
                
            elif opcion_actualizar == 1: #actualizar alumno
                idalumno = int(input("Ingresa la matricula del alumno a actualizar: "))
                idalumno2 = int(input("Ingresa la nueva matricula: "))
                nombre = input("Ingresa el nuevo nombre: ")
                try:
                        with sqlite3.connect("acm.db") as conn:
                                cursor = conn.cursor()
                                cursor.execute(f"update alumnos set idalumno = {idalumno2}, nombre = '{nombre}' WHERE idalumno = {idalumno}")
                                print("\n*** Se ha actualizado el alumno ***\n")
                                print("")
                except Error as e:
                        print (e)
                except:
                        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
                finally:
                        conn.close()
            
            elif opcion_actualizar == 2: #eliminar alumno
                idalumno = int(input("Ingresa la matricula del alumno a eliminar: "))
                try:
                        with sqlite3.connect("acm.db") as conn:
                                cursor = conn.cursor()
                                cursor.execute(f"delete from alumnos WHERE idalumno = {idalumno}")
                                print("\n*** Se ha eliminado el alumno ***\n")
                                print("")
                except Error as e:
                        print (e)
                except:
                        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
                finally:
                        conn.close()
                        
            elif opcion_actualizar == 3: #actualizar calificacion
                idalumno = int(input("Ingresa la matricula del alumno: "))
                idmateria = int(input("Ingresa la clave de la materia: "))
                calificacion = int(input("Ingresa la nueva calificacion: "))
                try:
                        with sqlite3.connect("acm.db") as conn:
                                cursor = conn.cursor()
                                cursor.execute(f"update calificaciones set calificacion = {calificacion} WHERE idalumno = {idalumno} and idmateria = {idmateria}")
                                print("\n*** Se ha actualizado la calificacion ***\n")
                                print("")
                except Error as e:
                        print (e)
                except:
                        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
                finally:
                        conn.close()
        
            elif opcion_actualizar == 4: #eliminar calificacion
                idalumno = int(input("Ingresa la matricula del alumno: "))
                idmateria = int(input("Ingresa la clave de la materia: "))
                try:
                        with sqlite3.connect("acm.db") as conn:
                                cursor = conn.cursor()
                                cursor.execute(f"delete from calificaciones WHERE idalumno = {idalumno} and idmateria = {idmateria}")
                                print("\n*** Se ha eliminado la calificacion ***\n")
                                print("")
                except Error as e:
                        print (e)
                except:
                        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
                finally:
                        conn.close()                        
            
      
    elif opcion == 4: #salir del programa
        salir = 2
        
    else:
        print("\n***Introduce una opcion valida***\n")
        
        
        
print("\n****Saliste****")
        