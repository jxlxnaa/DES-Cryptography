import math
import textwrap

#mawi
initial_perm = [58, 50, 42, 34, 26, 18, 10, 2,
                60, 52, 44, 36, 28, 20, 12, 4,
                62, 54, 46, 38, 30, 22, 14, 6,
                64, 56, 48, 40, 32, 24, 16, 8,
                57, 49, 41, 33, 25, 17, 9, 1,
                59, 51, 43, 35, 27, 19, 11, 3,
                61, 53, 45, 37, 29, 21, 13, 5,
                63, 55, 47, 39, 31, 23, 15, 7]

def str2bin(plain_text: str) -> str:
    return ''.join(format(ord(i), '08b') for i in plain_text)

def split_binary_text(bin_text: str) -> list:
    bytes: list =  textwrap.wrap(bin_text, 64)
    bytes[-1] = bytes[-1] + (64-len(bytes[-1]))*"0"
    return bytes

def initial_permutation(byte_sequence: str):
    new_bytes = ["0" for _ in range(len(initial_perm))]
    for i in range(len(initial_perm)):
        new_bytes[i] = byte_sequence[initial_perm[i] - 1]

    return "".join(new_bytes)

def main():
    plain_text: str = "Jelena je lepa"
    byte_sequences: list = split_binary_text(str2bin(plain_text))
    print(byte_sequences)
    byte_permutation: map = list(map(initial_permutation, byte_sequences))
        

main()
