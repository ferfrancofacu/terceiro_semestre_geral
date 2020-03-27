# RA 1900519 - Fernando de Souza Franco

from flask import Flask, jsonify, request

class Aluno():
    def __init__(self, id, nome, ra):
        self.id = id
        self.nome = nome
        self.ra = ra


class Professor():
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

database = {}
database["ALUNOS"] = []
database["PROFESSORES"] = []

app = Flask('app')

@app.route('/')
def ler_dados():
    return database

@app.route('/alunos', methods=['GET'])
def listar_alunos():
    return jsonify(database["ALUNOS"])

@app.route('/alunos/<int:id>', methods=['GET'])
def recuperar_aluno(id):
    for al in database["ALUNOS"]:
        if al["id"] == id:
            return jsonify(al)
    return {"erro": "aluno nao encontrado"}, 400

@app.route('/alunos', methods=["POST"])
def novo_aluno():
    if 'nome' in request.json.keys():
        aluno = request.json
        for al in database['ALUNOS']:
            if al["id"] == aluno['id']:
                return {"erro": "id ja utilizada"}, 400
        database['ALUNOS'].append(aluno)
        return aluno
    else:
        return {"erro": "aluno sem nome"}, 400


@app.route('/alunos/<int:id>', methods=["PUT"])
def atualiza_aluno(id):
    if 'nome' in request.json.keys():
        aluno = request.json
        for al in database['ALUNOS']:
            if al["id"] == id:
                al['nome'] = aluno['nome']
                return "ok", 200
        return {"erro": "aluno nao encontrado"}, 400
    else:
        return {"erro": "aluno sem nome"}, 400
        

@app.route('/alunos/<int:id>', methods=["DELETE"])
def deleta_aluno(id):
    for al in database['ALUNOS']:
        if al["id"] == id:
            database["ALUNOS"].remove(al)
            return "deleted", 200
    return {"erro": "aluno nao encontrado"}, 400


@app.route('/professores')
def listar_professores():
    return jsonify(database["PROFESSORES"])

@app.route('/professores/<int:id>', methods=['GET'])
def recuperar_professores(id):
    for al in database["PROFESSORES"]:
        if al["id"] == id:
            return jsonify(al)
    return {"erro": "professor nao encontrado"}, 400

@app.route('/professores', methods=["POST"])
def novo_professor():
    if 'nome' in request.json.keys():
        aluno = request.json
        for al in database['PROFESSORES']:
            if al["id"] == aluno['id']:
                return {"erro": "id ja utilizada"}, 400
        database['PROFESSORES'].append(aluno)
        return aluno
    else:
        return {"erro": "professor sem nome"}, 400


@app.route('/professores/<int:id>', methods=["PUT"])
def atualiza_professor(id):
    if 'nome' in request.json.keys():
        aluno = request.json
        for al in database['PROFESSORES']:
            if al["id"] == id:
                al['nome'] = aluno['nome']
                return "ok", 200
        return {"erro": "professor nao encontrado"}, 400
    else:
        return {"erro": "professor sem nome"}, 400
        

@app.route('/professores/<int:id>', methods=["DELETE"])
def deleta_professor(id):
    for al in database['PROFESSORES']:
        if al["id"] == id:
            database["PROFESSORES"].remove(al)
            return "deleted", 200
    return {"erro": "professor nao encontrado"}, 400

@app.route('/reseta', methods=['POST'])
def resetar_database():
    database['ALUNOS'] = []
    database['PROFESSORES'] = []
    return database


app.run(host='localhost', port=5002, debug=True)