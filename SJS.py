pro = [
    ["P1", 3, 5],
    ["P2", 2, 4],
    ["P3", 4, 3],
    ["P4", 1, 2],
    ["P5", 5, 3]
]


remaining_pro = pro.copy()

time = 0
total_tat = 0
total_wt = 0
execution_order = []

print("PID\tAT\tBT\tCT\tTAT\tWT")

while remaining_pro:
    
    available_pro = [p for p in remaining_pro if p[1] <= time]

    if not available_pro:
        
        time = min(remaining_pro, key=lambda x: x[1])[1]
        continue

    
    chosen = min(available_pro, key=lambda x: (x[2], x[1]))
    remaining_pro.remove(chosen)

    pid, at, bt = chosen
    ct = time + bt
    tat = ct - at
    wt = tat - bt

    total_tat += tat
    total_wt += wt
    execution_order.append(pid)

    print(f"{pid}\t{at}\t{bt}\t{ct}\t{tat}\t{wt}")
    time = ct

n = len(pro)
print(f"\nAverage TAT = {total_tat / n:.2f}")
print(f"Average WT = {total_wt / n:.2f}")

print("\nExecution Order (Gantt Chart):")
for pid in execution_order:
    print(pid, end=" --> ")
print("End")
