import turtle
import pandas
screen = turtle.Screen()
screen.title("Indian State")
image = "India-state.gif"
screen.addshape(image)
turtle.shape(image)

india = pandas.read_csv("states_data.csv")
all_state = india.state.to_list()
answered_state = []
total = 30
guessed = 0
while guessed != 30:
    answer = screen.textinput(title=f"Guess the state{guessed}/{total}", prompt="Name the states of INDIA").title()
    if answer == "Exit":
        break
    if answer in all_state:
        answered_state.append(answer)
        var = india[india.state == answer]
        t1 = turtle.Turtle()
        t1.penup()
        t1.hideturtle()
        t1.goto(int(var.x), int(var.y))
        t1.write(answer)
        guessed += 1
missed = [state for state in all_state if state not in answered_state]
print(missed)
new_data = pandas.DataFrame(missed)
new_data.to_csv("state_to_learn")
