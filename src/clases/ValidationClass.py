from tkinter import messagebox



class Validations():

    @classmethod
    def validaciones(cls, nombre, fecha, comentario, ganancia, dbturno):
        if nombre == "" or cls.notcharacter(nombre) or len(nombre) > 12:
            messagebox.showwarning(message="Valor erroneo para el campo NOMBRE", title="Advertencia")
            return False
        elif comentario == "" or len(comentario) > 50:
            messagebox.showwarning(message="Valor erroneo para el campo COMENTARIO", title="Advertencia")
            return False
        elif ganancia == "" or cls.notnumeric(ganancia):
            messagebox.showwarning(message="Valor erroneo para el campo GANANCIAS", title="Advertencia")
            return False
        return True

    @classmethod
    def notcharacter(cls, str):
        for x in str:
            if x.isdigit():
                return True
        return False

    @classmethod
    def notnumeric(cls, str):
        for x in str:
            if str.isalpha():
                return True
        return False