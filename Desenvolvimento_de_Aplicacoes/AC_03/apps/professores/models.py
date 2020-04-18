class Professor(object):
  def __init__(self, id, id_professor, nome):
    self.id = id
    self.id_professor = id_professor
    self.nome = nome

  def to_dict(self):
    rep = {}
    rep['id'] = self.id
    rep['id_professor'] = self.id_professor
    rep['nome'] = self.nome

    return rep