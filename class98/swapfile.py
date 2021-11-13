def swapFileData():
    file=input("file number: ")
    twofiletwofurious=input("file number: ")

    with open(file, "r") as a:
        data_a = a.read()

    with open(twofiletwofurious, "r") as b:
        data_b = b.read()

    with open(file, "w") as a:
        a.write(data_b)

    with open(twofiletwofurious, "w") as b:
        b.write(data_a)

swapFileData()