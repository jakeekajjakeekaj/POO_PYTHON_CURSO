# Se trabajará con la API de CHAT GPT

from openai import OpenAI;   #Para usarlo, necesitamos ir a la CMD y escribir py -m pip install openai

client = OpenAI(
    api_key = "api-key"
);

system_rol = "Haz de cuenta que eres un analizador de sentimientos. Yo te paso sentimientos y tú analizas el sentimiento de los mensajes y me das una respuesta con al menos 1 caracter y como máximo 4 caracteres. SOLO RESPUESTAS CON ints o floats, en donde puedes contestar en un rango de -1 que es Negatividad máxima, hasta 1 que es Positividad máxima. De igual manera puedes contestar con 0 si es neutral";   #Aquí se configura a la IA

mensajes = [{"role" : "system", "content" : system_rol}];    #Para el role se tiene system, user o assistant, si el role es user: Es lo que el usuario le está dando; Assistant: La respuesta que nos da la IA; System: Cómo se debe comportar la inteligencia artificial, cuál es el rol que debe tener; para este caso se coloca system porque nosotros definimos el comportamiento desde system_rol; el contenido es el system_rol

class AnalizadorDeSentimientos:
    def analizar_sentimiento(self, polaridad):
        if polaridad >= -1 and polaridad <= -0.6:
            return "\x1b[1;31m" + "Muy Negativo" + "\x1b[0;37m";    #31m ROJO, Esto es para colocerar la consola y así que nos salga el mensaje que queremos, para este caso de ROJO, pero es importante al final volver a cambiar el color al 37m para que vuelva a ser blanca y no se sigua coloreando la consola
        elif polaridad > -0.6 and polaridad <= -0.3:
            return "\x1b[1;31m" + "Negativo" + "\x1b[0;37m";
        elif polaridad > -0.3 and polaridad < -0.1:
            return "\x1b[1;31m" + "Medio Negativo" + "\x1b[0;37m";
        elif polaridad >= -0.1 and polaridad <= 0.1:
            return "\x1b[1;33m" + "Neutral" + "\x1b[0;37m"; #33m amarillo
        elif polaridad > 0.1 and polaridad < 0.3:
            return "\x1b[1;32m" + "Medio Positivo" + "\x1b[0;37m";  #32m VERDE
        elif polaridad >= 0.3 and polaridad < 0.6:
            return "\x1b[1;32m" + "Positivo" + "\x1b[0;37m";
        elif polaridad >= 0.6 and polaridad <= 1:
            return "\x1b[1;32m" + "Muy Positivo" + "\x1b[0;37m";
        else:
            return "NO SE PUDO CALCULAR";

# print("\x1b[1;31m" + "Hola");   #Si se imprime esto en pantalla, se puede ver un ejemplo de cómo se cambia el color
# \x1b[1;32m    VERDE
# \x1b[1;33m    AMARILLO

analizador = AnalizadorDeSentimientos();
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
    mensajes.append({"role" : "assistant", "content" : completion.choices[0].message.content.strip()});   #De esta manera se agrega la respuesta que dió CHAT GPT

    sentimiento = analizador.analizar_sentimiento(float(respuesta));
    print(sentimiento);