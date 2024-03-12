#MRO (METHOD RESOLUTION ORDER)

#En pocas palabras define a cuál método se le dará prioridad en caso de que tengamos el mismo nombre de método para varias clases

#Aquí se muestra como ejemplo cuando usamos en un método el super() y el self; para este caso al declarar el self, se ejecutará el método de la clase presente en caso de tener el mismo nombre para 2 métodos; pero si nosotros usamos el super(), nos daría prioridad al método de la clase Padre.

#Para el caso de no usar super o self y esas cosas; es decir suponiendo que nombramos a métodos con nombres iguales de diferentes clases, se seguirá una jerarquía, es decir que primro ejecutará el método más próxima a nuestra clase, pero a su vez tenemos que tener presente que estará buscando como si fuera un camino, es decir supongamos que tenemos nuestra clase A, aquí se empezará a buscar al método, pero de no encontrarse pasará a la siguiente clase, pero si nosotros tenemos en el mismo nivel B y C; primero buscaría en B al método y en caso de no encontrarse, uno podría pensar que buscaría en C, sin embargo si B tiene otras clases, entonces primero se seguiría por el camino de B, es decir iría buscando en B1, B2, B3 y así; ya hasta que no encuentre ningún método por el camino de B, ahora sí comenzaría a buscar en C y así sucesivamente.

# print(A.mro());   #Tomando el ejemplo anterior, de esta manera nosotros podríamos ver un ejemplo de la manera en que se seguiría la jerarquía