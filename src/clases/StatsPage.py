from tkinter import Frame, Label, Button, CENTER
from databases.Dia_Dao import DiaDAO

class StatsPage(Frame):
    _diamayor, _comentario = "", ""
    _cont_propina, _cont_bol, _cont_turno = 0, 0, 0
    _mayor = -1


    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller
        self.text_ganancia = Label(self)
        self.text_propina =  Label(self)
        self.text_propina_dia = Label(self)
        self.volver_button = Button(self, text="Volver", command=lambda:self.controller.show_frame("MainPage"), width=10)
        self.calculos()
        self.cfg()

    
    def cfg(self):
        for i in range(0,8):
            self.rowconfigure(i, weight=1)
        self.columnconfigure(0, weight=1)
        self.text_ganancia.grid(row=2,pady=10)
        self.text_propina.grid(row=3,pady=10)
        self.text_propina_dia.grid(row=4,pady=10)
        self.volver_button.grid(row=6,pady=10)

    def calculos(self, obj=None):
        if obj:
             self._cont_propina -= float(obj.ganancia)
             if obj.doble_turno:
                  self._cont_turno -= 6000
             else:
                  self._cont_turno -= 3000
        reg = DiaDAO.seleccionar()
        if reg == []:
             self._diamayor, self._comentario = "", ""
             self._cont_propina, self._cont_bol, self._cont_turno, self._mayor = 0, 0, 0, -1
        for i in reg:
            par = float(i.ganancia)
            if i.doble_turno:
                    self._cont_turno += 6000
            else:
                self._cont_turno += 3000

            if par > self._mayor:
                self._mayor = par
                self._diamayor = i.fecha
                self._comentario = i.comentario
                self._cont_bol += 1
            self._cont_propina += par
        self.text_ganancia.config(text=f"Ganancias totales: ${int(self._cont_propina + self._cont_turno)}")
        self.text_propina.config(text=f"Ganancias propina: ${int(self._cont_propina)}")
        self.text_propina_dia.config(text=f"El dia que mas propina se ganó: {self._diamayor} con ${(self._mayor)}")


