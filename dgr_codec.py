import zlib
import hashlib

# ---------- DELTA ----------

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

# ---------- CORE ----------

def encode_bytes(data: bytes) -> bytes:
    # 1. считаем отпечаток оригинала
    checksum = hashlib.sha256(data).digest()

    # 2. улучшаем сжимаемость
    transformed = delta_encode(data)

    # 3. сжимаем
    compressed = zlib.compress(transformed, level=9)

    # 4. формат: [checksum][compressed]
    return checksum + compressed


def decode_bytes(data: bytes) -> bytes:
    # 1. отделяем отпечаток
    checksum_stored = data[:32]
    compressed = data[32:]

    # 2. распаковываем
    transformed = zlib.decompress(compressed)
    raw = delta_decode(transformed)

    # 3. проверяем целостность
    checksum_now = hashlib.sha256(raw).digest()

    if checksum_now != checksum_stored:
        raise ValueError("DGR ERROR: file is corrupted")

    return raw    raw = zlib.decompress(data)
    return delta_decode(raw)
