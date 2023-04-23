from tkinter import messagebox
from datetime import datetime, timezone, timedelta


# Clase que contiene funciones para validar los datos de entrada
class Validations():
    
    @classmethod
    def validaciones(cls, nombre, fecha, comentario, ganancia): 
        return not(cls.verificar_nombre(nombre) or cls.verificar_comentario(comentario) or cls.verificar_ganancia(ganancia) or cls.verificar_fecha(fecha))     

    @classmethod
    def verificar_nombre(cls, nombre):
        proposicion = nombre == "" or cls.noEsChar(nombre) or len(nombre) > 12
        if proposicion:
            messagebox.showwarning(message="Valor erroneo para el campo NOMBRE", title="Advertencia")
        return proposicion
    
    @classmethod
    def verificar_comentario(cls, comentario):
        proposicion = comentario == "" or len(comentario) > 50
        if proposicion:
            messagebox.showwarning(message="Valor erroneo para el campo COMENTARIO", title="Advertencia")
        return proposicion
    
    @classmethod
    def verificar_ganancia(cls, ganancia):
        proposicion = ganancia == "" or cls.noEsNumerico(ganancia)
        if proposicion:
            messagebox.showwarning(message="Valor erroneo para el campo GANANCIA", title="Advertencia")
        return proposicion
    
    @classmethod
    def verificar_fecha(cls, fecha):
        today = str(datetime.now()) 
        lista_fecha, lista_datetime = fecha.split("/"), today.split("-")
        proposicion = fecha == "" or int(lista_fecha[0]) > (int(lista_datetime[2][0] + lista_datetime[2][1])) or int(lista_fecha[1]) > int(lista_datetime[1]) or int(lista_fecha[2]) > int(lista_datetime[0])
        if proposicion:
            messagebox.showwarning(message="Valor erroneo para el campo FECHA", title="Advertencia")
        return proposicion
    

    @classmethod
    def noEsChar(cls, str):
        return any(chr.isdigit() for chr in str)

    @classmethod
    def noEsNumerico(cls, str):
        return any(chr.isalpha() for chr in str)
