T= int(raw_input())

for i in range(0,T):
    n = int(raw_input())
    d_f = {}
    d_p = {}
    count = 0
    while n > 0:
        arr = raw_input().split()
        f = arr[0]
        p = arr[1]
        if d_f.has_key(f):
           d_f[f] = d_f[f] + 1
        else:
            d_f[f] = 1

        if d_f.has_key(p):
            if d_f[f] <= 0:
                count = count + 1
            else:
                d_f[f] = d_f[f] - 1
        else:
            count = count + 1
        n = n-1
    print count
    
            
            
        
    
    
