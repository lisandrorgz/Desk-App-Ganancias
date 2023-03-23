from databases.Dia_Dao import DiaDAO
from databases.Dia import Dia
from .ValidationClass import Validations
from tkinter import Label, Entry, StringVar, OptionMenu, Button, Frame, Tk, W, CENTER, LabelFrame, BOTTOM, Radiobutton, messagebox, END
from tkcalendar import Calendar, DateEntry
from .showTclass import TablePage



class RegPage(Frame, Validations):

    _Y = 135
    _VALORES = {"Si" : True, "No" : False}

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
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
        self.db_turno = v = StringVar(self.lbframe, "1")
        self.volver = Button(self, text="Volver", width=10, 
        command=lambda:self.controller.show_frame("MainPage"))
        self.cal = DateEntry(self.lbframe, selectmode="day", year=2023, month=2, day=1)
        self.reg_dia1 = Button(self.lbframe, width=15, justify=CENTER)
        self.cfgbuttons()


    def cfgbuttons(self):
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
        for (text, value) in RegPage._VALORES.items(): 
            Radiobutton(self.lbframe, text = text, variable = self.db_turno,
            value = value).place(x=primero, y=self._Y)
            primero += 50
        self.volver.pack()
        
        
    def set_text_value(self, value, obj=None):
        if value:
            self.reg_dia1.config(text="Registrar dia", command=lambda:self.guardar_un_dia(self.entry_nombre.get(), self.cal.get(), self.entry_comentario.get(), self.entry_ganancia.get(), self.db_turno.get()))
        else:
            self.reg_dia1.config(text="Modificar dia", command=lambda:self.modificar_un_dia(obj))
           


    def guardar_un_dia(self, nombre, fecha, comentario, ganancia, dbturno):
        dbt = self.validaciones(nombre, fecha, comentario, ganancia, dbturno)
        if dbt:
            obj = Dia(nombre=nombre, fecha=fecha, comentario=comentario, ganancia=int(ganancia), doble_turno=dbturno)
            DiaDAO.insertar(obj)
            self.controller.reloadQuery()
            messagebox.showinfo(title="Aviso", message="Dia registrado con éxito")
            self.limpiar_un_dia()
            self.controller.frames["StatsPage"].calculos()
        else:
            messagebox.showerror(title="Error", message="No se ha podido registrar el dia")

    def modificar_un_dia(self, obj):
        new_obj = Dia(id=obj.id, nombre=self.entry_nombre.get(), fecha=self.cal.get(), comentario=self.entry_comentario.get(), ganancia=self.entry_ganancia.get(), doble_turno=self.db_turno.get())
        self.validaciones(nombre=new_obj.nombre, fecha=new_obj.fecha, comentario=new_obj.comentario, ganancia=new_obj.ganancia, dbturno=new_obj.doble_turno)
        DiaDAO.actualizar(new_obj)
        self.controller.reloadQuery()
        messagebox.showinfo(title="Modificar un dia", message="Dia modificado con éxito")
        self.limpiar_un_dia()
        self.controller.frames["StatsPage"].calculos(obj)


    def limpiar_un_dia(self):
        self.entry_nombre.delete(0, END)
        self.cal.delete(0, END)
        self.entry_comentario.delete(0, END)
        self.entry_ganancia.delete(0, END)



    

