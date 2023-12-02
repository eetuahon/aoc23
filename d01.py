import re

def read_file():
    a = []
    f = open("input01", "r")
    for i in f:
        if len(i) > 1:
            a.append(i.replace("\n",""))
    f.close()
    return a

def task1(f):
    sum = 0
    for i in f:
        nums = re.findall("\d", i)
        n = int(nums[0] + nums[-1])
        sum += n
    print(sum) #1.1

def task2(f):
    sum = 0
    for i in f:
        n1match = re.search("\d|one|two|three|four|five|six|seven|eight|nine", i)
        j = i[n1match.start()+1:]
        n2match = re.search("\d|one|two|three|four|five|six|seven|eight|nine", j)
        if n2match:
            n2 = n2match.group()
        else:
            n2 = n1match.group()
        while n2match:
            j = j[n2match.start()+1:]
            n2match = re.search("\d|one|two|three|four|five|six|seven|eight|nine", j)
            if n2match:
                n2 = n2match.group()
        n1 = n1match.group().replace("one","1").replace("two","2").replace("three","3").replace("four","4").replace("five","5")
        n1 = n1.replace("six","6").replace("seven","7").replace("eight","8").replace("nine","9")
        n2 = n2.replace("one","1").replace("two","2").replace("three","3").replace("four","4").replace("five","5")
        n2 = n2.replace("six","6").replace("seven","7").replace("eight","8").replace("nine","9")
        sum += int(n1 + n2)
    print(sum) #1.2

def main():
    f = read_file()
    task1(f)
    task2(f)

if __name__== "__main__":
    main()