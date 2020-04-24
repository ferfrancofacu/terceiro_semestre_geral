from apps.db.datadb import db_selectAll, db_insert, db_remover
from apps.disciplinas.models import Disciplina
from flask import jsonify, request

table_name = "disciplinas"

class IntegridadeException(Exception):
    pass

class IntegridadeReferencialException(Exception):
    pass

def sv_getLista():
    return [row.to_dict() for row in db_selectAll(table_name)]


def sv_add(obj):
    if sv_consultar(None, obj["nome"]) != None:
        return None


    for prof in db_selectAll('professores'):
        if obj['id_coordenador'] == prof.id:
            listaDiscs = sv_getLista()
            ultid = listaDiscs[len(listaDiscs)-1]['id'] + 1
            obj = Disciplina().novoDisc(ultid, obj)
            db_insert(table_name, obj)  
            return obj
    return 'prof_none'

        
def sv_consultar(id, nome):
    for al in sv_getLista():
        if nome == al['nome'] or id == al['id']:
            return al
    return None


def sv_update(id, obj):
    if obj['nome'] == None or len(obj['nome']) <= 2:
        return 404 

    discRet = sv_consultar(id, None)
    if discRet == None:
        return None

    for prof in db_selectAll('professores'):
        if prof.id == obj['id_coordenador']:
            disc_alt = Disciplina()
            disc_alt.id = discRet['id']

            disc_alt.nome = obj['nome'] 
            disc_alt.status = obj['status'] 
            disc_alt.plano_ensino = obj['plano_ensino']
            disc_alt.carga_horaria = obj['carga_horaria']
            disc_alt.id_coordenador = obj['id_coordenador']

            sv_delete(id)
            db_insert(table_name, disc_alt)
            return disc_alt  
    return 403

def sv_delete(id):
    obj = db_remover(table_name,id)
    if obj == None:
        return None
    return obj
