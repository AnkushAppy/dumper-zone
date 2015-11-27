#for loop..lol insertion sort

a = [1,2,3,4,5,6]

print a

x_i = 0
for i in a[1:]:
    x_i = x_i + 1
    x_j = x_i
    for x in a[x_i-1::-1]:
        if i > x:
            a[x_j] = a[x_j-1]
            x_j = x_j - 1
    a[x_j] = i

print a
