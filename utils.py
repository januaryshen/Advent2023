def readFile(path):
    f = open(path, "r")
    content = f.read().splitlines()
    f.close()
    return content