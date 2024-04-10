from graphviz import Digraph
import re

# expresion_regular = "(a)(a|b)*"
# expresion_regular = "(a)(b)(c)*"
expresion_regular = "(a)*(a|b)(b)*"
# expresion_regular = "(a|b)*(b)(a|ab)*"
# expresion_regular = "ab(b)*|(a|b)*b(b)*"

estados_dos = []


def dividir_expresion(expresion):
    subexpresiones = []
    subexpresion_actual = ''
    nivel = 0

    for char in expresion:
        if char == '(':
            nivel += 1
            subexpresion_actual += char
        elif char == ')':
            nivel -= 1
            subexpresion_actual += char
            if nivel == 0:
                subexpresiones.append(subexpresion_actual)
                subexpresion_actual = ''
        elif char == '*' and nivel == 0:
            subexpresiones[-1] += char
        else:
            subexpresion_actual += char

    return subexpresiones


subexpresiones = dividir_expresion(expresion_regular)
print(subexpresiones)


def obtener_caracteres(expresion):
    # Busca todos los caracteres entre paréntesis
    caracteres_entre_parentesis = re.findall(r'\((.*?)\)', expresion)

    # Divide los caracteres y los une en una sola lista
    caracteres = ''.join(caracteres_entre_parentesis).split('|')

    return caracteres


def generar_afd(subexpresiones):
    estado = "q"
    numero = 0
    for expresion in subexpresiones:
        estado1 = estado + str(numero)
        estado2 = estado + str(numero + 1)
        estado3 = estado + str(numero + 2)
        if "*" in expresion and "|" in expresion:
            expresion_sin_asterisco = expresion.strip("*")
            expresion_sin_parentesis = expresion_sin_asterisco.strip("()")
            print(f"Estado {estado1} va con {expresion_sin_parentesis} hacia {estado2}")
            print(f"Estado {estado2} va con {expresion_sin_parentesis} hacia {estado2}")
            opciones = obtener_caracteres(expresion)
            afd2[estado1] = {opciones[0]: estado2, opciones[1]: estado2}
            afd2[estado2] = {expresion_sin_parentesis: estado2}
        elif "|" in expresion:
            opciones = obtener_caracteres(expresion)
            if (afd2[estado1]) != None:  # Verifica si el estado ya existe en afd2
                clav = ""
                val = ""
                transiciones = afd2[estado1].copy()  # Crea una copia de las transiciones existentes
                print(f"copia: {transiciones}")
                for clave, valor in transiciones.items():
                    clav = clave
                    val = valor

                afd2[estado1] = {opciones[0]: [estado2, val],
                                 opciones[1]: estado2}  # Actualiza afd2 con las transiciones combinadas
            else:
                afd2[estado1] = {opciones[0]: estado2,
                                 opciones[1]: estado2}  # Si no existe, crea las transiciones directamente
            print(f"Estado {estado1} va con {opciones[0]} hacia {estado2}")
            print(f"Estado {estado1} va con {opciones[1]} hacia {estado2}")
            # afd2[estado1] = {opciones[0]: estado2, opciones[1]: estado2}
        elif "*" in expresion:
            expresion_sin_asterisco = expresion.strip("*")
            expresion_sin_parentesis = expresion_sin_asterisco.strip("()")
            print(f"Estado {estado1} va con {expresion_sin_parentesis} hacia {estado2}")
            print(f"Estado {estado2} va con {expresion_sin_parentesis} hacia {estado2}")
            afd2[estado1] = {expresion_sin_parentesis: estado2, 'E': estado2}
            afd2[estado2] = {expresion_sin_parentesis: estado2}
        elif "*" not in expresion:
            expresion_sin_parentesis = expresion.strip("()")
            print(f"Estado {estado1} va con {expresion_sin_parentesis} hacia {estado2}")
            afd2[estado1] = {expresion_sin_parentesis: estado2}
        estado_final = estado1

        numero += 1
        estado = "q"


afd2 = {}
generar_afd(subexpresiones)
estado_final = {}

estado_inicial = 'q0'
estados_finales = {'q2'}

# Crea un objeto Digraph
dot = Digraph()

# Agrega los estados y transiciones al objeto Digraph
for estado, transiciones in afd2.items():
    if estado in estado_final:
        dot.node(estado, shape='doublecircle')
    else:
        dot.node(estado)

    for simbolo, destinos in transiciones.items():
        if isinstance(destinos, list):
            for destino in destinos:
                dot.edge(estado, destino, label=simbolo)
        else:
            dot.edge(estado, destinos, label=simbolo)

# Agrega la flecha entrante al estado inicial y lo hace invisible
dot.edge('', estado_inicial, arrowhead='vee', style='solid', color='black', headport='e', tailport='n', dir='forward',
         constraint='false')
dot.node('', shape='point', style='invis', width='0', height='0')

# Guarda el grafo en un archivo
dot.render('automata_afd', format='png', cleanup=True)
