#Crear clase Estudiante, con atributos Nombre, Edad y Grado; aparte de que tenga los métodos estudiar(), que escriba "El estudiante (nombre), está estudiando"

class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre;
        self.edad = edad;
        self.grado = grado;

    def estudiar(self):
        print(f"El estudiante {nombre}, está estudiando");

nombre = input("Esribe el nombre: ");
edad = input("Escribe la edad: ");
grado = input("Escribe el grado: ");

estudiante1 = Estudiante(nombre, edad, grado);

while True:
    estudiar = input();
    if estudiar.lower() == "estudiar":  #Con .lower() transformamos todo a minúsculas
        estudiante1.estudiar();