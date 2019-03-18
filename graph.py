import turtle

t = turtle.Turtle()
t.speed(20)

t.down()
t.goto(0,0) #middle
t.write ("0", font=("Arial", 0, "normal"))

t.goto(0, 100) #left
t.write("Y 100", font=("Arial", 12, "normal"))
t.goto(0,0)

t.goto(-100, 0)#right
t.write("X -100", font=("Arial", 12, "normal"))
t.goto(0,0)

t.goto(100,0)#right
t.write("100", font=("Arial", 12, "normal"))
t.goto(0,0)

t.goto(0,-100)# bottom
t.write("-100", font=("Arial", 12, "normal"))


t.up()
t.goto(50, 50)
t.down()
t.color("red")
t.circle(10)


t.up()
t.goto(50, -50)
t.color("blue")
t.down()
t.circle(10)


t.up()
t.goto(-100,-100)
t.down()
t.color("purple")
for i in range(3):
  t.forward(30)
  t.left(120)



t.up()
t.goto(-100,100)
t.down()
t.color("green")
for i in range(4):
  t.forward(20)
  t.right(90)

t.ht() #hide turtle
