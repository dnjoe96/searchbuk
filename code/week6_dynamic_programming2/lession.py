

def knapsack(W):
    value = [0]*W
    v = {12:2, 23:5, 30:10}
    for w in range(1, W):
        value[w] = 0
        for i in range(1, 30):
            if i <= w:
                val = value[w - i] + v[i]
                if val > value[w]:
                    value[w] = val