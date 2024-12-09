f = open("input.txt", "r").read().splitlines()
ans_array = []
ans_array_2 = []
id_total = []

def part_1():
    is_file = True
    id = 0
    for char in f[0]:
        if is_file:
            for i in range(int(char)):
                ans_array.append(str(id))
            id += 1
            is_file = False
        else:
            for i in range(int(char)):
                ans_array.append(".")
            is_file = True
    done = False
    for i in range(len(ans_array)):
        if done:
            break
        if ans_array[i] == ".":
            for j in range(len(ans_array)):
                if i >= len(ans_array) - 1 - j:
                    done = True
                    break
                if ans_array[len(ans_array) - 1 - j] != ".":
                    x = ans_array[len(ans_array) - 1 - j]
                    ans_array[len(ans_array) - 1 - j] = ans_array[i]
                    ans_array[i] = x
                    break
    print(ans_array)
    total = 0
    for char in range(len(ans_array)):
        if ans_array[char] != ".":
            total += int(ans_array[char]) * char
    print(total)

def part_2():
    is_file = True
    id = 0
    for char in f[0]:
        if is_file:
            for i in range(int(char)):
                ans_array_2.append(str(id))
            id_total.append([str(id), char])
            id += 1
            is_file = False
        else:
            for i in range(int(char)):
                ans_array_2.append(".")
            is_file = True
    for i in range(len(id_total)):
        for j in range(len(ans_array_2)):
            if ans_array_2[j] == ".":
                valid = False
                for k in range(int(id_total[len(id_total) - 1 - i][1])):
                    try:
                        if ans_array_2[j + k] != ".":
                            break
                    except IndexError:
                        break
                    if k == int(id_total[len(id_total) - 1 - i][1]) - 1:
                        valid = True
                if valid:
                    for k in range(int(id_total[len(id_total) - 1 - i][1])):
                        ans_array_2[j + k] = id_total[len(id_total) - 1 - i][0]
                    for k in range(len(ans_array_2)):
                        if ans_array_2[len(ans_array_2) - 1 - k] == id_total[len(id_total) - 1 - i][0]:
                            for l in range(int(id_total[len(id_total) - 1 - i][1])):
                                ans_array_2[len(ans_array_2) - 1 - k - l] = "."
                            break

                    break

    print(ans_array_2)
    total = 0
    for char in range(len(ans_array_2)):
        if ans_array_2[int(char)] != ".":
            total += int(ans_array_2[int(char)]) * int(char)
    print(total)

if __name__ == "__main__":
    part_1()
    part_2()