#pygame zero run library name
import pgzrun
import random
WIDTH = 600
HEIGHT = 500

def draw():
    screen.fill("White")
    #r1 = Rect((50,50),(100,50))
    #screen.draw.rect(r1,"red")
    #screen.draw.filled_rect(r1,"red")
    x = WIDTH/2
    y = HEIGHT/2
    w = 100
    h = 50
    for i in range(10):
     r = random.randint(0,255)
     g = random.randint(0,255)
     b = random.randint(0,255)  
     r1 = Rect((0,0),(w,h))
     r1.center = x,y
     screen.draw.rect(r1, (r,g,b))   
     w += 10
     h -= 10



    #r2 = Rect((50,100),(100,50))
    #screen.draw.rect(r2,"blue")
    #screen.draw.filled_rect(r2,"blue")
#mainloop the screen output
pgzrun.go()

#pygame zero run library name
import pgzrun
import random
WIDTH = 600
HEIGHT = 500

def draw():
    screen.fill("White")
    #r1 = Rect((50,50),(100,50))
    #screen.draw.rect(r1,"red")
    #screen.draw.filled_rect(r1,"red")
    x = WIDTH/2
    y = HEIGHT/2
    w = 100
    h = 50
    for i in range(10):
     r = random.randint(0,255)
     g = random.randint(0,255)
     b = random.randint(0,255)  
     r1 = Rect((0,0),(w,h))
     r1.center = x,y
     screen.draw.rect(r1, (r,g,b))   
     w += 10
     h -= 10



    #r2 = Rect((50,100),(100,50))
    #screen.draw.rect(r2,"blue")
    #screen.draw.filled_rect(r2,"blue")
#mainloop the screen output
pgzrun.go()


