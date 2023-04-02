def switch_bytes(num: int) -> int | None:
    if num > 2**16 - 1 or num < 255 or isinstance(num, float):
        print("Число не 2-x байтное")
        return
    b1 = num >> 8
    b2 = num & 255
    res = b2 << 8 | b1
    print(bin(num))
    print(bin(res))
    return res


print(switch_bytes(15))  # -> None
print(switch_bytes(2**16))  # -> None
print(switch_bytes(451))  # -> 49921 num: 0b1|11000011, res: 0b11000011|00000001
print(switch_bytes(2**13))  # -> 32 num: 0b100000|00000000 res:0b100000
print(switch_bytes(53943))  # -> 47058 num: 0b11010010|10110111 res: 0b10110111|11010010
print(switch_bytes(9988))  # -> 1063 num: 0b100111|00000100, res: 0b100|00100111
