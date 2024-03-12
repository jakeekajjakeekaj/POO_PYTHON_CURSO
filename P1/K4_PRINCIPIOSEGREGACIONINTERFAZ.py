# ISP (INTERFACE SEGREGATION PRINCIPLE) (PRINCIPIO DE SEGREGACIÓN SE LA INTERFAZ)

#En pythons las interfaces no se usan de la misma manera, para python se va más hacia lo que es typing

from abc import ABC, abstractmethod;

# class Trabajador(ABC):
#     @abstractmethod
#     def comer(self):
#         pass;

#     @abstractmethod
#     def trabajar(self):
#         pass;

#     @abstractmethod
#     def dormir(self):
#         pass;

# class Humano(Trabajador):
#     def comer(self):
#         print("El humano está comiendo");

#     def trabajar(self):
#         print("El humano está trabajando");

#     def dormir(self):
#         print("El humano está durmiendo");

# class Robot(Trabajador):    #Si lo manejamos así, nos saldrá el error de que se deben de agregar también la función de comer y dormir debido a que son fucniones abstractas; UNA MANERA DE SOLUCIONARLO ES AGREGANDO LAS FUNCIONES Y YA, PERO UN ROBOT NO COME Y NO DUERME, POR LO QUE AQUÍ ESTARÍAMOS VIOLANDO EL PRINCIPIO DE SEGREGACIÓN DE LA INTERFAZ. POR LO QUE SE DEBE DE HACER ES SEGMENTAR EN PARTES MÁS CHICAS, ES DECIR:
#     def trabajar(self):
#         print("El humano está trabajando");

# robot = Robot() #Si lo imprimos de esta manera, nos sale el error de que se deben agregar los métodos abstractos para poder trabajar

#EMPEZANDO DESDE AQUÍ:
#Como se puede ver abajo, lo primero que se hará es crear como métodos abstractos a cada uno, pero se realizará por separado en vez de un código unificado, esto lo que podrá realizar es que al momento de tener un humano que si trabaje, come y duerma, no hay ningún problema, pero que si se tenga un robot que solo trabaje, tampoco haya ningún problema, esto porque al momento de hacer a los métodos abstractos, si se tiene a un robot que no coma ni duerma, nos dará error, en cabmio de esta manera ahora si podemos definir las caracteristicas que deben de llevar cada cosa, manejando así una correcta interfaz

class Trabajador(ABC):
    @abstractmethod
    def trabajar(self): #Para este caso, es un método abstracto, en donde se declara a la función y de esta manera se indica que aunque parezca que no se hace nada, en donde se realizarán las cosas en las clases hereadas
        pass;

class Comedor(ABC):
    @abstractmethod
    def comer(self):
        pass;

class Durmiente(ABC):
    @abstractmethod
    def dormir(self):
        pass;

class Humano(Trabajador, Comedor, Durmiente):   # AQUÍ COMO SE PUEDE OBSERVAR, TENEMOS A ESTAR 3 CLASES HEREDADAS, INDICANDO QUE EL HUMANO SI O SI TENDRÁ LA CLASE TRABAJADOR, COMEDOR Y DURMIENTE
    def trabajar(self): #Al nombrar al mpetodo aquí, con este nombre se indica que es el método abstracto, es decir que si o si tiene que estar presente y al hacerlo desde esta zona se indica que el comportamiento es diferente
        print("El humano está trabajando");
    
    def comer(self):
        print("El humano está comiendo");

    def dormir(self):
        print("El humano está durmiendo");

class Robot(Trabajador):
    def trabajar(self): #Ahora si no hay ningún error, el robot ya solo trabaja, no come y duerme; y aparte en la impresión, ya se cambia El humano, por El robot; provocando así una acción diferente
        print("El robot está trabajando");

robot = Robot();