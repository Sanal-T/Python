def main():
    print("Enter number of process:", end=" ")
    a = int(input())
    wt = [0] * a
    tt = [0] * a
    p = [0] * a
    bt = [0] * a
    
    print("Enter the burst time in order")
    for b in range(a):
        p[b] = b + 1
        print(f"p{b+1}:", end=" ")
        bt[b] = int(input())

    for i in range(a - 1):
        for j in range(a - 1 - i):
            if bt[j] > bt[j + 1]:
                bt[j], bt[j + 1] = bt[j + 1], bt[j]
                p[j], p[j + 1] = p[j + 1], p[j]
    
    wt[0] = 0
    avgWT = 0.0
    for b in range(1, a):
        wt[b] = wt[b - 1] + bt[b - 1]
        avgWT += wt[b]
        print(avgWT)
    
    avgWT /= a

    avgTT = 0.0
    for b in range(a):
        tt[b] = wt[b] + bt[b]
        avgTT += tt[b]
        print(f"tt:{avgTT}")
    
    avgTT /= a
    print(f"average tt:{avgTT}")
    print(f"average wt:{avgWT}")
    print("PID\t\tTT\t\tWT")
    for b in range(a):
        print(f"p{p[b]}\t\t{tt[b]}\t\t{wt[b]}")
    
    print("\nGANT CHART")
    print("\n" + "-" * 80)
    for b in range(a):
        print(f"|\tp{p[b]}\t", end="")
    print("|")
    print("-" * 80)
    for b in range(a):
        print(f"{wt[b]}\t\t", end="")
    print(tt[a - 1])

if __name__ == "__main__":
    main()