
def winner(names, scores):
    max = -200.0
    winname = ''
    for i in range(len(scores)):
        if scores[i] > max:
            max = scores[i]
            winname = names[i]
    return winname

def average(scores):
    sum=0.0
    n=len(scores)
    if n==0:
        return 0.0
    for i in range(n):
        sum+=scores[i]
    return round(sum/n,2)

def ranking(names, scores):
    a = []
    newlist = sorted(range(len(scores)), key = lambda index:scores[index], reverse = True)
    for i in newlist:
        a.append(names[i])
    return a



def above_average(names, scores):
    morsr = []
    for i in range(len(scores)):
        if scores[i] > average(scores):
            morsr.append(names[i])
    return morsr
