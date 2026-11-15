
from bisect import bisect_left, bisect_right


def lis_strict(a):
    """狭義単調増加部分列（LIS）を1つ返す。O(N log N)"""
    n = len(a)
    if n == 0:
        return []

    # tails[i] = 長さ i+1 の増加部分列の末尾として最小の値
    tails = []
    tails_idx = []

    # 復元用
    prev = [-1] * n

    for i, x in enumerate(a):
        j = bisect_left(tails, x)

        if j == len(tails):
            tails.append(x)
            tails_idx.append(i)
        else:
            tails[j] = x
            tails_idx[j] = i

        if j > 0:
            prev[i] = tails_idx[j - 1]

    # 復元
    idx = tails_idx[-1]
    ans = []

    while idx != -1:
        ans.append(a[idx])
        idx = prev[idx]

    ans.reverse()
    return ans



def lis_non_strict(a):
    """広義単調増加部分列（LNDS）を1つ返す。O(N log N)"""
    n = len(a)
    if n == 0:
        return []

    tails = []
    tails_idx = []

    # 復元用
    prev = [-1] * n

    for i, x in enumerate(a):
        j = bisect_right(tails, x)

        if j == len(tails):
            tails.append(x)
            tails_idx.append(i)
        else:
            tails[j] = x
            tails_idx[j] = i

        if j > 0:
            prev[i] = tails_idx[j - 1]

    # 復元
    idx = tails_idx[-1]
    ans = []

    while idx != -1:
        ans.append(a[idx])
        idx = prev[idx]

    ans.reverse()
    return ans


a = [3, 1, 2, 2, 5, 4, 4, 6]
print(lis_strict(a))
print(lis_non_strict(a))
