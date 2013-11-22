# implementation of card game - Memory

import simplegui
import random

deck = range(0, 8) + range(0, 8)
exposed = [False] * 16
state = 0
pair = [-1, -1]
counter = 0

def update_counter():
    label.set_text("Turns = " + str(counter))

def new_game():
    global exposed, state, counter
    random.shuffle(deck)
    exposed = [False] * 16
    state = 0
    counter = 0
    pair = [-1, -1]
    update_counter()

def mouseclick(pos):
    global exposed, state, pair, counter
    i = pos[0] / 50
    if (not exposed[i]):
        if state == 0:
            exposed[i] = True
            pair[0] = i
            state = 1
            # print pair
        elif state == 1:
            exposed[i] = True
            pair[1] = i
            counter += 1
            update_counter()
            state = 2
            # print pair
        else:
            if (deck[pair[0]] != deck[pair[1]]):
                exposed[pair[0]] = False
                exposed[pair[1]] = False
            exposed[i] = True
            pair[0] = i
            state = 1
            # print pair

def draw(canvas):
    for ix, card in enumerate(deck):
        if (exposed[ix]):
            canvas.draw_text(str(card), (10 + 50 * ix, 75), 60, 'White')
        else:
            canvas.draw_polygon([(50 * ix, 0), (50 + 50 * ix, 0), (50 + 50 * ix, 100), (50 * ix, 100)], 0.5, 'Red', 'Green')

frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", new_game)
label = frame.add_label("Turns = 0")

frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

new_game()
frame.start()
