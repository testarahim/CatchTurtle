import time
import turtle
from random import random

screen = turtle.Screen()
screen.bgcolor("light green")
screen.title("Catch Turtle")


# deneme = turtle.Turtle()

turtle_instance = turtle.Turtle()
turtle_instance.shape("turtle")
timer_text = turtle.Turtle()
score_text = turtle.Turtle()
mouse = turtle.Turtle()
turtle_instance.penup()
timer_text.hideturtle()
timer_text.penup()
timer_text.setx(0)
timer_text.sety(350)
score_text.hideturtle()
score_text.penup()
score_text.setx(0)
score_text.sety(300)
mouse.penup()
mouse.hideturtle()

def click_pos(a, b):
    mouse.goto(a, b)

# ws = turtle.getcanvas()
# ws.bind("<Motion>", mouse_fun)
# print(turtle.pos())


#TODO Get and return mouse position(x,y)
start = time.time()

remain = 15
posX = 0.0
posY = 0.0
screen.onscreenclick(click_pos)
print(mouse.pos())


score = 0
while time.time() - start < remain:
    turtle_instance.setx(300 * random())
    time.sleep(0.4)
    turtle_instance.sety(300 * random())
    time.sleep(0.4)
    timer_text.clear()
    timer_text.write(int(start + remain - time.time()), font=("Courier", 30))
    if mouse.pos()[0] <= turtle_instance.pos()[0] * 10 and mouse.pos()[1] <= turtle_instance.pos()[1] * 10:
        score_text.clear()
        score_text.write(int(score), font=("Courier", 30))
        score += 1
        time.sleep(0.3)




    screen.update()

timer_text.clear()
timer_text.write("Game Over!", align="center", font=("Courier", 30))

turtle.mainloop()