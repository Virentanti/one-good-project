import abc
import turtle

class poligon:
    def __init__(self,sides,size=50,color="black",line=2):
        self.sides=sides
        self.size=size
        self.color=color
        self.line=line
    
    def draw(self):
        self.angle=(self.sides-2)*(180/self.sides)
        turtle.color(self.color)
        turtle.pensize(self.line)
        for i in range(self.sides):
            turtle.forward(self.size)
            turtle.left(180-self.angle)
        turtle.done()

poligon(3,size=200,color="red",line=20).draw()

