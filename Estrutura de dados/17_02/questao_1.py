def funcao1(a,b):
    cont = 0
    for i in range(a):
        for j in range(b):
           cont = cont + 1 #marca!
    return cont

def funcao2(a,b):
    cont=0
    for i in range(a):
        for j in range(b):
            cont = cont+1 #marca!
    for i in range(a):
        for j in range(b):
            cont = cont+1 #marca!
    return cont
