from flask import Blueprint, jsonify, request
from apps.disciplinas.services import IntegridadeException, IntegridadeReferencialException, sv_getLista, sv_add, sv_update, sv_delete
from apps.disciplinas.models import Disciplina

bp = Blueprint('bp_disciplinas', __name__)


@bp.route('/', methods = ['GET'])
def cadastrados():
    return jsonify(sv_getLista())


def unmarshalling():
    if request.json == None:
      return None
    return Disciplina().from_dict(request.json)


@bp.route('/', methods = ['POST'])
def adicionar():
  try:
    UnmObj = unmarshalling()
    if UnmObj == None:
      return f'Não há dados no corpo', 404

    lenNome = len(UnmObj.nome.replace(" ", ""))
    lenCoor = len(str(UnmObj.id_coordenador))
    if lenNome <= 2 or lenCoor < 5:
      return f'Dados inconsistentes', 404

    obj = sv_add(UnmObj.to_dict())

    if obj == None:
      return 'Disciplina já cadastrado: '+ UnmObj.to_dict()['nome'], 404

    if obj == 'prof_none':
      return 'Não existe id do coordenador: '+ UnmObj.to_dict()['nome'], 404
    
    return "Disciplina cadastrado: Disciplina {}".format(obj.nome), 201
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
      return f'Disciplina não encontrado',404
    if obj == 404:
      return f'Dados inconsistentes',404
    if obj == 403:
      return f'Id do professor não cadastrado',404
    return "Disciplina alterado: ID: {} Nome: {}".format(obj.id, obj.nome), 201


@bp.route('/<int:id>', methods = ['DELETE'])
def remover(id):
    obj = sv_delete(id)
    if obj == None:
      return f'Disciplina não encontrado',404
    
    return 'Disciplina removido: {}'.format(obj.nome), 201
