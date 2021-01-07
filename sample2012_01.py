#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
全国高校生プログラミングコンテスト CHaser 2012 ステップアップヒント 1
http://www.zenjouken.com/?action=common_download_main&upload_id=491
"""

import CHaser

def main():
    client = CHaser.Client()

    value = []
    while True:
        value = client.get_ready()
        print("GR: {}".format(value))
        value = client.search_up()
        print("SU: {}".format(value))

        value = client.get_ready()
        print("GR: {}".format(value))
        value = client.search_right()
        print("SR: {}".format(value))

        value = client.get_ready()
        print("GR: {}".format(value))
        value = client.search_down()
        print("SD: {}".format(value))

        value = client.get_ready()
        print("GR: {}".format(value))
        value = client.search_left()
        print("SL: {}".format(value))


if __name__ == "__main__":
    main()
