
def winner(names, scores):
    max = -200.0
    winname = ''
    for i in range(len(scores)):
        if scores[i] > max:
            max = scores[i]
            winname = names[i]
    return winname

def average(scores):
    sumsc = 0.0
    if len(scores) > 0:
        for i in range(len(scores)):
            sumsc += scores[i]
        srrez = sumsc / len(scores)
    return round(srrez, 2)
    if len(scores) == 0:
        return 0.0

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
