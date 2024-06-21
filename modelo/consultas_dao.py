from .conexiondb import Connector
import sqlite3


def crear_tabla():
    conn = Connector()
    sql = '''
    CREATE TABLE IF NOT EXISTS usuarios (
        id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre VARCHAR(100) NOT NULL,
        apellido VARCHAR(100) NOT NULL,
        email VARCHAR(100) NOT NULL UNIQUE,
        pelicula_id INTEGER,
        FOREIGN KEY (pelicula_id) REFERENCES peliculas(id_pelicula)
    );

    CREATE TABLE IF NOT EXISTS peliculas (
        id_pelicula INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo VARCHAR(100) NOT NULL,
        descripcion VARCHAR(200) NOT NULL,
        duracion INTEGER,
        genero_id INTEGER,
        FOREIGN KEY (genero_id) REFERENCES generos(id_genero)
    );

    CREATE TABLE IF NOT EXISTS generos (
        id_genero INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre VARCHAR(100) NOT NULL
    );
    '''
    try:
        conn.cursor.executescript(sql)
        conn.cerrar_connect()
        print("Tablas creadas exitosamente")
    except sqlite3.Error as e:
        print(f"Error al crear las tablas: {e}")

class Peliculas:
    def __init__(self, titulo, descripcion, duracion, genero_id):
        self.id_pelicula = None
        self.titulo = titulo
        self.descripcion = descripcion
        self.duracion = duracion
        self.genero_id = genero_id

    def __str__(self):
        return f'Pelicula: {self.titulo}, Descripcion: {self.descripcion}, Duracion: {self.duracion}, Genero: {self.genero_id}'


def listar_generos():
    conn = Connector()
    listar_generos = []
    sql = """
        SELECT * FROM generos
        """
    try:
        conn.cursor.execute(sql)
        listar_generos = conn.cursor.fetchall()
        conn.cerrar_connect()

    except sqlite3.Error as e:
        print(f"Error al listar los géneros: {e}")
    return listar_generos


def guardar_pelicula(pelicula):
    conn = Connector()
    sql =f"""
        INSERT INTO peliculas (titulo, descripcion, duracion, genero_id)
        VALUES (?, ?, ?, ?)
    """
    try:
        conn.cursor.execute(sql, (pelicula.titulo, pelicula.descripcion, pelicula.duracion, pelicula.genero_id))
        conn.cerrar_connect()
        print("Película guardada exitosamente")
    except sqlite3.Error as e:
        print(f"Error al guardar la película: {e}")

def listar_peliculas():
    conn = Connector()
    listar_peliculas = []
    sql = """
        SELECT * FROM peliculas as p 
        INNER JOIN generos as g ON p.genero_id = g.id_genero
        """
    try:
        conn.cursor.execute(sql)
        listar_peliculas = conn.cursor.fetchall()
        conn.cerrar_connect()
    except sqlite3.Error as e:
        print(f"Error al listar las películas: {e}")
    return listar_peliculas


def editar_pelicula(pelicula, id):
    conn = Connector()

    sql = f"""
            UPDATE  peliculas
            SET titulo = '{pelicula.titulo}', descripcion = '{pelicula.descripcion}', duracion = '{pelicula.duracion}', genero_id = {pelicula.genero_id}
            WHERE id_pelicula = {id};
            """

    conn.cursor.execute(sql)
    conn.cerrar_connect()


def borrar_pelicula(id):
    conn = Connector()
    sql = f"""
        DELETE FROM peliculas
        WHERE id_pelicula = {id};
        """
    conn.cursor.execute(sql)
    conn.cerrar_connect()
