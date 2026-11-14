# https://github.com/satomshr/atcoder/blob/main/Lib/header_heu.py

import sys
import time

def debug(*args):
    print(*args, file=sys.stderr)

class TimeKeeper:
    def __init__(self, time_limit_sec):
        self.time_limit = time_limit_sec
        self.start_time = time.time()

    def is_time_over(self):
        # 制限時間を超過したか判定
        return (time.time() - self.start_time) >= self.time_limit

    def get_elapsed_time(self):
        # 経過時間（秒）を取得
        return time.time() - self.start_time


sys.setrecursionlimit(2*(10**5)+2)
INF = 9*(10**18)

