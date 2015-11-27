def fact(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return fact(n-1)*n

T = int(raw_input())
while T > 0:
	n = int(raw_input())
	print fact(n)
	T= T-1
