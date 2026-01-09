import zlib
import struct

MAGIC = b"DGR1"


def encode_bytes(data: bytes) -> bytes:
    """
    Сжимает байты без потерь
    """
    compressed = zlib.compress(data, level=9)
    return compressed


def decode_bytes(data: bytes) -> bytes:
    """
    Распаковывает байты
    """
    raw = zlib.decompress(data)
    return raw


def pack_dgr(data: bytes) -> bytes:
    """
    Упаковывает данные в формат .dgr
    """
    compressed = encode_bytes(data)
    header = MAGIC + struct.pack(">I", len(data))
    return header + compressed


def unpack_dgr(dgr_data: bytes) -> bytes:
    """
    Распаковывает .dgr обратно в оригинальные байты
    """
    if not dgr_data.startswith(MAGIC):
        raise ValueError("Не DGR файл")

    original_size = struct.unpack(">I", dgr_data[4:8])[0]
    compressed = dgr_data[8:]

    raw = decode_bytes(compressed)

    if len(raw) != original_size:
        raise ValueError("Размер не совпадает, файл повреждён")

    return raw
