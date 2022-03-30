FONT = ("Courier", 12, "bold")
from turtle import Turtle

class WriteState(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.current_score = 0


    def write_name(self, x_cor,y_cor, statename):
        self.goto(x_cor,y_cor)
        self.write(f"{statename}", align="center", font= FONT)

