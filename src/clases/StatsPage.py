from tkinter import Frame, Label, Button, CENTER
from databases.Dia_Dao import DiaDAO

# Pagina de estadisticas
class StatsPage(Frame):      

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller
        self._diamayor, self._comentario = "", ""
        self._cont_propina, self._cont_turno = 0, 0
        self._mayor = -1
        self.text_ganancia = Label(self)
        self.text_propina = Label(self)
        self.text_propina_dia = Label(self)
        self.empty = Label(self)
        self.volver_button = Button(self, text="Volver", command=lambda: self.controller.mostrar_frame("MainPage"), width=10)
        self.reg = self.controller.frames["TablePage"].items
        self.calculos()
        self.cfg()

    # Busca el objeto que contenga la ganancia mayor y la reemplaza
    def busqueda_binaria_mayor(self, obj):
            if obj is None:        
                bajo = 0
                alto = len(self.reg) - 1
                while bajo <= alto:
                    medio = (bajo + alto) // 2
                    valor = int(self.controller.frames["TablePage"].items[medio][4])   
                    if valor > self._mayor:
                        self._mayor = valor    
                        self._diamayor = self.controller.frames["TablePage"].items[medio][2]
                        self._comentario = self.controller.frames["TablePage"].items[medio][3]
                        break
                    elif valor < self._mayor:
                        bajo = medio + 1
                    else:
                        alto = medio - 1
                
            # En caso de que ya haya un mayor, evalua si el nuevo objeto es mayor que el actual
            else:
                valor = int(obj.ganancia)
                if valor >= self._mayor:
                    self._mayor = valor
                    self._diamayor = obj.fecha

    # Muestra los widgets
    def cfg(self):
        self.empty.pack(pady=45)
        self.text_ganancia.pack()
        self.text_propina.pack(pady=10)
        self.text_propina_dia.pack()
        self.volver_button.pack(pady=30)

    # Incrementa y decrementa contadores segun el valor de los parametros pasados, por si se registro/modifico/elimino un registro
    def contar_turnos(self, item, valor):
        if valor is None:
            reg = self.controller.frames["TablePage"].items
            for i in reg:
                self._cont_propina += int(i[4])
                if i[5]:
                    self._cont_turno += 6000
                else:
                    self._cont_turno += 3000
        else:
            if valor:
                if item.doble_turno:
                    self._cont_turno += 6000
                else:
                    self._cont_turno += 3000
                self._cont_propina += float(item.ganancia)
            else:
                if item.doble_turno:
                    self._cont_turno -= 6000
                else:
                    self._cont_turno -= 3000
                self._cont_propina -= float(item.ganancia)

    # Funcion principal del frame, obtiene la informacion
    def calculos(self, obj=None, contar=None):
        self.busqueda_binaria_mayor(obj=obj)
        self.contar_turnos(item=obj, valor=contar)
        self.text_ganancia.config(text=f"Ganancias totales: ${int(self._cont_propina + self._cont_turno)}")        
        self.text_propina.config(text=f"Ganancias propina: ${int(self._cont_propina)}")        
        self.text_propina_dia.config(text=f"El dia que mas propina se ganó: {self._diamayor} con ${(self._mayor)}")
