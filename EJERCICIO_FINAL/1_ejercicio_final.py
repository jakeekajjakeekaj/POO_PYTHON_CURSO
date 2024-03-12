from textblob import TextBlob;  #Para usar esta librería se debe instalar, esto sería llendo a la cmd, y escribir pip install textblob; si no se reconoce escribir py -m pip install textblob

class AnalizadorDeSentimientos:
    def analizar_sentimiento(self, texto):
        analisis = TextBlob(texto);
        polaridad = analisis.sentiment.polarity;    #Esto lo que hace es acceder a una IA que procesa el lenguaje natural
        if polaridad > 0: #el .sentimient.polarity son propiedades de TextBlob, esto lo que dará será la polaridad, sería un resultado entre -1 y 1
            return "Positivo";
        elif polaridad == 0:
            return "Neutral";
        else:
            return "Negativo";

analizador = AnalizadorDeSentimientos();
resultado = analizador.analizar_sentimiento("Hello, im meh");   #Solo funciona en inglés
print(resultado);

# Hasta aquí es una manera de trabajar; peeeeeeero podemos hacerlo mejor, ya que la librería con esta IA no es tan precisa, en su lugar podríamos utilizar mejor a la API de chatGPT