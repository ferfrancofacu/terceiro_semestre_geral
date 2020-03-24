'''
1.
Implemente a função consulta que recebe uma agenda (um dicionário)
e uma pessoa, e retorna o telefone dessa pessoa.
'''


def consulta(agenda, pessoa):
    return agenda[pessoa]


'''
2.
Implemente a função adiciona que recebe uma agenda (um dicionário)
uma pessoa e um telefone, e adiciona o telefone dessa pessoa na agenda.

Adicionar um item num dicionário é simples:
dicionario['chave'] = valor
'''


def adiciona(agenda, pessoa, telefone):
    agenda[pessoa] = telefone


'''
Uma terceira feature que precisamos para a nossa agenda é
a possibilidade de verificar se uma pessoa já está na base de dados.

Simplesmente verificar agenda['pessoa'] não funciona:
se você acessar uma pessoa que não existe, o python dará um KeyError.

Precisamos, então usar o seguinte: 'chave' in dicionario
    Isso é um teste que retorna True se a chave está no dicionário,
    e False caso contrário.

Temos, por exemplo, os prints seguintes, que verificam se algumas
pessoas estão na agenda.
'''


'''
3.
Assim sendo, implemente a função verifica, que recebe uma agenda
e um nome de pessoa, e verifica se a pessoa está na agenda
(retorna True se a pessoa está e False caso contrário).
'''


def verifica(agenda, pessoa):
    return pessoa in agenda


'''
Para definir um dicionário vazio, fazemos o seguinte:
'''
vazio = {}


'''
4.
Usando seus conhecimentos de dicionário até agora, implemente a função
conta_letras que recebe uma palavra e retorna um dicionário com o número de
ocorrências de cada letra.

Por exemplo, conta_letras('abacaxi') deve retornar o seguinte dicionário:
    {'a':3,'b':1,'c':1,'x':1}

NÃO USE nenhuma função mágica do python. Escreva a lógica usando dicionários.

O seguinte trecho de código pode ser util:

palavra = 'ganancia'
nro_a = 0
for letra in palavra:
    print('estou olhando para', letra)
    if letra == 'a':
        nro_a = nro_a+1

Ele produz como resultado:
estou olhando para g
estou olhando para a
estou olhando para n
estou olhando para a
estou olhando para n
estou olhando para c
estou olhando para i
estou olhando para a

E no final, a variável nro_a vai estar valendo 3.
'''


def conta_letras(palavra):
    conta = {}
    for letra in palavra:
        if(letra in conta):
            conta[letra] += 1
        else:
            conta[letra] = 1
    return conta


'''
Agora, vamos usar listas e dicionários para criar uma agenda
um pouco mais completa. Veja o exemplo:
'''
agenda_melhor1 = {
    'lucas (professor)': {
        'email': 'lucas.goncalves@faculdadeimpacta.com.br',
        'telefones': [11999888999, 1177788899]
    },
    'maria': {
        'email': 'maria.aparecida@exemplo.com',
        'telefones': [84999777444]
    },
    'lucas': {
        'telefones': [1177788899]
    }
}

'''
5.
Implemente a função e-mail, que recebe uma agenda (dessas melhoradas, como
no exemplo acima) e uma pessoa. Ela retorna o e-mail da pessoa.

Não precisa se preocupar com o caso do registro da pessoa não ter e-mail
(faremos isso mais pra frente).
'''


def email(agenda, pessoa):
    if(pessoa in agenda):
        if('email' in agenda[pessoa]):
            return agenda[pessoa]['email']
        else:
            return 'e-mail não cadastrado'
    else:
        return 'pessoa não cadastrada'


'''
6.
Implemente a função telefone_principal, que recebe uma agenda (nessa versão
mais nova) e uma pessoa. Ela retorna o primeiro telefone da lista de
telefones da pessoa.
'''


def telefone_principal(agenda, pessoa):
    if(pessoa in agenda):
        if('telefones' in agenda[pessoa]):
            return agenda[pessoa]['telefones'][0]
        else:
            return 'telefone não cadastrado'
    else:
        return 'pessoa não cadastrada'


'''
7.
Se você quiser verificar todas as chaves de um dicionário,
pode fazer como a seguir:

for chave in agenda_melhor1:
    print(chave)

Ele vai produzir como saída:
lucas (professor)
maria
lucas

Assim sendo, implemente a função sem_email, que recebe uma agenda (nessa versão
mais nova) e retorna uma lista de todos os contatos sem e-mail.

Por exemplo, sem_email(agenda_melhor1) deve retornar uma
lista com um único contato: ['lucas']
'''


def sem_email(agenda):
    pessoas_sem_email = []
    for pessoa in agenda:
        if('email' not in agenda[pessoa]):
            pessoas_sem_email.append(pessoa)
    return pessoas_sem_email


'''
8.
Implemente uma função conta telefones, que recebe uma agenda (nessa versão
mais nova) e retorna a quantidade de números de telefone registrados.

Se houver telefones repetidos (o exemplo agenda_melhor1 tem!),
conte as repetições (então, para agenda_melhor1 a resposta deve
ser 4, por mais que o mesmo número apareça no item lucas
e no item lucas (professor)
'''


def conta_telefones(agenda):
    telefones = 0
    for pessoa in agenda:
        if('telefones' in agenda[pessoa]):
            telefones += len(agenda[pessoa]['telefones'])
    return telefones


'''
9.
Por último, vamos criar uma função conta_ocorrencias
que dirá quantas vezes um telefone ocorre na agenda.

Ela recebe uma agenda melhorada (um dicionário nesse formato
que estamos usando) e devolve um dicionário. As chaves são
os números de telefone, e os valores, às vezes que cada
número apareceu na agenda.
'''


def conta_ocorrencias(agenda):
    contagem = {}
    for pessoa in agenda:
        if('telefones' in agenda[pessoa]):
            for telefone in agenda[pessoa]['telefones']:
                if(telefone in contagem):
                    contagem[telefone] += 1
                else:
                    contagem[telefone] = 1
    return contagem
