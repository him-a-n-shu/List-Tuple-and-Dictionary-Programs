'''def increment(n):
    n += 5
    print(n)

num = int(input("1: "))
increment(num)'''


def meancount(mylist):
    total = 0
    count = 0
    for i in mylist:
        total += i
        count += 1
    mean = total / count
    print(mean)

l = eval(input("E: "))
meancount(l)
