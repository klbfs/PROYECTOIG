from Tkinter import * # Se importa la libreria de TKINTER

root=Tk() # Root muestra la ventana principal

one= Label(root, text="One",bg="red",fg="white")
one.pack()
two= Label(root, text="two",bg="green",fg="black")
two.pack(fill=X)
three= Label(root, text="three",bg="blue",fg="black")
three.pack(side=LEFT, fill=Y)



root.mainloop()# Esto hace qu ela ventana quede en un ciclo y no se cierre luego luego