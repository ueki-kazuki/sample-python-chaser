#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
全国高校生プログラミングコンテスト CHaser 2012 ステップアップヒント 2
http://www.zenjouken.com/?action=common_download_main&upload_id=522
"""

import CHaser
from enum import Enum

class Mode(Enum):
    Down = 1
    RIGHT = 2
    UP = 3
    LEFT = 4

def main():
    client = CHaser.Client()

    mode = Mode.Down
    value = []
    while True:
        value = client.get_ready()

        if mode == Mode.Down:
            if value[7] != 2:
                value = client.walk_down()
                print("WD: {}".format(value))
            else:
                mode = Mode.RIGHT

        if mode == Mode.RIGHT:
            if value[5] != 2:
                value = client.walk_right()
                print("WR: {}".format(value))
            else:
                mode = Mode.UP

        if mode == Mode.UP:
            if value[1] != 2:
                value = client.walk_up()
                print("WU: {}".format(value))
            else:
                mode = Mode.LEFT

        if mode == Mode.LEFT:
            if value[3] != 2:
                value = client.walk_left()
                print("WL: {}".format(value))
            else:
                value = client.search_down()
                print("SD: {}".format(value))
                mode = Mode.Down

if __name__ == "__main__":
    main()
