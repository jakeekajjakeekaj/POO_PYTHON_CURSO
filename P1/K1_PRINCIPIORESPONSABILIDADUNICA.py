#PRINCIPIO DE RESPONSABILIDAD ÚNICA (SRP) (SINGLE RESPONSABILITY PRINCIPLE)

#Este principio indica que una clase tiene que tener una razón para cambiar, es decir que debemos tener una clase para cada cosa.
#Aplicado como ejemplo, en la vida diaria, a las personas deberiamos asignarlas a ciertos tipos de tareas, es decir si hay alguien que se encarga de marketing, dejemos que esta persona se encargue de marketing, si hay alguien que se encarga para programar, dejemos que se encargue de programar, etc. ; dicho esto, es lo mismo para las clases, que deberían tener funcionalidas únicas.

#Una gran vetnaja de realizarlo de esta manera, es que el código se hace más legible y sostenible.

# Como ejemplo se tiene:

class Auto():
    def __init__(self, tanque): #PARA PODER TRABAJAR CON LO QUE SERÍA EL PRINCIPIO DE RESONSABILIDAD ÚNICA, DEBEMOS AGREGAR EL PARÁMETRO tanque, PARA ASÍ MANEJAR A LA GASOLINA POR APARTE, SI NO SE USARA OTRA CLASE, ESTO NO SERÍA NECESARIO, PERO SE ESTÁ VIENDO UN EJEMPLO PARA APLICAR EL PRINCIPIO DE RESPONSABILIDAD ÚNICA
        self.posicion = 0;
        self.tanque = tanque;

    def mover(self, distancia):
        if self.tanque.obtener_combustible() >= distancia / 2:
            self.posicion += distancia;
            self.tanque.usar_combustible(distancia / 2);
            return f"LLegaste a tu destino de {self.posicion}km con {self.tanque.obtener_combustible()}L de combustible";
        else:
            return f"No hay suficiente combustible";

    def obtener_posicion(self):
        return self.posicion;

    # def agregar_combustible(self, cantidad):    #Dejándolo de esta manera puede parecer buena idea, sin embargo en cuanto se escale el proyecto, esto ya no será del todo óptimo, esto porque al ir teneindo más y más métodos; se puede llegar a ser bastan más complejo el proyecto, tomando esto en cuenta lo que se debería de hacer para continuar el PRINCIPIO DE RESPONSABILIDAD ÚNICA, es dividir esta clase en 2, es decir una que se encargue por ejemplo de lo que es el movimiento del auto, pero otra que se encargue de la carga de gasolina
        # self.combustible += cantidad;

    # def obtener_combustible(self):
        # return self.combustible;

class TanqueDeCombustible:
    def __init__(self):
        self.combustible = 100;

    def agregar_combustible(self, cantidad):
        gas_total = cantidad + self.combustible;
        if gas_total > 100:
            return f"La cantidad a agregar más lo que ya había son de {gas_total}L, mientras que el tanque es de máximo 100L, por lo que no se permite esta operación, intente agregar un máximo de {100 - self.combustible}L para alcanzar los 100L máximos";
        else:
            self.combustible += cantidad;
            return(f"Operación realizada con éxito, el tanque tiene {self.combustible}L");

    def obtener_combustible(self):
        return self.combustible;

    def usar_combustible(self, cantidad):
        self.combustible -= cantidad;

tanque1 = TanqueDeCombustible();
auto1 = Auto(tanque1);

print(auto1.obtener_posicion());
print(auto1.mover(10));
print(auto1.obtener_posicion());
print(auto1.mover(20));
print(auto1.obtener_posicion());
print(auto1.mover(60));
print(auto1.obtener_posicion());
print(auto1.mover(100));
print(auto1.obtener_posicion());
print(auto1.mover(15));
print(tanque1.agregar_combustible(96));
print(tanque1.agregar_combustible(95));
print(auto1.mover(100));
print(auto1.obtener_posicion());