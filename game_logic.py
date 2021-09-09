# simple memory game, needs to be run with the simplegui library available on codeskulptor.com

import simpleguitk as simplegui
import random

avatar_links = [
    'https://www.avatarist.com/avatars/Cartoons/The-Simpsons/Agnes.gif',
    'https://www.avatarist.com/avatars/Cartoons/The-Simpsons/Apu2.gif',
    'https://www.avatarist.com/avatars/Cartoons/The-Simpsons/Avocat.gif',
    'https://www.avatarist.com/avatars/Cartoons/The-Simpsons/Barney.gif',
    'https://www.avatarist.com/avatars/Cartoons/The-Simpsons/Bart3.gif',
    'https://www.avatarist.com/avatars/Cartoons/The-Simpsons/Blinky-The-Fish.gif',
    'https://www.avatarist.com/avatars/Cartoons/The-Simpsons/Chalmers.gif',
    'https://www.avatarist.com/avatars/Cartoons/The-Simpsons/Chief-Wiggum2.gif',
]

a, b, c, d, e, f, g, h = None, None, None, None, None, None, None, None
image_vars = [a,b,c,d,e,f,g,h]

# load images to image_vars variables
for i in range(len(avatar_links)):
    image_vars[i] = simplegui.load_image(avatar_links[i])

# set up game variables
deck = [i for i in image_vars for i in image_vars]
state_counter = 0
cards_dict = {}
turn_counter = 0
list_pos = (1288, 85)


def new_game():
    """Resets all variables to restart the game"""
    global deck, turn_counter, state_counter, cards_dict, list_pos
    list_pos = (-1, -1)
    turn_counter = 0
    state_counter = 1
    cards_dict = {}
    random.shuffle(deck)
    counter = 0
    loc = [0, 0, 80, 80]
    for x in deck:
        cards_dict[counter] = [x, False, loc[:], 0]
        counter += 1
        loc[0] += 80
        loc[2] += 80


def mouseclick(pos):
    """Define game behaviour on mouse click input"""
    global state_counter, turn_counter, list_pos
    x = (list_pos[0] / 80) * 80
    state_counter += 1
    if state_counter < 2:
        turn_counter += 1
    if state_counter == 2:
        # determines selected cards
        t_counter = 0
        char = []
        for item in cards_dict.items():
            if item[1][1] == True:
                t_counter += 1
                char.append(item[1][0])
        # determines if selected cards are matched correctly
        if t_counter == 2 and char[0] == char[1]:
            for item in cards_dict.items():
                if item[1][1] == True:
                    item[1][3] = 1
        # reset everything apart from the correctly guessed cards
        state_counter = 0
        true_count = 0
        for item in cards_dict.items():
            item[1][1] = False
    list_pos = list(pos)


def determine_card(list_pos):
    if list_pos[1] > 80:
        return list_pos[0] / 80 - 1
    else:
        return list_pos[0] / 80 - 1


def draw(canvas):
    """Logic for drawing the game on the canvas"""
    for item in cards_dict.items():
        if item[1][1] == True or item[1][3] == 1:
            canvas.draw_image(item[1][0], (40, 40), (80, 80), (item[1][2][0] + 40, item[1][2][1] + 40), (80, 80))
        if list_pos[0] in range(item[1][2][0], item[1][2][2]) and list_pos[1] in range(item[1][2][3]):
            item[1][1] = True
    count = 0
    for x in range(17):
        canvas.draw_line((count, 0), (count, count + 80), 5, 'Yellow')
        count += 80
    #label.set_text("Turns = " + str(turn_counter))


def run():
    """Run the game"""
    frame = simplegui.create_frame("Memory", 1280, 80)
    frame.add_button("Reset", new_game)
    #label = frame.add_label("Turns = 0")

    frame.set_mouseclick_handler(mouseclick)
    frame.set_draw_handler(draw)

    new_game()
    frame.start()