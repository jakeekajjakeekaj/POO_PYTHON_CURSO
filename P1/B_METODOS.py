#Recordatorio: Son las funciones dentro de las clases xd

class Celular():
    def __init__(self, marca, modelo, camara):  #Al final esto es un método, es un método especial, pero es un método
        self.marca = marca;
        self.modelo = modelo;
        self.camara = camara;

    def llamar(self):   #Es importante mencionar que se debe colocar el parámetro self para que los métodos puedan funcionar
        print("Estás realizando un llamado");

celular1 = Celular("Samsung", "S23", "48MP");
print(celular1.marca);
celular1.llamar();  #De esta manera se manda a llamar a algún método