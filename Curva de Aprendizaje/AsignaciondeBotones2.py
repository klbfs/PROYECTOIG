from Tkinter import * # Se importa la libreria de TKINTER

root=Tk() # Root muestra la ventana principal


def lefclick(event):
	print("Izquierda")

def middleclick(event):
	print("Centro")

def rightclick(event):
	print("Derecha")


frame = Frame(root, width=300, height=250)
frame.pack()

frame.bind("<Button-1>", lefclick)
frame.bind("<Button-2>", middleclick)
frame.bind("<Button-3>", rightclick)

root.mainloop()# Esto hace qu ela ventana quede en un ciclo y no se cierre luego luego