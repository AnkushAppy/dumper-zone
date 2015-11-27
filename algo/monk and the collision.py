T = int(raw_input())

while T > 0:
    a = [0,0,0,0,0,0,0,0,0,0]
    n = int(raw_input())
    # print n
    count = 0
    i = raw_input().split(' ')
    # print len(i)
    for i in i:
        if n <= 0:
            break
        n = n-1
        if a[int(i)%10] == 0:
            a[int(i)%10] = 1
        else:
            count = count + 1
    print count
    T = T -1
