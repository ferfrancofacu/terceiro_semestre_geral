# importando dependencias
from flask import Blueprint, jsonify, request
from apps.models import Veiculo
from apps.services import consultar, atualizar, remover, adicionar, listar, IntegridadeException, IntegridadeReferencialException

# criando blueprint flask, usando seu construtor padrao
bp = Blueprint('vehiclesbp', __name__)

def unmarshalling():
    return Veiculo().from_dict(request.json)

# declarando rota do blueprint de veiculos para listar TODOS
@bp.route('/')
def lista_veiculos():
    return jsonify([v.to_dict() for v in listar()])

@bp.route('/', methods=['POST'])
def cria_veiculo():
    try:
        veiculo_novo = unmarshalling()
        veiculo_novo = adicionar(veiculo_novo)

        return veiculo_novo.to_dict(), 201
    except IntegridadeException as e:
        print(str(e))
        return str(e), 400
    except IntegridadeReferencialException as e:
        print(str(e))
        return str(e), 400

@bp.route('/<string:placa>')
def consulta_veiculo(placa):
    veiculo, indice = consultar(placa)
    if (veiculo != None):
            return jsonify(veiculo.to_dict())
    
    return f'não encontrado', 404

@bp.route('/<string:placa>', methods=['PUT'])
def atualiza_veiculo(placa):
    veiculo_atualizado = unmarshalling()
    veiculo_atualizado = atualizar(placa, veiculo_atualizado)
    if(veiculo_atualizado != None):
        return jsonify(veiculo_atualizado.to_dict())
        
    return f'não encontrado', 404

@bp.route('/<string:placa>', methods=['DELETE'])
def remove_veiculo(placa):
    veiculo = remover(placa)
    if(veiculo != None):
            return jsonify(veiculo.to_dict())
    
    return f'não encontrado', 404
