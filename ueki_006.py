#!/usr/bin/env python

import CHaser

UP = 1
LEFT = 3
RIGHT = 5
DOWN = 7

NONE = 0
ENEMY = 1
BLOCK = 2
ITEM = 3

def main():
    value = []
    client = CHaser.Client()

    zenkai = ""

    while(True):
        value = client.get_ready()

        if zenkai != "":
            if zenkai == DOWN:
                client.put_down()
            elif zenkai == UP:
                client.put_up()
            elif zenkai == RIGHT:
                client.put_right()
            elif zenkai == LEFT:
                client.put_left()

            zenkai = ""
            continue

        if value[DOWN] == ENEMY:
            value = client.put_down()
        elif value[RIGHT] == ENEMY:
            value = client.put_right()
        elif value[UP] == ENEMY:
            value = client.put_up()
        elif value[LEFT] == ENEMY:
            value = client.put_left()
        else:
            if value[DOWN] == ITEM:
                value = client.walk_down()
            elif value[RIGHT] == ITEM:
                value = client.walk_right()
            elif value[UP] == ITEM:
                value = client.walk_up()
            elif value[LEFT] == ITEM:
                value = client.walk_left()
            else:
                if value[DOWN] != BLOCK:
                    value = client.walk_down()
                    zenkai = UP
                elif value[RIGHT] != BLOCK:
                    value = client.walk_right()
                    zenkai = LEFT
                elif value[UP] != BLOCK:
                    value = client.walk_up()
                    zenkai = DOWN
                else:
                    value = client.walk_left()
                    zenkai = RIGHT


if __name__ == "__main__":
    main()
