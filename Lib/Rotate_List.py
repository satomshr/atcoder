# https://qiita.com/takenori_ohashi/items/229b80a1dd496f733fa7

from pprint import pprint

def rotate0(board: list) -> list:
    return board

def rotate90(board: list) -> list:
    return [[*row][::-1] for row in zip(*board)]

def rotate180(board: list) -> list:
    return [row[::-1] for row in board[::-1]]

def rotate270(board: list) -> list:
    return [[*row] for row in zip(*board)][::-1]

def rotate(board: list, m: int) -> list:
    return [rotate0, rotate90, rotate180, rotate270][m % 4](board)

# https://note.nkmk.me/python-list-transpose/
def transpose_to_tuple(board: list) -> list:
    return list(zip(*board))

def transpose_to_list(board: list) -> list:
    return [list(x) for x in zip(*board)]


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

print("転地させた結果")
result: list = transpose_to_tuple(example)
pprint(result, width=20)

result: list = transpose_to_list(example)
pprint(result, width=20)
