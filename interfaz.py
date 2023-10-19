from tkinter import *
from tkinter import messagebox


class Pycalc(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.parent = master
        self.grid()
        self.createWidgets()
        
    def createWidgets(self):
        
        self.aux0 = Label(self, text = "      ", font = ("Arial", 12))
        self.aux0.grid(row = 0, column = 0, columnspan = 4, sticky = "nsew")
        
        self.aux1 = Label(self, text = "      ", font = ("Arial", 12))
        self.aux1.grid(row = 1, column = 0, columnspan = 4, sticky = "nsew")
        
        self.dias = Label(self, text = "Días: ", font = ("Arial", 12))
        self.dias.grid(row = 1, column = 1, columnspan = 4, sticky = "nsew")
        
        self.eDia = Entry(self, font = ("Arial", 12), relief = RAISED, justify = RIGHT, borderwidth = 5)
        self.eDia.grid(row = 1, column = 5, columnspan = 4, sticky = "nsew")
        
        self.aux2 = Label(self, text = "                 ", font = ("Arial", 12))
        self.aux2.grid(row = 1, column = 10, columnspan = 4, sticky = "nsew")
        
        self.costos = Label(self, text = "Costos: ", font = ("Arial", 12))
        self.costos.grid(row = 2, column = 0, columnspan = 4, sticky = "nsew")
        
        self.eCostos = Entry(self, font = ("Arial", 12), relief = RAISED, justify = RIGHT, borderwidth = 5)
        self.eCostos.grid(row = 2, column = 5, columnspan = 4, sticky = "nsew")
        
        self.capacidades = Label(self, text = "Capacidades: ", font = ("Arial", 12))
        self.capacidades.grid(row = 3, column = 0, columnspan = 4, sticky = "nsew")
        
        self.eCapacidades = Entry(self, font = ("Arial", 12), relief = RAISED, justify = RIGHT, borderwidth = 5)
        self.eCapacidades.grid(row = 3, column = 5, columnspan = 4, sticky = "nsew")
        
        self.producciones = Label(self, text = "Producciones: ", font = ("Arial", 12))
        self.producciones.grid(row = 4, column = 0, columnspan = 4, sticky = "nsew")
        
        self.eProducciones = Entry(self, font = ("Arial", 12), relief = RAISED, justify = RIGHT, borderwidth = 5)
        self.eProducciones.grid(row = 4, column = 5, columnspan = 4, sticky = "nsew")
        
        self.necesidades = Label(self, text = "Necesidades: ", font = ("Arial", 12))
        self.necesidades.grid(row = 5, column = 0, columnspan = 4, sticky = "nsew")
        
        self.eNecesidades = Entry(self, font = ("Arial", 12), relief = RAISED, justify = RIGHT, borderwidth = 5)
        self.eNecesidades.grid(row = 5, column = 5, columnspan = 4, sticky = "nsew")
        
        self.aux3 = Label(self, text = "      ", font = ("Arial", 12))
        self.aux3.grid(row = 6, column = 0, columnspan = 4, sticky = "nsew")
        
        self.enter = Button(self, text = "Ingresar")
        self.enter.grid(row = 7, column = 4, columnspan = 4, sticky = "nsew")
        
        self.aux3 = Label(self, text = "      ", font = ("Arial", 12))
        self.aux3.grid(row = 8, column = 0, columnspan = 4, sticky = "nsew")


Planta = Tk()
Planta.title("Plantas de Energía")
Planta.resizable(False, False)
root = Pycalc(Planta).grid()
Planta.mainloop()