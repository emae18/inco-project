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
        yield Habitacion(servicio="Complementario", numero= "101", residencia="Nativo", cantidad="1", tipo="Single" )
        yield Habitacion(servicio="Complementario", numero= "201", residencia="Nativo", cantidad="2", tipo="Single doble" )
        yield Habitacion(servicio="Complementario", numero= "2011", residencia="Nativo", cantidad="4", tipo="Single cuádruple" )
        yield Habitacion(servicio="Complementario", numero= "2021", residencia="Nativo", cantidad="5", tipo="Single quíntuple" )
        yield Habitacion(servicio="2 ambientes", numero= "2031", residencia="Nativo", tipo="Suite junior" )
        yield Habitacion(servicio="Jacuzzi con hidromasaje", numero= "2031", residencia="Nativo", tipo="Suite junior" )
        yield Habitacion(servicio="2 ambientes", numero= "2041", residencia="Nativo", tipo="Suite senior" )
        yield Habitacion(servicio="Jacuzzi con hidromasaje", numero= "2041", residencia="Nativo", tipo="Suite senior" )
        yield Habitacion(servicio="Vista panoramica", numero= "2041", residencia="Nativo", tipo="Suite senior" )

        yield Habitacion(servicio="Complementario", numero= "101", residencia="Extranjero", cantidad="1", tipo="Single" )
        yield Habitacion(servicio="Complementario", numero= "201", residencia="Extranjero", cantidad="2", tipo="Single doble" )
        yield Habitacion(servicio="Complementario", numero= "2011", residencia="Extranjero", cantidad="4", tipo="Single cuádruple" )
        yield Habitacion(servicio="Complementario", numero= "2021", residencia="Extranjero", cantidad="5", tipo="Single quíntuple" )
        yield Habitacion(servicio="2 ambientes", numero= "2031", residencia="Extranjero", tipo="Suite junior" )
        yield Habitacion(servicio="Jacuzzi con hidromasaje", numero= "2031", residencia="Extranjero", tipo="Suite junior" )
        yield Habitacion(servicio="2 ambientes", numero= "2041", residencia="Extranjero", tipo="Suite senior" )
        yield Habitacion(servicio="Jacuzzi con hidromasaje", numero= "2041", residencia="Extranjero", tipo="Suite senior" )
        yield Habitacion(servicio="Vista panoramica", numero= "2041", residencia="Extranjero", tipo="Suite senior" )

        yield Habitacion(edad="adulto", numero= "2041", residencia="Extranjero", tipo="Suite senior con vista panorámica" )
        yield Habitacion(edad="joven", numero= "2041", residencia="Extranjero", tipo="Suite senior con vista panorámica" )
    

    @Rule(OR (Habitacion(servicio=MATCH.s), Habitacion (residencia=MATCH.r), Habitacion(cantidad=MATCH.c), Habitacion(tipo=MATCH.t), Habitacion(numero=MATCH.n), Habitacion(edad=MATCH.e)),Servicio(servicio=MATCH.s), Residencia(residencia=MATCH.r), Cantidad(cantidad=MATCH.c), Tipo(tipo=MATCH.t))
    def recomendación_1(self, s, r, c, t, n, e):
        """
        El cliente solo puede acceder a habitaciones según sus preferencias
        """
        print("recomendación 1 "+ t)
        self.declare(Recomendacion(servicio=s, residencia=r, cantidad=c, tipo=t, numero=n, edad=e))
        
    @Rule(Habitacion(servicio=MATCH.s, numero=MATCH.n), Servicio(servicio=MATCH.s))
    def recomendación_2(self, s, n):
        """
        El cliente puede acceder a la habitacion con el servicio seleccionado
        """
        print("recomendación 2 "+ s)
        self.declare(Recomendacion(servicio=s, numero=n))

    @Rule(Habitacion(servicio=MATCH.s, residencia=MATCH.r, numero=MATCH.n),Servicio(servicio=MATCH.s), Residencia(residencia=MATCH.r))
    def recomendación_3(self, s, r, n):
        """
        El cliente solo puede acceder a habitaciones según sus preferencias
        """
        print("recomendación 3 "+ r)
        self.declare(Recomendacion(servicio=s, residencia=r, numero=n))
        
    @Rule(OR (Habitacion(servicio=MATCH.s), Habitacion(cantidad=MATCH.c), Habitacion(numero=MATCH.n)),Servicio(servicio=MATCH.s), Cantidad(cantidad=MATCH.c))
    def recomendación_4(self, s, c, n):
        """
        El cliente solo puede acceder a habitaciones según sus preferencias
        """
        print("recomendación 4 "+ n)
        self.declare(Recomendacion(servicio=s, cantidad=c, numero=n))
        
    @Rule(Habitacion(edad=MATCH.e, cantidad=MATCH.c, numero=MATCH.n), Tipo(edad=MATCH.e), Cantidad(cantidad=MATCH.c,))
    def recomendación_5(self, e, c, n):
        """
        El cliente solo puede acceder a habitaciones según sus preferencias
        """
        print("recomendación 5 "+ c)
        self.declare(Recomendacion(edad=e, cantidad=c, numero=n))
        
    @Rule(Habitacion(cantidad=MATCH.c, tipo=MATCH.t, numero=MATCH.n),Cantidad(cantidad=MATCH.c), Tipo(tipo=MATCH.t))
    def recomendación_6(self, c, t, n):
        """
        El cliente solo puede acceder a habitaciones según sus preferencias
        """
        print("recomendación 7 "+ t)
        self.declare(Recomendacion(cantidad=c, tipo=t, numero=n))
        
    @Rule(OR (Habitacion(residencia=MATCH.r), Habitacion(tipo=MATCH.t), Habitacion(numero=MATCH.n)),Residencia(residencia=MATCH.r), Tipo(tipo=MATCH.t))
    def recomendación_7(self, r,t,n):
        """
        El cliente solo puede acceder a habitaciones según sus preferencias
        """
        print("recomendación 7 "+ t)
        self.declare(Recomendacion(residencia=r, tipo=t,numero=n))
    
    
    @Rule(Habitacion(residencia=MATCH.r, edad=MATCH.e, tipo=MATCH.t, numero=MATCH.n), Residencia(residencia=MATCH.r), Edad(edad=MATCH.e))
    def recomendación_8(self, r, e, t, n):
        """
        El cliente puede acceder a la habitacion con el servicio seleccionado
        """
        print("recomendación 8 "+ t)
        self.declare(Recomendacion(recidencia=r, edad=e,tipo=t, numero=n))
    
    @Rule(Habitacion(tipo=MATCH.t, numero=MATCH.n), Tipo(tipo=MATCH.t))
    def recomendación_9(self, t, n):
        """
        El cliente puede acceder a la habitacion con el servicio seleccionado
        """
<<<<<<< HEAD
        print(t)
        self.declare(Recomendacion(tipo=t, numero=n))
=======
        print("recomendación 9 "+ t)
        self.declare(Recomendacion(tipo=t, numero=n))
>>>>>>> 108e2c06b82360949c279f86bf9598d712541c5d
