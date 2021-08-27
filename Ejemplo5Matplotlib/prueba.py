from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
import numpy as np
import tkinter as Tk

 
class Ventana(Tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.f = Figure( figsize=(10, 9), dpi=80 )
        # Como pueden observar, aquí agregamos más graficos con add_axes
        self.ax0 = self.f.add_axes( (0.05, .05, .50, .50),frameon=False)
        self.ax1 = self.f.add_axes( (0.05, .55, .90, .45), frameon=False)
        self.ax2 = self.f.add_axes( (0.55, .05, .50, .50), frameon=False)

        
        self.ax0.set_xlabel('X')
        self.ax0.set_ylabel('Y')
        # utilizamos plot para generar los gráficos
        self.ax0.plot(np.max(np.random.rand(100,10)*10,axis=1),"r-")
        self.ax1.plot(np.max(np.random.rand(100,10)*10,axis=1),"g-")
        self.pack(side=Tk.LEFT, fill=Tk.BOTH, expand=1)

        self.canvas = FigureCanvasTkAgg(self.f, master=self)
        self.canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
        #self.canvas.show()
    """
        self.toolbar = NavigationToolbar2Tk(self.canvas, self )
        self.toolbar.pack()
        self.toolbar.update()
"""


root = Tk.Tk()
app = Ventana(root)
root.title( "Gráficos" )
root.update()
root.deiconify()
root.mainloop()
