from graphviz import Digraph
import os
class Vista:
    def __init__(self):
        pass

    def mostrar_menu(self):
        # Muestra el menú de opciones
        print("Bienvenido al Conversor de Expresiones Regulares a Autómatas")
        print("Seleccione una opción:")
        print("1. Ingresar una expresión regular")
        print("2. Convertir expresión regular a DFA")
        print("3. Convertir expresión regular a NFA")
        print("4. Salir")

    def obtener_expresion_regular(self):
        # Solicita al usuario ingresar una expresión regular y la devuelve
        expresion = input("Ingrese la expresión regular: ")
        return expresion

    def mostrar_resultado(self, resultado):
        # Muestra el resultado de la conversión
        if resultado:
            print("Expresión regular convertida exitosamente.")
        else:
            print("Error al convertir la expresión regular.")

    def mostrar_grafo(self, grafo):
        dot = Digraph(comment='Grafo')

        # Agregar nodos y transiciones al grafo
        for estado, transiciones in grafo.items():
            dot.node(str(estado), shape='doublecircle' if estado in grafo['estados_aceptacion'] else 'circle')
            for simbolo, siguiente_estado in transiciones.items():
                dot.edge(str(estado), str(siguiente_estado), label=simbolo)

        # Guardar el grafo como imagen
        dot.render('grafo', format='png', cleanup=True)
        print("Grafo generado correctamente.")

        # Obtener la ruta del archivo de imagen generado
        image_path = os.path.join(os.getcwd(), 'grafo.png')

        # Intentar abrir automáticamente el archivo de imagen
        try:
            if os.name == 'nt':  # Verificar si el sistema operativo es Windows
                os.startfile(image_path)  # Abrir automáticamente en Windows
            else:
                print(
                    f"La imagen del grafo se ha guardado en: {image_path}")  # Mostrar la ubicación del archivo en otros sistemas operativos
        except Exception as e:
            print(f"Error al abrir la imagen del grafo: {str(e)}")
