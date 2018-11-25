from Tkinter import * # Se importa la libreria de TKINTER

root=Tk() # Root muestra la ventana principal

def printName(event):
	print("Hola, mi nombre es Luis")

buttom_1=Button(root, text="Imprimir mi nombre")
buttom_1.pack()
buttom_1.bind("<Button-1>",printName)# Evento que va a ocurrir // Que funcion se llamara

root.mainloop()# Esto hace qu ela ventana quede en un ciclo y no se cierre luego luego