from turtle import *
color('red', 'yellow')

begin_fill()
f = 400
while True:
    forward(f)
    left(90)
    f -= 15

    if abs(pos()) < 1:
        break
end_fill()
done()