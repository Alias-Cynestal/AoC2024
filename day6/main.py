from datetime import datetime, timedelta

f = open("input.txt", "r").read().splitlines()

input = []
solutionInput = []

class Guard:
    position = (0,0)
    direction = (0, 0)
    startPos = (0,0)
    startDir = (0,0)

    def __init__(self, position, direction):
        self.direction_array = []
        self.startPos = position
        self.position = position
        self.startDir = direction
        self.direction = direction

    def move(self):
        solutionInput[self.position[0]][self.position[1]] = "X"
        try:
            if (self.position[0] + self.direction[0]) < 0 or (self.position[1] + self.direction[1]) < 0:
                return False
            elif input[self.position[0] + self.direction[0]][self.position[1] + self.direction[1]] != '#' :
                self.position = (self.direction[0] + self.position[0], self.direction[1] + self.position[1])
                return True
            else:
                self.change_direction()
                return True
        except IndexError:
            return False

    def move_part2(self):
        try:
            if (self.position[0] + self.direction[0]) < 0 or (self.position[1] + self.direction[1]) < 0:
                return 0
            elif input[self.position[0] + self.direction[0]][self.position[1] + self.direction[1]] == '.':
                self.position = (self.direction[0] + self.position[0], self.direction[1] + self.position[1])
                return 1
            else:
                if input[self.position[0] + self.direction[0]][self.position[1] + self.direction[1]] == "0":
                    if self.direction in self.direction_array:
                        return 2
                    else:
                        self.direction_array.append(self.direction)
                self.change_direction()
                return 1
        except IndexError:
            return 0

    def reset(self):
        self.position = self.startPos
        self.direction = self.startDir
        self.direction_array = []


    def change_direction(self):
        if self.direction == (0,1):
            self.direction = (1, 0)
        elif self.direction == (1,0):
            self.direction = (0, -1)
        elif self.direction == (0,-1):
            self.direction = (-1, 0)
        elif self.direction == (-1,0):
            self.direction = (0, 1)


def find_guard_position():
    direction = (0,0)
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] != "#" and input[i][j] != ".":
                playerPosition = (i,j)
                if input[i][j] == "^":
                    direction = (-1, 0)
                elif input[i][j] == "v":
                    direction = (1, 0)
                elif input[i][j] == ">":
                    direction = (0, 1)
                elif input[i][j] == "<":
                    direction = (0, -1)
                input[i][j] = "."
                return Guard(playerPosition, direction)



def part1(guard):
    while guard.move():
        pass
    total = 0
    for i in range(len(input)):
        for j in range(len(input[i])):
            if solutionInput[i][j] == "X":
                total += 1
    print(total)

def part2(guard):
    total = 0
    for i in range(len(input)):
        for j in range(len(input[i])):
            if solutionInput[i][j] == "X":
                input[i][j] = "0"
                guard.reset()
                time = datetime.now()
                while True:
                    result = guard.move_part2()
                    if datetime.now() - timedelta(milliseconds=500) >= time:
                        total += 1
                        break
                    if result == 0:
                        break
                    if result == 1:
                        continue
                    if result == 2:
                        total += 1
                        break
                input[i][j] = "."
    print(total)



if __name__ == "__main__":
    for i in f:
        input.append(list(i))
        solutionInput.append(list(i))
    guard = find_guard_position()
    part1(guard)
    part2(guard)