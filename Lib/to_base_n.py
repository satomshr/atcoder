def to_base_n(num: int, base: int) -> str:
    """
    10進数の正の整数 num を n進数 (2 <= base <= 9) に変換して文字列として返す。
    """
    if not (2 <= base <= 9):
        raise ValueError("基数は2以上9以下でなければなりません。")
    if num <= 0:
        raise ValueError("正の整数を指定してください。")

    digits = []
    while num > 0:
        digits.append(str(num % base))
        num //= base

    return ''.join(reversed(digits))

