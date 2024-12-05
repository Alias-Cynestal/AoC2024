f = open("input.txt", "r").read().splitlines()
wrongUpdates = []
rules = []

class Rule:
    _firstPage = 0
    _secondPage = 0

    def __init__(self, firstPage, secondPage):
        self._firstPage = firstPage
        self._secondPage = secondPage

    def numbersRespectsRule(self, firstPage, secondPage):
        return firstPage != self._secondPage or secondPage != self._firstPage

class Update:
    _numbers = []
    _middleNumber = 0

    def __init__(self, numbers):
        self._numbers = numbers
        self._middleNumber = int(self._numbers[len(self._numbers)//2])

    def checkIfUpdateIsValid(self, rules):
        for number in range(len(self._numbers)):
            for number2 in range(len(self._numbers)):
                if number < number2:
                    for rule in rules:
                        if not rule.numbersRespectsRule(self._numbers[number], self._numbers[number2]):
                            return False
        return True

    def correctUpdate(self, rules):
        for number in range(len(self._numbers)):
            for number2 in range(len(self._numbers)):
                if number < number2:
                    for rule in rules:
                        if not rule.numbersRespectsRule(self._numbers[number], self._numbers[number2]):
                            x = self._numbers[number]
                            self._numbers[number] = self._numbers[number2]
                            self._numbers[number2] = x
        self._middleNumber = int(self._numbers[len(self._numbers)//2])

def part1():
    on_rules = True
    total = 0
    for line in f:
        if line == "":
            on_rules = False
            continue
        if on_rules:
            numbers = line.split("|")
            rules.append(Rule(numbers[0], numbers[1]))
        else:
            update = Update(line.split(","))
            if update.checkIfUpdateIsValid(rules):
                total += update._middleNumber
            else:
                wrongUpdates.append(update)
    print(total)

def part2():
    total = 0
    for update in wrongUpdates:
        update.correctUpdate(rules)
        total += update._middleNumber
    print(total)


if __name__ == "__main__":
    part1()
    part2()







