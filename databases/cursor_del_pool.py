from .obtener_conexiones import Conexion

class CursorDelPool:
    def __init__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        #print("Inicio del método with __enter__")
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor

    def __exit__(self, tipo_excepcion, valor_excepcion, detalle_excepcion):
        #print('Se ejecuta metodo __exit__')
        if valor_excepcion:
            self._conexion.rollback()
           # print(f"Ocurrió una excepción: {valor_excepcion} {tipo_excepcion} {detalle_excepcion}")

        else:
            self._conexion.commit()
            #print("Commit de la transacción")
        
        self._cursor.close()
        Conexion.liberarConexion(self._conexion)

