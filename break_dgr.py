# break_dgr.py
with open("test3.dgr", "rb") as f:
    data = bytearray(f.read())

# удаляем несколько байт в середине
mid = len(data) // 2
del data[mid:mid+5]

with open("test3_broken.dgr", "wb") as f:
    f.write(data)

print("File broken: test3_broken.dgr")
