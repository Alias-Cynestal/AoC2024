f = open("input.txt", "r").read().splitlines()
lines = []

class Line:
    result = 0
    arguments = []

    def __init__(self, result, arguments):
        self.result = int(result)
        self.arguments = arguments

    def is_valid_part_2(self):
        possible_answers = []
        for argument in range(len(self.arguments)):
            possible_answers2 = []
            if len(possible_answers) == 0:
                possible_answers2.append(int(self.arguments[argument]))
            else:
                for possible_answer in possible_answers:
                    possible_answers2.append(int(str(possible_answer) + self.arguments[argument]))
                    possible_answers2.append(int(self.arguments[argument]) + int(possible_answer))
                    possible_answers2.append(int(self.arguments[argument]) * int(possible_answer))
            possible_answers = possible_answers2
        return self.result in possible_answers

    def is_valid_part_1(self):
        possible_answers = []
        for argument in range(len(self.arguments)):
            possible_answers2 = []
            if len(possible_answers) == 0:
                possible_answers2.append(int(self.arguments[argument]))
            else:
                for possible_answer in possible_answers:
                    possible_answers2.append(int(self.arguments[argument]) + int(possible_answer))
                    possible_answers2.append(int(self.arguments[argument]) * int(possible_answer))
            possible_answers = possible_answers2
        return self.result in possible_answers

if __name__ == "__main__":
    total_part_1 = 0
    total_part_2 = 0
    for line in f:
        l = line.split(":")
        lines.append(Line(l[0], l[1][1:].split(" ")))
    for line2 in lines:
        if line2.is_valid_part_1():
            total_part_1 += line2.result
        if line2.is_valid_part_2():
            total_part_2 += line2.result
    print(total_part_1, total_part_2)
