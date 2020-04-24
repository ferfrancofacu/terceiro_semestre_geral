from apps.alunos.models import Aluno
from apps.professores.models import Professor
from apps.disciplinas.models import Disciplina

banco_de_dados = {
    'alunos' : [
        Aluno(1900519,'Fernando Franco'),
        Aluno(1900520,'Leo Ferreira'),
        Aluno(1900521,'Nicholas Ferreira'),
        Aluno(1900522,'Lucas Ano'),
        Aluno(1900523,'Lara Argento')
        ],
    'professores' : [
        Professor(50000,'Valdemor Moraes'),
        Professor(50001,'Antonio Fagundis'),
        Professor(50002,'Mussu Alias'),
        Professor(50003,'Zeze Di Camargo'),
        Professor(50004,'Avril Lavigne'),
        Professor(50005,'Avril Lavigne'),
        Professor(50006,'Wando Lima'),
        Professor(50007,'Lucas Duarte')
        ],
    'disciplinas' : [
        Disciplina(1001,'Aplicações Web'        ,1,'plano de ensino do professor',120,50000),
        Disciplina(1002,'Devops'                ,1,'plano de ensino do professor',120,50001),
        Disciplina(1003,'Banco de dados'        ,1,'plano de ensino do professor',120,50002),
        Disciplina(1004,'Analise de dados'      ,1,'plano de ensino do professor',120,50003),
        Disciplina(1005,'Engenharia de Software',1,'plano de ensino do professor',120,50004)
        ]
}

def db_selectAll(param):
    if param == None:
        return None
    return banco_de_dados[param]

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
