import re
import utils

def day2_1():
    content = utils.readFile("./day2.txt")

    ans = 0
    colorDict = {"red": 12, "green": 13, "blue": 14}

    for line in content:
        id, game = line.split(": ")
        id = int(id.split(" ")[1])
        notAdd = False
        for batch in re.split('; |, ', game):
            number, color = int(batch.split(" ")[0]), batch.split(" ")[1]
            if number > colorDict[color]:
                notAdd = True
                break
        if not notAdd:
            ans += id

    return ans

# print(day2_1())

def day2_2():
    content = utils.readFile("./day2.txt")
    ans = 0

    for line in content:
        id, game = line.split(": ")
        id = int(id.split(" ")[1])
        colorDict = {"red": 0, "green": 0, "blue": 0}

        for batch in re.split('; |, ', game):
            number, color = int(batch.split(" ")[0]), batch.split(" ")[1]
            if number > colorDict[color]:
                colorDict[color] = number
        
        power = 1
        for v in colorDict.values():
            power *= v
        ans += power

    return ans

print(day2_2())