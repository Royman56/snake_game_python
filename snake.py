#se llaman las librerias especificas o general:
from turtle import Turtle, Screen, forward #las clases empiezan en mayusculas, turtle libreria para crear el cuerpo y scrren para el escenario.
import time

#Creacion del tablero de el juego.
screen = Screen() #los parentesis indican que se creara un objeto, aca le asignamos la clase Screen que se importa arriba.
screen.setup(width=600, height=600) #indicamos las medidas del escenario
screen.bgcolor("black") #el color que llevara el escenario
screen.title("Programate snake") #titulo arriba del juego

screen.tracer(0) #esto pausa la animacion automatica

#construir cuerpo serpiente optimizado
#listas, tuplas, diccionario
starting_position = [(0, 0), (-20, 0), (-40, 0)] #esta variable se convierte en lista y lleva las coordenadas(posiciones del plano)

#almaceno los segmentos

segments = [] #creamos una variable global para usar cada posicion y poder moverlos ya que quedan en el ciclo atrapados

for position in starting_position:   #los bloques de codigo en python no son con llaves sino con 2 puntos, position es la variable i en ejemplos de for
    snake_segment = Turtle("square") #identacion de 4 espacios CUIDADO con esto en python
    snake_segment.color("white")
    snake_segment.penup() #deja de dibujar y quita la linea blanca
    snake_segment.goto(position) #se le indica la position que es la variable del ciclo para que itere en las diferentes posiciones
    segments.append(snake_segment) #aca le agregamos con append a lo ultimo de la lista los cuadrados de snake_segment
#construir cuerpo serpiente sin optimizar
'''
snake_segment = Turtle("square") #convertimos en un objeto instaciando la clase declarada de arriba con la variable creada, con square le decimos que nos cree un dibujo cuadrado
snake_segment.color("white") #pasamos el color


snake_segment2 = Turtle("square") #creamos otra parte del cuerpo pero esta sale debajo de la primera, con goto() la enviamos hacia donde queramos, por que la ventana turtle es un plano cartesiano, por defecto se coloca en el centro
snake_segment2.color("white")
snake_segment2.goto(-20, 0) #aca le decimos que se vaya -20 en X y que en Y quede en la misma posicion

snake_segment3 = Turtle("square") #creamos otra parte del cuerpo pero esta sale debajo de la primera, con goto() la enviamos hacia donde queramos, por que la ventana turtle es un plano cartesiano, por defecto se coloca en el centro
snake_segment3.color("white")
snake_segment3.goto(-40, 0) #aca le decimos que se vaya -40 en X por que va de 20 en 20 y que en Y quede en la misma posicion
'''

#Animacion serpiente sin optimizar
game_is_on = True #verificamos si el juego esta activo con boolean y la primera letra en python debe ser mayuscula

while game_is_on:  #mientras sea verdadero que es el valor que indicamos arriba se ejecute esto
    screen.update() #actualizamos la pantalla
    time.sleep(0.1)#esto le da el tiempo que se desplaza los tres cuadritos
    #optimizado pero no podemos decirle que se mueva a otro lado
    '''
    for segment in segments: #con el ciclo indicamos que cada cuadrito se mueva
        segment.forward(20) #aca se mueve adelante en 20 frames
    '''
    #sin optimizar
   
    for seg_num in range(len(segments) -1, 0, -1): #creamos un ciclo que se alimenta de segments que son cada uno de los cuadros arriba, con range le decimos que va a ir de un lugar a el que le especifiquemos, para decir que no queremos el objeto de segments si no cada cosa lo hacemos con len
        #el -1 es por que al traer la lista desde 0 serian 4 elementos pero la lista de las coordenadas son solo 3 por eso se le resta uno
        new_x = segments[seg_num -1].xcor() #llamamos a algo dentro de una lista con corchetes, lo traemos el segmento y lo guardamos en la variable y se convierte en cordenada de x
        new_y = segments[seg_num -1].ycor() #aca con las coordenadas de y
        segments[seg_num].goto(new_x, new_y)#aca le decimos que se mueva segun las coordenadas que le entregamos arriba
    segments[0].forward(20) #indicamos la primera posicion que es la cabeza y forward yo lleva hacia adelante, tenemos que atrasar la identacion para que salga del ciclo

screen.exitonclick() #cierra el proceso con un click