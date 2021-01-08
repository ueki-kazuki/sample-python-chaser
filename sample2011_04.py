#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
全国高校生プログラミングコンテスト CHaser 2012 ステップアップヒント 4
http://www.zenjouken.com/?action=common_download_main&upload_id=533
"""

import CHaser
from enum import Enum, IntEnum

class Mode(Enum):
    Down = 1
    RIGHT = 2
    UP = 3
    LEFT = 4
    ITEM = 20
    ATACK = 90

class Tile(IntEnum):
    ENEMY = 1
    BLOCK = 2
    ITEM = 3

def main():
    client = CHaser.Client()
    turn = 0
    item = 0


    if client.port == 2009:
        cur_mode = Mode.Down
        print("クールで競技サーバに接続しました。")
    else:
        cur_mode = Mode.UP
        print("クールで競技サーバに接続しました。")

    old_mode = Mode.Down

    value = []
    while True:
        turn += 1
        print("\nturn={}、mode={}、item={}".format(turn, cur_mode, item))

        value = client.get_ready()

        if Tile.ENEMY in value[1::2]:
            cur_mode = Mode.ATACK

        if Tile.ITEM in value[1::2]:
            old_mode = cur_mode
            cur_mode = Mode.ITEM

        if cur_mode is Mode.Down:
            if value[7] != Tile.BLOCK:
                value = client.walk_down()
                print("WD: {}".format(value))
            else:
                cur_mode = Mode.RIGHT

        if cur_mode is Mode.RIGHT:
            if value[5] != Tile.BLOCK:
                value = client.walk_right()
                print("WR: {}".format(value))
            else:
                cur_mode = Mode.UP

        if cur_mode is Mode.UP:
            if value[1] != Tile.BLOCK:
                value = client.walk_up()
                print("WU: {}".format(value))
            else:
                cur_mode = Mode.LEFT

        if cur_mode is Mode.LEFT:
            if value[3] != Tile.BLOCK:
                value = client.walk_left()
                print("WL: {}".format(value))
            else:
                value = client.search_down()
                print("SD: {}".format(value))
                cur_mode = Mode.Down

        if cur_mode is Mode.ITEM:
            if value[1] == Tile.ITEM:
                value = client.walk_up()
            elif value[3] == Tile.ITEM:
                value = client.walk_left()
            elif value[5] == Tile.ITEM:
                value = client.walk_right()
            else:
                value = client.walk_down()
            cur_mode = old_mode
            item += 1

        if cur_mode is Mode.ATACK:
            if value[1] == Tile.ENEMY:
                value = client.put_up()
            elif value[3] == Tile.ENEMY:
                value = client.put_left()
            elif value[5] == Tile.ENEMY:
                value = client.put_right()
            else:
                value = client.put_down()
            cur_mode = old_mode

if __name__ == "__main__":
    main()

