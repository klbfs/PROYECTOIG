from Tkinter import * # Se importa la libreria de TKINTER


class Botones:

	def__init__(self, master):

		frame = Frame (master)
		frrame.pack()

		self.printButton(frame, text="Imprimir Mensaje", command=self.printMessage)
		self.printButton.pack(side=LEFT)

		self.quitButton = Button(frame, text="Salir", command=frame.quit)
		self.printButton.pack(side=LEFT)

	def printMessage(self):

		print("Wow this actually worked")


root=Tk() # Root muestra la ventana principal

b = Botones(root)

root.mainloop()# Esto hace qu ela ventana quede en un ciclo y no se cierre luego luego