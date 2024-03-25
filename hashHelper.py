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


def calculate_hash_collision(files_directory='test-files', output_file='hash_output.txt'):
    directory_hashes = compute_directory_hashes(files_directory)
    dump_hashes_to_file(directory_hashes, output_file)
    check_for_collisions(directory_hashes)


def create_collision(file_name='test-files/5.txt', output_file='hash_output.txt'):
    # read the original hash values from the file
    with open(output_file, 'r') as file:
        original_hashes = file.readlines()

    # Extract the hash values
    original_hashes = [int(hash_value.split(': ')[1]) for hash_value in original_hashes]

    #  Circular left shift by 4 bits for the first hash
    circular_shifted_first_hash = circular_left_shift(original_hashes[0], 4)

    # Calculate the XOR of the original hash values
    xored_hash = circular_shifted_first_hash
    for hash_value in original_hashes[1:]:
        xored_hash ^= hash_value

    # Write the bytes corresponding to the XORed hash value into 5.txt
    with open(file_name, 'ab') as file:
        # Convert the XORed hash value to bytes
        xored_hash_bytes = xored_hash.to_bytes(4, byteorder='big')
        # Append the bytes to 5.txt
        file.write(xored_hash_bytes)
