'''
Crie uma classe chamada Ingresso que possua um atributo valor e um 
método __str__() que retorne à informação do valor do ingresso. 

Crie uma classe IngressoVIP, que herda de Ingresso e possui um atributo
valor Adicional. O método __str__() da classe IngressoVIP deve considerar
que o valor do ingresso é o valor da superclasse somado ao valor Adicional do IngressoVIP. 

Crie uma classe para testar os objetos das classes Ingresso e IngressoVIP
Crie uma classe ColetorDeIngresso que recebe os ingressos e devolve o valor total.

'''
class Ingresso():
	valor = 0.0

	def __init__(self, valor):
		self.valor = valor

	def __str__(self):
		return str(self.valor)	

class IngressoVip(Ingresso):
	adicional = 0.0

	def __init__(self, valor, adicional):
		super().__init__(valor)
		self.adicional = adicional
		
	def __str__(self):
		return str(self.valor + self.adicional)


def test():
	ingresso = Ingresso(10.0)
	print(ingresso)
	
	ingressoVip = IngressoVip(10.0,-2.0)
	print(ingressoVip)

test()
