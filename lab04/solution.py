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
print(winner(names, scores))
