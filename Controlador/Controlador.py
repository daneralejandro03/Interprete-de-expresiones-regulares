from Modelo.Automata import Automata
from Vista.Vista import Vista

class Controlador:
    def __init__(self):
        self.modelo = Automata()
        self.vista = Vista()

    def ejecutar(self):
        expresion_regular = self.vista.ingresar_expresion_regular()
        try:
            self.modelo.construir_automata(expresion_regular)
            automata_minimizado = self.modelo.minimizar()
            self.vista.mostrar_automata(automata_minimizado)
        except Exception as e:
            self.vista.mostrar_error(str(e))


def main():
    controlador = Controlador()
    controlador.ejecutar()

if __name__ == "__main__":
    main()