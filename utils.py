def circular_left_shift(val, shift):
    return ((val << shift) | (val >> (32 - shift))) & 0xFFFFFFFF
