"""
    Guarda información en las entidades en la base de datos
"""

from crea_base_datos import conn

# se usa el objeto Connection y se accede al método cursor
# para poder realizar las acciones en la base de datos.

cursor = conn.cursor()

# a través de cursor su puede ejecutar comandos SQL mediante el método
# execute

# Crear una variables para almacenar atributos
print("Ingrese los datos del equipo:")
nombre = input("Ingrese el nombre del equipo:")
ciudad = input("Ingrese la ciudad del equipo:")
presidente = input("Ingrese el nombre del presidente del equipo:")
campeonatos = int(input("Ingrese el numero de campeonatos ganados (en numeros):"))
cadena_sql = """INSERT INTO Equipo (nombre, ciudad, presidente, campeonatos_ganados) VALUES ('%s', '%s', '%s', %d);""" % (nombre, ciudad, presidente, campeonatos)
print("\nIngresando registro............................\n")
# ejecutar el SQL
cursor.execute(cadena_sql)
print("\nRegistro ingresado correctamente\n\n")

#crera variables para el ingreso de datos en la tabla de jugador
print("Ingrese los datos del Jugador:")
nombre_equipo = input("Ingrese el nombre del equipo:")
nombre_jugador = input("Ingrese la ciudad del jugador:")
posicion = input("Ingrese la posicion en que juega:")
edad = int(input("Ingrese la edad del jugador (en numeros):"))
cadena_sql = """INSERT INTO Jugador (nombre_equipo, nombre, posicion, edad) VALUES ('%s', '%s', '%s', %d);""" % (nombre_equipo, nombre_jugador, posicion, edad)
print("\nIngresando registro............................\n")
# ejecutar el SQL
cursor.execute(cadena_sql)
print("\nRegistro ingresado correctamente\n\n")

# confirmar los cambios a través del objeto importado de tip Connection
conn.commit()

# cerrar el enlace a la base de datos (recomendado)
cursor.close()
