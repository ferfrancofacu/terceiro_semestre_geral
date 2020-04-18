from flask import Blueprint, jsonify, request
from apps.alunos.models import Aluno

alunos = [
    Aluno(1, 'RA 1900519','Fernando Franco'),
    Aluno(2, 'RA 1900520','Leo Ferreira'),
    Aluno(3, 'RA 1900521','Nicholas Ferreira'),
    Aluno(4, 'RA 1900522','Lucas Ano'),
    Aluno(5, 'RA 1900523','Lara Argento')
  ]

bp = Blueprint('alunos', __name__)

@bp.route('/', methods = ['GET'])
def list_all():
  return jsonify([aluno.to_dict() for aluno in alunos])

@bp.route('/', methods = ['POST'])
def adicionarAluno():
  ra = request.form['ra']
  nome = request.form['nome']
  ultid = alunos[len(alunos)-1].id + 1

  for al in alunos:
    if ra == al.ra and nome == al.nome:
      return 'Aluno já cadastrado!',400
  
  alunos.append(Aluno(ultid, ra,nome))
  return list_all(),201

  @bp.route('/<string:ra>', methods = ['PUT'])
  def alterarAluno(ra):
    ra = request.form['ra']
    nome = request.form['nome']

    for al in alunos:
      if ra == al.ra:
        al.nome = nome
