"""
    Guarda información en las entidades en la base de datos
"""

from base_datos import conn

# se usa el objeto Connection y se accede al método cursor
# para poder realizar las acciones en la base de datos.

cursor = conn.cursor()

# a través de cursor su puede ejecutar comandos SQL mediante el método
# execute


# Crear una variables para almacenar atributos
nombre = "Union Deportiva"
ciudad = "Guayaquil"
presidente = "Jose Perez"
campeonatos = 5
cadena_sql = """INSERT INTO Equipo (nombre, ciudad, presidente, campeonatos_ganados) VALUES ('%s', '%s', '%s', %d);""" % (nombre, ciudad, presidente, campeonatos)
print("")
# ejecutar el SQL
cursor.execute(cadena_sql)

#crera variables para el ingreso de datos en la tabla de jugador
nombre_equipo = "Union Deportiva"
nombre_jugador = "Pedro Pablo"
posicion = "Mediocampista"
edad = 25
cadena_sql = """INSERT INTO Jugador (nombre_equipo, nombre, posicion, edad) VALUES ('%s', '%s', '%s', %d);""" % (nombre_equipo, nombre_jugador, posicion, edad)
print("\nIngresando registro............................\n")
# ejecutar el SQL
cursor.execute(cadena_sql)
print("\nRegistros ingresados correctamente\n\n")

# confirmar los cambios a través del objeto importado de tip Connection
conn.commit()

# cerrar el enlace a la base de datos (recomendado)
cursor.close()
