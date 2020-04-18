# importando dependencias
from flask import Blueprint, jsonify, request
from apps.models import Veiculo

# criando blueprint flask, usando seu construtor padrao
bp = Blueprint('vehiclesbp', __name__)

banco_de_dados = {
    'marcas': [],
    'veiculos': []
}

# declarando rota do blueprint de veiculos para listar TODOS
@bp.route('/')
def lista_veiculos():
    return jsonify([v.to_dict() for v in banco_de_dados['veiculos']])

@bp.route('/', methods=['POST'])
def cria_veiculo():
    veiculo_dados = request.json
    veiculo_novo = Veiculo()
    veiculo_novo.from_dict(veiculo_dados)
    banco_de_dados['veiculos'].append(veiculo_novo)

    return veiculo_novo.to_dict,201

@bp.route('/<string:placa>')
def consulta_veiculo(placa):
    for veiculo in banco_de_dados['veiculos']:
        if veiculo.placa == placa:
            return jsonify(veiculo.to_dict())
    
    return f'não encontrado', 404

@bp.route('/<string:placa>', methods=['PUT'])
def atualiza_veiculo(placa):
    posicao = 0
    for veiculo in banco_de_dados['veiculos']:
        if veiculo.placa == placa:
            veiculo_dados = request.json
            veiculo_novo = Veiculo()
            veiculo_novo.from_dict(veiculo_dados)
            banco_de_dados['veiculos'].pop(posicao)
            banco_de_dados['veiculos'].append(veiculo_novo)
            return jsonify(veiculo_novo.to_dict())
        posicao = posicao + 1
    
    return f'não encontrado', 404

@bp.route('/<string:placa>', methods=['DELETE'])
def remove_veiculo(placa):
    posicao = 0
    for veiculo in banco_de_dados['veiculos']:
        if veiculo.placa == placa:
            banco_de_dados['veiculos'].pop(posicao)
            return jsonify(veiculo.to_dict())
        posicao = posicao + 1
    
    return f'não encontrado', 404