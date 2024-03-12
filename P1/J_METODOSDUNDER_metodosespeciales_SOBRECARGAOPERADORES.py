# Métodos Dunder (MÉTODOS ESPECIALES)

# Los métodos especiales, son métodos reservados especiales, estos suelen empezar con guines bajos y terminar con guines bajos, por ejemplo __init__

class Persona:
    def __init__(self, nombre, edad):   #Este es un constructor
        self.nombre = nombre;
        self.edad = edad;
    
    def __str__(self):  #Devuelve una representación del objeto en una cadena de texto, es decir, cuando nosotros imprimimos únicamente al objeto, nos devuelve al objeto, pero en su represntación de memoria y esas cosas; sin embargo gracias a este método especial, le estamos indicando que al momento de llamar al objeto, nos retorne en este caso la cadena de texto de abajo
        return f'Persona(nombre = {self.nombre}, edad = {self.edad})';
    
    def __repr__(self): #Gracias a esto, se puede obetener una representación del objeto
        return f'Persona(nombre = "{self.nombre}", edad = {self.edad})';    #Debido a que será una representación, se debe mantener una estructura, en este caso por ejemplo el {self.nombre}, se debe colocar en comillas para indicar que es un texto

    def __add__(self, otro):
        nuevo_valor = self.edad + otro.edad;
        return Persona(self.nombre + otro.nombre, nuevo_valor);

jake = Persona("Jake", 24);
print(jake);

repre = repr(jake); #De esta manera primero se obtiene una representación del objeto para despues reconstruirlo, gracias a la función repr podemos hacer esto
resultado = eval(repre);    #Ya para este caso almacenamos la representación de nuestro objeto, es necesario utilizar el método reservado eval

print(resultado.edad);   # Gracias a que se obtiene la representación del objeto, podemos obtener nuestros valores llamándolos como si fueran parte de un objeto, es decir aquí al escribir resultado.edad o .nombre, podemos obtener los valores respectivos a cada uno

pedro = Persona("Pedro", 30);   # Se crea al objeto pedro

resultado = jake + pedro;   # Gracias al __add__ al momento en el que se declar la suma de los objetos, ya definimos su comportamiento, que en este caso como en la clase lo indicamos, se realizará una suma de los nombres y los números

print(resultado);   #Una impresión con ayuda del __str__ y __add__ que devuelve la suma concatenada de los nombres y la suma de los números
print(resultado.edad);  #Devuelve únicamente la suma de los números
print(resultado.nombre);    # Devuelve únicamente la suma concatenada de los nombres