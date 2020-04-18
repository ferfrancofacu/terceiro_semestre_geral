class Marca(object):
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome


class Veiculo(object):
    def __init__(self, marca_id=None, modelo=None, preco=None, placa=None):
        self.marca_id = marca_id
        self.modelo = modelo
        self.preco = preco
        self.placa = placa

    def to_dict(self):
        data = {}
        data['marca_id'] = self.marca_id
        data['modelo'] = self.modelo
        data['preco'] = self.preco
        data['placa'] = self.placa

        return data

    def from_dict(self, data):
        self.marca_id = data['marca_id']
        self.modelo = data['modelo']
        self.preco = data['preco']
        self.placa = data['placa']
