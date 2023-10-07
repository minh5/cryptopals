from base64 import b16decode
from base64 import b64encode

TEST_VAL = b"49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
TEST_OUTPUT = b"SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

def convert_hex_to_bas64(text: bytes) -> bytes:
    decoded = b16decode(text, casefold=True)
    return b64encode(decoded)

print(TEST_VAL)
print(convert_hex_to_bas64(TEST_VAL))
assert convert_hex_to_bas64(TEST_VAL) == TEST_OUTPUT
