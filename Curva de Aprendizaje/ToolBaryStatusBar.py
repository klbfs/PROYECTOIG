from Tkinter import * # Se importa la libreria de TKINTER

def doNothing():
	print("ok ok I wont")


def doSomething():
	print("Lets Do It")

root=Tk() # Root muestra la ventana principal

menu = Menu(root)
root.config(menu=menu)

submenu = Menu(menu)

menu.add_cascade(label="File", menu=submenu)
submenu.add_command(label="New Proyect", command= doNothing)
submenu.add_command(label="Open_Proyect", command= doNothing)
submenu.add_separator()
submenu.add_command(label="Exit", command= doNothing)

editMenu= Menu(menu)

menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Redo", command= doSomething)

#TOOLBAR ****

toolbar = Frame(root, bg="blue")
insertar = Button(toolbar, text= "Insertar Imagen", command= doNothing)
insertar.pack(side=LEFT, padx=2, pady=2)
insertar1 = Button(toolbar, text= "Guardar", command= doNothing)
insertar1.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)


#STATUS BAR****

status = Label(root, text="Preparing to do Nothing", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)


root.mainloop()# Esto hace qu ela ventana quede en un ciclo y no se cierre luego luego