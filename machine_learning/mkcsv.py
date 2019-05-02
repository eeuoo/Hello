import struct

def writeCsv(name):

    labelFile = open("./data/" + name + "-labels-idx1-ubyte", "rb")
    imageFile = open("./data/" + name + "-images-idx3-ubyte", "rb")
    csvFile = open("./data/" + name + ".csv", "w", encoding="utf-8")

    magicNo, labelCnt = struct.unpack(">II", labelFile.read(8))
    print("답", magicNo, labelCnt)
    magicNo, imageCnt = struct.unpack(">II", imageFile.read(8))
    print("데이터", magicNo, labelCnt)

    rows, cols = struct.unpack(">II", imageFile.read(8))
    pixels = rows * cols            # 28 X 28

    # for j, x in enumerate(imgdata):
    #     if j % 28 == 0:
    #         print("\n")
    #     print('{:4s}'.format(str(x)), end='')

    # csvFile = open("./data/" + name + ".csv", "w", encoding="utf-8")
    for i in range(labelCnt):
        label = struct.unpack("B", labelFile.read(1))[0]
        imgdata = list(map(lambda b: str(b), imageFile.read(pixels)))
        csvFile.write(str(label) + ",")
        csvFile.write(",".join(imgdata) + "\n")

    labelFile.close()
    imageFile.close()
    csvFile.close()



writeCsv('t10k')
writeCsv('train')