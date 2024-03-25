from utils import *


class SimpleHash:
    def __init__(self):
        self.hash = 0

    def update(self, byte):
        # Circularly shift left by 4 bits
        self.hash = circular_left_shift(self.hash, 4)
        # XOR with byte
        self.hash = self.hash ^ byte
