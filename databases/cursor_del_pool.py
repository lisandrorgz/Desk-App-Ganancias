from .obtener_conexiones import Conexion

# Clase que abrevia el procedimiento arduo de inicar y finalizar una conexion a través del metodo enter y exit, para ser usados con un bloque with 
class CursorDelPool:
    def __init__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor

    def __exit__(self, tipo_excepcion, valor_excepcion, detalle_excepcion):
        if valor_excepcion:
            self._conexion.rollback()

        else:
            self._conexion.commit()
        self._cursor.close()
        Conexion.liberarConexion(self._conexion)

