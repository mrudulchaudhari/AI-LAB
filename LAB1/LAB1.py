# Water jug problem
x, xm, y, ym = 0, 4, 0, 3
print("Initial state: ",x,y)
while (x != 2 or y!= 0):
    if x == 0:
        x = xm
        print("Fill the jug x,",x,xm)
    elif y == ym:
        y = 0
        print("Empty jug y : ", x, y)
    elif x > 0 and y < ym:
        d = min(x, ym - y)
        x -= d
        y += d
        print("Pour from jug x to jug y : ", x, y)
    elif x == 0 and y > 0:
        x = y
        y = 0
        print("Transfer from jug y to jug x : ", x, y)
    elif x == 2 and y == 0:
        print("Goal state achieved : ", x, y)