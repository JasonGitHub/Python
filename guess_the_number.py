import simplegui, random, math

secret = 0
cnt = 0
hi = 100

def new_game():
    global secret, cnt
    cnt = 0
    secret = random.randrange(0, hi)
    print 'New Game Started in Range(0, ' + str(hi) + ').'
    print 'Number of remaining guess is', get_remaining(), '\n'

def range100():
    global hi
    hi = 100
    new_game()

def range1000():
    global hi
    hi = 1000
    new_game()
    
def get_remaining():
    return int(math.ceil(math.log(hi + 1, 2))) - cnt
    
def input_guess(guess):
    global cnt
    cnt += 1
    print 'Guess was', guess
    print 'Number of remaining guess is', get_remaining()
    if (int(guess) == secret):
        print 'Correct!\n'
        new_game()
    elif get_remaining() == 0:
        print 'You ran out of guesses. The number was', secret, '\n'
        new_game()
    elif int(guess) < secret:
        print 'Higher!\n'
    else: 
        print 'Lower!\n'
    
f = simplegui.create_frame('Main', 200, 200)
f.add_input('Enter a guess:', input_guess, 200)
f.add_button('Range: 0 - 100', range100, 200)
f.add_button('Range: 0 - 1000', range1000, 200)
f.start()
new_game()
