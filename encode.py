import sys
from dgr_format import write_header
from dgr_codec import encode_bytes

inp, out = sys.argv[1], sys.argv[2]

raw = open(inp, "rb").read()
compressed = encode_bytes(raw)

with open(out, "wb") as f:
    write_header(f, len(raw))
    f.write(compressed)

print("Encoded:", inp, "->", out)
