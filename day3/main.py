f = open("input.txt", "r").read().splitlines()

def part1():
    total = 0
    for line in f:
        l = line.split("mul(")
        for l2 in l:
            l2 = l2.split(")")[0]
            l2 = l2.split(",")
            if 1 <= len(l2[0]) <= 3 and 1 <= len(l2[1]) <= 3 and l2[0].isnumeric() and l2[1].isnumeric() and len(l2) == 2:
                total += int(l2[0])*int(l2[1])
    print(total)

def part2():
    total = 0
    can_mul = True
    for line in f:
        l = line.split("mul(")
        for l2 in l:
            do_index = l2.find("do()")
            dont_index = l2.find("don't()")
            l2 = l2.split(")")[0]
            l2 = l2.split(",")
            if 1 <= len(l2[0]) <= 3 and 1 <= len(l2[1]) <= 3 and l2[0].isnumeric() and l2[1].isnumeric() and len(l2) == 2 and can_mul:
                total += int(l2[0])*int(l2[1])
            if do_index != -1 and dont_index != -1:
                can_mul = do_index > dont_index
            elif do_index != -1:
                can_mul = True
            elif dont_index != -1:
                can_mul = False
    print(total)


if __name__ == "__main__":
    part1()
    part2()