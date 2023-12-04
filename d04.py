from collections import defaultdict
import re

def read_file():
    a = []
    f = open("input04", "r")
    for i in f:
        if len(i) > 1:
            a.append(i.replace("\n",""))
    f.close()
    return a

def format_file(f):
    a = []
    for r in f:
        n = r.split(":")
        nv = int(re.search("\d+", n[0]).group())
        nb = n[1].split(" | ")
        wn = re.findall("\d+", nb[0])
        mn = re.findall("\d+", nb[1])
        wn = [int(i) for i in wn]
        mn = [int(i) for i in mn]
        a.append((nv, wn, mn))
    return a

def task1(f):
    s = 0
    for c in f:
        counter = 0
        wn = c[1]
        nb = c[2]
        for n in wn:
            if n in nb:
                counter += 1
        if counter > 0:
            s += 2 ** (counter - 1)
    print(s) #4.1

def task2(f):
    s = 0
    coupons = defaultdict(lambda: 1)
    for c in f:
        v = c[0]
        counter = 0
        wn = c[1]
        nb = c[2]
        for n in wn:
            if n in nb:
                counter += 1
        nofc = coupons[v]
        for i in range(1, counter + 1):
            coupons[v + i] += nofc
        s += nofc
    print(s) #4.2

def main():
    f = read_file()
    f = format_file(f)
    task1(f)
    task2(f)

if __name__== "__main__":
    main()