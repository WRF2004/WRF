try:
    m = int(input())
    n = int(input())
    list1 = [int(m), int(n)]
    pre1 = int(m)
    pre2 = int(n)
    for i in range(18):
        list1.append(pre1 + pre2)
        tmp = pre1
        pre1 = pre2
        pre2 = tmp + pre2
    print(sum(list1))
except ValueError:
    print("illegal input")