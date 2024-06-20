import sqlite3

class Connector:
    def __init__(self):
        self.base_datos = 'ddbb/web_peliculas.db'
        try:
            self.conn = sqlite3.connect(self.base_datos)
            self.cursor = self.conn.cursor()
            print("Conexión exitosa a la base de datos")
        except sqlite3.Error as e:
            print(f"Error al conectar a la base de datos: {e}")

    def cerrar_connect(self):
        try:
            self.conn.commit()
            self.conn.close()
            print("Conexión cerrada correctamente")
        except sqlite3.Error as e:
            print(f"Error al cerrar la conexión a la base de datos: {e}")