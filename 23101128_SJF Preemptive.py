

pro = [
    ["P1", 0, 4],
    ["P2", 1, 2],
    ["P3", 3, 2],
    ["P4", 2, 1],
    
]


remaining_bt = {p[0]: p[2] for p in pro}
process_dict = {p[0]: {"at": p[1], "bt": p[2]} for p in pro}

time = 0
completed = 0
n = len(pro)
execution_order = []
ct_dict = {}

while completed < n:

    available = [
        pid for pid, info in process_dict.items()
        if info["at"] <= time and remaining_bt[pid] > 0
    ]

    if not available:

        uncompleted = [info["at"] for pid, info in process_dict.items() if remaining_bt[pid] > 0]
        time = min(uncompleted)
        continue


    chosen_pid = min(available, key=lambda x: (remaining_bt[x], process_dict[x]["at"]))


    remaining_bt[chosen_pid] -= 1


    if not execution_order or execution_order[-1] != chosen_pid:
        execution_order.append(chosen_pid)

    time += 1


    if remaining_bt[chosen_pid] == 0:
        ct_dict[chosen_pid] = time
        completed += 1

total_tat = 0
total_wt = 0

print("PID\tAT\tBT\tCT\tTAT\tWT")
for p in pro:
    pid, at, bt = p
    ct = ct_dict[pid]
    tat = ct - at
    wt = tat - bt
    total_tat += tat
    total_wt += wt
    print(f"{pid}\t{at}\t{bt}\t{ct}\t{tat}\t{wt}")

print(f"\nAverage TAT = {total_tat / n:.2f}")
print(f"Average WT = {total_wt / n:.2f}")

print("\nExecution Order (Gantt Chart):")
for pid in execution_order:
    print(pid, end=" --> ")
print("End")

