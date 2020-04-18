from flask import Blueprint, jsonify
from apps.disciplinas.models import Disciplina

#id, nome, status, plano_ensino, carga_horaria, id_coordenador

disciplinas = [
  Disciplina(1,'Banco de Dados',1,'Noite',120,1),
  Disciplina(2,'Infra Estrutura',1,'Noite',80,2),
  Disciplina(3,'Analitycs',0,'Noite',120,3),
  Disciplina(4,'Desenvolvimento de Sistemas',1,'Noite',200,4)
]

bp = Blueprint('disciplinas', __name__)

@bp.route('/')
def list_all():
  return jsonify([disciplina.to_dict() for disciplina in disciplinas])
 