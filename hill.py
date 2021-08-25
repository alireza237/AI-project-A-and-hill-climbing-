x = [0 for i in range(9)]
y = [0 for i in range(9)]

goal_x=[1,0,1,2,2,2,1,0,0]
goal_y=[1,0,0,0,1,2,2,2,1]


def mojaver(n1,n2):
    global x,y
    if x[n1]==x[n2] and abs(y[n1]-y[n2])==1:
        return 1
    if y[n1] == y[n2] and abs(x[n1] - x[n2]) == 1:
        return 1
    return 0


def distance():
    dis=0
    global goal_x,goal_y,x,y
    for i in range(9):
        dis = dis + abs(goal_x[i] - x[i]) + abs(goal_y[i] - y[i])
    return dis

def chap():
    global x,y
    for  s in range (9):
        for i in range (9):
            for j in range(9):
                    if x[j]==i  and y[j]==s :
                        if i%3==0:
                            print()
                        print(j,end=" ")



b=[]
for j in range (3):
    a=list(map(int,input().split()))
    for i in range(3):

        x[a[i]]=(i)
        y[a[i]] =(j)

cost=0
while True:
    b=0

    for i in range(9):
        if mojaver(0,i):
            dis=distance()
            x[0], x[i] = x[i], x[0]
            y[0], y[i] = y[i], y[0]
            if distance()>=dis:
                x[0],x[i] = x[i],x[0]
                y[0],y[i] = y[i],y[0]
            else:
                b=1
                chap()
                cost=cost+1
                print(cost)
                break
    if b ==0 :
        break


print()

