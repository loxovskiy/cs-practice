mx = float(input())
n = int(input())
mr = 0.0
maxN = 0
ErN = 0
sm = 0
for i in range(n):
    st = input()

    if str(st) == 'error':
        ErN += 1

    else:
        sm += float(st)
        if float(st) > float(mr):
            mr = st
        if float(st) > mx:
            maxN += 1
