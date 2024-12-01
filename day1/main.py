firstList = []
secondList = []

def part1():
    f= open("input.txt", "r").read().splitlines()
    for line in f:
        firstList.append(line[0:5])
        secondList.append(line[8:13])
    firstList.sort()
    secondList.sort()
    total = 0
    for i in range(len(firstList)):
        total += abs(int(firstList[i])-int(secondList[i]))
    print(total)

def part2():
    total = 0
    for i in range(len(firstList)):
        total += int(firstList[i]) * secondList.count(firstList[i])
    print(total)

if __name__ == '__main__':
    part1()
    part2()