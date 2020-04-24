from apps.db.datadb import db_selectAll, db_insert, db_remover
from apps.professores.models import Professor
from flask import jsonify, request

table_name = "professores"

class IntegridadeException(Exception):
    pass

class IntegridadeReferencialException(Exception):
    pass

def sv_getLista():
    return [row.to_dict() for row in db_selectAll(table_name)]

def sv_add(obj):
    if sv_consultar(None, obj["nome"]) != None:
        return None
        
    listaProfs = sv_getLista()
    ultid = listaProfs[len(listaProfs)-1]['id'] + 1
    obj = Professor().novoProf(ultid, obj["nome"])
    
    db_insert(table_name, obj)
    return obj   

def sv_consultar(id, nome):
    for al in sv_getLista():
        if nome == al['nome'] or id == al['id']:
            return al
    return None

def sv_update(id, obj):
    profRet = sv_consultar(id, None)
    if profRet == None:
        return None
    if obj['nome'] == None or len(obj['nome']) <= 2:
        return 404   

    prof_alt = Professor()
    prof_alt.id = profRet['id']
    prof_alt.nome = obj['nome'] 
    sv_delete(profRet['id'])
    db_insert(table_name, prof_alt)
    return prof_alt   

def sv_delete(id):
    for disc in db_selectAll('disciplinas'):
        if disc.id_coordenador == id:
            return 'bloqueado'

    obj = db_remover(table_name,id)
    if obj == None:
        return None
    return obj
