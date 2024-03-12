#SETTERS Y GETTERS

# Haciendo el uso de estos, nosotros podemos acceder a lo que son los métodos o atributos muy muy privados

class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre;
        self.__edad = edad;

    def get_nombre(self):   #Esto se realiza para obtener los datos protectes, la variable puede llevar el nombre que sea, pero esto se conoce como getter
        return self._nombre;

    def get__edad(self):    #Lo mismo que el caso de arriba, pero esta vez para los atributos private
        return self.__edad;

    def set_nombre(self):   #Lo mismo que el caso de arriba, solo que en vez de ser llamados gettes, se llaman setters, a su vez modifica a los valores 'protected'
        self._nombre = "Jake 2";

    def set__edad(self):    #Lo mismo que el de arriba, pero modificando a los atributos private
        self.__edad = 2;

jake = Persona("Jake", 24);
# print(jake._nombre);  #Aunque esta forma funcione, no se debe realizar de esta manera, el guión bajo nos indica que a pesar de que se puede acceder de esta manera, no se debería acceder así, se tiene que utilizar otro método para poder acceder a la misma
print(jake.get_nombre());   #Esta sería la manera correcta, como se puede ver, ya no se accede directamente a través del atributo, se obtiene a través de un método que puede llevar cualquier nombre, pero lo denominamos como get indicando que se obtendrá la información
print(jake.get__edad());    #Como se puede observar, también podemos acceder a los atributos muy muy privados a través de este mismo método

jake.set_nombre();  #De esta manera podemos modificar a un atributo 'protected'
jake.set__edad();   #De esta manera podemos modificar a un atributo 'private'
print(jake.get_nombre());
print(jake.get__edad());