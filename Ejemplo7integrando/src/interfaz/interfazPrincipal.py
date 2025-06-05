import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

from src.interfaz.PanelBotones import PanelBotones
from src.interfaz.PanelDatos import PanelDatos
from src.interfaz.PanelSuperior import PanelSuperior
from src.interfaz.VentanaExtra import VentanaExtra

from src.mundo.claseEstudiante import Estudiante


# Ventana principal
class InterfazPrincipal(tk.Tk):
    def __init__(self, estudiante):
        super().__init__()
        self.est = estudiante
        self.title("Perfil de Estudiante")
        self.geometry("600x500")
        self.resizable(False, False)
        self.icono()

        # Paneles
        self.pSuperior = PanelSuperior(self)
        self.pSuperior.pack(side="top", fill="x")

        self.pDatos = PanelDatos(self)
        self.pDatos.pack(expand=True, fill="both")

        self.pBotones = PanelBotones(self)
        self.pBotones.pack(side="bottom", fill="x")

   

    def icono(self):
        try:
            ruta_base = os.path.dirname(os.path.abspath(__file__))
            ruta_icono = os.path.join(ruta_base, "..", "..", "data", "icono2.png")
            imagen = Image.open(ruta_icono)
            icono = ImageTk.PhotoImage(imagen)
            self.iconphoto(False, icono)
        except Exception as e:
            print("No se pudo cargar el icono:", e)

