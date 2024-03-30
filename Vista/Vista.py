
from graphviz import Digraph

class Vista:
    def ingresar_expresion_regular(self):
        expresion_regular = input("Ingrese la expresión regular: ")
        return expresion_regular

    def mostrar_automata(self, automata):
        automata_dibujado = automata.dibujar()
        automata_dibujado.view()

    def mostrar_error(self, mensaje):
        print("Error:", mensaje)