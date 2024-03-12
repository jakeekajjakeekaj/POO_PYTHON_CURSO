#OCP (OPEN/CLOSED PRINCIPLE) (PRINCIPIO DE ABIERTO CERRADO)

#El principio de abierto cerrado nos dice que los módulos, las clases, las funciones (todas la entidades de software), deben estar abiertas para la extensión, pero cerradas para la modificación; es decir que debemos de poder agregar nuevas funcionalidades sin cambiar el código fuente

class Notificador:
    def __init__(self, usuario, mensaje):
        self.usuario = usuario;
        self.mensaje = mensaje;

    def notificar(self):
        raise NotImplementedError;  #Esto le idncia al desarrollador que se tienen que crear las notificaciones diferentes, el NotImplementedError es como definir una excepción

class NotificadorEmail(Notificador):
    def notificar(self):
        print(f"Enviando mensaje a {self.usuario.email}");

class NotificadorSms(Notificador):
    def notificar(self):
        print(f"Enviando SMS a {self.usuario.sms}");

# HASTA AQUÍ SE PUEDE OBSERVAR QUE SE HA DIVIDIDO EN PARTES MÁS PEQUEÑAS, LA VENTAJA DE REALIZAR ESTO ES QUE SI POR EJEMPLO SI SE QUIERE ESCALAR AL CÓDIGO, LO QUE DEBE DE HACER ES:

class NotificadorWhatsApp(Notificador): #Así de sencillo ya se pudo agregar un notificador para lo que sería WhatsApp, y así para todos los futuros notificadores
    def notificar(self):
        print(f"Enviando WhatsApp a {self.usuario.whatsapp}");