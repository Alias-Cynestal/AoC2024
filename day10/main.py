f = open("input.txt", "r").read().splitlines()
topo_map = []
current_found = []
total = 0
total_2 = 0

def crawl(i,j, current):
    total = 0
    if i-1 >= 0 and int(topo_map[i - 1][j]) == current + 1:
        total += crawl(i-1,j, current + 1)
    if i+1 < len(topo_map) and int(topo_map[i + 1][j]) == current + 1:
        total += crawl(i + 1, j, current + 1)
    if j-1 >= 0 and int(topo_map[i][j - 1]) == current + 1:
        total += crawl(i,j - 1, current + 1)
    if j+1 < len(topo_map[0]) and int(topo_map[i][j + 1]) == current + 1:
        total += crawl(i,j+1, current + 1)
    if int(topo_map[i][j]) == 9 and  (i,j) not in current_found:
        total += 1
        current_found.append((i,j))
    return total

def crawl_2(i,j, current):
    total = 0
    if i-1 >= 0 and int(topo_map[i - 1][j]) == current + 1:
        total += crawl_2(i-1,j, current + 1)
    if i+1 < len(topo_map) and int(topo_map[i + 1][j]) == current + 1:
        total += crawl_2(i + 1, j, current + 1)
    if j-1 >= 0 and int(topo_map[i][j - 1]) == current + 1:
        total += crawl_2(i,j - 1, current + 1)
    if j+1 < len(topo_map[0]) and int(topo_map[i][j + 1]) == current + 1:
        total += crawl_2(i,j+1, current + 1)
    if int(topo_map[i][j]) == 9:
        total += 1
    return total


if __name__ == "__main__":
    for line in f:
        topo_map.append(list(line))
    for i in range(len(topo_map)):
        for j in range(len(topo_map[0])):
            current_found = []
            if int(topo_map[i][j]) == 0 :
                total += crawl(i, j, 0)
                total_2 += crawl_2(i, j, 0)
    print(total)
    print(total_2)