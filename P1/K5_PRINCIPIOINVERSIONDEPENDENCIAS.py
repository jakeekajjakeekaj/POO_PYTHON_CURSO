#DIP (PRINCIPIO DE INVERSIÓN DE DEPENDENCIAS) (DEPENDENCY INVERSION PRINCIPLE)

#ESTABLECE 2 COSAS:
# - LOS MÓDULOS DE ALTO NIVEL, NO TIENEN QUE DEPENDER DE LOS DE BAJO NIVEL, SINO QUE LOS 2 DEBEN DEPENDER DE LAS ABSTRACCIONES

# - LAS ABSTRACCIONES NO DEBEN DEPENDER DE LOS DETALLES, SINO QUE LOS DETALLES DEBEN DEPENDER DE LAS ABSTRACCIONES.
# Osea que no debemos depender de implementaciones específicas, osea no depender de una función, sino que DEBEMOS DEPENDER DE INTERFACES MÁS COMLEJAS, DE COSAS MÁS GRANDES; osea no hay que hacer que una calculadora dependa de una función que después se pueda romper, sino que debería depender de una clase mucho más grande que contenga incluso toda la calculadora por ejemplo; así las FUNCIONES DE ALTO NIVEL, SE MANTENGAN INDEPENDIENTES DE LAS DE BAJO NIVEL.

# class Diccionario:
#     def verificar_palabra(self, palabra):
#         #Lógica para verificar palabras
#         pass;

# class Corrector:
#     def __init__(self):
#         self.diccionario = Diccionario();

#     def corregir_texto(self, texto):
#         #Usamos el diccionario para corregir el texto
#         pass;

# Hasta aquí si lo hacemos de esta manera, nosotros estamos realizando un error, esto debido a que diccionario de la clase Corrector está fuertmenete ligado a la clase Diccionario, y aquí está el error, porque no debemos depender en una clase como la que se tiene, de una clase más pequeña, ya que la clase más importante es corrector, no es la clase de diccionario; tomando como ejemplo el ejercicio pasado, es como decir que el auto depende del tanque, cuando el tanque es una pequeña interfaz, lo ideal más bien es que el tanque dependa del auto, ahí ya sería lo correcto; pues para este caso es lo mismo, el diccionario sería algo pequeño, mientras que el autocorrector sería algo bastante más grande, entonces hace sentido que más bien el diccionario dependa del corrector

#Ahora ya sería la manera correcta de hacer las cosas:
from abc import ABC, abstractmethod;

class VerificadorOrtografico(ABC):
    @abstractmethod
    def verificar_palabra(self, palabra):
        pass;

class Diccionario(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        #Lógica para vrificar palabras si está en el diccionario
        pass;

class CorrectorOrtografico:
    def __init__(self, verificador):
        self.verificador = verificador;

    def corregir_texto(self, texto):
        #Usamos el verificador para corregir texto
        pass;

# corrector = CorrectorOrtografico(ServicioWeb());  #Este sería el ejemplo de la ventaja de implementarlo de esta manera, ya que como se puede observar, si nosotros quisiéramos ahora hacerlo desde el ServicioWeb, pues si se podría, no se tendrpia que modificar toda la clase Diccionario para poder realizarlo; esta es la gran ventaja de poder hacerlo de esta manera

# HASTA AQUÍ FINALIZAN LOS PRINCIPIOS SOLID
#S: SRP, PRINCIPIO DE RESPONSABILIDAD ÚNICA
#O: OCP, PRINCIPIO DE ABIERTO/CERRADO
#L: LSP, PRINCIPIO DE SUSTITUCIÓN DE LISKOV
#I: ISP, PRINCIPIO DE SEGREGACIÓN DE INTERFAZ
#D: DIP, PRINCIPIO DE INVERSIÓN DE DEPENDENCIAS