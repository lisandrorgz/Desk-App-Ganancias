from tkinter import Button, Frame, N, E, Label


class MainPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        for i in range(0, 11):
            self.grid_rowconfigure(i, weight=1)
        self.columnconfigure(0, weight=1)
        self.parent = parent
        self.controller = controller
        self.version_text = Label(self, text="version 1.0.0 Alpha", fg="grey")
        self.menuMenuprincipal()
    
    def menuMenuprincipal(self):
        label_registrar = Button(self, text="Registrar un dia",width=20,
        command=lambda:self.controller.show_frame("RegPage", True))
        label_registrar.grid(row=3, column=0)
        label_actualizar = Button(self, text="Actualizar un dia", width=20, command=lambda:self.controller.show_frame("TablePage", value=True))
        label_actualizar.grid(row=4, column=0)
        label_eliminar = Button(self, text="Eliminar un dia", width=20, command=lambda:self.controller.show_frame("TablePage", value=False))
        label_eliminar.grid(row=5, column=0)
        label_estadisticas = Button(self, text="Ver estadisticas", width=20, command=lambda:self.controller.show_frame("StatsPage"))
        label_estadisticas.grid(row=6, column=0)
        self.version_text.grid(row=7)

    



