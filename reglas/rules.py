from experta import *
from collections import Mapping



class Residencia(Fact):
    """Info about the traffic light."""
    pass


class ReservarHabitacion(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.resultados = {}

    @Rule(Residencia(tipo='nativo'))
    def green_light(self):
        print("Walk")
        self.resultados["residencia"]="Elegiste Nativo"


    @Rule(Residencia(tipo='exterior'))
    def red_light(self):
        print("Don't walk")