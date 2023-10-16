import binascii
from itertools import cycle
from itertools import islice

from s01c02 import xor_op


INPUT_TEXT = (
    b"Burning 'em, if you ain't quick and nimble\n"
    b"I go crazy when I hear a cymbal"
)
EXPECTED_OUTPUT = (
    b"0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272"
    b"a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
)

def repeated_text_xor(input_text: bytes, key_text: str) -> bytes:
    """
    Using XOR on an input byte stream using a text as a key which will
    repeat for the length of the input byte stream
    """
    key_prep = islice(cycle(key_text), len(input_text))
    xor_key = bytes("".join(key_prep).encode())
    results = xor_op(input_text, xor_key)
    return results


try:
    encrypted = repeated_text_xor(INPUT_TEXT, "ICE")
    assert binascii.hexlify(encrypted) == EXPECTED_OUTPUT
except:
    import ipdb; ipdb.post_mortem()
