class Aluno():
  def __init__(self, id, ra, nome):
    self.id = id
    self.ra = ra
    self.nome = nome

  def to_dict(self):
    rep = {}
    rep['id'] = self.id
    rep['ra'] = self.ra
    rep['nome'] = self.nome

    return rep