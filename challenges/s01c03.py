from collections import Counter
from typing import Any
from typing import List

from s01c02 import xor_op

EXAMPLE = bytes.fromhex("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")

def heuristic(plaintext: str) -> float:
    """
    Lazy heuristic to figure out if its vernacular english by comparing the ratio
    of non-alphanumeric characters to alphanumeric ones.
    """
    counts = Counter([i.isalpha() for i in str(plaintext)])
    return counts[True]/counts[False]


# typing Any because mypy assumes lists to contain homogenous elements
def decipher(ciphertext: bytes) -> List[List[Any]]:
    results = []
    for i in range(256):
        key = bytes([i]) * len(ciphertext)
        plaintext = xor_op(key, ciphertext)
        score = heuristic(str(plaintext))
        results.append([i, plaintext, score])

    results.sort(key=lambda x: x[2], reverse=True)

    return results[:5]

results = decipher(EXAMPLE)
for i in results:
    print(f"key used: {i[0]}, decoded text: {i[1]}, score: {i[2]}")
