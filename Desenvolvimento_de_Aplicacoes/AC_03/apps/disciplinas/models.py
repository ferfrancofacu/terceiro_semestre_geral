class Disciplina(object):
    def __init__(self,id=None, nome=None, status=None, plano_ensino=None, carga_horaria=None, id_coordenador=None):
        self.id = id
        self.nome = nome
        self.status = status 
        self.plano_ensino = plano_ensino
        self.carga_horaria = carga_horaria 
        self.id_coordenador = id_coordenador

    def novoDisc(self,id, obj):
        self.id = id
        self.nome = obj['nome']
        self.status = obj['status']
        self.plano_ensino = obj['plano_ensino']
        self.carga_horaria = obj['carga_horaria'] 
        self.id_coordenador = obj['id_coordenador']
        return self    

    def to_dict(self):
        rep = {}
        rep['id'] = self.id
        rep['nome'] = self.nome
        rep['status'] = self.status 
        rep['plano_ensino'] = self.plano_ensino
        rep['carga_horaria'] = self.carga_horaria 
        rep['id_coordenador'] = self.id_coordenador
        return rep

    def from_dict(self, data):
          self.id = data.get('id', None)
          self.nome = data.get('nome', None)
          self.status = data.get('status', None)
          self.plano_ensino = data.get('plano_ensino', None)
          self.carga_horaria = data.get('carga_horaria', None)
          self.id_coordenador = data.get('id_coordenador', None)
          return self
