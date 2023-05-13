"""
    Consulta de información en las entidades en la base de datos
"""

from crea_base_datos import conn

# se usa el objeto Connection y se accede al método cursor
# para poder realizar las acciones en la base de datos.

cursor = conn.cursor()

# hace consultas a la base de datos
cadena_consulta_sql = "SELECT * from Equipo"
cursor.execute(cadena_consulta_sql)
# la información resultante se la obtiene del método fetchall de cursor.
informacion = cursor.fetchall()

# se realiza un ciclo repetitivo para recorrer la secuencia de información
# resultante
print("Informacion de Equipos:")
for d in informacion:
    print("%s - %s - %s - %d" % (d[0], d[1], d[2], d[3]))

print("")
#consultar informacion de Jugadores
cadena_consulta_sql = "SELECT * from Jugador"
cursor.execute(cadena_consulta_sql)

informacion_libro = cursor.fetchall()

#presentar informacion de libros
print("Informacion de Jugadores:")
for d in informacion_libro:
    print("%s - %s - %s - %d" % (d[0], d[1], d[2], d[3]))

print("")
# cerrar el enlace a la base de datos (recomendado)
cursor.close()
