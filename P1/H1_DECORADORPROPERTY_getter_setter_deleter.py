#DECORADOR PROPERTY

# class Persona:
#     def __init__(self, nombre, edad):
#         self._nombre = nombre;
#         self._edad = edad;

#     def get_nombre(self):
#         return self._nombre;

#     def set_nombre(self, new_nombre):
#         self._nombre = new_nombre;

# jake = Persona("Jake", 24);

# nombre = jake.get_nombre();
# print(nombre);

#Hasta aquí era la manera en que se trabajaba con los getters y setters, y también está bien; pero existe otra manera de poder trabajar con los mismos:

class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre;
        self._edad = edad;

    @property   #Esto es un decorador, que tiene una palabra reservada para así determinar a los setters y getters, de esta manera al mandar a llamar a la función ya no es necesario declararla como función, sino como propiedad
    def get_nombre(self):
        return self._nombre;

    @get_nombre.setter  #De esta manera, nosotros podemos aplicar los setters, indicamos que de la propiedad get_nombre, se aplicará un .setter y de esta manera ya podemos settear los resultados
    def get_nombre(self, new_nombre):
        self._nombre = new_nombre;

    @get_nombre.deleter #De esta manera nosotros podemos aplicar el deleter
    def get_nombre(self):
        del self._nombre;   #La palabra del, indica delete

jake = Persona("Jake", 24);

nombre1 = jake.get_nombre;   #Como se muestra aquí, ya no es necesario mandar a llamar a la función como una fucnión, si no ya se puede mandar a llamar como propiedad

print(nombre1);

jake.get_nombre = "Pepe";   #De esta manera mandamos a llamar a nuestro setter, a través de la función dentro del setter y como con el getter, sin hacerlo ver como una función

nombre1 = jake.get_nombre;

print(nombre1);

del jake.get_nombre;    #De esta manera eliminamos a get_nombre, es decir que aunque la mandemos a llamar, nos mandará error ya que se verá como que no existe

# nombre1 = jake.get_nombre;

# print(nombre1);