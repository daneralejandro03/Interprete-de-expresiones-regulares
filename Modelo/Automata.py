class Automata:
    def __init__(self):
        self.estados = []
        self.alfabeto = []
        self.transiciones = {}
        self.estado_inicial = None
        self.estados_finales = []

    def agregar_estado(self, estado: str):
        self.estados.append(estado)

    def agregar_transicion(self, origen: str, destino: str, simbolo: str):
        self.transiciones[(origen, simbolo)] = destino

    def ejecutar(self, entrada: str) -> bool:
        estado_actual = self.estado_inicial
        for simbolo in entrada:
            if (estado_actual, simbolo) in self.transiciones:
                estado_actual = self.transiciones[(estado_actual, simbolo)]
            else:
                return False
        return estado_actual in self.estados_finales