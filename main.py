import tkinter as tk
from user.vista import Frame, barrita_menu, centrar_ventana

def main():
    ventana = tk.Tk()
    ventana.title('Listado Peliculas')
    #ventana.iconbitmap('img/videocamara.ico')
    ventana.resizable(0,0)
    centrar_ventana(ventana, 800, 600)
    barrita_menu(ventana)
    app = Frame(root = ventana)

    ventana.mainloop()



if __name__ == '__main__':
    main()