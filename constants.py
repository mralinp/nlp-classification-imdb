TRAIN = 0
TEST = 1
VALID = 2

class dataset:
    def __init__(self, addr="", dbName="", rwStatus="r"):
        self.__dbAddr = addr
        self.__dbName = dbName
        self.__rwStatus = rwStatus
        
    def get(self, name):
        if (name == TRAIN):
            return self.__train
        elif (name == TEST):
            return self.__test
        elif(name == VALID):
            return self.__Valid
        
if __name__ == "__main__":
    d = dataset()
    print(d.get(TRAIN))
    