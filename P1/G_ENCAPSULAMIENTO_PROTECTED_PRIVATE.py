#ENCAPSULAMIENTO

class MiClase:
    def __init__(self):
        self._atributo_privado = "valor";  #La manera en la que nosotros le indicamos a python que se está creando un atributo privado, es delcarando al principio del nombre un guión bajo, de esta manera es como si estuviéramos utilizando private; sin embargo hay que hacer conciencia respecto a que en PYTHON no funciona tal cual es PRIVATE o el PUBLIC como en otros lenguajes, de hecho como tal todo es público, lo único que se hace con el guión bajo es aumentar la seguridad del mismo. En pocas palabras al usar este, es como indicar que es protegido en otros lenguajes.

        self.__atributo_muy_privado = "valor2"; #De esta manera se crean digamos atributos muy muy privados, aquí ya se pueden observar ciertos cambios ahora sí, ya que fuera del mismo, mandándolo a llamar de la manera convencional con un print, nos daría un error de que el atributo no existe. En pocas palabras es como indicar el PRIVATE en otros lenguajes.

objeto = MiClase();
print(objeto._atributo_privado);    #De esta manera como se puede observar, se tiene acceso al atributo privado, se puede ver que es un atributo privado, pero podemos seguir accediendo al mismo

# print(objeto.__atributo_muy_privado); #Esto tiene que ir comentado, ya que al final ahora si se podría considerar un atributo privado, y no se tiene acceso al mismo, directamente es como si no existiera dicho atributo mas que en la propia clase