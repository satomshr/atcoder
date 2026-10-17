class FastBitSet:
    """
    FastBitSet は、64bit チャンク配列を用いた高速なビット集合クラスです。

    - 管理対象は [0, n) の整数
    - 内部表現は list[int]（各要素が 64bit 分）
    - 集合演算（OR / AND / 差集合）を in-place で高速に実行可能
    - 10^5 ビット規模に対応し、競技プログラミング向け

    Attributes
    ----------
    n : int
        管理する要素の上限（0 以上 n 未満）
    m : int
        64bit チャンク数
    bits : list[int]
        ビット集合の内部表現
    """

    def __init__(self, n: int):
        """
        空のビット集合を生成します。

        Parameters
        ----------
        n : int
            管理する整数の範囲 [0, n)
        """
        self.n = n
        self.m = (n + 63) >> 6
        self.bits = [0] * self.m

    def add(self, i: int):
        """
        要素 i を集合に追加します。

        Parameters
        ----------
        i : int
            追加する要素（0 <= i < n）
        """
        self.bits[i >> 6] |= 1 << (i & 63)

    def remove(self, i: int):
        """
        要素 i を集合から削除します。

        Parameters
        ----------
        i : int
            削除する要素（0 <= i < n）
        """
        self.bits[i >> 6] &= ~(1 << (i & 63))

    def contains(self, i: int) -> bool:
        """
        要素 i が集合に含まれているかを判定します。

        Parameters
        ----------
        i : int
            判定する要素（0 <= i < n）

        Returns
        -------
        bool
            含まれていれば True、そうでなければ False
        """
        return ((self.bits[i >> 6] >> (i & 63)) & 1) == 1

    def count(self) -> int:
        """
        集合に含まれる要素数（立っているビット数）を返します。

        Returns
        -------
        int
            ビットが 1 になっている要素の個数
        """
        s = 0
        for x in self.bits:
            s += x.bit_count()
        return s

    def or_eq(self, other: "FastBitSet"):
        """
        他の集合との和集合を in-place で計算します。
        self ← self ∪ other

        Parameters
        ----------
        other : FastBitSet
            和集合を取る相手
        """
        for i in range(self.m):
            self.bits[i] |= other.bits[i]

    def and_eq(self, other: "FastBitSet"):
        """
        他の集合との積集合を in-place で計算します。
        self ← self ∩ other

        Parameters
        ----------
        other : FastBitSet
            積集合を取る相手
        """
        for i in range(self.m):
            self.bits[i] &= other.bits[i]

    def sub_eq(self, other: "FastBitSet"):
        """
        他の集合との差集合を in-place で計算します。
        self ← self \\ other

        Parameters
        ----------
        other : FastBitSet
            差を取る相手
        """
        for i in range(self.m):
            self.bits[i] &= ~other.bits[i]

    def intersects(self, other: "FastBitSet") -> bool:
        """
        他の集合と共通要素が存在するかを判定します。

        Parameters
        ----------
        other : FastBitSet
            判定する相手

        Returns
        -------
        bool
            共通要素があれば True
        """
        for i in range(self.m):
            if self.bits[i] & other.bits[i]:
                return True
        return False

    def any(self) -> bool:
        """
        集合が空でないかを判定します。

        Returns
        -------
        bool
            少なくとも 1 要素含まれていれば True
        """
        for x in self.bits:
            if x:
                return True
        return False

    def clear(self):
        """
        集合を空にします。
        """
        for i in range(self.m):
            self.bits[i] = 0
