from Modelo.Automata import Automata
from Modelo.Analizador import Analizador

class Controlador:
    def __init__(self):
        self.vista = Vista()
        self.automata = Automata()
        self.analizador = Analizador()

    def procesar_expresion(self, expresion: str):
        automata_generado = self.analizador.analizar_expresion(expresion)
        if automata_generado:
            self.vista.mostrar_automata("Autómata generado correctamente.")
        else:
            self.vista.mostrar_error("Error al generar el autómata.")