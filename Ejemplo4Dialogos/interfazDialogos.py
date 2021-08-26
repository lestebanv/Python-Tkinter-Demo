import tkinter as tk
import os


from tkinter import colorchooser
from tkinter import filedialog
from tkinter.simpledialog import askstring

class PanelDialogos(tk.Frame):
    def __init__(self,ventana_padre):
        super().__init__(ventana_padre)
        tk.Label(self,text="Dialogos").grid(row=1,column=1)
        tk.Label(self,text="Salida").grid(row=1,column=2)
        tk.Button(self, width=20,text="Mensaje",command=lambda: self.eventos("Mensaje")).grid(row=2, column=1)
        tk.Button(self,width=20, text="Error",command=lambda: self.eventos("Error")).grid(row=3, column=1)
        tk.Button(self,width=20, text="Advertencia",command=lambda: self.eventos("Advertencia")).grid(row=4, column=1)
        tk.Button(self, width=20,text="Pregunta",command=lambda: self.eventos("Pregunta")).grid(row=5, column=1)
        tk.Button(self, width=20, text="Ok Cancelar",command=lambda: self.eventos("Cancelar")).grid(row=6, column=1)
        tk.Button(self, width=20, text="Reintentar",command=lambda: self.eventos("Reintentar")).grid(row=7, column=1)
        tk.Button(self, width=20,text="Color",command=lambda: self.eventos("Color")).grid(row=8, column=1)
        tk.Button(self,width=20, text="Abrir Archivos",command=lambda: self.eventos("Archivos")).grid(row=9, column=1)
        tk.Button(self, width=20,text="Guardar como",command=lambda: self.eventos("Guardar")).grid(row=10, column=1)
        tk.Button(self, width=20,text="Entrada",command=lambda: self.eventos("Entrada")).grid(row=10, column=1)
        tk.Button(self, width=20,text="Limpiar",command=lambda: self.eventos("Limpiar")).grid(row=11, column=2)

        self.caja2=tk.Text(self,width=40, height=10)
        self.caja2.config(font=("Consolas",12), selectbackground="blue", padx=5, pady=5)
        self.caja2.grid(row=2,column=2,rowspan=9)
    def ejecutar_pregunta(self):
        resultado = tk.messagebox.askquestion("Salir","¿Está seguro que desea salir sin guardar?")
     
        self.caja2.insert(tk.INSERT,resultado+"\n")
        if resultado=="yes":
           pass
        else:
           pass
    def eventos(self,comando:str):
        if comando=="Entrada":
            nombre=tk.simpledialog.askstring("Titulo ventana", "Cuál es su nombre")
            self.caja2.insert(tk.INSERT,nombre+"\n")
        if comando=="Mensaje":
            tk.messagebox.showinfo("Titulo ventana xxxxx", "Mensaje a mostrar") 
            self.caja2.insert(tk.INSERT,"Solo muestra mensaje...\n")
        if comando=="Error":
            tk.messagebox.showerror("Error", "Mensaje Error") 
            self.caja2.insert(tk.INSERT,"Muestra mensaje de error\n")
        if comando=="Advertencia":
            tk.messagebox.showwarning("Advertencia", "Mensaje de advertencia Warning") 
            self.caja2.insert(tk.INSERT,"Muestra mensaje adverntecia\n")
        if comando=="Limpiar":
            self.caja2.delete("1.0","end")
        if comando=="Pregunta":
            self.ejecutar_pregunta()
        if comando=="Cancelar":
            resultado = tk.messagebox.askokcancel("Sobrescribir","¿Está seguro de sobreescribir el archivo?")
            self.caja2.insert(tk.INSERT,str(resultado)+"\n")
        if comando=="Reintentar":
            resultado = tk.messagebox.askretrycancel("Reintentar","No se puede conectar")
            self.caja2.insert(tk.INSERT,str(resultado)+"\n")
        if comando=="Color":
            resultado = colorchooser.askcolor(title="Elige un color")
            self.caja2.insert(tk.INSERT,str(resultado)+"\n")
        if comando=="Archivos":
            resultado =  filedialog.askopenfilename(title="Abrir un fichero")
            self.caja2.insert(tk.INSERT,str(resultado)+"\n")
        if comando=="Guardar":
            resultado =  filedialog.asksaveasfile(title="Guardar un archivo")
            self.caja2.insert(tk.INSERT,str(resultado)+"\n")

class InterfazDialogos(tk.Tk):
    def __init__(self,tituloventana):
        super().__init__()
        self.title(tituloventana)
        
        #Imangen de cabecera
        file_path = os.path.dirname(os.path.abspath(__file__))
        imagen_path = os.path.join(file_path, 'imagenes', "softwarelibre.png")
        self.imagen_cabecera=tk.PhotoImage(file=imagen_path) 
        tk.Label(self,image=self.imagen_cabecera).grid(row=1,column=1)
        #Panel dialogos
        PanelDialogos(self).grid(row=2,column=1)

        
#codigo de arranque
x=InterfazDialogos("Diversas ventanas de dialogo")
x.mainloop()

