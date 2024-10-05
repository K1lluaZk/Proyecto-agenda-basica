import sqlite3

def conectar():
    conexion = sqlite3.connect("Agenda.db")
    cursor = conexion.cursor()
    return conexion, cursor


def creartabla():
    conexion, cursor = conectar()
    sql = """
        CREATE TABLE IF NOT EXISTS agenda(
            codigo INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            nombre VARCHAR(20)NOT NULL,
            descripcion VARCHAR(30) NOT NULL,
            tipo VARCHAR(20) NOT NULL,
            cantidad INTEGER NOT NULL,
            costo INTEGER NOT NULL,
            observacion VARCHAR(20) NOT NULL
         )
      """
      
    if(cursor.execute(sql)):
          print("Tabla creada")
    else:
          print("No se pudo crear la tabla")
    conexion.close()
    
def insertar(datos):
    conexion, cursor = conectar()
    sql = """
    INSERT INTO agenda(nombre,descripcion,tipo,cantidad,costo,observacion) VALUES (?,?,?,?,?,?)
         """
    if(cursor.execute(sql, datos)):
       print("Datos guardados")
    else:
       print("No se pudieron guardar los datos")
    conexion.commit()
    conexion.close()
    
def consultar():
    conexion,cursor = conectar()
    cursor.execute("SELECT codigo,nombre,descripcion,tipo,cantidad,costo,observacion from agenda")
    listado = []
    for fila in cursor:
        listado.append(fila)
        # print("codigo = ",fila[0])
        # print("nombre = ", fila[1])
        # print("descripcion = ", fila[2] )
        # print("tipo = ",fila[3])
        # print("cantidad = ", fila[4])
        # print("costo = ", fila[5])
        # print("observacion = ", fila[6],"\n")
    listado.sort()
    conexion.close()
    return listado
    
def modificar(codigo, nombre, descripcion, tipo, cantidad, costo, observacion):
    conexion, cursor = conectar()
    sql = """
        UPDATE agenda SET nombre=?, descripcion=?, tipo=?, cantidad=?, costo=?, observacion=? WHERE codigo=?
    """
    cursor.execute(sql, (nombre, descripcion, tipo, cantidad, costo, observacion, codigo))
    conexion.commit()
    conexion.close()

def borrar(codigo):
    conexion, cursor = conectar()
    sql = "DELETE from agenda where codigo="+str(codigo)
    cursor.execute(sql)
    cursor.close()
    print("Registro borrado exitosamente")
    conexion.commit()
    conexion.close()
