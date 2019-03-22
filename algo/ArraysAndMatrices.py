"""
spiral order input matrix

(tR,tC) .....
.............
.............
......(dR,dC)
"""
X = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

def printEdge(X, tR, tC, dR, dC):
    result = []
    if tR == dR:
        result.extend([X[tR][i] for i in range(tC,dC + 1)])
    elif tC == dC:
        result.extend([X[i][tC] for i in range(tR, dR + 1)])
    else:
        curC = tC
        curR = tR
        while curC != dC:
            result.append(X[tR][curC])
            curC += 1
        while curR != dR:
            result.append(X[curR][dC])
            curR += 1
        while curC != tC:
            result.append(X[dR][curC])
            curC -= 1
        while curR != tR:
            result.append(X[curR][tC])
            curR -= 1
    return result


def spiral_order_input_matrix(X):
    assert X is not None

    tR,tC = 0,0
    dR,dC = len(X) - 1,len(X[0]) - 1

    result = []
    while tR <= dR and tC <= dC:
        result.extend(printEdge(X,tR,tC,dR,dC))
        tR += 1
        tC += 1
        dR -= 1
        dC -= 1
    return result
if __name__ == '__main__':
    print(spiral_order_input_matrix(X))