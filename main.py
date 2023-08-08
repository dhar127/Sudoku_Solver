import pgzrun # Do not edit this line
#Screen Width in pixels
WIDTH=500
#Screen height in pixels
HEIGHT=500

circle_color = 'white'
circle_posx = 250
circle_posy = 250

#function that draws
def draw():
    #screen is your window
    #screen.fill(colorname)
    screen.fill('black')

    #screen.draw.circle((posx,posy),radius,color)
    screen.draw.circle((circle_posx,circle_posy),50,circle_color)

def on_key_down(key):
    print(key)
    global circle_posx,circle_posy
    if(key == key.UP):
        circle_posy = circle_posy - 4
    elif(key == key.DOWN):
        circle_posy = circle_posy + 4
    elif(key == key.LEFT):
        circle_posx = circle_posx - 4
    elif(key == key.RIGHT):
        circle_posx = circle_posx + 4

pgzrun.go() # Do not edit this line