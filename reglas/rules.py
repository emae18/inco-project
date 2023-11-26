from experta import *


class Residencia(Fact):
    """Info about the traffic light."""
    pass


class ReservarHabitacion(KnowledgeEngine):
    @Rule(Residencia(tipo='nativo'))
    def green_light(self):
        print("Walk")

    @Rule(Residencia(tipo='exterior'))
    def red_light(self):
        print("Don't walk")