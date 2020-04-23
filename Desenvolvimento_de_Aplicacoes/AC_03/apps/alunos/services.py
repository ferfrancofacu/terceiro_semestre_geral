from apps.db.datadb import db_selectAll, db_insert, db_remover
from apps.alunos.models import Aluno
from flask import jsonify, request

table_name = "alunos"

class IntegridadeException(Exception):
    pass

class IntegridadeReferencialException(Exception):
    pass

def sv_getLista():
    return [row.to_dict() for row in db_selectAll(table_name)]

def sv_add(objAluno):
    if sv_consultar(None, objAluno["nome"]) != None:
        return None

    listaAlunos = sv_getLista()
    ultid = listaAlunos[len(listaAlunos)-1]['id'] + 1
    objAluno = Aluno().novoAluno(ultid,objAluno["nome"])
    
    db_insert(table_name, objAluno)
    return objAluno   

def sv_consultar(id, nome):
    for al in sv_getLista():
        if nome == al['nome'] or id == al['id']:
            return al
    return None

def sv_update(id, objAluno):
    alunoRet = sv_consultar(id, None)
    if alunoRet == None:
        return None
    if objAluno['nome'] == None or len(objAluno['nome']) <= 2:
        return 404   
    
    alunoRet['id'] = id
    alunoRet['nome'] = objAluno['nome']   
    aluno_alt = Aluno()
    aluno_alt.id = id
    aluno_alt.nome = objAluno['nome']
    sv_delete(id)
    db_insert(table_name, aluno_alt)
    return alunoRet   

def sv_delete(id):
    obj = db_remover(table_name,id)
    if obj == None:
        return None
    return obj

