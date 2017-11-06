#myFunctionfile
def polygon (t,s,d):
    a=360/s
    t.begin_fill()
    for times in range(s):
      t.forward(d)
      t.right(a)
    t.end_fill()
def jump(t,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
def cool(t,d,c1,c2,c3):
    t.color(c1)
    polygon(t,6,d)
    t.color(c2)
    polygon(t,5,d)
    t.color(c3)
    polygon(t,4,d)

def draw_star(t,s,a):
    count=0
    while count<=5:
        t.forward(s)
        t.right(a)
        count+=1
    return
    

    

    

