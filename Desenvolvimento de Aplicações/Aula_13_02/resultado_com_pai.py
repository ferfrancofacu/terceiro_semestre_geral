def resultado_com_pai(frequencia,ac1,ac2,ac3,ac4,ac5,prova):
    acs = remove_menor_valor([ac1,ac2,ac3,ac4,ac5])
    provas = remove_menor_valor([prova])
    pais = remove_menor_valor([pai1,pai2,pai3])

def remove_menor_valor(lista):
    return lista.sort().reverse
