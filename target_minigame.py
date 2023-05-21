import keyboard
import time
import random

def game_func(trials):
    print('Press SPACE to shoot small game when the arrow changes to >>-<<.')
    target_line = "====>"
    target_position = 0
    terminal_width = 80
    attempts = 0
    hits = 0
    lenience = 5
    while attempts < trials:
        target_position = (target_position + .002) % terminal_width
        target_line = '>>-<<' if target_position < terminal_width/2+lenience and target_position > terminal_width/2-lenience else '====>'
        line = " " * int(target_position) + target_line
        print(line,end='\r')
        if keyboard.is_pressed("space"):
            attempts += 1
            if target_position < terminal_width/2+lenience and target_position > terminal_width/2-lenience:
                print('Hit!')
                hits += 1
            else:
                print('Miss')
            time.sleep(1)
            target_position = 0
    return hits
if __name__ == '__main__':
    game_func(5)
