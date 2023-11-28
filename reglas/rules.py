from experta import *
from collections import Mapping


class Servicio(Fact):
    """ Inicializar la clase servicio """
    pass

class Bandera(Fact):
    """ Inicializar la clase bandera """
    pass

class Residencia(Fact):
    """ Inicializar la clase residencia """
    pass
class Cantidad(Fact):
    """ Inicializar la clase cantidad"""
    pass

class Edad(Fact):
    """ Inicializar la clase edad """
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
        yield Habitacion(numero= "101", cantidad="1", edad="joven", tipo="Single" )
        yield Habitacion(numero= "2041", cantidad="1", edad="joven", tipo="Suite senior sin vista panorámica" )
        yield Habitacion(numero= "2015", cantidad="1", edad="joven", tipo="Suite senior con vista panorámica" )
        yield Habitacion(numero= "2031", cantidad="1", edad="joven", tipo="Suite junior" )

        yield Habitacion(numero= "201", cantidad="2", edad="joven", tipo="Single doble" )
        yield Habitacion(numero= "2031", cantidad="2", edad="joven", tipo="Suite junior" )
        yield Habitacion(numero= "2041", cantidad="2", edad="joven", tipo="Suite senior" )
        yield Habitacion(numero= "2015", cantidad="2", edad="joven", tipo="Suite senior" )
        
        yield Habitacion(numero= "2011", cantidad="4", edad="joven", tipo="Single cuádruple" )
        yield Habitacion(numero= "2021", cantidad="5", edad="joven", tipo="Single quíntuple" )

        yield Habitacion(numero= "101", cantidad="1", edad="adulto", tipo="Single" )
        yield Habitacion(numero= "2041", cantidad="1", edad="adulto", tipo="Suite senior sin vista panorámica" )
        yield Habitacion(numero= "2015", cantidad="1", edad="adulto", tipo="Suite senior con vista panorámica" )

        yield Habitacion(numero= "201", cantidad="2", edad="adulto", tipo="Single doble" )
        yield Habitacion(numero= "2031", cantidad="2", edad="adulto", tipo="Suite junior" )
        yield Habitacion(numero= "2041", cantidad="2", edad="adulto", tipo="Suite senior" )
        yield Habitacion(numero= "2015", cantidad="2", edad="adulto", tipo="Suite senior" )
        
        yield Habitacion(numero= "2011", cantidad="4", edad="adulto", tipo="Single cuádruple" )
        yield Habitacion(numero= "2021", cantidad="5", edad="adulto", tipo="Single quíntuple" )

        yield Habitacion(numero= "2041", residencia="Nativo", cantidad="1", tipo="Suite senior sin vista panorámica" )
        yield Habitacion(numero= "2041", residencia="Nativo", cantidad="2", tipo="Suite senior sin vista panorámica" )
        yield Habitacion(numero= "2015", residencia="Extranjero", cantidad="1", tipo="Suite senior con vista panorámica" )
        yield Habitacion(numero= "2015", residencia="Extranjero", cantidad="2", tipo="Suite senior con vista panorámica" )

        yield Habitacion(numero= "101", tipo="Single" )
        yield Habitacion(numero= "201", tipo="Single doble" )
        yield Habitacion(numero= "2011", tipo="Single cuádruple" )
        yield Habitacion(numero= "2021", tipo="Single quíntuple" )
        yield Habitacion(numero= "2031", tipo="Suite junior" )
        yield Habitacion(numero= "2041", tipo="Suite senior sin vista panorámica" )
        yield Habitacion(numero= "2015", tipo="Suite senior con vista panorámica" )
    
        yield Habitacion(numero= "101", servicio="Complementario", cantidad="1", tipo="Single" )
        yield Habitacion(numero= "201", servicio="Complementario", cantidad="2", tipo="Single doble" )
        yield Habitacion(numero= "2011", servicio="Complementario", cantidad="4", tipo="Single cuádruple" )
        yield Habitacion(numero= "2021", servicio="Complementario", cantidad="5", tipo="Single quíntuple" )
        yield Habitacion(numero= "2031", servicio="Jacuzzi con hidromasajes", cantidad="1", tipo="Suite junior" )
        yield Habitacion(numero= "2031", servicio="2 ambientes", cantidad="2", tipo="Suite junior" )
        yield Habitacion(numero= "2041", servicio="2 ambientes", cantidad="1", tipo="Suite senior" )
        yield Habitacion(numero= "2041", servicio="Vista panorámica", cantidad="2", tipo="Suite senior" )
        yield Habitacion(numero= "2015", servicio="Vista panorámica", cantidad="1", tipo="Suite senior" )
        yield Habitacion(numero= "2015", servicio="2 ambientes", cantidad="2", tipo="Suite senior" )
    

        
    
    @Rule(Habitacion (residencia=MATCH.r, cantidad=MATCH.c, numero=MATCH.n), Residencia(residencia=MATCH.r), Cantidad(cantidad=MATCH.c))
    def recomendación_2(self, r, c, n):
        """
        El cliente solo puede acceder a habitaciones según sus preferencias
        """
        print("recomendación 2 "+ n)
        self.declare(Recomendacion(residencia=r, cantidad=c, numero=n))

    @Rule(Habitacion (tipo=MATCH.t, numero=MATCH.n), Tipo(tipo=MATCH.t))
    def recomendación_3(self, t, n):
        """
        El cliente solo puede acceder a habitaciones según sus preferencias
        """
        print("recomendación 3 "+ n)
        self.declare(Recomendacion(tipo=t, numero=n))
        self.halt()
        
    @Rule(Habitacion(servicio=MATCH.s, cantidad=MATCH.c, numero=MATCH.n), Servicio(servicio=MATCH.s),Cantidad(cantidad=MATCH.c))
    def recomendación_4(self, s, n):
        """
        El cliente puede acceder a la habitacion con el servicio seleccionado
        """
        print("recomendación 4 "+ n)
        self.declare(Recomendacion(servicio=s, numero=n))
        self.halt()

    @Rule(Habitacion (cantidad=MATCH.c, numero=MATCH.n, edad=MATCH.e), Cantidad(cantidad=MATCH.c), Edad(edad=MATCH.e) )
    def recomendación_1(self, c, n, e):
        """
        El cliente solo puede acceder a habitaciones según sus preferencias
        """
        print("recomendación 1 "+ n)
        self.declare(Recomendacion(cantidad=c, numero=n, edad=e))
        
