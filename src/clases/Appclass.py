from tkinter import Label, Entry, StringVar, OptionMenu, messagebox, Button, Frame, Tk, W, CENTER, LabelFrame, BOTTOM, Tk, PhotoImage
from .MainPageclass import MainPage
from .RegPageclass import RegPage
from .showTclass import TablePage
from .StatsPage import StatsPage
from datetime import datetime, timezone, timedelta
import base64, os

class App(Tk):
     
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        # Variables de configuración
        self.tiempo_de_la_zona_latam = timezone(timedelta(hours=-5))
        self.hoy = datetime.now(self.tiempo_de_la_zona_latam)
        self.option_add('*timezone', self.tiempo_de_la_zona_latam)
        self.geometry("600x400")
        self.resizable(False,False)
        self.title("Ganancias")
        # logo 
        self.img = """
        AAABAAEAEBAAAAEAIABoBAAAFgAAACgAAAAQAAAAIAAAAAEAIAAAAAAAAAQAAHYAAAB2AAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAvAAAATQAAAE0AAAAvAAAAAgAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAAAAEQsSFUgZLzbZPW+B7FKXrfxSl638O26A7BkvNdgL
        EhZHAAAAEQAAAAUAAAAAAAAAABEgI1gXLDPSJURO4S9YZuIOGx/3cM3t/1ihuv9pwuD/acLg/1ih
        uv9wze3/Dhsf9y9YZuIlRE7hFywz0hIdIFceNz/fd9r8/2e+2/9gscz/JENN/yhJVP9Pkqj/ddf4
        /3XX+P9Pkaf/KElU/yRDTf9gscz/Z77b/3fa/P8eNz/fChMW9SlMWP8+coP/RoGV/xgsM/9lutf/
        RH6R/zVicf81YnH/RH6R/2W61/8YLDP/RoGV/z5yg/8pTFj/ChMW9R45QeRwze3/WKO8/1CTqv8g
        OkP/NmNy/1+uyf9vzez/b83s/1+uyf82Y3L/IDpD/1CTqv9Yo7z/cM3t/x45QeQIDxL3MVpo/02N
        o/9UmrL/PXCB/y5VYv9Yorv/aL/c/2nB3/9Yo7z/MFhm/z1xgv9UmrL/TY2j/zFaaP8IDxL3Ij5H
        4mK00P9Jh5z/QXiK/0uKn/9apsD/FCQq5xMhJpUTISaVFCQq51unwf9Lip//QXiK/0mHnP9itND/
        Ij5H4gcNDvg/dIb/XKnD/2K10f9Zpb7/OWl5/w0YG+sAAAAAAAAAAA0YG+s5anr/WaW+/2K10f9c
        qcP/P3SG/wcNDvgSIifRU5mw+TBEQ/8+STv/NlJU/0yLofYTIye8AAAAAAAAAAATIyi9TIyi9zZS
        VP8+STv/MERD/1OZsPkSIifRAAAACwgOEVwoKRzk6Nh7/xkbFOQDCgpQAAAABgAAAAAAAAAAAAAA
        BgMKClAZGxTk6Nh7/ygpHOQIDhFcAAAACwAAAAAAAAAANjMcz+jYe/8rJxbDAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAKycWw+jYe/82MxzPAAAAAAAAAAAAAAABExEKzkVAJebo2Hv/LSoY6BYVDbYA
        AAAAAAAAAAAAAAAAAAAAFhUNti0qGOjo2Hv/RUAl5hMRCs4AAAABAAAAABoXD1dqYjjo59d7/1BJ
        KuYUFAhAAAAAAAAAAAAAAAAAAAAAABINCTpJRSfl59d7/2liN+sbGA5eAAAAAAAAAAAAAAAAHBoQ
        gTMwG+wbGA5eAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGRYOXDMwG+wfHRCDAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAA
        AAAA+B8AAMADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAYAAAAGAAADH4wAAA8AAAIPB
        AADH4wAA7/cAAA=="""
        # Contenedor de frames (1 por pagina)
        contenedor = Frame(self)
        contenedor.pack()
        # Todos puestos uno arriba del otro
        contenedor.grid_rowconfigure(0, weight=1)
        contenedor.grid_columnconfigure(0, weight=1)
        self.frames = {}
        # Instancias de cada pagina en el mismo contenedor
        for F in (MainPage, RegPage, TablePage, StatsPage):
            nombre_de_la_pagina = F.__name__
            frame = F(contenedor, self) 
            self.frames[nombre_de_la_pagina] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        # Se instancia app y renderiza la pagina principal
        self.mostrar_frame("MainPage")
        self.tempFile = "coin.ico"
        # Decodificación y sobreescritura del logo
        self.icondata = base64.b64decode(self.img)
        self.iconfile = open(self.tempFile,"wb")
        self.iconfile.write(self.icondata)
        self.iconfile.close()
        self.wm_iconbitmap(self.tempFile)
        os.remove(self.tempFile)
        
    # Funcion que navega entra frames, cada vez que es llamado por algun boton en los otros frames, tomando valores respectivos para ejecutar acciones
    def mostrar_frame(self, nombre_pag, valor=None, objeto=None):
        frame = self.frames[nombre_pag]
        if frame.__class__.__name__ == "TablePage":
                frame.texto_mod_reg(valor)
        elif frame.__class__.__name__ == "RegPage":
                if not objeto == None:
                    frame.texto_mod_reg(valor, objeto)
                else:
                     frame.texto_mod_reg(valor)
        elif frame.__class__.__name__ == "StatsPage":
             if not(self.frames["TablePage"].items):
                  messagebox.showerror(title="Error", message="No hay dias registrados")
                  return None
        frame.tkraise()
    
    

        
        
         

        
       
