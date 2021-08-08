import CHaser # 同じディレクトリに CHaser.py がある前提

上 = 1
左 = 3
右 = 5
下 = 7

敵 = 1
壁 = 2
宝 = 3

def main():
    value = [] # フィールド情報を保存するリスト
    client = CHaser.Client() # サーバーと通信するためのインスタンス

    # 前回位置を保存する変数
    zenkai = ""

    while(True):
        # 前回いた位置にブロックを置く
        if zenkai:
            value = client.get_ready()
            if zenkai == 上:
                value = client.put_down()
            elif zenkai == 左:
                value = client.put_left()
            elif zenkai == 下:
                value = client.put_down()
            elif zenkai == 右:
                value = client.put_left()

        # 壁がなければそこに移動する
        # 下右上左の順に壁のありなしをしらべる
        value = client.get_ready()
        if value[下] != 壁:
            value = client.walk_down()
            zenkai = 下
        elif value[右] != 壁:
            value = client.walk_right()
            zenkai = 右
        elif value[上] != 壁:
            value = client.walk_up()
        else:
            value = client.walk_left()

"""
python sample.py のようにこのファイルを直接実行すると，
__name__ は "__main__" となる．これを利用して main() を実行する．
"""
if __name__ == "__main__":
    main()