from functools import cache

f = open("input.txt", "r").read().splitlines()
input = f[0].split(" ")

# cache : permet de garder en mémoire tous les appels à la fonction, y compris ceux récursifs, ce qui permet de grandement améliorer le temps d'exécution
@cache
def count(string, level):
    if level == 0:
        return 1
    if string == "0":
        return count("1", level - 1)
    if len(str(int(string))) % 2 == 0:
        return count(str(int(string[ :len(str(int(string))) //2])), level - 1) + count(str(int(string[len(str(int(string))) //2:])), level - 1)
    return count(str(int(string) * 2024), level - 1)

if __name__ == "__main__":
    total = 0
    total_2 = 0
    for i in range(len(input)):
        total += count(input[i], 25)
        total_2 += count(input[i], 75)

    print(total)
    print(total_2)