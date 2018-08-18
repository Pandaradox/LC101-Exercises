import turtle, random
dojo = turtle.Screen()
ninjurtle = turtle.Turtle()
ninjurtle.shape("turtle")
rainbow = ["red", "orange", "blue", "purple"]
sfx = ["Hiya!", "Kiya", "SHING!", "*Slice*", "Wahh"]
for moving in range(20):
    ninjurtle.up()
    ninjurtle.goto(random.randint(-50,50),random.randint(-50,50))
    ninjurtle.down()
    ninjurtle.color(random.choice(rainbow))
    ninjurtle.forward(random.randint(10,50))
    ninjurtle.left(random.randint(0,181))
    ninjurtle.write(random.choice(sfx))

ninjurtle.clear()
ninjurtle.color("orange")
ninjurtle.up()
ninjurtle.goto(0,0)
ninjurtle.write("    <COWABUNGA, DUDES!")

dojo.exitonclick()
