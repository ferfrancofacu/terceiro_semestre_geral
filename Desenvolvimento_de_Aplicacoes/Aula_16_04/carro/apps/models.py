class Marca(object):
    def __init__(self, id, nome):
      self.id = id
      self.nome = nome

class Veiculo(object):
    def __init__(self, marca_id, modelo, preco, placa):
        self.marca_id = marca_id
        self.modelo = modelo
        self.preco = preco
        self.placa = placa