pro = [
    ["P1", 3, 4, 2],
    ["P2", 0, 4, 0],
    ["P3", 2,3,1],
    ["P4", 1,6,1],
    ["P5", 4,2,3],
]

time = 0
total_tat = 0
total_wt = 0
completion_time = {}
remaining_bt = {p[0]: p[2] for p in pro}
execution_order = []

print("PID\tAT\tBT\tPT\tCT\tTAT\tWT")

while remaining_bt:
    available_pro = [
        p for p in pro
        if p[1] <= time and remaining_bt[p[0]] > 0
    ]


    if not available_pro:
        time += 1
        continue


    chosen = min(available_pro, key=lambda x: (x[3], x[1]))

    pid, at, bt, pt = chosen


    remaining_bt[pid] -= 1
    time += 1


    if not execution_order or execution_order[-1] != pid:
        execution_order.append(pid)


    if remaining_bt[pid] == 0:
        completion_time[pid] = time

        tat = time - at
        wt = tat - bt

        total_tat += tat
        total_wt += wt

        print(f"{pid}\t{at}\t{bt}\t{pt}\t{time}\t{tat}\t{wt}")
        print("Total Waiting time")
        print(total_wt)
        print("Avg Waiting time")
        print(total_wt/5)
        print("Total Turn Around time")
        print(total_tat)
        print("Avg Turn Around time")
        print(total_tat/5)





        pro = [p for p in pro if p[0] != pid]
print("Labib")
print(total_wt)
n = 5

print("\nAverage TAT =", total_tat / n)
print("Average WT =", total_wt / n)
print(execution_order)
print("\nExecution Order:")
for pid in execution_order:
    print(pid[0], end="-->")
print("End")
