import random
from turtle import Turtle, goto 

#Herencia: una clase padre le entrega atributos a sus hijos

VAL1 = -200
VAL2 = 200

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("triangle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("orange")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(VAL1,VAL2) #aca le decimos a la comida que salga en x o en y aleatorio con un paquete que importamos con randint le pasamos las coordenadas en numero enteros
        random_y = random.randint(VAL1,VAL2)
        self.goto(random_x, random_y) #esto muestra en pantalla segun las coordenadas de manera aleatoria