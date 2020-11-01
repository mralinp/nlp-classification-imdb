


if __name__ == '__main__':
    print("hello, world!", __name__)
    ds = open("./data-sets/Test.csv")
    for i in range(2):
        buff = ds.readline()
        print(buff.split(','))
    print("done!")