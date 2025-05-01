def main():
    print("Enter no of resources:", end="")
    r = int(input())
    max_res = [0] * r
    print("Enter max instances of each resource:")
    for i in range(r):
        print(f"R{i+1}:", end="")
        max_res[i] = int(input())
    
    print("Enter no of processes:", end="")
    p = int(input())
    alloc = [[0] * r for _ in range(p)]
    max_req = [[0] * r for _ in range(p)]
    need = [[0] * r for _ in range(p)]
    fin = [0] * p
    finf = [0] * p
    
    print("Enter instances allocated for each process:")
    for i in range(p):
        print(f"P{i+1}:", end="")
        for j in range(r):
            print(f"\tR{j+1}:", end="")
            alloc[i][j] = int(input())
    
    print("Enter max instances required for each process:")
    for i in range(p):
        print(f"P{i+1}:", end="")
        for j in range(r):
            print(f"\tR{j+1}:", end="")
            max_req[i][j] = int(input())
    
    avail = [0] * r
    avail_og = [0] * r
    for i in range(r):
        sum_res = 0
        for j in range(p):
            sum_res += alloc[j][i]
        avail_og[i] = avail[i] = max_res[i] - sum_res
    
    for i in range(p):
        for j in range(r):
            need[i][j] = max_req[i][j] - alloc[i][j]
    
    print("\nNeed Matrix:")
    for i in range(p):
        print()
        for j in range(r):
            print(f"\t{need[i][j]}", end="")
    
    print("\navail:", end="")
    for i in range(r):
        print(f"\t{avail[i]}", end="")
    
    count = 0
    k = 0
    lim = 0
    
    while count != p:
        for i in range(p):
            if finf[i] == 0:
                flag = 1
                for j in range(r):
                    if need[i][j] > avail[j]:
                        flag = 0
                        break
                
                if flag == 1:
                    finf[i] = 1
                    fin[k] = i + 1
                    k += 1
                    count += 1
                    
                    for j in range(r):
                        avail[j] += alloc[i][j]
        
        lim += 1
        if lim > 100:
            break
    
    if count != p:
        print("\ndeadlock occurred!!!!!!!!!!!!!!!!!")
    else:
        print("\nNo deadlock occurred")
        print("safe seq: <", end="")
        for i in range(p):
            print(f"\tP{fin[i]}\t", end="")
            if i < p - 1:
                print(",", end="")
        print(">")

if __name__ == "__main__":
    main()