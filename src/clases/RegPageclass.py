from databases.Dia_Dao import DiaDAO
from databases.Dia import Dia
from .ValidationClass import Validations
from tkinter import Label, Entry, StringVar, OptionMenu, Button, Frame, Tk, W, CENTER, LabelFrame, BOTTOM, Radiobutton, messagebox, END
from tkcalendar import DateEntry
from .showTclass import TablePage
from datetime import datetime, timezone, timedelta


# Pagina de Registro y Modificación
class RegPage(Frame, Validations):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self._Y = 135
        self._VALORES = {"Si" : True, "No" : False}
        self.parent = parent
        self.controller = controller
        self.lbframe = LabelFrame(self, text="Datos del dia")
        self.entry_nombre = Entry(self.lbframe) 
        self.label_nombre = Label(self.lbframe, text="Nombre")
        self.label_fecha = Label(self.lbframe, text="Fecha")
        self.label_comentario = Label(self.lbframe, text = "Comentario")
        self.entry_comentario = Entry(self.lbframe)
        self.label_ganancia = Label(self.lbframe, text="Ganancias")
        self.entry_ganancia = Entry(self.lbframe)
        self.label_db_turno = Label(self.lbframe, text="Doble turno?")
        self.db_turno =  StringVar(self.lbframe, "1")
        self.volver = Button(self, text="Volver", width=10, 
        command=lambda:self.volver_button())
        self.cal = DateEntry(self.lbframe, selectmode="day", year=2023, month=2, day=1, date_pattern='dd/mm/yyyy')
        self.reg_dia1 = Button(self.lbframe, width=15, justify=CENTER)
        self.cfgbuttons()

    # Posicionamiento de los elementos dentro de un grid
    def cfgbuttons(self):
        self.cal.set_date(self.controller.hoy)
        self.lbframe.pack(pady=40)
        self.label_nombre.grid(row=1, column=0, pady=10, padx=10, sticky=W)
        self.entry_nombre.grid(row=1, column=1, pady=10, padx=15, columnspan=2)
        self.label_fecha.grid(row=2, column=0, padx=10, sticky=W)
        self.cal.grid(row=2,column=1, sticky=W, padx=15)
        self.label_comentario.grid(row=3, column=0, padx=10, pady=10, sticky=W)
        self.entry_comentario.grid(row=3, column=1, padx=10, pady=10, columnspan=2)
        self.label_ganancia.grid(row=4, column=0, padx=10, sticky=W)
        self.entry_ganancia.grid(row=4, column=1, padx=10, columnspan=2)
        self.label_db_turno.grid(row=5, column=0, padx=10, sticky=W, pady=10)
        self.reg_dia1.grid(row=6, column=0, columnspan=3, pady=10)
        primero = 102
        for (text, value) in self._VALORES.items(): 
            Radiobutton(self.lbframe, text = text, variable = self.db_turno,
            value = value).place(x=primero, y=self._Y)
            primero += 50
        self.volver.pack()
        
    # Limpia los campos del form
    def volver_button(self):
        self.limpiar_un_dia()
        self.volver.focus()
        self.controller.mostrar_frame("MainPage")

    # Dependiendo del valor del parametro valor modifica o registra un objeto
    def texto_mod_reg(self, valor, obj=None):
        if valor:
            self.reg_dia1.config(text="Registrar dia", command=lambda:self.guardar_un_dia(self.entry_nombre.get(), self.cal.get(), self.entry_comentario.get(), self.entry_ganancia.get(), self.db_turno.get()))
        else:
            self.reg_dia1.config(text="Modificar dia", command=lambda:self.modificar_un_dia(obj))
    
    # En caso de modificacion, recibe los parametros para incorporarlos en los campos del form
    def ingresar_datos_campos(self, nombre, comentario, ganancias):
        self.entry_nombre.insert(0, nombre)
        self.entry_comentario.insert(0, comentario)
        self.entry_ganancia.insert(0, ganancias)

    # Registra un dia
    def guardar_un_dia(self, nombre, fecha, comentario, ganancia, dbturno):
        validacion = self.validaciones(nombre, fecha, comentario, ganancia)
        obj = None
        if validacion:
            # Si la lista no contiene items, crea el primer elemento
            if self.controller.frames["TablePage"].items == []:
                obj = Dia(id=1, nombre=nombre, fecha=fecha, comentario=comentario, ganancia=int(ganancia), doble_turno=self.truncar_1_0(dbturno))
                DiaDAO.insertar(obj, 1)   
            else:
                # Toma el ultimo elemento de la lista y suma uno, para registrar el siguiente elemento
                # Debido a que puede haber tuplas muertas en la base de datos y se perturbe el valor del id
                ultimo_registro_mas_uno = int(self.controller.frames["TablePage"].items[-1][0])+1
                obj = Dia(id=ultimo_registro_mas_uno, nombre=nombre, fecha=fecha, comentario=comentario, ganancia=int(ganancia), doble_turno=self.truncar_1_0(dbturno))
                DiaDAO.insertar(obj, ultimo_registro_mas_uno)
            self.controller.frames["TablePage"].añadir_a_la_lista(obj)
            messagebox.showinfo(title="Aviso", message="Dia registrado con éxito")
            self.limpiar_un_dia()
            self.controller.frames["StatsPage"].calculos(obj, True)
            self.volver.focus()
        else:
            messagebox.showerror(title="Error", message="No se ha podido registrar el dia")

    # Modifica un dia
    def modificar_un_dia(self, obj_ant):
        new_obj = Dia(id=obj_ant.id, nombre=self.entry_nombre.get(), fecha=self.cal.get(), comentario=self.entry_comentario.get(), ganancia=self.entry_ganancia.get(), doble_turno=self.truncar_1_0(self.db_turno.get()))
        validacion = self.validaciones(new_obj.nombre, new_obj.fecha, new_obj.comentario, new_obj.ganancia)
        if validacion:
            self.controller.frames["StatsPage"].calculos(obj_ant, False)
            self.controller.frames["StatsPage"].calculos(new_obj, True)
            DiaDAO.actualizar(new_obj)
            self.controller.frames["TablePage"].modificar_en_la_lista(new_obj)
            messagebox.showinfo(title="Modificar un dia", message="Dia modificado con éxito")
            self.limpiar_un_dia()
            self.volver.focus()
        else:
            messagebox.showerror(message="No se pudo modificar el dia")

    # Limpia los campos del form
    def limpiar_un_dia(self):
        self.entry_nombre.delete(0, END)
        self.cal.delete(0, END)
        self.entry_comentario.delete(0, END)
        self.entry_ganancia.delete(0, END)

    def truncar_1_0(self, valor):
        return valor == "1" 



    

