import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from modelo.consultas_dao import Usuarios, listar_usuarios, guardar_usuario, editar_usuario, borrar_usuario, listar_peliculas




class Frame_usuarios(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root,width=680,height=620)
        self.root = root
        self.pack(padx=20, pady=20)
        self.id_usuario = None
        self.label_form()
        self.input_form()
        self.botones_principales()
        self.mostrar_tabla()
        self.config(bg='grey')


    def editar_registro_usuario(self):
        try:
            self.id_usuario = self.tabla.item(self.tabla.selection())['text']
            self.nombre_usuario_e = self.tabla.item(self.tabla.selection())['values'][0]
            self.apellido_usuario_e = self.tabla.item(self.tabla.selection())['values'][1]
            self.email_usuario_e = self.tabla.item(self.tabla.selection())['values'][2]
            self.peliculas_vistas_e = self.tabla.item(self.tabla.selection())['values'][3]

            self.habilitar_campos()
            self.nombre.set(self.nombre_usuario_e)
            self.apellido.set(self.apellido_usuario_e)
            self.email.set(self.email_usuario_e)
            self.entry_peliculas.current(self.peliculas_vistas_e)

        except:
            pass


           
    def eliminar_registro_usuario(self):
        try:
            self.id_usuario = self.tabla.item(self.tabla.selection())['text']
            self.nombre_usuario = self.tabla.item(self.tabla.selection())['values'][0]
           
            respuesta = messagebox.askyesno("Confirmar Borrado", f"¿Estás seguro de que quieres borrar al usuario '{self.nombre_usuario}'?")
            if respuesta:
                borrar_usuario(int(self.id_usuario))
                self.mostrar_tabla()
                self.id_usuario = None
        except IndexError:
            messagebox.showerror("Error", "No se seleccionó ningun usuario")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo borrar el usuario: {e}")



    def label_form(self):
        self.label_nombre = tk.Label(self, text='Nombre: ')
        self.label_nombre.config(font=('Arial',12,'bold'))
        self.label_nombre.grid(row=0, column=0,padx=10,pady=10)

        self.label_nombre = tk.Label(self, text='Apellido: ')
        self.label_nombre.config(font=('Arial',12,'bold'))
        self.label_nombre.grid(row=1, column=0,padx=10,pady=10)


        self.label_nombre = tk.Label(self, text='Email: ')
        self.label_nombre.config(font=('Arial',12,'bold'))
        self.label_nombre.grid(row=2,column=0,padx=10,pady=10)

        self.label_nombre = tk.Label(self, text='Peliculas vistas: ')
        self.label_nombre.config(font=('Arial',12,'bold'))
        self.label_nombre.grid(row=3,column=0,padx=10,pady=10)



    def input_form(self):
        self.nombre = tk.StringVar()
        self.entry_nombre = tk.Entry(self,textvariable=self.nombre)
        self.entry_nombre.config(width=70, state='disabled')
        self.entry_nombre.grid(row= 0, column=1,padx=10,pady=10, columnspan='2')

        self.apellido = tk.StringVar()
        self.entry_apellido = tk.Entry(self,textvariable=self.apellido)
        self.entry_apellido.config(width=70, state='disabled')
        self.entry_apellido.grid(row= 1, column=1,padx=10,pady=10, columnspan='2')


        self.email = tk.StringVar()
        self.entry_email = tk.Entry(self,textvariable=self.email)
        self.entry_email.config(width=70, state='disabled')
        self.entry_email.grid(row= 2, column=1,padx=10,pady=10, columnspan='2')

        self.lista_peliculas = listar_peliculas()

        #Concatenamos el nuevo array
        self.peliculas = ['Seleccione una'] + [p[1] for p in self.lista_peliculas]
        self.entry_peliculas = ttk.Combobox(self, state="readonly")
        self.entry_peliculas['values'] = self.peliculas
        self.entry_peliculas.current(0)
        self.entry_peliculas.config(width=70, font=('Arial',12))
        self.entry_peliculas.bind("<<ComboboxSelected>>")
        self.entry_peliculas.grid(row= 3, column=1,padx=10,pady=10, columnspan='2')
        


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

        self.btn_volver = tk.Button(self, text='Ir al menú de Peliculas', command=self.volver_menu_peliculas)
        self.btn_volver.config(width=20, font=('Arial', 12, 'bold'), fg='#FFFFFF',
                               bg='#008000', cursor='hand2', activebackground='#70DB70', activeforeground='#000000')
        self.btn_volver.grid(row=4, column=3, padx=10, pady=10)

    def habilitar_campos(self):
        self.entry_nombre.config(state='normal')
        self.entry_apellido.config(state='normal')
        self.entry_email.config(state='normal')
        
        self.btn_modi.config(state='normal')
        self.btn_cance.config(state='normal')
        self.btn_alta.config(state='disabled')

    def bloquear_campos(self):
        self.entry_peliculas.current(0)
        self.entry_nombre.config(state='disabled')
        self.entry_apellido.config(state='disabled')
        self.entry_email.config(state='disabled')
        
        self.btn_modi.config(state='disabled')
        self.btn_cance.config(state='disabled')

        self.nombre.set('')
        self.apellido.set('')
        self.email.set('')
        self.id_usuario = None
        self.btn_alta.config(state='normal')

    def guardar_campos(self):
        usuario = Usuarios(
            self.nombre.get(),
            self.apellido.get(),
            self.email.get(),
            self.entry_peliculas.current()
        )
        if self.id_usuario == None:
            guardar_usuario(usuario)
        else:
            editar_usuario(usuario, int(self.id_usuario))

        self.mostrar_tabla()
        self.bloquear_campos()

    

    def mostrar_tabla(self):
        self.lista_usuario = listar_usuarios()
        #print(listar_usuarios())
        self.lista_usuario.reverse() #Invierte el orden , asi nos muestra por pantalla a partir del 1.
        self.tabla = ttk.Treeview(self, columns=('Nombre', 'Apellido', 'Email', 'Peliculas'))
        self.tabla.grid(row=5, column=0,columnspan=4,sticky='nse')

        self.scroll = ttk.Scrollbar(self, orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=5, column=4, sticky='nse')
        self.tabla.configure(yscrollcommand=self.scroll.set)

        self.tabla.heading('#0',text='ID')
        self.tabla.heading('#1',text='Nombre')
        self.tabla.heading('#2',text='Apellido')
        self.tabla.heading('#3',text='Email')
        self.tabla.heading('#4',text='Peliculas Vistas')

        for u in self.lista_usuario:
            self.tabla.insert('',0,text=u[0], values = (u[1],u[2],u[3],u[4]))

        #Creamos los botones de Editar y Borrar
        self.btn_editar = tk.Button(self, text='Editar',command=self.editar_registro_usuario)
        self.btn_editar.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' ,
        bg='#0D2A83',cursor='hand2',activebackground='#7594F5',activeforeground='#000000')
        self.btn_editar.grid(row= 6, column=1,padx=10,pady=10)

        self.btn_borrar = tk.Button(self, text='Borrar', command=self.eliminar_registro_usuario)
        self.btn_borrar.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' ,
        bg='#A90A0A',cursor='hand2',activebackground='#F35B5B',activeforeground='#000000')
        self.btn_borrar.grid(row= 6, column=2,padx=10,pady=10)

    
    def volver_menu_peliculas(self):
        self.pack_forget()
        self.root.mostrar_vista_peliculas()