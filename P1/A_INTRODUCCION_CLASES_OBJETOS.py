#Introduccion POO

#AL DEFINIR CLASES, SE TRABAJA CON PASCAL CASE, ESTO QUIERE DECIR QUE TODAS LAS PRIMERAS LETRAS LLEVAN MAYÚSCULAS, ES DECIR SE PARECE AL CAMEL CASE, SOLO QUE AL NOMBRA LA CLASE, LA PRIMER LETRA TAMBIPEN LLEVA MAYÚSCULA

# class Celular():    #Creación de una clase
#     marca = "Samsgung";
#     modelo = "S23";
#     camara = "48MP";

# celular1 = Celular();
# print(celular1);    #De esta manera se imprime que es un objeto guardado en cierta dirección de memoria
# print(celular1.marca);  #De esta manera ya accedemos a la información almacenada

# - Creacion de clases con atributos

class Celular:
    def __init__(self, marca, modelo, camara):  #init indica lo que es un constructor, a su vez al declarar self, se indica que se hará a sí mismo, es decir que como colocar Celular
        self.marca = marca; #Nuevamente aquí al indicar el self, es como decir Celular.marca
        self.modelo = modelo;
        self.camara = camara;

celular1 = Celular("Samsung", "S23", "48MP");
celular2 = Celular("Iphone", "15", "12MP");
print(celular1.marca);
print(celular2.marca);