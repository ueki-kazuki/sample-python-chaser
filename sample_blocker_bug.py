import CHaser  # 同じディレクトリに CHaser.py がある前提

UP = 1
LEFT = 3
RIGHT = 5
DOWN = 7

ENEMY = 1
BLOCK = 2
ITEM = 3


def main():
    value = []  # フィールド情報を保存するリスト
    client = CHaser.Client()  # サーバーと通信するためのインスタンス

    # 前回位置を保存する変数
    zenkai = ""

    while(True):
        # 前回いた位置にブロックを置く
        if zenkai:
            value = client.get_ready()
            if zenkai == UP:
                value = client.put_down()
            elif zenkai == LEFT:
                value = client.put_left()
            elif zenkai == DOWN:
                value = client.put_down()
            elif zenkai == RIGHT:
                value = client.put_left()

        # 壁がなければそこに移動する
        # 下右上左の順に壁のありなしをしらべる
        value = client.get_ready()
        if value[DOWN] != BLOCK:
            value = client.walk_down()
            zenkai = DOWN
        elif value[RIGHT] != BLOCK:
            value = client.walk_right()
            zenkai = RIGHT
        elif value[UP] != BLOCK:
            value = client.walk_up()
        else:
            value = client.walk_left()


"""
python sample.py のようにこのファイルを直接実行すると，
__name__ は "__main__" となる．これを利用して main() を実行する．
"""
if __name__ == "__main__":
    main()
