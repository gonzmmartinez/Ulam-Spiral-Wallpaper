import turtle # import turtle package


turtle.setup(1366, 768) # creating a canvas (according to my screen resolution)
turtle.bgcolor('black') # setting black color for background
turtle.hideturtle() # hiding the cursor
turtle.tracer(False) # for the animation to be fast
turtle.speed(0)

turtle.penup()
turtle.goto(0,0) # starting point, right in the middle

size = 5

for i in range(1, 3000+1):
    if i > 1:
        for j in range(2, int(i / 2) + 1): # Ulam's spiral highlights the prime numbers in a range
            if (i % j) == 0:
                prime = False
                break
        else:
            prime = True
    else:
        prime = False

    if prime:
        turtle.dot(6, 'white') # if the number is prime, the dot is bigger
    else:
        turtle.dot(2, 'white') # if the numer is not prime, the dot is smaller

    turtle.forward(size+0.2*i) # a small increase in the distance between the placed point and the previous one
    turtle.left(35) # a 35 dg turn for making the spiral effect

cv = turtle.getcanvas()
cv.postscript(file="Ulam.ps", colormode='color') # the spiral is exported as a .ps file

turtle.done()