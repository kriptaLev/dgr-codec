MAGIC = b"DGR1"

def write_header(f, size):
    f.write(MAGIC)
    f.write(size.to_bytes(8, "big"))

def read_header(f):
    if f.read(4) != MAGIC:
        raise ValueError("Not DGR")
    return int.from_bytes(f.read(8), "big")
