from threading import Thread

f = open("input.txt", "r").read().splitlines()
input = f[0].split(" ")
global to_add

def threadCheck(start, length):
    for i in range(length):
        checkStone(start + i)

def checkStone(j):
    if int(input[j]) == 0:
        input[j] = "1"
    elif len(str(int(input[j]))) % 2 == 0:
        x = str(int(input[j]))
        to_add.append(x[int(len(x) / 2):len(x)])
        input[j] = x[0:int(len(x) / 2)]
    else:
        input[j] = str(int(input[j]) * 2024)

if __name__ == "__main__":
    for i in range(75):
        print(i)
        to_add = []
        start = 0
        length = len(input)
        x = int(length / 8)
        t0 = Thread(target=threadCheck, args=(start, x))
        start += x
        length -= x
        x = int(length / 7)
        t1 = Thread(target=threadCheck, args=(start, x))
        start += x
        length -= x
        x = int(length / 6)
        t2 = Thread(target=threadCheck, args=(start, x))
        start += x
        length -= x
        x = int(length / 5)
        t3 = Thread(target=threadCheck, args=(start, x))
        start += x
        length -= x
        x = int(length / 4)
        t4 = Thread(target=threadCheck, args=(start, x))
        start += x
        length -= x
        x = int(length / 3)
        t5 = Thread(target=threadCheck, args=(start, x))
        start += x
        length -= x
        x = int(length / 2)
        t6 = Thread(target=threadCheck, args=(start, x))
        start += x
        length -= x
        t7 = Thread(target=threadCheck, args=(start,length))

        t0.start()
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
        t6.start()
        t7.start()

        t0.join()
        t1.join()
        t2.join()
        t3.join()
        t4.join()
        t5.join()
        t6.join()
        t7.join()

        input += to_add
    print(len(input))