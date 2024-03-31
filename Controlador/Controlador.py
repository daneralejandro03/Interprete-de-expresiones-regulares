from modelo.automata import Automata
from modelo.analizador import Analizador
from vista.vista import Vista

class Controlador:
    def __init__(self):
        self.vista = Vista()
        self.automata = Automata()
        self.analizador = Analizador()
    
    def iniciar(self):
        self.vista.mostrar_menu()
        opcion = self.vista.leer_opcion()
        if opcion == 1:
            self.vista.mostrar_mensaje("Introduce una expresión regular:")
            expresion = self.vista.leer_expresion()
            self.procesar_expresion(expresion)

    def procesar_expresion(self, expresion: str):
        automata_generado = self.analizador.analizar_expresion(expresion)
        if automata_generado:
            self.vista.mostrar_automata("Autómata generado correctamente.")
        else:
            self.vista.mostrar_error("Error al generar el autómata.")

if __name__ == "__main__":
    controlador = Controlador()