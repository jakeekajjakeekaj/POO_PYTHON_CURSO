#LSP (LISKOV'S SUBSTITUTION PRINCIPLE) (PRINCIPIO DE SUSTITUCIÓN DE LISKOV)

# Este nombre de debe a la científica Bárbara Liskov, este principio indica que LAS CLASES DERIVDADAS, TIENEN QUE SER SUSTITUIDAS POR LAS CLASES BASE. ES DECIR:
# SI LA CLASE B, ES UNA SUB CLASE DE A, LA CLASE A DEBERÍA PODER UTILIZARSE EN TODOS LOS LUGARES DONDE LA SUBCLASE B SE UTILIZA

# class Ave:
#     def volar(self):
#         return "Estoy volando";

# class Pinguino(Ave):
#     def volar(self):
#         return "No puedo volar";

# def hacer_volar(ave = Ave):
#     return ave.volar();

#Hasta aquí, se puede ver como algo sencillo, sin embargo el principio de Liskov indica que la clase Padre pueda hacer todo lo que la clase hija, pero esto no es posible, debio a que en la clase padre, todas las aves pueden volar, sin embargo al mandar a llamar a la clase Pinguino, que está heredada, pues al final el pinguino no puede volar, por lo que para resolver este problema lo que se debe de hacer es:

class Ave:
    pass;

class AveVoladora(Ave):
    def volar(self):
        return "Estoy volando";

class AveNoVoladora(Ave):
    pass;

# ESTO ES UN EJEMPLO BIEN APLICADO DEL PRINCIPIO DE LISKOV, AQUI LO QUE SE EST´PA VIENDO ES QUE LA CLASE PADRE TIENE ATRIBUTOS Y TODO, Y LO QUE SE DEBE RESPETAR ES QUE TODO LO DE LA CLASE PADRE, SEA BIEN HEREDADO A LAS CLASES HIJAS, PARA ESTE CASO SE PUEDE OBSERVAR QUE NO TODAS LAS AVES VUELAN, ENTONCES SE CREA UNA SUBCATEGORÍA DE AVEVOLADORA Y AVENOVOLADORA, PARA DE ESTA MANERA AHORA SI TODO LO DE LA CLASE PADRE ES UTILIZADO EN LAS CLASES HIJAS, Y SE MANTIENE BIEN SEPARADO TODO