import time
import os
from termcolor import colored

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def moving_text_left_to_right(
    text,
    text_color='white',
    highlight_color='on_light_green',
    delay=0.08,
    width=40,
    height=6,
    row=3
):

    for pos in range(-len(text), width + 1):
        clear()
        for h in range(height):
            if h == row:
                line = ''
                for i in range(width):
                    text_index = i - pos
                    if 0 <= text_index < len(text):
                        char = text[text_index]
                        line += colored(char, text_color, highlight_color)
                    else:
                        line += colored(' ', text_color, highlight_color)
                print(line)
            else:
                print()
        time.sleep(delay)

moving_text_left_to_right(
    text="HAPPY EID",
    text_color='yellow',
    highlight_color='on_red',
    delay=0.05,
    width=40,
    height=6,
    row=3
)
