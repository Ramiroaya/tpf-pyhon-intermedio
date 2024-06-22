

import tkinter as tk
from user.vista_peliculas import Frame_peliculas
from user.vista_usuarios import Frame_usuarios

def centrar_ventana(root, ancho, alto):
    ancho_pantalla = root.winfo_screenwidth()
    alto_pantalla = root.winfo_screenheight()
    x = (ancho_pantalla // 2) - (ancho // 2)
    y = (alto_pantalla // 2) - (alto // 2)
    root.geometry(f'{ancho}x{alto}+{x}+{y}')

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Gestión de Usuarios y Películas')
        self.geometry('1000x700')
        centrar_ventana(self, 1100, 700)
        self.vista_peliculas = None
        self.vista_usuarios = None
        self.mostrar_vista_usuarios()

    def mostrar_vista_usuarios(self):
        if self.vista_peliculas:
            self.vista_peliculas.pack_forget()
        self.vista_usuarios = Frame_usuarios(self)
        self.vista_usuarios.pack()

    def mostrar_vista_peliculas(self):
        if self.vista_usuarios:
            self.vista_usuarios.pack_forget()
        self.vista_peliculas = Frame_peliculas(self)
        self.vista_peliculas.pack()

if __name__ == '__main__':
    app = MainApp()
    app.mainloop()
