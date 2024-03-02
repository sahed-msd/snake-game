import turtle
import time
import random

turtle.color('black')
turtle.setup(0,0)
style = ('Courier',0, 'italic')
turtle.write("""

██████╗░░█████╗░  ░█████╗░██████╗░  ██████╗░██╗███████╗
██╔══██╗██╔══██╗  ██╔══██╗██╔══██╗  ██╔══██╗██║██╔════╝
██║░░██║██║░░██║  ██║░░██║██████╔╝  ██║░░██║██║█████╗░░
██║░░██║██║░░██║  ██║░░██║██╔══██╗  ██║░░██║██║██╔══╝░░
██████╔╝╚█████╔╝  ╚█████╔╝██║░░██║  ██████╔╝██║███████╗
╚═════╝░░╚════╝░  ░╚════╝░╚═╝░░╚═╝  ╚═════╝░╚═╝╚══════╝""", font=style, align='center')
turtle.hideturtle()
wn = turtle.Screen()
wn.title("🍔👣 𝕊𝑛𝖆𝚔🄴 𝑮🄰𝙢𝗲 𝚌🅡𝐞𝚊𝔱𝙤𝓇 𝔟𝐲 🆂🅰🅷🅴🅳 ✌🍧")
wn.bgpic("play.gif")
wn.addshape('head.gif')
wn.addshape("food.gif")
wn.addshape("body.gif")
wn.setup(width=600, height=600)
wn.tracer(0)
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.shape("head.gif")
head.color("blue")
head.penup()
head.goto(0, 0)
head.direction = "Stop"
speed = 1
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.shape("food.gif")
food.penup()
food.goto(0, 100)
segments = []
def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def go_right():
    if head.direction != "left":
        head.direction = "right"
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")
while True:
    wn.update()
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("blue")
        new_segment.shape("body.gif")
        new_segment.penup()
        segments.append(new_segment)
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    move()
    if (
        head.xcor() > 290
        or head.xcor() < -290
        or head.ycor() > 290
        or head.ycor() < -290
    ):
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"

        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "Stop"
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
    time.sleep(0.1)

