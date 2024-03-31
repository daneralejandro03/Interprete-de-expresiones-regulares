from graphviz import Digraph

class Automata:
    def __init__(self):
        self.transiciones = {}
        self.estado_inicial = None
        self.estados_finales = set()

    def agregar_transicion(self, estado_actual, simbolo, siguiente_estado):
        if estado_actual not in self.transiciones:
            self.transiciones[estado_actual] = {}
        self.transiciones[estado_actual][simbolo] = siguiente_estado

    def definir_estado_inicial(self, estado):
        self.estado_inicial = estado

    def agregar_estado_final(self, estado):
        self.estados_finales.add(estado)

    def construir_automata(self, expresion_regular):
        # Creamos un estado inicial
        estado_actual = 'q0'
        self.definir_estado_inicial(estado_actual)

        for i, caracter in enumerate(expresion_regular):
            if caracter == '(':
                # Encontramos una apertura de paréntesis, creamos un nuevo estado para manejar la parte dentro de los paréntesis
                nuevo_estado = 'q{}'.format(i + 1)
                self.agregar_transicion(estado_actual, '', nuevo_estado)
                estado_actual = nuevo_estado
            elif caracter == '|':
                # Continuamos con la próxima parte de la expresión regular
                estado_actual = 'q{}'.format(i + 1)
            elif caracter == ')':
                # Encontramos un cierre de paréntesis, volvemos al estado anterior
                estado_actual = 'q{}'.format(i)
            else:
                # Caracteres individuales, creamos transiciones para ellos
                nuevo_estado = 'q{}'.format(i + 1)
                self.agregar_transicion(estado_actual, caracter, nuevo_estado)
                estado_actual = nuevo_estado

        # Agregamos un estado final
        estado_final = 'q{}'.format(len(expresion_regular))
        self.agregar_estado_final(estado_final)

        # Agregamos una transición epsilon desde el último estado al estado final
        self.agregar_transicion(estado_actual, '', estado_final)

    def minimizar(self):
        # Pasos preliminares: dividir los estados en dos conjuntos, finales y no finales
        estados_finales = self.estados_finales
        estados_no_finales = set(self.transiciones.keys()) - estados_finales

        particion_actual = [estados_finales, estados_no_finales]
        particion_anterior = []

        # Iteramos hasta que no haya cambios en la partición
        while particion_actual != particion_anterior:
            particion_anterior = particion_actual
            nueva_particion = []

            for conjunto in particion_actual:
                for simbolo in self.obtener_alfabeto():
                    # Dividimos el conjunto actual en subconjuntos según la transición con el símbolo actual
                    subconjuntos = self.dividir_conjunto(conjunto, simbolo, particion_actual)
                    for subconjunto in subconjuntos:
                        if subconjunto not in nueva_particion:
                            nueva_particion.append(subconjunto)

            particion_actual = nueva_particion

        # Creamos un nuevo autómata con la partición final
        automata_minimizado = Automata()

        for i, conjunto in enumerate(particion_actual):
            nuevo_estado = 'q{}'.format(i)
            automata_minimizado.agregar_estado_final(nuevo_estado)
            for estado in conjunto:
                automata_minimizado.transiciones[estado] = {simbolo: nuevo_estado for simbolo, siguiente_estado in
                                                            self.transiciones[estado].items()}

        # Establecemos el nuevo estado inicial
        estado_inicial_original = self.estado_inicial
        estado_inicial_minimizado = next(
            iter([estado for estado in particion_actual if estado_inicial_original in estado]))
        automata_minimizado.definir_estado_inicial(estado_inicial_minimizado)

        return automata_minimizado

    def obtener_alfabeto(self):
        # Método auxiliar para obtener el alfabeto del autómata
        alfabeto = set()
        for transiciones in self.transiciones.values():
            for simbolo in transiciones.keys():
                if simbolo != '':
                    alfabeto.add(simbolo)
        return alfabeto

    def dividir_conjunto(self, conjunto, simbolo, particion_actual):
        # Método auxiliar para dividir un conjunto en subconjuntos según la transición con un símbolo
        subconjuntos = []
        for estado in conjunto:
            siguiente_estado = self.transiciones[estado].get(simbolo, None)
            for subconjunto in particion_actual:
                if siguiente_estado in subconjunto:
                    subconjuntos.append(subconjunto)
                    break
        return subconjuntos

    def dibujar(self):
        dot = Digraph()

        for estado, transiciones in self.transiciones.items():
            if estado in self.estados_finales:
                dot.node(estado, shape='doublecircle')
            else:
                dot.node(estado)

            for simbolo, siguiente_estado in transiciones.items():
                dot.edge(estado, siguiente_estado, label=simbolo)

        dot.edge('', self.estado_inicial, arrowhead='vee', style='solid', color='black', headport='e', tailport='n', dir='forward', constraint='false')
        dot.node('', shape='point', style='invis', width='0', height='0')

        return dot
