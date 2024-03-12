#CLASES ABSTRACTAS

# Las clases abstractas, es como una especie de plantilla para crear otras clases, no es como cuando creamos una clase y la heredamos, ya que con las clases abstractas no podemos crear objetos, pero si podemos usarlas para la creación de otras clases

from abc import ABC, abstractclassmethod;    #abc es un módulo de python, ABC es una clase del módulo y el abstractclassmethod es un decorado

class Persona(ABC): #Para que al clase abstracta funcione, se debe contener como parámetro el módulo ABC así como se muestra en este caso
    @abstractclassmethod    #Este es el decorador que se encargaría de comentar que la función de abajo sería de una clase abstracta
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre;
        self.edad = edad;
        self.sexo = sexo;
        self.actividad = actividad;

    @abstractclassmethod
    def hacer_actividad(self):
        pass;

    def presentarse(self):
        print(f"Hola, me llamo: {self.nombre} y tengo {self.edad} años");

# jake = Persona("Jake", 24, "Masculino", "Programador");   #De esta manera ya no se puede mandar a llamar, debido a que al ser una clase abstracta, ya no es posible de la manera convencional

#Procederemos a crear 2 clases más:

class Estudiante(Persona):  #De esta manera creamos una clase heredando a la clase Persona
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad) #Recordemos que con super() indicamos que accedemos a la clase Padre, y a su vez tenemos que agregar los parámetros de la clase Padre

    def hacer_actividad(self):  #Tenemos el mismo nombre de la clase abstracta
        print(f"Estoy estudiando: {self.actividad}");   #Para los estudiantes la actividad es diferente


class Trabajador(Persona):  #Se crea otra clase, heredando de igual manera a la clase Persona
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad);    #El mismo caso que con la clase de arriba

    def hacer_actividad(self):  #Se crea una función con el mismo nombre de la clase Padre abstracta
        print(f"Estoy trabajando como: {self.actividad}");  #La actividad que realiza un trabajador es diferente


jake = Estudiante("Jake", 24, "Masculino", "Programación"); #Llenamos los datos para lo que sería un estudiante
ekaj = Trabajador("Ekaj", 25, "Masculino", "Desarrollador");    #Llenamos los datos para lo que sería un trabajador

jake.hacer_actividad(); # El estudiante realiza una diferente acción a pesar de tener el mismo nombre de función
ekaj.hacer_actividad(); # El trabajador realiza una diferente acción a pesar de tener el mismo nombre de función

# Hasta este punto, se puede observar que esta misma situación se puede resolver con lo que es una simple herencia de clases, no es necesario una abstracción de clases; sin embargo realizar abstracciones tienen sus ventajas, y aunque generalmente se trabaja más con simple herencia, las abstracción tiene como ventaja:
# - Documentado: Es como si se pusieran reglas, al momento de crear una clase abstracta, le estamos obligando a las demás clases que hereden a nuestra clase, que si o si tengan los métodos abstractos implementados.
# - Fomenta el polimorfismo