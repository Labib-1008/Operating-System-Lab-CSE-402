def fifo(pages: list[int], capacity: int):
    memory=[]
    hit = 0
    fault=0
    print(f"{'page':^6} | {'Frames (memory)':^16} | {'Status':^8}")
    print("-" * 38)
    for p in pages:
        if p in memory:
            hit += 1
            s = "hit"
            memory.remove(p)
            memory.append(p)
        else:
            fault += 1
            s = "Miss"
            if len(memory) == capacity:
                memory.pop()
        memory.append(p)
        print(f"{'p':^6} | {str(memory):^16} | {'s':^8}")
    print("-" * 36)
    print(f"Hit = {hit}")
    print(f"Miss = {fault}")
    print(f"Ratio = {hit/len(pages)}")

refString = [1, 2, 3, 4, 5, 1, 2, 3, 1]
frameSize = 3

fifo(refString, frameSize)
