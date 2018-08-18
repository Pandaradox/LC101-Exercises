import turtle, random              # 1. import the modules
thunderdome = turtle.Screen()       # 2. Create a screen
thunderdome.bgcolor('lightblue')
mario = turtle.Turtle()    # 3. Create two turtles
sonic = turtle.Turtle()
mario.color('red')
sonic.color('blue')
mario.shape('turtle')
sonic.shape('turtle')
sonic.up()                  # 4. Move the turtles to their starting point
mario.up()
sonic.goto(-200,20)
mario.goto(-200,-20)

trash = ["F-off", "You suck", "Eat my dust", "Your mom's faster than this!"]
# your code goes here

for rounds in range(20):
    sonic.forward(random.randint(0,25))
    sonic.write("      "+random.choice(trash))
    mario.forward(random.randint(0,25))
    mario.write("      "+random.choice(trash))
    turtle.delay(50)
    sonic.clear()
    turtle.delay(50)
    mario.clear()
mario.write("     "+random.choice(trash))
sonic.write("     "+random.choice(trash))

thunderdome.exitonclick()
