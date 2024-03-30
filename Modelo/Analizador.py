from Modelo.Automata import Automata

class Analizador:
    def __init__(self):
        self.automata = Automata()

    def analizar_expresion(self, expresion: str):
        # Limpiar la expresión regular
        expresion_limpia = expresion.replace(' ', '')

        # Validar si la expresión regular es válida
        if not self.validar_expresion(expresion_limpia):
            return False

        # Crear el autómata correspondiente
        self.automata = self.generar_automata(expresion_limpia)
        return True

    def validar_expresion(self, expresion: str) -> bool:
        # Verificar si la expresión regular es válida utilizando una expresión regular
        # Esto es una implementación básica y puede necesitar ajustes según los requisitos exactos
        try:
            re.compile(expresion)
            return True
        except re.error:
            return False

    def generar_automata(self, expresion: str) -> Automata:
        # Aquí implementarías la lógica para generar el autómata a partir de la expresión regular
        automata_generado = Automata()
        # Implementación de la generación del autómata...
        return automata_generado