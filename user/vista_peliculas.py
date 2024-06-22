import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from modelo.consultas_dao import Peliculas, listar_generos, listar_peliculas, guardar_pelicula, editar_pelicula, borrar_pelicula

def centrar_ventana(root, ancho, alto):
    ancho_pantalla = root.winfo_screenwidth()
    alto_pantalla = root.winfo_screenheight()
    x = (ancho_pantalla // 2) - (ancho // 2)
    y = (alto_pantalla // 2) - (alto // 2)
    
    root.geometry(f'{ancho}x{alto}+{x}+{y}')


def barrita_menu(root):
    barra = tk.Menu(root)
    root.config(menu = barra, width = 1000, height = 700)
    menu_inicio = tk.Menu(barra, tearoff=0)

    #Niveles#

    #Principal

    barra.add_cascade(label='Inicio', menu = menu_inicio)
    barra.add_cascade(label='Consultas', menu = menu_inicio)
    barra.add_cascade(label='Acerca de..', menu = menu_inicio)
    barra.add_cascade(label='Ayuda', menu = menu_inicio)

    #Submenu

    menu_inicio.add_command(label='Conectar DB')
    menu_inicio.add_command(label='Desconectar DB')
    menu_inicio.add_command(label='Salir', command =root.destroy)


class Frame_peliculas(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root,width=680,height=620)
        self.root = root
        self.pack(padx=20, pady=20)
        self.id_peli = None        
        self.label_form()
        self.input_form()
        self.botones_principales()
        self.mostrar_tabla()
        self.config(bg='grey')

    def editar_registro(self):
        try:
            self.id_peli = self.tabla.item(self.tabla.selection())['text']
            self.titulo_peli_e = self.tabla.item(self.tabla.selection())['values'][0]
            self.descripcion_peli_e = self.tabla.item(self.tabla.selection())['values'][1]
            self.duracion_peli_e = self.tabla.item(self.tabla.selection())['values'][2]
            self.genero_id_peli_e = self.tabla.item(self.tabla.selection())['values'][3]

            self.habilitar_campos()
            self.titulo.set(self.titulo_peli_e)
            self.descripcion.set(self.descripcion_peli_e)
            self.duracion.set(self.duracion_peli_e)
            self.entry_genero.current(self.generos.index(self.genero_id_peli_e))

        except:
            pass


           
    def eliminar_registro(self):
        try:
            self.id_peli = self.tabla.item(self.tabla.selection())['text']
            self.titulo_peli = self.tabla.item(self.tabla.selection())['values'][0]
           
            respuesta = messagebox.askyesno("Confirmar Borrado", f"¿Estás seguro de que quieres borrar la película '{self.titulo_peli}'?")
            if respuesta:
                borrar_pelicula(int(self.id_peli))
                self.mostrar_tabla()
                self.id_peli = None
        except IndexError:
            messagebox.showerror("Error", "No se seleccionó ninguna película")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo borrar la película: {e}")



    def label_form(self):
        self.label_nombre = tk.Label(self, text='Titulo: ')
        self.label_nombre.config(font=('Arial',12,'bold'))
        self.label_nombre.grid(row=0, column=0,padx=10,pady=10)

        self.label_nombre = tk.Label(self, text='Descripcion: ')
        self.label_nombre.config(font=('Arial',12,'bold'))
        self.label_nombre.grid(row=1, column=0,padx=10,pady=10)


        self.label_nombre = tk.Label(self, text='Duracion: ')
        self.label_nombre.config(font=('Arial',12,'bold'))
        self.label_nombre.grid(row=2,column=0,padx=10,pady=10)

        self.label_nombre = tk.Label(self, text='Genero: ')
        self.label_nombre.config(font=('Arial',12,'bold'))
        self.label_nombre.grid(row=3,column=0,padx=10,pady=10)



    def input_form(self):
        self.titulo = tk.StringVar()
        self.entry_titulo = tk.Entry(self,textvariable=self.titulo)
        self.entry_titulo.config(width=70, state='disabled')
        self.entry_titulo.grid(row= 0, column=1,padx=10,pady=10, columnspan='2')

        self.descripcion = tk.StringVar()
        self.entry_descripcion = tk.Entry(self,textvariable=self.descripcion)
        self.entry_descripcion.config(width=70, state='disabled')
        self.entry_descripcion.grid(row= 1, column=1,padx=10,pady=10, columnspan='2')

        self.duracion = tk.StringVar()
        self.entry_duracion = tk.Entry(self,textvariable=self.duracion)
        self.entry_duracion.config(width=70, state='disabled')
        self.entry_duracion.grid(row= 2, column=1,padx=10,pady=10, columnspan='2')


        #Limpiamos la lista de tuplas que nos retorna la funcion
        x = listar_generos()
        #print (x)
        y = []
        for i in x:
            y.append(i[1])
        #print(y)

        #Concatenamos el nuevo array
        self.generos = ['Seleccione uno'] + y
        self.entry_genero = ttk.Combobox(self, state="readonly")
        self.entry_genero['values'] = self.generos
        self.entry_genero.current(0)
        self.entry_genero.config(width=25, state='disabled',font=('Arial',12))
        self.entry_genero.bind("<<ComboboxSelected>>")
        self.entry_genero.grid(row= 3, column=1,padx=10,pady=10, columnspan='2')


    def botones_principales(self):
        self.btn_alta = tk.Button(self, text='Nuevo', command=self.habilitar_campos)
        self.btn_alta.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' ,
        bg='#1C500B',cursor='hand2',activebackground='#3FD83F',activeforeground='#000000')
        self.btn_alta.grid(row= 4, column=0,padx=10,pady=10)

        self.btn_modi = tk.Button(self, text='Guardar', command=self.guardar_campos)
        self.btn_modi.config(command=self.guardar_campos,width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' ,
        bg='#0D2A83',cursor='hand2',activebackground='#7594F5',activeforeground='#000000')
        self.btn_modi.grid(row= 4, column=1,padx=10,pady=10)

        self.btn_cance = tk.Button(self, text='Cancelar', command=self.bloquear_campos)
        self.btn_cance.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' ,
        bg='#A90A0A',cursor='hand2',activebackground='#F35B5B',activeforeground='#000000')
        self.btn_cance.grid(row= 4, column=2,padx=10,pady=10)

        self.btn_volver = tk.Button(self, text='Volver al menú de Usuarios', command=self.volver_menu_usuarios)
        self.btn_volver.config(width=20, font=('Arial', 12, 'bold'), fg='#FFFFFF',
                               bg='#008000', cursor='hand2', activebackground='#70DB70', activeforeground='#000000')
        self.btn_volver.grid(row=4, column=3, padx=10, pady=10)

    


    def habilitar_campos(self):
        self.entry_titulo.config(state='normal')
        self.entry_descripcion.config(state='normal')
        self.entry_genero.config(state='normal')
        self.entry_duracion.config(state='normal')

        self.btn_modi.config(state='normal')
        self.btn_cance.config(state='normal')
        self.btn_alta.config(state='disabled')

    def bloquear_campos(self):
        self.entry_genero.current(0)
        self.entry_titulo.config(state='disabled')
        self.entry_descripcion.config(state='disabled')
        self.entry_genero.config(state='disabled')
        self.entry_duracion.config(state='disabled')

        self.btn_modi.config(state='disabled')
        self.btn_cance.config(state='disabled')
        
        self.titulo.set('')
        self.descripcion.set('')
        self.duracion.set('')
        self.id_peli = None
        self.btn_alta.config(state='normal')

    def guardar_campos(self):
        pelicula = Peliculas(
            self.titulo.get(),
            self.descripcion.get(),
            self.duracion.get(),
            self.entry_genero.current()
        )
        if self.id_peli == None:
            guardar_pelicula(pelicula)
        else:
            editar_pelicula(pelicula, int(self.id_peli))

        self.mostrar_tabla()
        self.bloquear_campos()

    

    def mostrar_tabla(self):
        self.lista_p = listar_peliculas()
        #print(listar_peliculas())
        self.lista_p.reverse() #Invierte el orden , asi nos muestra por pantalla a partir del 1.
        self.tabla = ttk.Treeview(self, columns=('Titulo', 'Descripcion', 'Duracion', 'Genero'))
        self.tabla.grid(row=5, column=0,columnspan=4,sticky='nse')

        self.scroll = ttk.Scrollbar(self, orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=5, column=4, sticky='nse')
        self.tabla.configure(yscrollcommand=self.scroll.set)

        self.tabla.heading('#0',text='ID')
        self.tabla.heading('#1',text='Titulo')
        self.tabla.heading('#2',text='Descripcion')
        self.tabla.heading('#3',text='Duración')
        self.tabla.heading('#4',text='Género')

        for p in self.lista_p:
            self.tabla.insert('',0,text=p[0], values = (p[1],p[2],p[3],p[4]))

        #Creamos los botones de Editar y Borrar
        self.btn_editar = tk.Button(self, text='Editar',command=self.editar_registro)
        self.btn_editar.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' ,
        bg='#0D2A83',cursor='hand2',activebackground='#7594F5',activeforeground='#000000')
        self.btn_editar.grid(row= 6, column=1,padx=10,pady=10)

        self.btn_borrar = tk.Button(self, text='Borrar', command=self.eliminar_registro)
        self.btn_borrar.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' ,
        bg='#A90A0A',cursor='hand2',activebackground='#F35B5B',activeforeground='#000000')
        self.btn_borrar.grid(row= 6, column=2,padx=10,pady=10)

    def volver_menu_usuarios(self):
        self.pack_forget()
        self.root.mostrar_vista_usuarios()