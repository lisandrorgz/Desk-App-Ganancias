from psycopg2 import pool
import sys

class Conexion:
    _DATABASE = 'railway'
    _USERNAME = 'postgres'
    _PASSWORD = 'Ozr5kNh0KD1OyCfEj2mv'
    _DB_PORT = '6186'
    _HOST = 'containers-us-west-41.railway.app'
    _MIN_CON = 1
    _MAX_CON = 5 
    _pool = None
    


    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON, cls._MAX_CON,
                                                      host = cls._HOST,
                                                      user = cls._USERNAME,
                                                      password = cls._PASSWORD,
                                                      port = cls._DB_PORT,
                                                      database = cls._DATABASE)
                #print(f'Creación del pool exitosa: {cls._pool}')
                return cls._pool
            except Exception as e:
                #print(f'Ocurrió un error al obtener el pool {e}')
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()
        #print(f'Conexión obtenida del pool: {conexion}')
        return conexion

    @classmethod
    def liberarConexion(cls, conexion):
        cls.obtenerPool().putconn(conexion)
        #print(f'Regresamos la conexión al pool: {conexion}')

    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall()

