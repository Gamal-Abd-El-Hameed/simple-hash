def circular_left_shift(val, shift):
    return ((val << shift) | (val >> (32 - shift))) & 0xFFFFFFFF


def split_bytes_to_nibbles(byte_array):
    nibbles = []
    for byte in byte_array:
        high_nibble = byte >> 4
        low_nibble = byte & 0x0F
        nibbles.extend([high_nibble, low_nibble])
    return nibbles
