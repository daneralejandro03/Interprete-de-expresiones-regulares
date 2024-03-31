class Vista:
    def mostrar_menu(self):
        # Implementación para mostrar el menú
        print("1. Ingresar expresión regular")
        print("2. Salir")
    
    def mostrar_mensaje(self, mensaje: str):
        # Implementación para mostrar mensajes
        print(mensaje)
        
    def leer_opcion(self) -> int:
        # Implementación para leer la opción del usuario
        return int(input("Introduce una opción: "))
    
    def leer_expresion(self) -> str:
        # Implementación para leer la expresión regular del usuario
        return input("Introduce una expresión regular: ")

    def mostrar_automata(self, info_automata: str):
        # Implementación para mostrar la información del autómata
        print(info_automata)
        
    def mostrar_error(self, mensaje_error: str):
        # Implementación para mostrar mensajes de error
        print(f"Error: {mensaje_error}")