from Tkinter import * # Se importa la libreria de TKINTER

root=Tk() # Root muestra la ventana principal

VentanaSuperior=Frame (root) # Dividimos la ventana principal en dos y esta es la SUPERIOR
VentanaSuperior.pack() #ESTE COMANDO DE pack.(), siempre se utilizara para empaquetar

VentanaInferior= Frame(root) #Venta inferior
VentanaInferior.pack(side=BOTTOM)

Boton1= Button(VentanaSuperior, text="Boton 1", fg="red")
Boton2= Button(VentanaSuperior, text="Boton 2", fg="blue")
Boton3= Button(VentanaSuperior, text="Boton 3", fg="green")
Boton4= Button(VentanaInferior, text="Boton 4", fg="purple")


Boton1.pack(side= LEFT)
Boton2.pack(side= LEFT)
Boton3.pack(side= LEFT)
Boton4.pack(side= BOTTOM)




root.mainloop()# Esto hace qu ela ventana quede en un ciclo y no se cierre luego luego