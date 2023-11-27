from experta import *
from collections import Mapping


class Servicio(Fact):
    """ Inicializar la clase servicio """
    pass

class Residencia(Fact):
    """ Inicializar la clase recidencia """
    pass
class Cantidad(Fact):
    """ Inicializar la clase cantidad"""
    pass

class Precio(Fact):
    """ Inicializar la clase precio """
    pass
class Tipo(Fact):
    """ Inicializar la clase tipo"""
    pass

class Habitacion(Fact):
    """ Inicializar la clase habitación"""
    pass

class Recomendacion(Fact):
    """ Inicializar la clase recomendación"""
    pass

class RecomendarHabitacion(KnowledgeEngine):
    @DefFacts()
    def carga_habitación(self):
        """
        Hechos iniciales.
        """
        yield Habitacion(servicio="Complementario", residencia="Nativo", cantidad="1", tipo="Single" )
        yield Habitacion(servicio="Complementario", residencia="Nativo", cantidad="2", tipo="Single doble" )
        yield Habitacion(servicio="Complementario", residencia="Nativo", cantidad="4", tipo="Single cuádruple" )
        yield Habitacion(servicio="Complementario", residencia="Nativo", cantidad="5", tipo="Single quíntuple" )
        yield Habitacion(servicio="Complementario", residencia="Nativo", cantidad="1", tipo="Suite junior" )
        yield Habitacion(servicio="Vista panoramica", residencia="Extrangero", cantidad="2", tipo="Suite senior" )
    

    @Rule(Habitacion(servicio=MATCH.s, recidencia=MATCH.r, cantidad=MATCH.c, tipo=MATCH.t),Servicio(servicio=MATCH.s), Residencia(residencia=MATCH.r), Cantidad(cantidad=MATCH.c), Tipo(tipo=MATCH.t))
    def recomendación_1(self, s, r, c, t):
        """
        El cliente solo puede acceder a habitaciones tipo single si solo desea servicios complementarios
        """
        self.declare(Recomendacion(servicio=s, residencia=r, cantidad=c, tipo=t))
        
    @Rule(Habitacion(servicio=MATCH.s),
          Servicio(servicio=MATCH.s))
    def recomendación_2(self, s):
        """
        El cliente puede acceder a la habitacion con el servicio personalizado y servicios complementarios
        """
        print(s)
        self.declare(Recomendacion(servicio=s))
     