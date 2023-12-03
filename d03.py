from collections import defaultdict
import re

def read_file():
    a = []
    f = open("input03", "r")
    for i in f:
        if len(i) > 1:
            a.append(i.replace("\n",""))
    f.close()
    return a

def find_coordinates(f):
    coords = defaultdict(lambda: 0)
    items = []
    yl = len(f)
    xl = len(f[0])
    for y in range(yl):
        n = re.findall("\d+", f[y])
        n.append(-1)
        i = 0
        nv = int(n[i])
        for x in range(xl):
            if f[y][x].isdigit():
                coords[(x,y)] = nv
                if type(nv) == int:
                    nv = (x,y)
                    i += 1
            if f[y][x] != "." and not f[y][x].isdigit():
                items.append((x,y))
            if type(nv) == tuple and not f[y][x].isdigit():
                nv = int(n[i])
    return (f, items, coords)

def task1(f):
    s = 0
    items = f[1]
    coords = f[2]
    f = f[0]
    found = set()
    for i in items:
        y = i[1]
        x = i[0]
        t = [(-1,-1), (-1, 0), (-1, 1), (0,-1), (0, 1), (1,-1), (1, 0), (1, 1)]
        for tt in t:
            r = coords[(x + tt[0], y + tt[1])]
            if type(r) == tuple:
                found.add(r)
            elif r != 0:
                found.add((x + tt[0], y + tt[1]))
    for c in found:
        s += coords[(c[0], c[1])]
    print(s) #3.1

def task2(f):
    s = 0
    items = f[1]
    coords = f[2]
    f = f[0]
    for i in items:
        y = i[1]
        x = i[0]
        if f[y][x] != "*":
            continue
        found = set()
        t = [(-1,-1), (-1, 0), (-1, 1), (0,-1), (0, 1), (1,-1), (1, 0), (1, 1)]
        for tt in t:
            r = coords[(x + tt[0], y + tt[1])]
            if type(r) == tuple:
                found.add(r)
            elif r != 0:
                found.add((x + tt[0], y + tt[1]))
        if len(found) == 2:
            ratio = 1
            for c in found:
                ratio *= coords[(c[0], c[1])]
            s += ratio
    print(s) #3.2

def main():
    f = read_file()
    f = find_coordinates(f)
    task1(f)
    task2(f)

if __name__== "__main__":
    main()