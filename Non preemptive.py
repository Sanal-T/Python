def fcfs() :
    a=int(input('enter no of processes:'))
    bt=[]
    wt=[0]
    avgwt=0
    avgtt=0
    tt=[]
    print('enter the bt of processes in order:')
    for i in range(0,a):
        print('p',i)
        bt.append(int(input()))
        i=i+1
    for i in range(1,a):
        wt.append(wt[i-1]+bt[i-1])
        avgwt+=wt[i]
        i=i+1
    print('avgwt=',avgwt/a)
    for i in range(0,a):
        tt.append(wt[i]+bt[i])
        avgtt+=tt[i]
        i=i+1
    print('avgtt=',avgtt/a)
    print('\nPID\t TT\t WT\n')
    for i in range(0,a):
        print('p',i,'\t' ,tt[i],'\t', wt[i],'\n')
fcfs()