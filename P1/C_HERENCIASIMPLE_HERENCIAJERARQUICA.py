#Recordatorio: La herencia básicamente es heredar cosas de la clase padre a una clase hija, es decir si nosotros tenemos una clase persona, pero a su vez tenemos otra clase estudiante; pues al final un estudiante es una persona, entonces en vez de recrear todo, podemos heredar todo lo de la clase persona a la clase estudiante ya que también es una prsona, pero a su vez poder agregar otras características que solo un estudiante tendría.

# - HERENCIA SIMPLE:
#Básicamente consite en que una clase Padre, hereda a UNA SOLA CLASE HIJA, si nosotros quisiéramos heredar a más clases, ya sería llamada HERENCIA JERÁRQUICA, que anivel código de igual manera vendría siendo lo mismo.
#A su vez, existe otro tipo de herencia llamada MÚLTIPLE, que básicamente es cuando 2 CLASES heredan a una sola

class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre;
        self.edad = edad;
        self.nacionalidad = nacionalidad;

class Empleado(Persona):    #De esta manera realizamos un heredado
    # pass;   #pass sirve para saltar lo que sea, es decir que no haya ningún problema, que si se mande a llamar, pero que no realice ninguna acción
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):   #Es importante colocar dentro de nuestro constructor hijo, a todos los parámetros, tanto de la clase Padre, como de la clase hijo
        super().__init__(nombre, edad, nacionalidad);   #De esta manera es como indicar que se va a heredar al constructor, es decir aquí declaramos al constructor de la clase Padre
        self.trabajo = trabajo; #Los parámetros que irán dentro de la clase hijo, se declaran de esta manera, así como lo "normal"
        self.salario = salario;

    def ocupacion(self): #De esta manera indicamos que se trabajará con la información de otra clase
        print(f"{self.nombre} es un empleado");  #De esta manera mandamos a llamar a la información de otra clase

    def oracion(self):
        print(f"""
            {self.nombre} tiene {self.edad} años, es {self.nacionalidad}; actualmente se encuentra trabajando de {self.trabajo} y gana {self.salario};
        """)

persona1 = Empleado("Roberto", 20, "Mexicano", "Programador", 12000); #De esta manera mandamos a asignar a los datos heredados, pero se guardan en la clase padre
persona1.ocupacion();   #De esta manera se manda a llamar a la función declarada en la clase hija usando los datos almacenados de la clase padre
persona1.oracion();