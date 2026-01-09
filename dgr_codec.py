import zlib

def delta_encode(data: bytes) -> bytes:
    if not data:
        return b""

    out = bytearray()
    prev = data[0]
    out.append(prev)

    for b in data[1:]:
        out.append((b - prev) % 256)
        prev = b

    return bytes(out)

def delta_decode(data: bytes) -> bytes:
    if not data:
        return b""

    out = bytearray()
    prev = data[0]
    out.append(prev)

    for d in data[1:]:
        b = (prev + d) % 256
        out.append(b)
        prev = b

    return bytes(out)

def encode_bytes(data: bytes) -> bytes:
    transformed = delta_encode(data)
    return zlib.compress(transformed, level=9)

def decode_bytes(data: bytes) -> bytes:
    raw = zlib.decompress(data)
    return delta_decode(raw)
