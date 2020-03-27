# RA 1900519 - Fernando de Souza Franco

from flask import Flask, jsonify, request

class Aluno():
        def __init__(self, id, nome,ra):
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
    return jsonify(database)

@app.route('/alunos',methods=['GET'])
def listar_alunos():
    return jsonify(database["ALUNOS"])    

@app.route('/alunos/<int:id>', methods=['GET'])
def recuoerar_alunos(id):
    for aluno in database['ALUNOS']:
        if aluno['id'] == id:
            return jsonify(aluno)
    return 'não encontrado', 404      

@app.route('/alunos', methods=['POST'])
def novo_aluno():
    novo_aluno = request.json
    database['ALUNOS'].append(novo_aluno)
    return jsonify(database['ALUNOS']) 

@app.route('/reseta',methods=['POST'])
def reseta():
    database['ALUNOS'] = []
    database['PROFESSORES'] = []
    return {} ,200

@app.route('/alunos/<int:id>', methods=["PUT"])
def atualiza_aluno(id):
    if 'nome' in request.json.keys():
        aluno = request.json
        for al in database['ALUNOS']:
            if al["id"] == id:
                al['nome'] = aluno['nome']
                return "ok", 200
    return {"erro": "aluno nao encontrado"}, 400    

@app.route('/alunos/<int:id>', methods=["PUT"])
def id_inexistente(id):
    if 'nome' in request.json.keys():
        aluno = request.json
        for al in database['ALUNOS']:
            if al["id"] == id:
                al['nome'] = aluno['nome']
                return "ok", 200
    return {"erro": "aluno nao encontrado"}, 400       

@app.route('/alunos/<int:id>', methods=['DELETE'])
def deletar(id):
    for aluno in database['ALUNOS']:
        if aluno['id'] == id:
            database["ALUNOS"].remove(aluno)
            return "deleted", 200
    return 'não encontrado', 404   


@app.route('/professores')
def listar_professores():
    return jsonify(database['PROFESSORES'])    

@app.route('/professores', methods=['POST'])
def novo_professores():
    novo_aluno = request.json
    database['PROFESSORES'].append(novo_aluno)
    return jsonify(database['PROFESSORES'])     

@app.route('/professores/<int:id>', methods=['GET'])
def recuoerar_professores(id):
    for aluno in database['PROFESSORES']:
        if aluno['id'] == id:
            return jsonify(aluno)
    return 'não encontrado', 404  

app.run(host='localhost', port=5002, debug=True)