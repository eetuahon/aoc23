import re

def read_file():
    a = []
    f = open("input02", "r")
    for i in f:
        if len(i) > 1:
            a.append(i.replace("\n",""))
    f.close()
    return a

def task1(f):
    s = 0
    for i in f:
        game = i.split(":")
        reds = re.findall("\d+ red", game[1])
        greens = re.findall("\d+ green", game[1])
        blues = re.findall("\d+ blue", game[1])
        r = [int(x.split()[0]) for x in reds]
        g = [int(x.split()[0]) for x in greens]
        b = [int(x.split()[0]) for x in blues]
        if max(r) <= 12 and max(g) <= 13 and max(b) <= 14:
            s += int(game[0].split()[1])
    print(s) #2.1

def task2(f):
    s = 0
    for i in f:
        game = i.split(":")
        reds = re.findall("\d+ red", game[1])
        greens = re.findall("\d+ green", game[1])
        blues = re.findall("\d+ blue", game[1])
        r = [int(x.split()[0]) for x in reds]
        g = [int(x.split()[0]) for x in greens]
        b = [int(x.split()[0]) for x in blues]
        s += max(r) * max(g) * max(b)
    print(s) #2.2

def main():
    f = read_file()
    task1(f)
    task2(f)

if __name__== "__main__":
    main()