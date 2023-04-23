from tkinter import Button, Frame, N, E, Label

# Pagina principal
class MainPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        # Grid del frame
        for i in range(0, 11):
            self.grid_rowconfigure(i, weight=1)
        self.columnconfigure(0, weight=1)
         # parent: Representa Widget padre
        self.parent = parent
        # controller: Instancia de objeto de Appclass, contiene la funcion para navegar entre otros frames
        self.controller = controller
        self.version = Label(self, text="version 1.0.0 Beta", fg="grey")
        self.menuMenuprincipal()
    
    # Botones y acciones
    def menuMenuprincipal(self):
        label_registrar = Button(self, text="Registrar un dia",width=20,
        command=lambda:self.controller.mostrar_frame("RegPage", True))
        label_registrar.grid(row=3, column=0)
        label_actualizar = Button(self, text="Actualizar un dia", width=20, command=lambda:self.controller.mostrar_frame("TablePage", valor=True))
        label_actualizar.grid(row=4, column=0)
        label_eliminar = Button(self, text="Eliminar un dia", width=20, command=lambda:self.controller.mostrar_frame("TablePage", valor=False))
        label_eliminar.grid(row=5, column=0)
        label_estadisticas = Button(self, text="Ver estadisticas", width=20, command=lambda:self.controller.mostrar_frame("StatsPage"))
        label_estadisticas.grid(row=6, column=0)
        self.version.grid(row=7)

    



