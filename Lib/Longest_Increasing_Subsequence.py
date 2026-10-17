# https://qiita.com/python_walker/items/d1e2be789f6e7a0851e5

import bisect

def Longest_Increasing_Subsequence(lst):
    LIS = [lst[0]]

    for i in range(len(lst)):
        if lst[i] > LIS[-1]:
            LIS.append(lst[i])
        else:
            LIS[bisect.bisect_left(LIS, lst[i])] = lst[i]

    return(len(LIS))

A = [1, 3, 5, 4, 2, 6]
print(Longest_Increasing_Subsequence(A))
