from Vista.Vista import Vista
from Modelo.ExpresionRegular import ExpresionRegular
class Controlador:
    def __init__(self):
        self.vista = Vista()
        self.expresion_regular = None

    def ejecutar(self):
        while True:
            self.vista.mostrar_menu()
            opcion = input("Ingrese el número de la opción deseada: ")

            if opcion == '1':
                expresion_regular = self.vista.obtener_expresion_regular()
                self.procesar_expresion_regular(expresion_regular)
            elif opcion == '2':
                self.convertir_a_dfa()
            elif opcion == '3':
                self.convertir_a_nfa()
            elif opcion == '4':
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Por favor, ingrese un número válido.")

    def procesar_expresion_regular(self, expresion_regular):
        try:
            self.expresion_regular = ExpresionRegular(expresion_regular)
            print("Expresión regular procesada correctamente.")
        except Exception as e:
            print(f"Error al procesar la expresión regular: {str(e)}")

    def convertir_a_dfa(self):
        if self.expresion_regular is None:
            print("Primero debe ingresar una expresión regular.")
            return

        try:
            dfa = self.expresion_regular.convertir_a_DFA()
            self.vista.mostrar_grafo(dfa)  # Aquí se llama a mostrar_grafo
            self.vista.mostrar_resultado(dfa)
        except Exception as e:
            print(f"Error al convertir a DFA: {str(e)}")

    def convertir_a_nfa(self):
        if self.expresion_regular is None:
            print("Primero debe ingresar una expresión regular.")
            return

        try:
            nfa = self.expresion_regular.convertir_a_NFA()
            self.vista.mostrar_grafo(nfa)  # Aquí también se llama a mostrar_grafo
            self.vista.mostrar_resultado(nfa)
        except Exception as e:
            print(f"Error al convertir a NFA: {str(e)}")

if __name__ == "__main__":
    controlador = Controlador()
    controlador.ejecutar()
