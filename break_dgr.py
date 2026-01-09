with open("test3.dgr", "rb") as f:
    data = bytearray(f.read())

print("Original size:", len(data))

# ломаем файл: удаляем 5 байт из середины
mid = len(data) // 2
del data[mid:mid+5]

with open("test3_broken.dgr", "wb") as f:
    f.write(data)

print("Broken file written: test3_broken.dgr")
print("New size:", len(data))
