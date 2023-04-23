import sys
sys.path.append('../')
from databases.Dia_Dao import DiaDAO
from databases.Dia import Dia
from tkinter import Listbox, W, E, END, EXTENDED, VERTICAL, Entry, ACTIVE, Label, HORIZONTAL, Frame, Button, messagebox, Scrollbar, RIGHT, Y, X, BOTTOM, LEFT, TOP

# Pagina que contiene la tabla que modifica/elimina un registro
class TablePage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        # Query Select de todos los registros
        self.items = self.truncar_query() 
        self.scrollv = Scrollbar(self, orient=VERTICAL)
        self.scrollh = Scrollbar(self, orient=HORIZONTAL)
        self.listbox = Listbox(self,selectmode=EXTENDED, yscrollcommand=self.scrollv.set, xscrollcommand=self.scrollh.set,width=50, height=15)
        self.id_entry = Entry(self, width=50)
        self.boton_de_accion1 = Button(self, width=10)
        self.volver = Button(self, text="Volver", width=10, command=lambda:self.volver_button())
        self.empty_label1 = Label(self)
        self.empty_label2 = Label(self)
        self.boton_de_limpieza = Button(self, width=10, text="Limpiar", command=lambda:self.limpiar_entrada())
        self.configurar_elementos()
        self.update(self.items)
        self.bind()

    
    # Dependiendo del valor de valor pasado como parametro, se realizan distintas acciones modificar/eliminar
    def texto_mod_reg(self, valor):
        if valor:
            self.boton_de_accion1.config(text="Modificar", command=lambda:self.modificarRegistro()) 
        else:
            self.boton_de_accion1.config(text="Eliminar", command=lambda:self.borrarRegistro())
        
    # Muestra en un grid los elementos
    def configurar_elementos(self):   
        self.boton_de_accion1.grid(row=4, column=2, sticky=W, pady=25)
        self.id_entry.grid(row=1, column=0, columnspan=3)
        self.poner_placeholder()
        self.empty_label1.grid(row=0, column=0, columnspan=3)
        self.empty_label2.grid(row=2, column=0, columnspan=3)
        self.listbox.grid(row=3, column=0, columnspan=3)
        self.scrollv.config(command=self.listbox.yview)
        self.scrollv.grid(row=3, column=3)
        self.scrollh.config(command=self.listbox.xview)
        self.scrollh.place(x=130, y=310)
        self.volver.grid(row=4, column=0, sticky=W, pady=25)
        self.boton_de_limpieza.grid(row=4, column=1, sticky=W, pady=25, padx=15)
        
    # Resetea la tabla si se sale del frame
    def volver_button(self):
        self.id_entry.delete(0,END)
        self.listbox.selection_clear(0, END)
        if self.items == []:
            for i in self.items:
                self.listbox.insert(END,i)
        self.controller.mostrar_frame("MainPage")
        self.poner_placeholder()

    # Placeholder del widget entry
    def poner_placeholder(self):
        self.id_entry['fg'] = 'grey'
        self.id_entry.insert(0, "Escribe algo...")
        self.volver.focus()
    
        
    # Saca el apuntador del mouse del widget entry
    def focus_out(self, event):
        if not self.id_entry.get():
            self.id_entry.delete('0', END)
            self.poner_placeholder()
       
    # Pone el apuntador del mouse del widget entry y borra el placeholder
    def focus_in(self, event):
        self.id_entry.delete('0', END)
        self.id_entry['fg'] = "black"
        
    # Añade un objeto insertado a la lista
    def añadir_a_la_lista(self, obj):
        new_obj = self.truncar_objeto(obj)
        self.items.append(new_obj)
        self.listbox.insert(END, new_obj)

    # Algoritmo de busqueda binaria para encontrar el objeto en la lista
    def busqueda_binaria(self, nuevo_obj):
        bajo = 0
        alto = len(self.items) - 1
        while bajo <= alto:
            medio = (bajo + alto) // 2
            if self.items[medio][0] == nuevo_obj[0]:
                self.listbox.delete(medio)
                self.items[medio] = nuevo_obj
                self.listbox.insert(medio, nuevo_obj)
                break
            elif int(self.items[medio][0]) < int(nuevo_obj[0]):
                bajo = medio + 1
            else:
                alto = medio - 1

    # Modifica un objeto dado, encontrandolo en la lista
    def modificar_en_la_lista(self, obj):
        new_obj = self.truncar_objeto(obj)
        self.busqueda_binaria(new_obj)
    
    # Cambia el tipo de dato de id y ganancia para ser operados posteriormente
    def truncar_objeto(self, obj):
        string_del_turno = self.retornar_str_v_f(obj.doble_turno)   
        return [str(obj.id), obj.nombre, obj.fecha, obj.comentario, str(obj.ganancia), string_del_turno]

    # Cambia el valor del field booleano para mostrar en la lista
    def retornar_str_v_f(self, valor):
        return "Doble turno" if valor else "Simple turno"
 
    # A cada registro en la lista, se parcean los tipos de datos que se necesitan para operar posteriormente
    
    def truncar_query(self):
        listObj = DiaDAO.seleccionar()
        cont = 0
        for i in listObj:
            string_del_turno = self.retornar_str_v_f(i.doble_turno)
            listObj[cont] = [str(i.id), i.nombre, i.fecha, i.comentario, str(i.ganancia), string_del_turno]
            cont+=1
        return listObj
    

    def update(self, itemList):
        self.listbox.delete(0, END)
        for i in itemList:
            self.listbox.insert(END, i)

    # Bindea los botones
    def bind(self):
        self.listbox.bind("<<ListboxSelect>>", self.ingresar_entry)
        self.id_entry.bind("<KeyRelease>", self.check)
        self.id_entry.bind("<FocusIn>", self.focus_in)
        self.id_entry.bind("<FocusOut>", self.focus_out)

    # Quita los caracteres ingresados en el id entry y el apuntador del cursor
    def limpiar_entrada(self):
        self.id_entry.delete(0,END)
        self.listbox.selection_clear(0, END)
        self.update(self.items)
        self.poner_placeholder()
    
    # Ingresa objeto seleccionado por el cursor al widget entry
    def ingresar_entry(self, event):
        self.id_entry['fg'] = 'black'
        self.id_entry.delete(0, END)
        if self.listbox.curselection():
            index = self.listbox.curselection()[0]
            item_seleccionado = self.listbox.get(index)
            self.id_entry.insert(0, item_seleccionado)
    
    # Actualiza el listbox segun lo que vaya escribiendo el usuario en el widget entry
    def check(self, evento):
        self.id_entry["fg"] = "black"
        data = []
        tipeado = self.id_entry.get()
        if tipeado == "":
            data = self.items
        else:
            for item in self.items:
                for i in item:
                    if tipeado.lower() in i.lower() or tipeado.lower == "True" or tipeado.lower == "False":
                        data.append(item)
                        break           
        self.update(data)

    # Si hay un objeto seleccionado, lo retorna
    def obtener_objeto_lista(self):
        valor_entry = self.id_entry.get()
        if valor_entry != "" and valor_entry != "Escribe algo...":
            var_tuple = self.listbox.get(ACTIVE)
            dia_obj = Dia(id=var_tuple[0], nombre=var_tuple[1], fecha=var_tuple[2], comentario=var_tuple[3], ganancia=var_tuple[4],doble_turno=var_tuple[5])
            return dia_obj
        messagebox.showerror(message="No hay ningun registro seleccionado", title="Error")
        return None
            
    # Borra un objeto seleccionado
    def borrarRegistro(self):
        elem_to_del = self.obtener_objeto_lista()
        if elem_to_del:
            DiaDAO.eliminar(elem_to_del)
            tupla_truncada = self.truncar_objeto(elem_to_del)
            self.items.remove(tupla_truncada)
            self.update(self.items)
            messagebox.showinfo(message="Dia eliminado con exito", title="Dia eliminado")
            self.controller.frames["StatsPage"].calculos(obj=elem_to_del, contar=False)

    # Modifica un objeto seleccionado
    def modificarRegistro(self):
        elem_to_mod = self.obtener_objeto_lista()
        if elem_to_mod:
            self.controller.mostrar_frame("RegPage", False, objeto=elem_to_mod)
            self.controller.frames["RegPage"].ingresar_datos_campos(elem_to_mod.nombre, elem_to_mod.comentario, elem_to_mod.ganancia)
    
        




    

        
         
         

 
    

        
        



  




    

    
