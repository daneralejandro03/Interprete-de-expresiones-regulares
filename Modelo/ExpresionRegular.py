from collections import deque

class ExpresionRegular:
    def __init__(self, expresion):
        self.expresion = expresion

    def convertir_a_DFA(self):
        nfa = self.convertir_a_NFA()
        dfa = self.convertir_NFA_a_DFA(nfa)
        return dfa

    def convertir_a_NFA(self):
        stack = []
        operadores = set('(|*')
        nfa = {'transiciones': []}

        for char in self.expresion:
            if char.isalnum():
                estado_inicial = len(nfa['transiciones'])
                estado_aceptacion = estado_inicial + 1
                nfa['transiciones'].append({'origen': estado_inicial, 'destino': estado_aceptacion, 'simbolo': char})
                nfa.update({'estado_inicial': estado_inicial, 'estado_aceptacion': estado_aceptacion})
                stack.append(nfa)
                nfa = {'transiciones': []}
            elif char == '|':
                nfa2 = stack.pop()
                nfa1 = stack.pop()
                nuevo_nfa = self.unir_NFA(nfa1, nfa2)
                stack.append(nuevo_nfa)
            elif char == '.':
                nfa2 = stack.pop()
                nfa1 = stack.pop()
                nuevo_nfa = self.concatenar_NFA(nfa1, nfa2)
                stack.append(nuevo_nfa)
            elif char == '*':
                nfa1 = stack.pop()
                nuevo_nfa = self.cerrar_NFA(nfa1)
                stack.append(nuevo_nfa)

        return stack.pop()  # Devolver el NFA completo

    def convertir_NFA_a_DFA(self, nfa):
        def obtener_epsilon_cerradura(estado, transiciones):
            cerradura = set()
            por_explorar = deque()
            por_explorar.append(estado)

            while por_explorar:
                actual = por_explorar.pop()
                cerradura.add(actual)

                for transicion in transiciones:
                    origen, destino, simbolo = transicion.values()
                    if origen == actual and simbolo is None and destino not in cerradura:
                        por_explorar.append(destino)

            return frozenset(cerradura)

        def obtener_transicion(estado, simbolo, transiciones):
            nuevos_estados = set()

            for transicion in transiciones:
                origen, destino, sim = transicion.values()
                if origen in estado and sim == simbolo:
                    nuevos_estados.add(destino)

            if nuevos_estados:
                return frozenset(nuevos_estados)
            else:
                return None

        estado_inicial_nfa = frozenset([nfa['estado_inicial']])
        estados_aceptacion_nfa = frozenset([nfa['estado_aceptacion']])
        transiciones_nfa = nfa['transiciones']

        alfabeto = set()
        for transicion in transiciones_nfa:
            alfabeto.add(transicion['simbolo'])

        cola = deque()
        estado_inicial_dfa = obtener_epsilon_cerradura(estado_inicial_nfa, transiciones_nfa)
        cola.append(estado_inicial_dfa)
        estados_dfa = {estado_inicial_dfa}
        dfa_transiciones = {}

        while cola:
            estado = cola.popleft()
            dfa_transiciones[estado] = {}

            for simbolo in alfabeto:
                nuevo_estado = obtener_transicion(estado, simbolo, transiciones_nfa)

                if nuevo_estado is not None:
                    cerradura = obtener_epsilon_cerradura(nuevo_estado, transiciones_nfa)
                    dfa_transiciones[estado][simbolo] = cerradura

                    if cerradura not in estados_dfa:
                        estados_dfa.add(cerradura)
                        cola.append(cerradura)

        estados_aceptacion_dfa = {estado for estado in estados_dfa if estados_aceptacion_nfa & estado}

        return {
            'estado_inicial': estado_inicial_dfa,
            'estados_aceptacion': estados_aceptacion_dfa,
            'transiciones': dfa_transiciones
        }
    def unir_NFA(self, nfa1, nfa2):
        estado_inicial = len(nfa1['transiciones'])
        estado_aceptacion = estado_inicial + len(nfa2['transiciones']) + 1

        transiciones = []
        for transicion in nfa1['transiciones']:
            transiciones.append({'origen': transicion['origen'] + 1, 'destino': transicion['destino'] + 1, 'simbolo': transicion['simbolo']})

        for transicion in nfa2['transiciones']:
            transiciones.append({'origen': transicion['origen'] + len(nfa1['transiciones']) + 1, 'destino': transicion['destino'] + len(nfa1['transiciones']) + 1, 'simbolo': transicion['simbolo']})

        transiciones.append({'origen': estado_inicial, 'destino': nfa1['estado_inicial'] + 1, 'simbolo': None})
        transiciones.append({'origen': estado_inicial, 'destino': len(nfa1['transiciones']) + 1, 'simbolo': None})
        transiciones.append({'origen': nfa1['estado_aceptacion'], 'destino': estado_aceptacion, 'simbolo': None})
        transiciones.append({'origen': len(nfa1['transiciones']) + len(nfa2['transiciones']), 'destino': estado_aceptacion, 'simbolo': None})

        return {'estado_inicial': estado_inicial, 'estado_aceptacion': estado_aceptacion, 'transiciones': transiciones}

    def concatenar_NFA(self, nfa1, nfa2):
        transiciones = []
        for transicion in nfa1['transiciones']:
            transiciones.append({'origen': transicion['origen'], 'destino': transicion['destino'], 'simbolo': transicion['simbolo']})

        for transicion in nfa2['transiciones']:
            transiciones.append({'origen': transicion['origen'] + len(nfa1['transiciones']), 'destino': transicion['destino'] + len(nfa1['transiciones']), 'simbolo': transicion['simbolo']})

        transiciones.append({'origen': nfa1['estado_aceptacion'], 'destino': nfa1['estado_aceptacion'] + len(nfa1['transiciones']), 'simbolo': None})

        return {'estado_inicial': nfa1['estado_inicial'], 'estado_aceptacion': nfa2['estado_aceptacion'] + len(nfa1['transiciones']), 'transiciones': transiciones}

    def cerrar_NFA(self, nfa):
        transiciones = []
        for transicion in nfa['transiciones']:
            transiciones.append({'origen': transicion['origen'] + 1, 'destino': transicion['destino'] + 1, 'simbolo': transicion['simbolo']})

        transiciones.append({'origen': 0, 'destino': len(nfa['transiciones']) + 1, 'simbolo': None})
        transiciones.append({'origen': 0, 'destino': 1, 'simbolo': None})
        transiciones.append({'origen': nfa['estado_aceptacion'], 'destino': 0, 'simbolo': None})
        transiciones.append({'origen': nfa['estado_aceptacion'], 'destino': len(nfa['transiciones']) + 1, 'simbolo': None})

        return {'estado_inicial': 0, 'estado_aceptacion': len(nfa['transiciones']) + 1, 'transiciones': transiciones}
