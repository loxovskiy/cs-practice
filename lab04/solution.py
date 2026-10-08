
def winner(names, scores):
    max = -200.0
    winname = ''
    for i in range(len(scores)):
        if scores[i] > max:
            max = scores[i]
            winname = names[i]
    return winname

def average(scores):
    null = 0.0
    sumsc = 0.0
    if len(scores) > 0:
        for i in range(len(scores)):
            sumsc += scores[i]
        srrez = sumsc / len(scores)
    return round(srrez, 2)
    if len(scores) == 0:
        return null

def ranking(names, scores):

    zipped = zip(scores, names)
    sort = sorted(zipped, reverse = True)
    tupl = zip(*sort)
    scores_sort, names_sort = [list(x) for x in tupl]
    return names_sort


def above_average(names, scores):
    morsr = []
    for i in range(len(scores)):
        if scores[i] > average(scores):
            morsr.append(names[i])
    return morsr
