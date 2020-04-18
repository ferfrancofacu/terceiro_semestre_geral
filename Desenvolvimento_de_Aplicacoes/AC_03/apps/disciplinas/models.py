class Disciplina():
  def __init__(self, id, nome, status, plano_ensino, carga_horaria, id_coordenador):
    self.id = id
    self.nome = nome
    self.status = status
    self.plano_ensino = plano_ensino
    self.carga_horaria = carga_horaria
    self.id_coordenador = id_coordenador

  def to_dict(self):
    rep = {}
    rep['id'] = self.id
    rep['nome'] = self.nome
    rep['status'] = self.status
    rep['plano_ensino'] = self.plano_ensino
    rep['carga_horaria'] = self.carga_horaria
    rep['id_coordenador'] = self.id_coordenador
    
    return rep