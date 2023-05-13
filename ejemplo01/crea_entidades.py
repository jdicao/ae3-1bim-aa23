"""
    Crear entidades en la base de datos
"""

from crea_base_datos import conn

# se usa el objeto Connection y se accede al método cursor
# para poder realizar las acciones en la base de datos.

cursor = conn.cursor()

# a través de cursor su puede ejecutar comandos SQL mediante el método
# execute

# Crear tabla Equipo en la base de datos
# con atributos: nombre, ciudad, presidente y campeonatos ganados

cadena_sql = 'CREATE TABLE Equipo (nombre TEXT, ciudad TEXT, presidente TEXT, campeonatos_ganados INTEGER)'

# ejecutar el SQL
cursor.execute(cadena_sql)

#crear tabla jugador
cadena_sql = 'CREATE TABLE Jugador (nombre_equipo TEXT, nombre TEXT, posicion TEXT, edad INTEGER)'

# ejecutar el SQL
cursor.execute(cadena_sql)

# cerrar la enlace a la base de datos (recomendado)
cursor.close()
