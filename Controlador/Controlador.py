from Modelo.Analizador import Analizador
from Modelo.Automata import Automata
from Vista.Vista import Vista

class Controlador:
    def __init__(self):
        self.automata = Automata()
        self.vista = Vista()
        self.analizador = Analizador()

    def procesar_expresion(self, expresion: str):
        return self.analizador.analizar_expresion(expresion)

    def ejecutar(self):
        self.vista.mostrar_menu()
        opcion = self.vista.leer_opcion()
        if opcion == 1:
            self.vista.mostrar_mensaje("Introduce una expresión regular:")
            expresion_regular = self.vista.leer_expresion()
            if self.procesar_expresion(expresion_regular):    
                try:
                    self.automata.construir_automata(expresion_regular)
                    automata_minimizado = self.automata.minimizar()
                    self.vista.mostrar_automata(automata_minimizado)
                except Exception as e:
                    self.vista.mostrar_error(str(e))
            else:
                self.vista.mostrar_error("Expresión regular inválida")