import turtle
import pandas
from write_state import WriteState
correct_guess = 0
number_of_states= 50

answer_write = WriteState()
screen = turtle.Screen()
screen.title(f" U.S States Game {correct_guess} / {number_of_states}")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)
data =pandas.read_csv("50_states.csv")
states = data["state"].to_list()

# coordinates = data[data.state == "Ohio"]
# x_cor = int(coordinates.x)
#
# print(x_cor)

# print(answer_state)
correct_guess = 0
number_of_states= 50
states_covered = []
while correct_guess <=50:
    answer_state = screen.textinput(title=f"Guess the state {correct_guess} / {number_of_states}" , prompt=" what's another state's name?")
    answer_state = answer_state.title()

    if answer_state == "Exit":
        states_to_learn = []
        for ii in range(0, len(states)):
            if states[ii] not in states_covered:
                states_to_learn.append(states[ii])
        print(f"States to learn : \n {states_to_learn}")
        # data_1 = pandas.DataFrame(states_to_learn)
        # data_1.to_csv("states_to_learn.csv")
        break

    if answer_state in states:
        coordinates = data[data.state == answer_state]
        x_cor = int(coordinates.x)
        y_cor = int(coordinates.y)
        answer_write.write_name(x_cor,y_cor,answer_state)
        if answer_state in states_covered:
            pass
        else:
            states_covered.append(answer_state)
            correct_guess +=1
        pass

states_to_learn = []
for ii in range(0,len(states)):
    if states[ii] not in states_covered:
        states_to_learn.append(states[ii])
data_1 = pandas.DataFrame(states_to_learn)
data_1.to_csv("states_to_learn.csv")