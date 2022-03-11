#crear clase que herede de otra aca se van a hacer dos clases en un mismo archivo lo recomendable es en dos archivos

class Animal: #esta es la clase padre

    def __init__(self): #todas las clases llevan esto sea padre o hijo por que es el constructor
        self.num_ojos = 2

    def respirar(self):
        print("Inhale, Exhale")

class Pez(Animal):  #se abre parentesis con animal por que va a heredar de animal esta es la clase hijo

    def __init__(self):
        super().__init__() #con esto se le dice que de animal traiga todo lo que lleve
        #super().num_ojos = 3#aca le decimos que ya no queremos que tenga dos ojos como arriba en animal si no 3
    def respirar(self):
        super().respirar()#aca traemos el metodo respirar o,sea que mostraria inhale, exhale y gluglu con lo de abajo
        print("Glu Glu")  #sobreescribir el metodo de respirar en animal

    def nadar(self):
        print("nadaremos")

nemo = Pez() #asi le decimos que nemo es de Pez
nemo.respirar() #aca mostramos lo de la funcion nadar