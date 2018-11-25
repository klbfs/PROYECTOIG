from Tkinter import * # Se importa la libreria de TKINTER

root=Tk() # Root muestra la ventana principal

def printName():
	print("Hola, mi nombre es Luis")

buttom_1=Button(root, text="Imprimir mi nombre",command=printName)
buttom_1.pack()

root.mainloop()# Esto hace qu ela ventana quede en un ciclo y no se cierre luego luego