from turtle import*
import copy

speed(0)
penup()
goto(494,300)
right(180)
pendown()
for i in range(12):
    color("indianred")
    left(90)
    penup()
    forward(40)
    pendown()
    right(90)
    for i in range(2):
        forward(988)
        right(90)
        forward(40)
        right(90)
right(180)
y_pos = 300
distt = -80
start_y = copy.deepcopy(y_pos)
for i in range(7):
    penup()
    goto(-494, start_y)
    start_y = start_y+distt
    pendown()
    for i in range(2):
        begin_fill()
        forward(988)
        right(90)
        forward(40)
        right(90)
        end_fill()
color("darkblue")
penup()
goto(-494,300)
pendown()
begin_fill()
for i in range(2):
    forward (396)
    right(90)
    forward(280)
    right(90)
end_fill()
dist = 66
down = -50
x_pos = -467
y_pos = 260
start_x = copy.deepcopy(x_pos)
start_y = copy.deepcopy(y_pos)
left(15)
for i in range(6):
    penup()
    goto(start_x, 260)
    pendown()
    for i in range(6):
        color("white")
        begin_fill()
        for i in range(5):
            forward(5)
            right(36)
            forward(5)
            left(108)
        end_fill()
        penup()
        goto(start_x, start_y)
        start_y = start_y+down
    start_x = start_x+dist
    start_y = start_y+300
xx_pos = -434
yy_pos = 235
start_xx = copy.deepcopy(xx_pos)
start_yy = copy.deepcopy(yy_pos)
for i in range (5):
    penup()
    goto(start_xx, 235)
    for i in range(5):
        color("white")
        begin_fill()
        for i in range(5):
            forward(5)
            right(36)
            forward(5)
            left(108)
        end_fill()
        penup()
        goto(start_xx, start_yy)
        start_yy = start_yy+down
    start_xx = start_xx+dist
    start_yy = start_yy+250
right(15)
penup()
goto(-494,300)
pendown()
color("black")
for i in range(2):
    forward(988)
    right(90)
    forward(520)
    right(90)