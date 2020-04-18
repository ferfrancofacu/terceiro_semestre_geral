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
	def __init__(self, valor):
		self.__valor = valor

	def __str__(self):
		return 'R${:.2f}'.format(self.__valor)

	@property
	def valor_total(self):
		return self.__valor

class IngressoVip(Ingresso):
	def __init__(self, valor, adicional):
		super().__init__(valor)
		self.__adicional = adicional
		
	@property
	def __str__(self):
		return super().valor_total + self.__adicional

class ColetorDeIngresso:
	def __init__(self):
		self.total = 0.0
	def recebe(self, ingresso):
		self.total += ingresso.valor_total
	def __str__(self):
		return 'R${:.2f}'.format(self.total)

if __name__ == '__main__':
	ingresso = Ingresso(100.0)
	print(Ingresso)

	IngressoVip = IngressoVip(100.0, 50.0)
	print(IngressoVip)

	coletor = ColetorDeIngresso()
	coletor.recebe(ingresso)
	coletor.recebe(IngressoVip)
