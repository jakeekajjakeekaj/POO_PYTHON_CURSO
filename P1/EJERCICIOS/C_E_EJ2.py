class Animal:
    def comer(self):
        print("El animal está comiendo");

class Ave(Animal):
    def volar(self):
        print("El ave está volando");

class Mamifero(Animal):
    def beber(self):
        print("El mamífero está bebiendo");

class Murcielago(Mamifero, Ave):
    pass;

murcielago = Murcielago();  #De esta manera nosotros podemos ver primero a un objeto creándose con todas las clases heredadas
ave = Ave();    #De esta manera nosotros podemos ver a un objeto creado a partir de ciertas clases, pudiendo ver así la ventaja de trabajar con clases heredadas, en donde podemos mencionar características de un murciélago, y las características de un ave por ejemplo; y ya solo definimos con pocas lineas de código a qué clases corresponde cada cosa

murcielago.comer();
murcielago.volar();
murcielago.beber();

ave.comer();
ave.volar();

print(Murcielago.mro());