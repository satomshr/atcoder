'''
座標圧縮 (coordinate compression)
'''
def compress(values):
    unique = sorted(set(values))
    value_to_index = {v: i for i, v in enumerate(unique)}
    index_to_value = {i: v for i, v in enumerate(unique)}
    compressed = [value_to_index[v] for v in values]
    return compressed, value_to_index, index_to_value

A = [100, 300, 1000, 300]
compressed, to_idx, to_val = compress(A)
print("圧縮後:", compressed)           # [0, 1, 2, 1]
print("元に戻す:", [to_val[i] for i in compressed])  # [100, 300, 1000, 300]
