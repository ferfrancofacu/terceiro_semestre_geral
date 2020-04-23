from apps.alunos.models import Aluno

banco_de_dados = {
    'alunos' : [
        Aluno(1900519,'Fernando Franco'),
        Aluno(1900520,'Leo Ferreira'),
        Aluno(1900521,'Nicholas Ferreira'),
        Aluno(1900522,'Lucas Ano'),
        Aluno(1900523,'Lara Argento')
        ],
    'professores' : [
        Aluno(50000,'Valdemor Moraes'),
        Aluno(50001,'Antonio Fagundis'),
        Aluno(50002,'Mussu Alias'),
        Aluno(50003,'Zeze Di Camargo'),
        Aluno(50004,'Avril Lavigne')
        ]
}

def db_selectAll(param):
    lista = {}

    if param == None:
        return None

    if param == 'alunos':
        lista = banco_de_dados[param]

    return lista

def db_insert(param, obj):
    banco_de_dados[param].append(obj)

def db_remover(param, id):
    index = 0
    for al in db_selectAll(param):
        if id == al.id:
            db_selectAll(param).pop(index)
            return al
        index +=1
    return None
