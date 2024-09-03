from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)

my_turtle = Turtle()
write_turtle = Turtle()
my_turtle.shape(image)

data = pandas.read_csv('50_states.csv')

all_states = data['state'].to_list()

list_of_known_state = []


while len(list_of_known_state) < 50:
    answer_state = screen.textinput(title=f'{len(list_of_known_state)}/50', prompt='What is the name of another state?').title()
    if answer_state == "Exit":
        break
    if answer_state in all_states:
        list_of_known_state.append(answer_state)
        t = Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data['state'] == answer_state]
        x_cor = state_data['x']
        y_cor = state_data['y']
        t.goto(int(x_cor), int(y_cor))
        t.write(answer_state)

# states_to_learn.csv
# for state in list_of_known_state:
#     if state in all_states:
#         all_states.remove(state)

learn_state = [state for state in all_states if not state in list_of_known_state]


# print(all_states)
# states_to_learn = all_states.to_csv()
dict  = {
    'state': learn_state

}

df = pandas.DataFrame(dict)

need_to_learn_state = df.to_csv('Need_to_learn_state')
print(need_to_learn_state)
