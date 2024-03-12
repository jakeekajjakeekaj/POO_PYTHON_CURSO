# Se trabajará con la API de CHAT GPT

from openai import OpenAI;   #Para usarlo, necesitamos ir a la CMD y escribir py -m pip install openai

client = OpenAI(
    api_key = "api-key"
);

system_rol = "Haz de cuenta que eres un analizador de sentimientos. Yo te paso sentimientos y tú analizas el sentimiento de los mensajes y me das una respuesta con al menos 1 caracter y como máximo 4 caracteres. SOLO RESPUESTAS CON ints o floats, en donde puedes contestar en un rango de -1 que es Negatividad máxima, hasta 1 que es Positividad máxima. De igual manera puedes contestar con 0 si es neutral";   #Aquí se configura a la IA

mensajes = [{"role" : "system", "content" : system_rol}];    #Para el role se tiene system, user o assistant, si el role es user: Es lo que el usuario le está dando; Assistant: La respuesta que nos da la IA; System: Cómo se debe comportar la inteligencia artificial, cuál es el rol que debe tener; para este caso se coloca system porque nosotros definimos el comportamiento desde system_rol; el contenido es el system_rol

class Sentimiento:  #Se crea una clase extra para seguir nuestros principios SOLID
    def __init__(self, nombre, color):
        self.nombre = nombre;
        self.color = color;

    def __str__(self):
        return "\x1b[1;{}m{}\x1b[0;37m".format(self.color, self.nombre);    #De esta manera ya podemos modificar los colores de cada resultado

class AnalizadorDeSentimientos:
    def __init__(self, rangos):
        self.rangos = rangos;

    def analizar_sentimiento(self, polaridad):
        for rango, sentimiento in self.rangos:   #El rango indica el rango que se abarca, para este caso se tiene una tupla, que contiene pares de tuplas, se contará a cada par; 
            if rango[0] < polaridad <= rango[1]:    #Aquí se indica que si la polaridad se encuentra en cierto rango, es decir de un punto a otro punto debido a las tuplas, se retornará el sentimiento
                return sentimiento; #Retorna la tupla del sentimiento junto con el valor numérico del color
        return Sentimiento("Muy Negativo", "31");   #Si al pasar durante todo el arreglo no se encuentra nada, e retornará el sentimiento de "Muy Negativo", con color de 31 (rojo), debido a que sería el rango no especificado, es decir -1 a -0.6

rangos = [
    ((-0.6, -0.3), Sentimiento("Negativo", "31")),
    ((-0.3, -0.1), Sentimiento("Medio Negativo", "31")),
    ((-0.1, 0.1), Sentimiento("neutral", "33")),
    ((0.1, 0.3), Sentimiento("Medio Positivo", "32")),
    ((0.3, 0.5), Sentimiento("Positivo", "32")),
    ((0.5, 1), Sentimiento("Muy Positivo", "32")),
]

# print("\x1b[1;31m" + "Hola");   #Si se imprime esto en pantalla, se puede ver un ejemplo de cómo se cambia el color
# \x1b[1;32m    VERDE
# \x1b[1;33m    AMARILLO

analizador = AnalizadorDeSentimientos(rangos);
# resultado = analizador.analizar_sentimiento(-0.6);  #Se verifica el funcionamiento de la función
# print(resultado);

while True:
    user_prompt = input("\x1b[1;33m" + "\nDí algo: " + "\x1b[0;37m");
    mensajes.append({"role" : "user", "content" : user_prompt});    #De esta manera cada que el usuario escriba algo, se indica que el rol es del usuario, y a su vez le estamos indicando que el contenido es lo almacenado en el user_propmt; pero no solo eso, sino que estamos indicando que se va a almacenar en nuestra lista de mensajes previamente creada
    completion = client.chat.completions.create(  #Con el ChatCompletion se indica que el texto se va a completar, ya que visto desde cierto punto de vista, lo que para nosotros sería una respuesta por parte de CHAT GPT, para CHAT GPT es simplemente acompletar el texto
        model = "gpt-3.5-turbo",
        messages = mensajes,
        max_tokens = 8
    )

    respuesta = completion.choices[0].message.content.strip();
    mensajes.append({"role" : "assistant", "content" : respuesta});   #De esta manera se agrega la respuesta que dió CHAT GPT

    sentimiento = analizador.analizar_sentimiento(float(respuesta));
    print(sentimiento);