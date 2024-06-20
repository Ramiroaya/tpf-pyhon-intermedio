from conexiondb import Connector


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
    def __init__(self, titulo, descripcion, duracion, genero):
        self.id_pelicula = None
        self.titulo = titulo
        self.descripcion = descripcion
        self.duracion = duracion
        self.genero = genero

    def __str__(self):
        return f'Pelicula: {self.titulo}, Descripcion: {self.descripcion}, Duracion: {self.duracion}, Genero: {self.genero}'

def guardar_pelicula(pelicula):
    conn = Connector()
    sql = """
        INSERT INTO peliculas (titulo, descripcion, duracion, genero_id)
        VALUES (?, ?, ?, ?)
    """
    try:
        conn.cursor.execute(sql, (pelicula.titulo, pelicula.descripcion, pelicula.duracion, pelicula.genero))
        conn.cerrar_connect()
        print("Película guardada exitosamente")
    except sqlite3.Error as e:
        print(f"Error al guardar la película: {e}")

def listar_peliculas():
    conn = Connector()
    listar_peliculas = []
    sql = """
        SELECT p.id_pelicula, p.titulo, p.descripcion, p.duracion, g.nombre as genero 
        FROM peliculas as p 
        INNER JOIN generos as g ON p.genero_id = g.id_genero
    """
    try:
        conn.cursor.execute(sql)
        listar_peliculas = conn.cursor.fetchall()
        conn.cerrar_connect()
        return listar_peliculas
    except sqlite3.Error as e:
        print(f"Error al listar las películas: {e}")
        return []