def exponential_growth(n, factor, days):
    res = [n]
    for i in range(1, days + 1):
        res.append(res[i - 1] * factor)
    return res
