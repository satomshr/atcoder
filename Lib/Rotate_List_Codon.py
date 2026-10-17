from pprint import pprint

from typing import List

def rotate0(board: List[List[str]]) -> List[List[str]]:
    return board

def rotate90(board: List[List[str]]) -> List[List[str]]:
    n_rows = len(board)
    n_cols = len(board[0]) if n_rows > 0 else 0
    rotated: List[List[str]] = []

    for j in range(n_cols):
        new_row: List[str] = []
        for i in range(n_rows - 1, -1, -1):
            new_row.append(board[i][j])
        rotated.append(new_row)
    return rotated

def rotate180(board: List[List[str]]) -> List[List[str]]:
    n_rows = len(board)
    rotated: List[List[str]] = []

    for i in range(n_rows - 1, -1, -1):  # 行を逆順に
        row = board[i]
        new_row: List[str] = []
        for j in range(len(row) - 1, -1, -1):  # 列も逆順に
            new_row.append(row[j])
        rotated.append(new_row)

    return rotated

def rotate270(board: List[List[str]]) -> List[List[str]]:
    n_rows = len(board)
    n_cols = len(board[0]) if n_rows > 0 else 0
    rotated: List[List[str]] = []

    for j in range(n_cols - 1, -1, -1):  # 右端の列から左へ
        new_row: List[str] = []
        for i in range(n_rows):          # 上から下へ
            new_row.append(board[i][j])
        rotated.append(new_row)
    return rotated

def rotate(board: List[List[str]], m: int) -> List[List[str]]:
    m = m % 4
    if m == 0:
        return rotate0(board)
    elif m == 1:
        return rotate90(board)
    elif m == 2:
        return rotate180(board)
    else:
        return rotate270(board)


# 元の盤面
example: list = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

print("時計回りに90度回転させた結果")
result: list = rotate(example, 1)
pprint(result, width=20)
print()

print("時計回りに180度回転させた結果")
result: list = rotate(example, 2)
pprint(result, width=20)
print()

print("時計回りに270度回転させた結果")
result: list = rotate(example, 3)
pprint(result, width=20)

