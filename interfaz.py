from tkinter import *
from tkinter import messagebox

class PlantaEnergia(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.parent = master
        self.grid()
        self.ventana()
        
    def ventana(self):
        self.aux0 = Label(self, text="      ", font=("Arial", 12))
        self.aux0.grid(row=0, column=0, columnspan=4, sticky="nsew")

        self.aux1 = Label(self, text="      ", font=("Arial", 12))
        self.aux1.grid(row=0, column=1, columnspan=4, sticky="nsew")

        self.dias = Label(self, text="Días: ", font=("Arial", 12))
        self.dias.grid(row=1, column=5, columnspan=4, sticky="nsew")

        self.eDias = Entry(self, font=("Arial", 12), relief=RAISED, justify=RIGHT, borderwidth=5)
        self.eDias.grid(row=1, column=9, columnspan=4, sticky="nsew")

        self.aux2 = Label(self, text="      ", font=("Arial", 12))
        self.aux2.grid(row=0, column=13, columnspan=4, sticky="nsew")

        self.clientes = Label(self, text="Clientes: ", font=("Arial", 12))
        self.clientes.grid(row=2, column=5, columnspan=4, sticky="nsew")

        self.eClientes = Entry(self, font=("Arial", 12), relief=RAISED, justify=RIGHT, borderwidth=5)
        self.eClientes.grid(row=2, column=9, columnspan=4, sticky="nsew")

        self.porcentaje = Label(self, text="Porcentaje mínimo de MW: ", font=("Arial", 12))
        self.porcentaje.grid(row=3, column=5, columnspan=4, sticky="nsew")

        self.ePorcentaje = Entry(self, font=("Arial", 12), relief=RAISED, justify=RIGHT, borderwidth=5)
        self.ePorcentaje.grid(row=3, column=9, columnspan=4, sticky="nsew")

        self.aux3 = Label(self, text="      ", font=("Arial", 12))
        self.aux3.grid(row=4, column=0, columnspan=15, sticky="nsew")

        self.ingreso = Button(self, text="Ingresar ", font=("Arial", 12), command=self.interDatos)
        self.ingreso.grid(row=5, column=7, columnspan=4, sticky="nsew")

        self.aux4 = Label(self, text="      ", font=("Arial", 12))
        self.aux4.grid(row=6, column=0, columnspan=15, sticky="nsew")

    def interDatos(self):
        try:
            self.diasVar = int(self.eDias.get())
            self.clientesVar = int(self.eClientes.get())
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese números válidos en los campos Días y Clientes")
            return

        self.eDias.config(state="disabled")
        self.eClientes.config(state="disabled")
        self.ePorcentaje.config(state="disabled")
        self.ingreso.config(state="disabled")

        # Crear y centrar las entradas de demanda en la ventana
        fila = 7 + (15 - self.diasVar) // 2
        columna = 2 + (15 - self.clientesVar) // 2

        demanda = Label(self, text="Demanda cliente(s) por día", font=("Arial", 12))
        demanda.grid(row=7, column=0, columnspan=15, sticky="nsew")

        self.demandaEntries = []
        for dias in range(self.diasVar):
            row_entries = []
            for clientes in range(self.clientesVar):
                aux = Entry(self, font=("Arial", 12), relief=RAISED, justify=RIGHT, borderwidth=5)
                aux.grid(row=fila + dias, column=columna + clientes, sticky="nsew")
                row_entries.append(aux)
            self.demandaEntries.append(row_entries)

        self.aux5 = Label(self, text="      ", font=("Arial", 12))
        self.aux5.grid(row=fila + dias + 1, column=0, columnspan=15, sticky="nsew")

        # Crear las entradas de precio en la ventana
        precio = Label(self, text="Precios por cliente", font=("Arial", 12))
        precio.grid(row=fila + self.diasVar + 2, column=0, columnspan=15, sticky="nsew")

        filaPrecio = fila + self.diasVar + 3

        self.precioEntries = []
        for cliente in range(self.clientesVar):
            lPrecio = Label(self, text=f" Cliente {cliente + 1}", font=("Arial", 12))
            lPrecio.grid(row=filaPrecio, column=columna + cliente, sticky="w")

            ePrecio = Entry(self, font=("Arial", 12), relief=RAISED, justify=RIGHT, borderwidth=5, width=8)
            ePrecio.grid(row=filaPrecio, column=columna + cliente, sticky="e")
            self.precioEntries.append(ePrecio)

        # Crear las entradas de costo de cada central en la ventana
        
        self.aux6 = Label(self, text = "      ", font = ("Arial", 12))
        self.aux6.grid(row = filaPrecio + 1, column = 0, columnspan = 15, sticky = "nsew")
        
        filaCentrales = filaPrecio + 3
        lCentrales = Label(self, text="Costo de cada central", font=("Arial", 12))
        lCentrales.grid(row = filaCentrales - 1, column = 0, columnspan = 15, sticky = "nsew")
        
        nombresCentrales = ["Central 1", "Central 2", "Central 3"]
        
        self.costoEntries = []
        for i, nombre in enumerate(nombresCentrales):
            lCentral = Label(self, text = nombre, font=("Arial", 12))
            lCentral.grid(row = filaCentrales, column = columna + i + 1, sticky = "w")

            costoCentral = Entry(self, font=("Arial", 12), relief = RAISED, justify = RIGHT, borderwidth = 5, width = 8)
            costoCentral.grid(row = filaCentrales, column = columna + i +1, sticky="e")
            self.costoEntries.append(costoCentral)
            
        # Crear las entradas de capacidad máxima de cada central en la ventana
        
        self.aux7 = Label(self, text = "      ", font = ("Arial", 12))
        self.aux7.grid(row = filaCentrales + 1, column = 0, columnspan = 15, sticky = "nsew")
        
        filaCapacidad = filaCentrales + 3
        lCapacidad = Label(self, text="Capacidad máxima de cada central", font=("Arial", 12))
        lCapacidad.grid(row = filaCapacidad - 1, column = 0, columnspan = 15, sticky = "nsew")

        self.capacidadEntries = []
        for i, nombre in enumerate(nombresCentrales):
            lCentralCapacidad = Label(self, text = nombre, font = ("Arial", 12))
            lCentralCapacidad.grid(row = filaCapacidad, column = columna + i + 1, sticky = "w")

            capacidadCentral = Entry(self, font = ("Arial", 12), relief = RAISED, justify = RIGHT, borderwidth = 5, width = 8)
            capacidadCentral.grid(row = filaCapacidad, column = columna + i + 1, sticky = "e")
            self.capacidadEntries.append(capacidadCentral)
            
        self.aux8 = Label(self, text = "      ", font = ("Arial", 12))
        self.aux8.grid(row = filaCapacidad + 1, column = 0, columnspan = 15, sticky = "nsew")
            
        self.datos = Button(self, text="Generar", font=("Arial", 12), command=self.generarArchivo)
        self.datos.grid(row = filaCapacidad + 2, column = 1, columnspan = 17, sticky="nsew")

    def generarArchivo(self):
        try:
            N = int(self.eDias.get())
            M = int(self.eClientes.get())
            G = float(self.ePorcentaje.get())
            
            DEMANDA = [[int(entry.get()) for entry in row] for row in self.demandaEntries]
            PRECIOXCLIENTE = [float(entry.get()) for entry in self.precioEntries]
            COSTOXCENTRAL = [float(entry.get()) for entry in self.costoEntries]
            MAXXCENTRAL = [float(entry.get()) for entry in self.capacidadEntries]

            demandaS = ' |\n    '.join([', '.join(map(str, row)) for row in DEMANDA])

            with open("Datos.dzn", "w") as file:
                file.write(
                    f"% Problema de las plantas de energia, datos de prueba.\n"
                    f"% Autores:\n"
                    f"%  * Alvaro Portocarrero.  1922171.\n"
                    f"%  * Juan David Cabrera.   1924619.\n"
                    f"%  * Karen Daniela Moreno. 1922373.\n\n"
                    f"int: N = {N}; % Numero de dias.\n"
                    f"int: M = {M}; % Numero de clientes.\n\n"
                    f"float: G = {G}; % Porcentaje minimo de MW entregable a un cliente al dia.\n\n"
                    f"array [1..N, 1..M] of int: DEMANDA = \n"
                    f" [| {demandaS} |];\n\n"
                    f"array [1..M] of float: PRECIOXCLIENTE = [ {', '.join(map(str, PRECIOXCLIENTE))} ];\n\n"
                    f"array [1..3] of float: COSTOXCENTRAL = [ {', '.join(map(str, COSTOXCENTRAL))} ];\n\n"
                    f"array [1..3] of float: MAXXCENTRAL = [ {', '.join(map(str, MAXXCENTRAL))} ];"
                )

            messagebox.showinfo("Éxito", "Archivo Datos.dzn generado con éxito")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al generar el archivo: {str(e)}")

Planta = Tk()
Planta.title("Plantas de Energía")
Planta.geometry("+0+0")
Planta.resizable(False, False)
root = PlantaEnergia(Planta).grid()
Planta.mainloop()
