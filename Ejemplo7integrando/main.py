# main.py
from src.mundo.claseEstudiante import Estudiante
from src.interfaz.interfazPrincipal import InterfazPrincipal

# Ejecución principal
if __name__ == "__main__":
    est = Estudiante("Juanito Jaimes", 312345, "calle 5 4-19", "pepito@gmail.com")
    app = InterfazPrincipal(est)
    app.mainloop()
