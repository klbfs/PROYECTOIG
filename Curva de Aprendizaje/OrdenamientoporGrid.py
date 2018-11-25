from Tkinter import * # Se importa la libreria de TKINTER

root=Tk() # Root muestra la ventana principal

label_1 = Label(root, text= "Nombre")
label_2 = Label(root, text= "Contrasena")

entry_1 = Entry(root)
entry_2 = Entry(root)

label_1.grid(row=0, column=0, sticky=E)
label_2.grid(row=1, column=0, sticky=E)

entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)

c = Checkbutton(root, text="Mantener mi Sesion")
c.grid(columnspan=2)

Boton1=Button(text="Iniciar Sesion", fg="white", bg="red")
Boton1.grid(row=4,columnspan=2)


root.mainloop()# Esto hace qu ela ventana quede en un ciclo y no se cierre luego luego