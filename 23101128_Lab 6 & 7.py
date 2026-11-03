def fcfs(req, h):
    tmv = 0
    c = h

    for t in req:
        if t == h:
            continue
        tmv += abs(t-c)
        c = t

    return tmv


def sstf(req, h):
    tmv = 0
    c = h
    rem = req.copy()
    seq = []

    while rem:
        clos = min(rem, key=lambda t:abs(t-c))
        tmv += abs(clos - c)
        c = clos
        seq.append(clos)
        rem.remove(clos)



    return tmv



req = [0, 30, 41, 62, 14, 20]
h = 20

cost1 = fcfs(req, h)
print(f"FCFS total cost: {cost1}")

cost2 = sstf(req, h)
print(f"SSTF total cost: {cost2}")

