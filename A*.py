x = [0 for _ in range(9)]
y = [0 for _ in range(9)]

goal_x = [1, 0, 1, 2, 2, 2, 1, 0, 0]
goal_y = [1, 0, 0, 0, 1, 2, 2, 2, 1]


def hamsaye():
    global x, y

    hamsaye_x = []
    hamsaye_y = []

    b = 0
    for n2 in range(1, 9):

        if abs(x[0] - x[n2]) + abs(y[0] - y[n2]) == 1:
            nx = x.copy()
            ny = y.copy()
            nx[0], nx[n2] = nx[n2], nx[0]
            ny[0], ny[n2] = ny[n2], ny[0]

            hamsaye_x.append(nx)
            hamsaye_y.append(ny)
    return hamsaye_x, hamsaye_y


def h(x, y):
    dis = 0
    global goal_x, goal_y
    for i in range(1, 9):
        dis = dis + abs(goal_x[i] - x[i]) + abs(goal_y[i] - y[i])
    return dis


def chap():
    global x, y
    for s in range(9):
        for i in range(9):
            for j in range(9):
                if x[j] == i and y[j] == s:
                    if i % 3 == 0:
                        print()
                    print(j, end=" ")


b = []
for j in range(3):
    p = list(map(int, input().split()))
    for i in range(3):
        x[p[i]] = i
        y[p[i]] = j

a = []
a.append([h(x, y), 0, x, y])

while True:
    a.sort()

    x = a[0][2]
    y = a[0][3]
    cost = a[0][1]
    a = a[1:len(a)]
    nx, ny = hamsaye()

    for i in range(len(nx)):
        f = 1
        for j in a:
            if j[2] == nx[i] and j[3] == ny[i]:
                f = 0
                if j[0] > h(nx[i], ny[i]) + cost + 1:
                    j[0] = j[0] > h(nx[i], ny[i]) + cost + 1
                    j[1] = cost + 1
        if f:
            a.append([h(nx[i], ny[i]) + cost + 1, cost + 1, nx[i], ny[i]])

    chap()
    print()

    if x == goal_x and y == goal_y:
        break

print("cost", end=" ")
print(cost)
