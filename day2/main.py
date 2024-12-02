f = open("input.txt", "r").read().splitlines()

def validate_line(l):
    increase = int(l[0]) - int(l[1])
    for i in range(len(l) - 1):
        x = (int(l[i]) - int(l[i + 1]))
        if increase > 0 and 0 < x <= 3:
            continue
        elif increase < 0 and 0 > x >= -3:
            continue
        else:
            return False
    return True

def part1():
    total=0
    for line in f:
        l = line.split(" ")
        if validate_line(l):
            total += 1
    print(total)

def part2():
    total=0
    for line in f:
        l = line.split(" ")
        valid = validate_line(l)
        if not valid:
            for i in range(len(l)):
                l2 = l.copy()
                l2.pop(i)
                if validate_line(l2):
                    valid = True
                    break
        if valid:
            total += 1
    print(total)


if __name__ == "__main__":
    part1()
    part2()