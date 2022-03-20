from turtle import Turtle
ALIGNMENT = "center"
FONT = "Courier"
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto (0,270)
        self.color("white")
        self.score = 0
        self.write(f"Score:{self.score}", True, align=ALIGNMENT,font=(FONT, 16, 'normal'))
        self.hideturtle()
    def update_scoreboard(self):
        self.write(f"Score:{self.score}", True, align="center",font=('Arial', 16, 'normal'))


    def calculate_score(self):
        self.score +=1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", True, align="center",font=('Arial', 16, 'normal'))



