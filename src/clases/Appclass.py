from tkinter import Label, Entry, StringVar, OptionMenu, messagebox, Button, Frame, Tk, W, CENTER, LabelFrame, BOTTOM, Tk, PhotoImage
from .MainPageclass import MainPage
from .RegPageclass import RegPage
from .showTclass import TablePage
from .StatsPage import StatsPage
import base64, os

class App(Tk):
   
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.geometry("600x400")
        self.resizable(False,False)
        self.title("Ganancias")
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
       
        container = Frame(self)
        container.pack()
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (MainPage, RegPage, TablePage, StatsPage):
            page_name = F.__name__
            frame = F(container, self) 
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainPage")
        self.tempFile= "coin.ico"
        self.icondata= base64.b64decode(self.img)
        self.iconfile= open(self.tempFile,"wb")
        self.iconfile.write(self.icondata)
        self.iconfile.close()
        self.wm_iconbitmap(self.tempFile)
        os.remove(self.tempFile)
        

    def show_frame(self, page_name, value=None, obj=None):
        frame = self.frames[page_name]
        if frame.__class__.__name__ == "TablePage":
                frame.set_text_page(value)
        elif frame.__class__.__name__ == "RegPage":
                if not obj == None:
                    frame.set_text_value(value, obj)
                else:
                     frame.set_text_value(value)
        elif frame.__class__.__name__ == "StatsPage":
             if self.frames["StatsPage"]._mayor == -1:
                  messagebox.showerror(title="Error", message="No hay dias registrados")
                  return None
        frame.tkraise()
    
    
    def reloadQuery(self):
        self.frames["TablePage"].reload_list()

        
        
         

        
       
