import turtle
def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def draw_koch_snowflake(order, size=300, spokes=6):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)  
    t.penup()
    t.goto(-size / 2, 0)
    t.pendown()
#spokes - для вибору кількості променів зірки
    for _ in range(spokes):
        koch_curve(t, order, size)
        t.right(360 / spokes)

    window.mainloop()

# Виклик функції
draw_koch_snowflake(order=2, spokes=3)