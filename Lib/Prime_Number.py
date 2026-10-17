import math

def build_prime(n: int):
    '''
    0 から n までのリストを返す. True なら素数, False なら素数ではない
    '''
    is_prime = [True] * (n + 1)
    is_prime[0], is_prime[1] = False, False
    i = 2
    while i * i <= n:
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

        i += 1

    return is_prime


def build_spf(n: int) -> list[int]:
    '''
    0 から n までの最小素因数を求める
    spf[x] = x の最小素因数
    '''
    spf = [i for i in range(n + 1)] # 自身が初期値

    i = 2
    while i * i <= n:
        if spf[i] == i:  # i が素数
            j = i * i
            while j <= n:
                if spf[j] == j:
                    spf[j] = i
                j += i
        i += 1

    return spf


def factorize(x: int, spf: list[int]) -> list[tuple[int, int]]:
    '''
    素因数分解
    '''
    res = []
    while x > 1:
        p = spf[x]
        cnt = 0
        while x > 1 and spf[x] == p:
            x //= p
            cnt += 1
        res.append((p, cnt))
    return res


def divisor(n: int) -> list[int]:
    '''
    約数列挙
    '''
    l = []
    r = []

    i = 1
    while i * i <= n:
        if n % i == 0:
            l.append(i)

            if i * i != n:
                r.append(n // i)

        i += 1

    return l + r[::-1]
