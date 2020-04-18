from apps.models import Marca

banco_de_dados = {
    'marcas': [
        Marca(1, 'Honda'),
        Marca(2, 'Toyota'),
    ],
    'veiculos': []
}

class IntegridadeException(Exception):
    pass

class IntegridadeReferencialException(Exception):
    pass

def listar():
    return banco_de_dados['veiculos']

def adicionar(veiculo):
    if(veiculo.placa == None or veiculo.placa == ''):
        raise IntegridadeException('Chave [placa] deve ser string válida')
    if(consultar(veiculo.placa) != (None, None)):
        raise IntegridadeException('Chaves duplicadas [placa] não são permitidas')

    if(consultar_marca(veiculo.marca_id) == None):
        raise IntegridadeReferencialException('Chave estrangeira (marca_id) inválida')

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
    
def consultar_marca(id):
    if id == None:
        return None

    for marca in banco_de_dados['marcas']:
        if marca.id == id:
            return marca
    
    return None
