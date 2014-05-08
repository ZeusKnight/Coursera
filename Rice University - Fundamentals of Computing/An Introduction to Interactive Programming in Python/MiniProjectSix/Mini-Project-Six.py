# implementation of card game - Memory

import simplegui
import random
y_up = 0
y_down = 100
deck = []
up = []
round = 0
check = []

# helper function to initialize globals
def new_game():
    global deck, up, round, check
    round = 0
    check = []
    deck = range(0,8)
    deck.extend(range(0,8))
    up = [False for i in deck ]
    random.shuffle(deck)
     
# define event handlers
def mouseclick(pos):
    global check, round
    x = pos[0]
    y = pos[1]
    if x % 50 > 0 and x % 50 < 50:
        index = x / 50
        if up[index] != True: 
            up[index] = not up[index]
            if round == 0 or len(check) == 2: round += 1
            if len(check) >= 2:
                if deck[check[0]] != deck[check[1]]:
                    up[check[0]] = False
                    up[check[1]] = False
                check = []
            if len(check) < 2:
                check.append(index)             
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    x = 15
    for i in range(len(deck)):
        if up[i]:
            canvas.draw_text(str(deck[i]), [x, 75], 45, 'Red')
        else:
            canvas.draw_line([x + 10, 0], [x + 10, 100], 49, "Green")
        x = x + 50
    tmp = 0
    for i in range(len(deck) + 1):
        canvas.draw_line([tmp, 0], [tmp, 100], 1, "Red")
        tmp = tmp + 50
    label.set_text("Turns = " + str(round))

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()