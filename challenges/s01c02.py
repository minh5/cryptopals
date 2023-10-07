FIRST_INPUT = bytes.fromhex("1c0111001f010100061a024b53535009181c")
SECOND_INPUT = bytes.fromhex("686974207468652062756c6c277320657965")
OUTPUT = bytes.fromhex("746865206b696420646f6e277420706c6179")

def xor_op(first_input: bytes, second_input: bytes) -> bytes:
    return bytes([a ^ b for a, b in zip(first_input, second_input)])

assert xor_op(FIRST_INPUT, SECOND_INPUT) == OUTPUT
