names =  ["Аня", "Боря", "Вика"]
scores = [7.0,   9.0,    9.0]

def winner(names, scores):
    max = -200.0
    winname = ''
    for i in range(len(scores)):
        if scores[i] > max:
            max = scores[i]
            winname = names[i]
    return winname

def average(names, scores):
    null = 0.0
    sumsc = 0.0
    if len(scores) > 0:
        for i in range(len(scores)):
            sumsc += scores[i]
        srrez = sumsc / len(scores)
    return f'{srrez:.2f}'
    if len(scores) == 0:
        return null

#def ranking(names, scores)
# scores[:i] + scores[i:]
def above_average(names, scores):
    for i in range(len(scores)):
        if scores[i] > average(names, scores):
            return names[i]



print(f'Победитель - {winner(names, scores)}')
print(f'Средний результат - {average(names, scores)}')
print(f'Выше среднего - {above_average(names, scores)}')
