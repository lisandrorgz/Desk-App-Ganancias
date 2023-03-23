from .Dia import Dia 
from .cursor_del_pool import CursorDelPool

class DiaDAO:
    _SELECCIONAR = 'SELECT * FROM dia ORDER BY id'
    _INSERTAR = 'INSERT INTO dia(nombre, fecha, comentario, ganancia, doble_turno) VALUES(%s,%s,%s,%s, %s)'
    _ACTUALIZAR = 'UPDATE dia SET nombre=%s, fecha=%s, comentario=%s, ganancia=%s, doble_turno=%s WHERE id=%s'
    _ELIMINAR = 'DELETE FROM dia WHERE id=%s' 

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            dias = []
            for registro in registros:
                persona = Dia(registro[0],registro[1],registro[2],registro[3],registro[4], registro[5])
                dias.append(persona)
            return dias

    @classmethod
    def insertar(cls, dia):
        with CursorDelPool() as cursor:      
            valores = (dia.nombre, dia.fecha, dia.comentario, dia.ganancia, dia.doble_turno)
            cursor.execute(cls._INSERTAR, valores)
            #print("Dia Insertado")
            return cursor.rowcount

    @classmethod
    def actualizar(cls, dia):
        with CursorDelPool() as cursor:
            valores = (dia.nombre, dia.fecha, dia.comentario, dia.ganancia, dia.doble_turno, dia.id)
            cursor.execute(cls._ACTUALIZAR, valores)
            #print(f"Dia actualizado {dia.id}")
            return cursor.rowcount

    @classmethod
    def eliminar(cls,dia):
        with CursorDelPool() as cursor:
            valores = (dia.id,)
            cursor.execute(cls._ELIMINAR, valores)
            #print(f"Dia eliminado: {dia.id}")
            return cursor.rowcount





    
