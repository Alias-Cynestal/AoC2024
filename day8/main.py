from copy import copy

f = open("input.txt", "r").read().splitlines()
antinode_map = []
frequencies = []

class Frequency:

    positions = []
    frequency = ""

    def __init__(self, positions, frenquency):
        self.positions = positions
        self.frequency = frenquency


def part1():
    for freq in frequencies:
        for position in freq.positions:
            for position2 in freq.positions:
                if position[0] == position2[0] and position[1] == position2[1]:
                    continue
                xDelta = position[0] - position2[0]
                yDelta = position[1] - position2[1]
                try:
                        if position[0] + xDelta < 0 or position[1] + yDelta < 0:
                            continue
                        antinode_map[position[0] + xDelta][position[1] + yDelta] = "#"
                except IndexError:
                    continue
    total = 0
    for line in antinode_map:
        for char in line:
            if char == "#":
                total += 1
    print(total)

def part2():
    for freq in frequencies:
        for position in freq.positions:
            for position2 in freq.positions:
                if position[0] == position2[0] and position[1] == position2[1]:
                    continue
                xDelta = position[0] - position2[0]
                yDelta = position[1] - position2[1]
                try:
                    for i in range(len(f)):
                        if position[0] + xDelta * i < 0 or position[1] + yDelta * i < 0:
                            continue
                        antinode_map[position[0] + xDelta * i][position[1] + yDelta * i] = "#"
                except IndexError:
                    continue
    total = 0
    for line in antinode_map:
        for char in line:
            if char == "#":
                total += 1
    print(total)

if __name__ == "__main__":
    for line in range(len(f)):
        antinode_map.append(list("." * int(len(f[line]))))
        for char in range(len(f[line])):
            if f[line][char] != ".":
                placed = False
                for frequency in frequencies:
                    if f[line][char] == frequency.frequency:
                        frequency.positions.append((line, char))
                if not placed:
                    frequencies.append(Frequency([(line, char)], f[line][char]))
    part1()
    part2()


