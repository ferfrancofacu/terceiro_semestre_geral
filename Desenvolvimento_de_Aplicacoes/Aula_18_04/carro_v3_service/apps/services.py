banco_de_dados = {
    'marcas': [],
    'veiculos': []
}

def listar():
    return banco_de_dados['veiculos']

def adicionar(veiculo):
    banco_de_dados['veiculos'].append(veiculo)
    return veiculo

def consultar(placa):
    indice = 0
    for veiculo in banco_de_dados['veiculos']:
        if veiculo.placa == placa:
            return veiculo, indice
        indice = indice + 1
    
    return None, None

def remover(placa):
    veiculo_a_remover, indice = consultar(placa)
    if(veiculo_a_remover != None):
        banco_de_dados['veiculos'].pop(indice)
        return veiculo_a_remover
    
    return None


def atualizar(placa, novo_veiculo):
    veiculo_removido = remover(placa)
    if(veiculo_removido != None):
        adicionar(novo_veiculo)
        return novo_veiculo
    
    return None
    