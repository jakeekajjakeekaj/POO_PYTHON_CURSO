#HERENCIA MULTIPLE
#Básicamente es cuando 2 o más clases, heredan a una clase

class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre;
        self.edad = edad;
        self.nacionalidad = nacionalidad;

    def hablar(self):
        print("Hola, estoy hablando");

class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad;
    
    def mostrar_habilidad(self):
        print(f"Mi habilidad es: {self.habilidad}");

class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        Persona.__init__(self, nombre, edad, nacionalidad);   #Antes, se usaba el Super().__init__(), pero para este caso que no se sabe extactamente de dónde se va a heredar, tenemos que nombrar directamente a la clase en vez de escribir Super()
        Artista.__init__(self, habilidad);
        self.salario = salario;
        self.empresa = empresa;

    def info(self):
        print(f"Mi nombre es {self.nombre}, tengo {self.edad} años, soy de nacionalidad {self.nacionalidad} y soy {self.habilidad}, mi salario es de {self.salario} y trabajo en {self.empresa}");

    def habilidades(self):
        super().mostrar_habilidad();    #Para este caso, podemos escribir self. en vez del super(), sin embargo es considerado buena práctica que si el método forma parte de alguna clase Padre, se coloque el super() indicando que es un método de otra clase; y se coloque el self. para indicar que es un método de la propia clase, ESTO PARA SABER CUANDO SE USA UN MÉTODO HEREDADO Y UN MÉTODO PROPIO

empleado_artista = EmpleadoArtista("Jake", 24, "Mexicano", "actor", 12000, "Hollywood");
empleado_artista.info();
empleado_artista.habilidades();

herencia = issubclass(EmpleadoArtista, Artista); #Para este caso se utiliza la función issubclass oara determinar si es una clase hija, al colocar el primer parámetro y el segundo parámetro, estamos preguntando si EmpleadoArtista es una clase hija de la clase Artisa; LA MANRA DE RESPONDER ES TRUE O FALSE
print(herencia); #True

herencia = issubclass(Artista, Persona);    #Para este caso es False, ya que ambas clases son clases padre, no se están heredando entre ellas, solo están heredando su información hacia la clase ArtistaEmpleado, pero no entre ellas
print(herencia);    #False

instancia = isinstance(empleado_artista, EmpleadoArtista);  #isinstance se utiliza para conocer si cierto objeto es una instancia de cierta clase, es decir aquí se pregunta si empleado_artista es un objeto de la clase EmpleadoArtista, donde la respuesta es True
print(instancia);   #True

instancia = isinstance(empleado_artista, Artista);  #Si colocamos de la clase EmpleadoArtista, Artisa o Persona, en todos los casos nos devolverá True, esto es porque al final el objeto es una instancia de todas, es decir debido al tema del heredado, este objeto usa todas estas clases por lo que el valor es True
print(instancia);   #True