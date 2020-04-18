from flask import Blueprint, jsonify
from apps.professores.models import Professor

professores = [
  Professor(1,'RP-15000','Joaquim'),
  Professor(2,'RP-15001','Chaves'),
  Professor(3,'RP-15002','Chapolin'),
  Professor(4,'RP-15003','Power Range Branco')
  ]

bp = Blueprint('professores', __name__)

@bp.route('/')
def list_all():
  return jsonify([professor.to_dict() for professor in professores])