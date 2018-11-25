#INEGI_GUI

from Tkinter import *

def CuentaAdmin():
	print("Clase Cuenta de Administrador")

def Clases():
	print("Actividad Economica")
	print("Buscador")
	print("Capital")
	print("Departamentos")
	print("Empresa")
	print("Estadisticas")
	print("Fundaciones")
	print("Instalaciones")
	print("Imagenes y Video")
	print("Informacion de la Empresa")
	print("Ubicacion")
	print("Redes Sociales")

def Atributos():
	print("De que clase?")

def Tecnicas_Prog():
	print("Profesor: Emiliavo Nava")
	print("Grupo 2")
	print("Horario: \n Lunes: 7:00 - 9:00 \n Miercoles: 7:00 - 9:00 \n Viernes 7:00 - 9:00")
	print("Semestre: 2019-1")
def Referencias():
	print("URL: http://www.beta.inegi.org.mx/temas/directorio/")

def MenuBusqueda():
	print("Clase Menu Busqueda")

def Lideres():
	print("Clase Lideres Empresariales")

root = Tk()

foto = PhotoImage(file="inegi.png")
etiqueta= Label(root, image=foto)
etiqueta.pack(side=TOP)

bienvenida= Label(root, text="Bienvenido a la Pagina Oficial del INEGI",bg="grey50",fg="white",  font='Helvetica 14 bold')
bienvenida.pack(side=TOP, fill=X)
modulo= Label(root, text="EMPRESAS",bg="white",fg="navy", font='Helvetica 18 bold')
modulo.pack(side=TOP, fill=X)

menu = Menu(root)
root.config(menu=menu)

subMenu1 = Menu(menu)

menu.add_cascade(label="Usuario", menu=subMenu1)
subMenu1.add_command(label="Cuenta Administrador", command= CuentaAdmin)
subMenu1.add_separator()
subMenu1.add_command(label="Salir", command= root.quit)

subMenu2= Menu(menu)

menu.add_cascade(label="Informacion Proyecto", menu=subMenu2)
subMenu2.add_command(label="Clases", command= Clases )
subMenu2.add_command(label="Atributos", command= Atributos)
subMenu2.add_separator()
subMenu2.add_command(label="Tecnicas de Programacion", command= Tecnicas_Prog)

subMenu3 = Menu(menu)

menu.add_cascade(label="INEGI", menu=subMenu3)
subMenu3.add_command(label="Referencias", command= Referencias)
subMenu3.add_separator()



#TOOLBAR ****

toolbar = Frame(root, bg="medium aquamarine")
insertar = Button(toolbar, text= "Busqueda Avanzada", command= MenuBusqueda, bg="white")
insertar.pack(side=LEFT, padx=2, pady=2)
insertar1 = Button(toolbar, text= "Lideres Empresariales", command= Lideres, bg="white")
insertar1.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)


#STATUS BAR****

status = Label(root, text="Todos los Derechos Reservados. Tecnicas de Programacion 2019", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)


root.mainloop()