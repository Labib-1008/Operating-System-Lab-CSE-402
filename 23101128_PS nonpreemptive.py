pro = [
    ["P1", 0, 3, 4],
    ["P2", 3, 2, 0],
    ["P3", 1, 2, 2],
    ["P4", 2, 1, 1]
]

time = 0
total_tat = 0
total_wt = 0
execution_order = []
remaining_pro = pro.copy()
print("PID\tAT\tBT\tPT\tCT\tTAT\tWT")

while remaining_pro:
    available_pro = [p for  p in remaining_pro if p[1] <= time]
    if not available_pro:
        time = min(remaining_pro, key = lambda x: x[1])[1]
        continue

    chosen = min(available_pro, key = lambda x: (x[3], x[1]))
    remaining_pro.remove(chosen)
    pid, at, bt, pt = chosen
    if time < at:
        time = at

    ct = time + bt
    tat = ct - at
    wt = tat - bt
    total_tat += tat
    total_wt += wt
    execution_order.append(pid)
    print(f"{pid}\t{at}\t{bt}\t{pt}\t{ct}\t{tat}\t{wt}")

    time = ct

n = len(pro)

print("\nAverage TAT =", total_tat / n)
print("Average WT =", total_wt / n)

for pid in execution_order:
    print(pid, end = "-->")
print("End")