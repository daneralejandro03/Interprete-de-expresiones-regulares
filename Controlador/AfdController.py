from Modelo.AfdModel import AfdModel
from Vista.AfdView import AfdView
class AfdController:
    def __init__(self):
        self.model = AfdModel()
        self.view = AfdView()

    def generate_afd(self, expresion_regular):
        subexpresiones = self.model.dividir_expresion(expresion_regular)
        self.model.generar_afd(subexpresiones)
        return self.model.get_afd()

    def render_afd(self, afd, filename):
        for estado, transiciones in afd.items():
            self.view.add_node(estado)

            for simbolo, destinos in transiciones.items():
                if isinstance(destinos, list):
                    for destino in destinos:
                        self.view.add_edge(estado, destino, simbolo)
                else:
                    self.view.add_edge(estado, destinos, simbolo)

        self.view.render(filename)

# Example usage
controller = AfdController()
#afd = controller.generate_afd("(a)(a|b)*")
#afd = controller.generate_afd("(a)(b)(c)*")
afd = controller.generate_afd("(a)*(a|b)(b)*")
#afd = controller.generate_afd("(a|b)*(b)(a|ab)*")
#afd = controller.generate_afd("ab(b)*|(a|b)*b(b)*")
controller.render_afd(afd, "automata_afd")