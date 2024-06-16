import random
import time

import colorgram
import turtle as t

t.colormode(255)
t.penup()

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))

print(rgb_colors)
x = 0.0

time.sleep(4)

for i in range(10):
    t.setx(-200)
    t.sety(-200 + x)

    for i in range(10):
        t.dot(20, random.choice(rgb_colors))
        t.forward(50)

    x += 50

t.Screen().exitonclick()
