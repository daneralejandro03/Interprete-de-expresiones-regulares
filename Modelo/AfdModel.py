import re
class AfdModel:
    def __init__(self):
        self.afd = {}

    def dividir_expresion(self, expresion):
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

    def obtener_caracteres(self, expresion):
        # Busca todos los caracteres entre paréntesis
        caracteres_entre_parentesis = re.findall(r'\((.*?)\)', expresion)

        # Divide los caracteres y los une en una sola lista
        caracteres = ''.join(caracteres_entre_parentesis).split('|')

        return caracteres

    def generar_afd(self, subexpresiones):
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
                opciones = self.obtener_caracteres(expresion)
                self.afd[estado1] = {opciones[0]: estado2, opciones[1]: estado2}
                self.afd[estado2] = {expresion_sin_parentesis: estado2}
            elif "|" in expresion:
                opciones = self.obtener_caracteres(expresion)
                if (self.afd[estado1]) != None:  # Verifica si el estado ya existe en afd2
                    clav = ""
                    val = ""
                    transiciones = self.afd[estado1].copy()  # Crea una copia de las transiciones existentes
                    print(f"copia: {transiciones}")
                    for clave, valor in transiciones.items():
                        clav = clave
                        val = valor

                    self.afd[estado1] = {opciones[0]: [estado2, val],
                                         opciones[1]: estado2}  # Actualiza afd2 con las transiciones combinadas
                else:
                    self.afd[estado1] = {opciones[0]: estado2,
                                         opciones[1]: estado2}  # Si no existe, crea las transiciones directamente
                print(f"Estado {estado1} va con {opciones[0]} hacia {estado2}")
                print(f"Estado {estado1} va con {opciones[1]} hacia {estado2}")
                # afd2[estado1] = {opciones[0]: estado2, opciones[1]: estado2}
            elif "*" in expresion:
                expresion_sin_asterisco = expresion.strip("*")
                expresion_sin_parentesis = expresion_sin_asterisco.strip("()")
                print(f"Estado {estado1} va con {expresion_sin_parentesis} hacia {estado2}")
                print(f"Estado {estado2} va con {expresion_sin_parentesis} hacia {estado2}")
                self.afd[estado1] = {expresion_sin_parentesis: estado2, 'E': estado2}
                self.afd[estado2] = {expresion_sin_parentesis: estado2}
            elif "*" not in expresion:
                expresion_sin_parentesis = expresion.strip("()")
                print(f"Estado {estado1} va con {expresion_sin_parentesis} hacia {estado2}")
                self.afd[estado1] = {expresion_sin_parentesis: estado2}
            estado_final = estado1

            numero += 1
            estado = "q"

    def get_afd(self):
        return self.afd