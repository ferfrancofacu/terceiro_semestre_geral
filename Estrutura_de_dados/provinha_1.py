def encaixa(topo,c):
    pass


def balanceada(string):
    pilha = [ ]
    for c in string:
        print(pilha)
        if c in '([{':
            pilha.append(c)
        else:
            topo = pilha.pop()
            if not encaixa(topo,c):
                return False
    if len(pilha) > 0:
        return False
    return True


balanceada('(()[]){}')