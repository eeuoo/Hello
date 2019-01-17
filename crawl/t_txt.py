data = 100

with open("test.txt", "w") as f:
    f.write(str(data))

with open("text.bin", "wb") as f:
    f.write(bytearray([data]))
