import zlib

def encode_bytes(data: bytes) -> bytes:
    return zlib.compress(data, level=9)

def decode_bytes(data: bytes) -> bytes:
    return zlib.decompress(data)
