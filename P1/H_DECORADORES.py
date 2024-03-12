#DECORADORES

#El decorador toma una cunción de entrada, usa otra función o algo diferente a la propia entrada de la función, entrega un resultado, pero al final de todo no modifica a la función original

def decorador(funcion): #Se indica que se recibirá a un valor, en este caso una función llamada saludo
    def funcion_modificada():
        print("Antes de llamar a la funcion");
        funcion();  #Esto estaría provocando que dentro de nuestra función, se ejecutaría otra función
        print("Despues de llamar a la funcion");
    return funcion_modificada;

# def saludo():
#     print("Hola a todos");

# saludo_modificado = decorador(saludo)   #Aquí asignamos el valor de la función decorador a una variable, a su vez mandamos a la función saludo
# saludo_modificado();    #Se obtiene el resultado esperado, ya que ha agregado una funcionalidad antes o después

# Hasta aquí era la manera en que se trabajaba con los decoradores antes; sin embargo actualmente se trabaja así:

@decorador  #Esto indica lo que es el decorador, básicamente en vez de asignar la variable y todo, directamente desde aquí se declara que irá indexada con la función de abajo; de igual manera se tiene que indicar que dentro irá una función
def saludo():
    print("Hola a todos");

saludo();

# En pocas palabras, EL DECORADOR AGARRA OTRA FUNCIÓN Y LA ANEXA, COMO TAL NO ES QUE MODIFIQUE CIERTA FUNCIÓN O ALGO POR EL ESTILO