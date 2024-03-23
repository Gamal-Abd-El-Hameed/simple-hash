import os


class SimpleHash:
    def __init__(self):
        self.hash = 0

    def update(self, byte):
        # Circularly shift left by 4 bits
        self.hash = ((self.hash << 4) | (self.hash >> (32 - 4)))
        # Mask to 32 bits
        self.hash = self.hash & 0xFFFFFFFF
        # XOR with byte
        self.hash = self.hash ^ byte


def compute_file_hash(filename):
    hash_obj = SimpleHash()
    with open(filename, 'rb') as file:
        byte = file.read(1)
        while byte:
            hash_obj.update(ord(byte))
            byte = file.read(1)
    return hash_obj.hash


def compute_directory_hashes(directory):
    hashes = {}
    for filename in os.listdir(directory):
        file = os.path.join(directory, filename)
        if os.path.isfile(file):
            hash_value = compute_file_hash(file)
            hashes[filename] = hash_value
    return hashes


def dump_hashes_to_file(hashes, output_file):
    with open(output_file, 'w') as file:
        for filename, hash_value in hashes.items():
            file.write(f"{filename}: {hash_value}\n")


def check_for_collisions(hashes):
    collision_detected = False
    seen_hashes = set()
    for filename, hash_value in hashes.items():
        if hash_value in seen_hashes:
            collision_detected = True
            print(f"Collision detected for files: {filename} and another file")
        seen_hashes.add(hash_value)
    if not collision_detected:
        print("No collisions detected.")


# Example usage
directory_hashes = compute_directory_hashes('test-files')
dump_hashes_to_file(directory_hashes, 'hash_output.txt')
check_for_collisions(directory_hashes)
