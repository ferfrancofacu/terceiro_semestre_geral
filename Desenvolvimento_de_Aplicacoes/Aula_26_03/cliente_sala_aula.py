# RA 1900519 - Fernando de Souza Franco
import requests as r

aluno = {}
aluno['id'] = 3
aluno['RA']  = '1900519'
aluno['nome']  = 'Fernando de Souza Franco'

print('lendo database completo')
ret = r.get('http://localhost:5002')
print(ret.json())

r.post('http://localhost:5002/alunos', json=aluno)

print('lendo database completo')
ret = r.get('http://localhost:5002')
print(ret.json())

print('lendo somente o aluno 1')
ret = r.get('http://localhost:5002/alunos/1')
print(ret.text)

print('lendo somente o aluno 99 ##erro##')
ret = r.get('http://localhost:5002/alunos/99')
print(ret.status_code)
print(ret.text)
