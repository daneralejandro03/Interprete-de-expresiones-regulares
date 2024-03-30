class Vista:
    def mostrar_menu(self):
        # Implementación para mostrar el menú
        print("1. Ingresar expresión regular")
        print("2. Salir")

    def mostrar_automata(self, info_automata: str):
        # Implementación para mostrar la información del autómata
        print(info_automata)

    def mostrar_error(self, mensaje_error: str):
        # Implementación para mostrar mensajes de error
        print(f"Error: {mensaje_error}")