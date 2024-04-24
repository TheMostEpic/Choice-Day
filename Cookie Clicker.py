import turtle

wn = turtle.Screen()
wn.bgcolor("black")

wn.register_shape(r"C:\Users\iCan Student\Desktop\Ican3\Coding Stuff\Choice-Day\cookie.gif")
wn.register_shape(r"C:\Users\iCan Student\Desktop\Ican3\Coding Stuff\Choice-Day\cursor.gif")
wn.register_shape(r"C:\Users\iCan Student\Desktop\Ican3\Coding Stuff\Choice-Day\grandma.gif")

cookie = turtle.Turtle()
cookie.shape(r"C:\Users\iCan Student\Desktop\Ican3\Coding Stuff\Choice-Day\cookie.gif")
cookie.speed(0)

cursor = turtle.Turtle()
cursor.shape(r"C:\Users\iCan Student\Desktop\Ican3\Coding Stuff\Choice-Day\cursor.gif")
cursor.speed(0)
cursor.penup()
cursor.goto(-400, 0)
cursor_cost = 50
cursor_multiplier = 1

cursor_desc = turtle.Turtle()
cursor_desc.hideturtle()
cursor_desc.penup()
cursor_desc.color("white")
cursor_desc.goto(-400, -200)
cursor_desc.write("Increases the amount of cookies gained per click by 1", align="center", font=("Courier", 10, "normal"))

cursor_info = turtle.Turtle()
cursor_info.hideturtle()
cursor_info.penup()
cursor_info.color("white")
cursor_info.goto(-400, 200)
cursor_info.write(f"Cost: {cursor_cost}, Amount: {cursor_multiplier}", align="center", font=("Courier", 15, "normal"))

grandma = turtle.Turtle()
grandma.shape(r"C:\Users\iCan Student\Desktop\Ican3\Coding Stuff\Choice-Day\grandma.gif")
grandma.speed(0)
grandma.penup()
grandma.goto(400, 0)
grandma_cost = 100
grandma_clicks = 0

grandma_info = turtle.Turtle()
grandma_info.hideturtle()
grandma_info.penup()
grandma_info.color("white")
grandma_info.goto(400, 300)
grandma_info.write(f"Cost: {grandma_cost}, Amount: {grandma_clicks}", align="center", font=("Courier", 15, "normal"))

grandma_desc = turtle.Turtle()
grandma_desc.hideturtle()
grandma_desc.penup()
grandma_desc.color("white")
grandma_desc.goto(400, -300)
grandma_desc.write("Generates 1 cookie a second", align="center", font=("Courier", 10, "normal"))


clicks = 0

pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(0, 200)
pen.write(f"Clicks: {clicks}", align="center", font=("Courier", 20, "normal"))

grandma_timer_active = False

def clicked(x, y):
    global clicks
    clicks += cursor_multiplier
    pen.clear()
    pen.write(f"Clicks: {clicks}", align="center", font=("Courier", 20, "normal"))

def buy_cursor(x, y):
    global clicks, cursor_cost, cursor_multiplier
    if clicks >= cursor_cost:
        clicks -= cursor_cost
        cursor_multiplier += 1
        cursor_cost += 50
        cursor_info.clear()
        cursor_info.write(f"Cost: {cursor_cost}, Amount: {cursor_multiplier}", align="center", font=("Courier", 15, "normal"))
        pen.clear()
        pen.write(f"Clicks: {clicks}", align="center", font=("Courier", 20, "normal"))

def buy_grandma(x, y):
    global clicks, grandma_cost, grandma_clicks, grandma_timer_active
    if clicks >= grandma_cost:
        clicks -= grandma_cost
        grandma_clicks += 1
        grandma_cost += 100
        grandma_info.clear()
        grandma_info.write(f"Cost: {grandma_cost}, Amount: {grandma_clicks}", align="center", font=("Courier", 15, "normal"))
        pen.clear()
        pen.write(f"Clicks: {clicks}", align="center", font=("Courier", 20, "normal"))
        if not grandma_timer_active:
            grandma_timer_active = True
            wn.ontimer(grandma_click, 1000)

def grandma_click():
    global clicks, grandma_clicks, grandma_timer_active
    clicks += grandma_clicks
    pen.clear()
    pen.write(f"Clicks: {clicks}", align="center", font=("Courier", 20, "normal"))
    if grandma_timer_active:
        wn.ontimer(grandma_click, 1000)
    else:
        grandma_timer_active = False

cookie.onclick(clicked)
cursor.onclick(buy_cursor)
grandma.onclick(buy_grandma)
wn.mainloop()
