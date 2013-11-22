import simplegui

# define global variables
curr_time = 0
x = 0
y = 0
running = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    a = t / 600 % 60
    b = t % 600 / 100 % 10
    c = t % 600 / 10 % 10
    d = t % 600 % 10
    return str(a) + ':' + str(b) + str(c) + '.' + str(d)
    
def start():
    global running
    running = True
    t.start()
def stop():
    global x, y, running
    t.stop()
    if (running): 
        y += 1
        if curr_time % 600 % 10 == 0: x += 1
    running = False
def reset():
    global t, curr_time, x, y, running
    x = 0
    y = 0
    running = False
    t.stop()
    t = simplegui.create_timer(100, tick)
    curr_time = 0
def tick():
    global curr_time
    curr_time += 1
def draw(canvas):
    canvas.draw_text(format(curr_time), [65, 85], 30, 'White')
    canvas.draw_text(str(x) + '/' + str(y), [165, 20], 20, 'Green')

t = simplegui.create_timer(100, tick)    
f = simplegui.create_frame("Main", 200, 150)
f.set_draw_handler(draw)
f.add_button("Start", start, 50)
f.add_button("Stop", stop, 50)
f.add_button("Reset", reset, 50)
f.start()

