# ABSTRACCION

# En pocas palabras sería una interfaz simple, que tape a la interfa compleja

class Auto:
    def __init__(self):
        self._estado = "Apagado";

    def encender(self):
        self._estado = "Encendido";
        print("El auto está encendido");

    def conducir(self):
        if self._estado == "Apagado":
            self.encender();
        print("Conduciendo el auto");

# Hasta aquí, es todo lo que puede ameritar complejidad dentro de lo que es el código

mi_auto = Auto();
mi_auto.conducir(); #Y esto es lo que ya vendría siendo un ejemplo de la abstracción, es decir, el usuario simplemente utilizando el método conducir, su auto enciende y empieza a conducir, no tiene que ver por todo lo que se tiene que pasar para que el auto consiga conducir