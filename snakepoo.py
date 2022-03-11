#aca va solo el cuerpo y el movimiento de laserpiente

#se llaman las librerias especificas o general:
from turtle import Turtle #las clases empiezan en mayusculas, turtle libreria para crear el cuerpo y scrren para el escenario.

starting_position = [(0, 0), (-20, 0), (-40, 0)] #esta variable se convierte en lista y lleva las coordenadas(posiciones del plano)
UP = 90 #creamos constantes para las variables que mueven a las serpientes las constantes van en mayusculas
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:

    def __init__(self):  #constructor con esto crea el objeto serpiente, activa las funciones para yo poder utilizarlas como quiera
        self.segments = [] #creamos una variable global para usar cada posicion y poder moverlos ya que quedan en el ciclo atrapados, self es como this le decimos que es un atributo/variable de la clase

    #Metodo de crear la serpiente
        self.create_snake() 

    def create_snake(self):
        
        for position in starting_position:   #los bloques de codigo en python no son con llaves sino con 2 puntos, position es la variable i en ejemplos de for
            self.add_segment(position)
    
    def add_segment(self, position):
        snake_segment = Turtle("square") #identacion de 4 espacios CUIDADO con esto en python
        snake_segment.color("white")
        snake_segment.penup() #deja de dibujar y quita la linea blanca
        snake_segment.goto(position) #se le indica la position que es la variable del ciclo para que itere en las diferentes posiciones
        self.segments.append(snake_segment) #aca le agregamos con append a lo ultimo de la lista los cuadrados de snake_segment
#construir cuerpo serpiente sin optimizar

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):

         for seg_num in range(len(self.segments) -1, 0, -1):

             new_x = self.segments[seg_num -1].xcor() 
             new_y = self.segments[seg_num -1].ycor()
             self.segments[seg_num].goto(new_x, new_y)
         self.segments[0].forward(20)

    def up(self): #aca creamos la funcion para escuchar las letras en main con self entra en la clase snake
        if self.segments[0].heading() != DOWN: #aca creamos un condicional para decirle que si esta yendo hacia arriba la primera posicion no pueda volver
            self.segments[0].setheading(UP) #aca indicamos la primera posicion de la serpiente que se movera y con setheading le indicamos el movimiento 
    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)
        
    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)
    
    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

