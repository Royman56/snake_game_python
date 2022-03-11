#aca va lo que se va a ejecutar a el archivo snake solo dejamos las caracteristicas de la serpiente, el escenario y la ejecucion estaran aca
#se llaman las librerias especificas o general:
from turtle import Screen #las clases empiezan en mayusculas, turtle libreria para crear el cuerpo y scrren para el escenario.
import time
from snakepoo import Snake #asi se llama la clase
from food import Food
from scoreboard import Score

#Creacion del tablero de el juego.
screen = Screen() #los parentesis indican que se creara un objeto, aca le asignamos la clase Screen que se importa arriba.
screen.setup(width=600, height=600) #indicamos las medidas del escenario
screen.bgcolor("blue") #el color que llevara el escenario
screen.title("Programate snake") #titulo arriba del juego

screen.tracer(0) #esto pausa la animacion automatica
snake = Snake() #aca se crea la serpiente se instancia el objeto
food = Food() #aca se crea la comida se instancia el objeto y por eso se visualiza
score = Score()
game_is_on = True #verificamos si el juego esta activo con boolean y la primera letra en python debe ser mayuscula

screen.listen() #metodo de escucha de las teclas
screen.onkey(snake.up, "Up") #se establece, aca al metodo up no se le pone parentesis por que esta esperando lo que esta en las comillas para funcionar 
screen.onkey(snake.down, "Down") 
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move() #aca se le pasa el movimiento creado en la funcion move de snakepoo

    if snake.segments[0].distance(food) < 15: #detectar colision de comida
       food.refresh()
       score.increase_score()#aca le decimos que cuando la serpiente coma la comida se cumpla esta funcion que es que aumente en 1
       snake.extend()

    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280: #detector de colisiones, con xcor le decimos que en esa cordenada en este caso 280 aplique la funcion de abajo, or es los demas lado por que x solo es al lado derecho
        game_is_on = False #aca le decimos que no se mueva la serpiente por que game_is_on esta true en inicio
        score.game_over() #aca le cambiamos el letrero score por que ha terminado el juego

    for segment in snake.segments:    #detector de colisiones de segmento deserpiente
        if segment == snake.segments[0]:
            pass
        elif snake.segments[0].distance(segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick() #cierra el proceso con un click