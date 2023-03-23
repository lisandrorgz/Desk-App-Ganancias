import sys
sys.path.append('../')
from databases.Dia_Dao import DiaDAO
from databases.Dia import Dia
from tkinter import Listbox, W, E, END, EXTENDED, VERTICAL, Entry, ACTIVE, Label, HORIZONTAL, Frame, Button, messagebox, Scrollbar, RIGHT, Y, X, BOTTOM, LEFT, TOP


class TablePage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.items = self.parceQuery()
        self.scrollv = Scrollbar(self, orient=VERTICAL)
        self.scrollh = Scrollbar(self, orient=HORIZONTAL)
        self.listbox = Listbox(self,selectmode=EXTENDED, yscrollcommand=self.scrollv.set, xscrollcommand=self.scrollh.set,width=50, height=15)
        self.id_entry = Entry(self, width=50)
        self.action_button1 = Button(self, width=10)
        self.volver = Button(self, text="Volver", width=10, command=lambda:self.controller.show_frame("MainPage"))
        self.empty_label1 = Label(self)
        self.empty_label2 = Label(self)
        self.clean_button = Button(self, width=10, text="Limpiar", command=lambda:self.clean_entry())
        self.configElements()
        self.update(self.items)
        self.bind()
        

    def set_text_page(self, value):
        if value:
            self.action_button1.config(text="Modificar", command=lambda:self.modificarRegistro()) 
        else:
            self.action_button1.config(text="Eliminar", command=self.borrarRegistro)
        

       
    def configElements(self):   
        self.action_button1.grid(row=4, column=2, sticky=W, pady=25)
        self.id_entry.grid(row=1, column=0, columnspan=3)
        self.put_placeholder()
        self.empty_label1.grid(row=0, column=0, columnspan=3)
        self.empty_label2.grid(row=2, column=0, columnspan=3)
        self.listbox.grid(row=3, column=0, columnspan=3)
        self.scrollv.config(command=self.listbox.yview)
        self.scrollv.grid(row=3, column=3)
        self.scrollh.config(command=self.listbox.xview)
        self.scrollh.place(x=130, y=310)
        self.volver.grid(row=4, column=0, sticky=W, pady=25)
        self.clean_button.grid(row=4, column=1, sticky=W, pady=25, padx=15)
        
 


    def put_placeholder(self):
        self.id_entry['fg'] = 'grey'
        self.id_entry.insert(0, "Escribe algo...")
        

    def focus_out(self, event):
        if not self.id_entry.get():
            self.id_entry.delete('0', END)
            self.put_placeholder()
       

    def focus_in(self, event):
        self.id_entry.delete('0', END)
        self.id_entry['fg'] = "black"
        


    def reload_list(self):
        new_list = self.parceQuery()
        self.update(new_list)

   
    @classmethod
    def parceQuery(cls):
        listObj = DiaDAO.seleccionar()
        cont = 0
        for i in listObj:
            listObj[cont] = [str(i.id), i.nombre, i.fecha, i.comentario, str(i.ganancia), str(i.doble_turno)]
            cont+=1
        return listObj
    

    def update(self, itemList):
        self.listbox.delete(0, END)
        for i in itemList:
            self.listbox.insert(END, i)


    def bind(self):
        self.listbox.bind("<<ListboxSelect>>", self.fillout)
        self.id_entry.bind("<KeyRelease>", self.check)
        self.id_entry.bind("<FocusIn>", self.focus_in)
        self.id_entry.bind("<FocusOut>", self.focus_out)


    def clean_entry(self):
        self.id_entry.delete(0,END)
        self.put_placeholder()
        #self.reload_list()
    
    def fillout(self, event):
        self.id_entry.delete(0, END)
        self.id_entry['fg'] = 'black'
        self.id_entry.insert(0, self.listbox.get(ACTIVE))
    
    def check(self, event):
        self.id_entry["fg"] = "black"
        data = []
        typed = self.id_entry.get()
        if typed == "":
            data = self.items
        else:
            for item in self.items:
                for i in item:
                    if typed.lower() in i.lower():
                        data.append(item)            
        self.update(data)

    

    def getobjectfromList(self):
        entryget = self.id_entry.get()
        if entryget != "" and entryget != "Escribe algo...":
            var = self.listbox.get(ACTIVE)
            dia_obj = Dia(id=var[0], nombre=var[1], fecha=var[2], comentario=var[3], ganancia=var[4],doble_turno=var[5])
            return dia_obj
        messagebox.showerror(message="No hay ningun registro seleccionado", title="Error")
        return None
            
    
    def borrarRegistro(self):
        elem_to_del = self.getobjectfromList()
        if elem_to_del != None:
            DiaDAO.eliminar(elem_to_del)
            self.reload_list()
            messagebox.showinfo(message="Dia eliminado con exito", title="Dia eliminado")
            self.controller.frames["StatsPage"].calculos(obj=elem_to_del)

    def modificarRegistro(self):
        elem_to_mod = self.getobjectfromList()
        if elem_to_mod != None:
            self.controller.show_frame("RegPage", False, obj=elem_to_mod)




    

        
         
         

 
    

        
        



  




    

    
