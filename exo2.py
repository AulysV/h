def init(n):
    return [[False]*n]*n

print(init(5))

def gang(p):
    for i in range(n):
        for j in range(n):
            if p[i][j] == True:
                return True
            else :
                return False

def voisines(i, j, t):
    l = init(t)

    a = l[i+1][j]
    b = l[i-1][j]
    c = l[i][j+1]
    d = l[i][j-1]
    
    return [a, b, c, d]

