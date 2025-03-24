from operator import itemgetter
def scoreboard(who_ate_what):
    res = list()
    for obj in who_ate_what:
        score = 0
        for key, value in obj.items():
            if key == 'chickenwings':
                score += value * 5 
            if key == 'hamburgers':
                score += value * 3
            if key == 'hotdogs':
                score += value * 2
        res.append({"name": obj["name"], "score": score})
    res = sorted(res, key=itemgetter('name'))
    return sorted(res, key=itemgetter('score'), reverse=True)
​