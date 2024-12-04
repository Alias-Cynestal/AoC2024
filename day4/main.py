f = open("input.txt", "r").read().splitlines()
array = []

def checkAllDirections(x, y):
    total = 0
    total += int(checkInDirection(x, y, 1, 0))
    total += int(checkInDirection(x, y, 0, 1))
    total += int(checkInDirection(x, y, -1, 0))
    total += int(checkInDirection(x, y, 0, -1))
    total += int(checkInDirection(x, y, -1, 1))
    total += int(checkInDirection(x, y, 1, -1))
    total += int(checkInDirection(x, y, -1, -1))
    total += int(checkInDirection(x, y, 1, 1))
    return total

def checkInDirection(baseX, baseY, x,y):
    if baseY + y*3 < 0 :
        return False
    if baseX + x*3 < 0 :
        return False
    try:
        return array[baseX + x][baseY + y] == "M" and array[baseX + x*2][baseY + y*2] == "A" and array[baseX + x*3][baseY + y*3] == "S"
    except IndexError:
        return False

def checkMas(x, y):
    total = 0
    if x + 2 < len(array) and y + 2 < len(array[0]) :
        total += int(array[x][y + 2] == "S" and array[x + 2][y + 2] == "S" and array[x + 2][y] == "M" and array[x+1][y+1] == "A")
    if x + 2 < len(array) and y - 2 >= 0:
        total += int(array[x][y - 2] == "M" and array[x + 2][y - 2] == "S" and array[x + 2][y] == "S" and array[x + 1][y - 1] == "A")
    if x - 2 >= 0 and y + 2 < len(array[0]) :
        total += int(array[x][y + 2] == "M" and array[x - 2][y + 2] == "S" and array[x - 2][y] == "S" and array[x - 1][y + 1] == "A")
    if x - 2 >= 0 and y - 2 >= 0:
        total += int(array[x][y - 2] == "S" and array[x - 2][y - 2] == "S" and array[x - 2][y] == "M" and array[x - 1][y - 1] == "A")
    return total

def part1():
    total = 0
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == 'X':
                total += checkAllDirections(i, j)
    print(total)

def part2():
    total = 0
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == 'M':
                total += checkMas(i, j)
    print(total)

if __name__ == "__main__":
    for line in f:
        array.append(list(line))
    part1()
    part2()