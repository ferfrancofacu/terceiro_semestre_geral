from flask import Blueprint, jsonify, request
from apps.professores.services import IntegridadeException, IntegridadeReferencialException, sv_getLista, sv_add, sv_update, sv_delete
from apps.professores.models import Professor

bp = Blueprint('bp_professores', __name__)

@bp.route('/', methods = ['GET'])
def cadastrados():
    return jsonify(sv_getLista())

def unmarshalling():
    return Professor().from_dict(request.json)

@bp.route('/', methods = ['POST'])
def adicionar():
  try:
    UnmObj = unmarshalling()
    if len(UnmObj.nome.replace(" ", "")) <= 3:
      return f'Dados inconsistentes', 404

    obj = sv_add(UnmObj.to_dict())

    if obj == None:
      return 'Professor já cadastrado: '+ UnmObj.to_dict()['nome'], 404
    
    return "Professor cadastrado: RA: {} Nome: {}".format(obj.id,obj.nome), 201
  except IntegridadeException as e:
      print(str(e))
      return str(e), 400
  except IntegridadeReferencialException as e:
      print(str(e))
      return str(e), 400

@bp.route('/<int:id>', methods = ['PUT'])
def alterar(id):
    UnmObj = unmarshalling()
    obj = sv_update(id, UnmObj.to_dict())

    if obj == None:
      return f'Professor não encontrado',404
    if obj == 404:
      return f'Dados inconsistentes',404
    return obj, 201

@bp.route('/<int:id>', methods = ['DELETE'])
def remover(id):
    obj = sv_delete(id)
    if obj == None:
      return f'Professor não encontrado',404
    
    return 'Professor removido: {}'.format(obj.nome), 201
