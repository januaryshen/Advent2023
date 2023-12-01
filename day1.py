import re

def day1_1():
    f = open("./day1.txt", "r")
    content = f.readlines()
    ans = 0
    for line in content:
        l = 0
        r = len(line) - 1
        curNum = ""
        while l <= r:
            if line[l].isdigit():
                curNum += line[l]
                break
            l += 1

        while l <= r:
            if line[r].isdigit():
                curNum += line[r]
                break
            r -= 1
        # print(curNum)
        ans += int(curNum)

    return ans

# print(day1_1())

def day1_2():
    f = open("./day1.txt", "r")
    content = f.readlines()
    numDict = {"one": "1", "two":"2", "three":"3", "four":"4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    ans = 0
    for line in content:

        n = len(line)
        l = 0
        r = n - 1
        curNum = ""

        while l <= r:
            if line[l].isdigit():
                curNum += line[l]
                break
            elif l + 5 < n and line[l:l + 5] in numDict.keys():
                curNum += numDict[line[l:l + 5]]
                break
            elif l + 4 < n and line[l:l + 4] in numDict.keys():
                curNum += numDict[line[l:l + 4]]
                break
            elif l + 3 < n and line[l:l + 3] in numDict.keys():
                curNum += numDict[line[l:l + 3]]
                break            
            l += 1

        while l <= r:
            if line[r].isdigit():
                curNum += line[r]
                break
            elif r + 5 < n and line[r:r + 5] in numDict.keys():
                curNum += numDict[line[r:r + 5]]
                break
            elif r + 4 < n and line[r:r + 4] in numDict.keys():
                curNum += numDict[line[r:r + 4]]
                break
            elif r + 3 < n and line[r:r + 3] in numDict.keys():
                curNum += numDict[line[r:r + 3]]
                break             
            r -= 1
        ans += int(curNum)

    return ans

print(day1_2())