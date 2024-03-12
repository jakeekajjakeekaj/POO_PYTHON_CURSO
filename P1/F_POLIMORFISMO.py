#Polimorfismo

#Nosotros al darle un objeto a un método, su comportamiento debe ser diferente dependiendo de sus diferentes propiedades; es decir si nosotros enviamos el mensaje de caminar, se debe de caminar diferente en caso de que sea un humano, un perro, un cocodrilo, etc.

class Gato():
    def sonido(self):
        return "Miau";

class Perro():
    def sonido(self):
        return "Guau";

gato = Gato();
perro = Perro();

print(gato.sonido());   #De esta manera aplicamos polimorfismo, porque con el mismo nombre de la función, se reproduce una acción distinta, en este caso se reproduce "Miau"
print(perro.sonido());  #El mismo ejemplo de polimorfismo, ya que con el mismo nombre de la función se preoduce otra acción, en este caso "Guau"