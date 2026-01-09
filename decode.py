import sys
from dgr_format import read_header
from dgr_codec import decode_bytes

inp, out = sys.argv[1], sys.argv[2]

with open(inp, "rb") as f:
    size = read_header(f)
    compressed = f.read()

raw = decode_bytes(compressed)

if len(raw) != size:
    raise ValueError("Corrupted file")

open(out, "wb").write(raw)
print("Decoded:", inp, "->", out)
