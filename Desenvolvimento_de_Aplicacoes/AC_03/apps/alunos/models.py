class Aluno(object):
    def __init__(self,id=None, nome=None):
        self.id = id
        self.nome = nome

    def novoAluno(self,id, nome):
        self.id = id
        self.nome = nome
        return self    

    def to_dict(self):
        rep = {}
        rep['id'] = self.id
        rep['nome'] = self.nome
        return rep

    def from_dict(self, data):
          self.nome = data.get('nome', None)
          return self
