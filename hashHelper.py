import os

from SimpleHash import *
from utils import *


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


def print_hash_values(directory_hashes):
    for filename, hash_value in directory_hashes.items():
        print(f"{filename}: {hash_value}")


def calculate_hash_collision(files_directory='test-files', output_file='hash_output.txt'):
    directory_hashes = compute_directory_hashes(files_directory)
    dump_hashes_to_file(directory_hashes, output_file)
    print_hash_values(directory_hashes)
    check_for_collisions(directory_hashes)


def create_collision(target='test-files/5.txt', collided='test-files/4.txt'):
    target_hash_value = 0
    if os.path.isfile(target):
        target_hash_value = compute_file_hash(target)

    collied_hash_value = 0
    if os.path.isfile(collided):
        collied_hash_value = compute_file_hash(collided)

    split_1 = split_bytes_to_nibbles(target_hash_value.to_bytes(4, byteorder='big'))
    split_1 = bytes(split_1)

    split_2 = split_bytes_to_nibbles(collied_hash_value.to_bytes(4, byteorder='big'))
    split_2 = bytes(split_2)
    # Write the bytes corresponding to the XORed hash value into 5.txt

    with open(target, 'ab') as file:
        file.write(split_1)
        file.write(split_2)
