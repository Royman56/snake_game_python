from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 270)
        self.color("white") 
        self.update_score() #aca le pasamos la actualizacion con el metodo creado de abajo
        self.write(f"El puntaje es: {self.score}", font=("Arial", 22, "normal"), align="center") #la f significa que se podra concatenar con las llaves, font es tuplas para indicar diferentes instrucciones por eso va entre parentesis a diferencia de lista que va en corchetes
        self.hideturtle() #aca ocultamos el puntero de turtle

    def update_score(self):
        self.write(f"El puntaje es: {self.score}", font=("Arial", 22, "normal"), align="center") #la f significa que se podra concatenar con las llaves, font es tuplas para indicar diferentes instrucciones por eso va entre parentesis a diferencia de lista que va en corchetes

    def increase_score(self):
        self.clear() #se limpia el score y se actualiza en uno con la linea de abajo
        self.score += 1
        self.update_score()#aca dibuja de nuevo el marcador

    def game_over(self):
        self.clear() 
        self.write("Que man tan manco", font=("Arial", 22, "normal"), align="center")