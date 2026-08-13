

pro = [
    ["P1", 3, 5],
    ["P2", 2, 4],
    ["P3", 4, 3],
    ["P4", 1, 2],
    ["P5", 5, 3]
]
pro.sort(key=lambda x: x[1])
time = 0
total_tat = 0
total_wt = 0

print("PID\tAT\tBT\tCT\tTAT\tWT")

for p in pro:
    pid, at , bt  = p
    if time < at:
        time = at

    ct = time + bt
    tat = ct - at
    wt = tat - bt
    total_tat += tat
    total_wt += wt

    print(f"{pid}\t{at}\t{bt}\t{ct}\t{tat}\t{wt}")

    time = ct

n = len(pro)

print("\nAverage TAT =", total_tat / n)
print("Average WT =", total_wt / n)

for p in pro:
    print(p[0], end = "-->")
print("End")