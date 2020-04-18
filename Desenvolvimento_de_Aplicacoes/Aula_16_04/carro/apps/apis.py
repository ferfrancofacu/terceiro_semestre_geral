from flask import Blueprint, jsonify, request

bp = Blueprint('vehiclesbp',__name__)

banco_de_dados = {
    'marcas':[],
    'veiculos': []
}

@bp.route('/')
def lista_veiculos():
    return jsonify(banco_de_dados['veiculos'])

@bp.route('/', methods=['POST'])
def cria_veiculo():
    veiculo_dados = request.json()
    
    return 'Cria novo veiculo'

@bp.route('/<string:placa>')
def consultando_veiculo(placa):
    veiculos = banco_de_dados['veiculos']
    for v in veiculos:
        if v.placa == placa:
            return jsonify(v)
    return f'consultando veiculo {id}'

@bp.route('/<int:id>', methods=['PUT'])
def atualizando_veiculo(id):
    return f'Atualiando um veiculo {id}'

@bp.route('/<int:id>', methods=['DELETE'])
def remove_veiculo(id):
    return f'Remove um veiculo {id}'