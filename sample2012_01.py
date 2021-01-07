#!/usr/bin/env python
# -*- coding: utf-8 -*-

import CHaser

def main():
    client = CHaser.Client()

    value = []
    while True:
        value = client.get_ready()
        value = client.search_up()

        value = client.get_ready()
        value = client.search_right()

        value = client.get_ready()
        value = client.search_down()

        value = client.get_ready()
        value = client.search_left()


if __name__ == "__main__":
    main()
