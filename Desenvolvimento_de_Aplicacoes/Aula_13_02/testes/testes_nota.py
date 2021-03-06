import unittest
from ..resultado_com_pai import resultado_com_pai

class TestNota(unittest.TestCase):

    # Testes que verificam se a menor AC é descartada.

    def test_01a_media_acs_descarta_menor(self):
        r = resultado_com_pai(0.9, 10, 10, 10, 1, 10, 0, 0, 0, 0, 0, 10, 10, 10)
        self.assertEqual(r, (3, 'RM'))

    def test_01b_media_acs_descarta_menor(self):
        r = resultado_com_pai(0.9, 5.5, 4, 1, 6, 4.5, 0, 0, 0, 0, 0, 10, 10, 10)
        self.assertEqual(r, (1.5, 'RM'))

    def test_01c_media_acs_descarta_menor(self):
        r = resultado_com_pai(0.9, 7, 2, 7, 7, 7, 0, 0, 0, 0, 0, 10, 10, 10)
        self.assertEqual(r, (2, 'RM'))

    # Testes que verificam se apenas a melhor prova é considerada.

    def test_02a_escolhe_melhor_prova(self):
        r = resultado_com_pai(0.9, 0, 0, 0, 0, 0, 3, 4, 0, 0, 0, 10, 10, 10)
        self.assertEqual(r, (1.5, 'RM'))

    def test_02b_escolhe_melhor_prova(self):
        r = resultado_com_pai(0.9, 0, 0, 0, 0, 0, 6, 4, 0, 0, 0, 10, 10, 10)
        self.assertEqual(r, (2.5, 'RM'))

    # Testes que verificam se a menor nota do PAI é descartada.

    def test_03a_media_pai_descarta_menor(self):
        r = resultado_com_pai(0.9, 0, 0, 0, 0, 0, 0, 0, 9, 18, 22, 10, 10, 10)
        self.assertEqual(r, (1, 'RM'))

    def test_03b_media_pai_descarta_menor(self):
        r = resultado_com_pai(0.9, 0, 0, 0, 0, 0, 0, 0, 16, 2, 20, 10, 10, 10)
        self.assertEqual(r, (1, 'RM'))

    # Testes que verificam como se dá o ajuste das notas do PAI maiores que metade dos acertos da prova.

    def test_04a_media_pai_porcentagem_acertos(self):
        r = resultado_com_pai(0.9, 0, 0, 0, 0, 0, 0, 0, 22, 22, 22, 10, 10, 10) # 44% em cada prova PAI.
        self.assertEqual(r, (1.5, 'RM'))

    def test_04b_media_pai_porcentagem_acertos(self):
        r = resultado_com_pai(0.9, 0, 0, 0, 0, 0, 0, 0, 23, 23, 23, 10, 10, 10) # 46% em cada prova PAI.
        self.assertEqual(r, (1.5, 'RM'))

    def test_04c_media_pai_porcentagem_acertos(self):
        r = resultado_com_pai(0.9, 0, 0, 0, 0, 0, 0, 0, 24, 24, 24, 10, 10, 10) # 48% em cada prova PAI.
        self.assertEqual(r, (1.5, 'RM'))

    def test_04d_media_pai_porcentagem_acertos(self):
        r = resultado_com_pai(0.9, 0, 0, 0, 0, 0, 0, 0, 25, 25, 25, 10, 10, 10) # 50% em cada prova PAI. Nota do PAI vai para 6.
        self.assertEqual(r, (2, 'RM'))

    def test_04e_media_pai_porcentagem_acertos(self):
        r = resultado_com_pai(0.9, 0, 0, 0, 0, 0, 0, 0, 29, 29, 29, 10, 10, 10) # 58% em cada prova PAI. Nota do PAI vai para 6.
        self.assertEqual(r, (2, 'RM'))

    def test_04f_media_pai_porcentagem_acertos(self):
        r = resultado_com_pai(0.9, 0, 0, 0, 0, 0, 0, 0, 30, 30, 30, 10, 10, 10) # 60% em cada prova PAI. Nota do PAI vai para 8.
        self.assertEqual(r, (2.5, 'RM'))

    def test_04g_media_pai_porcentagem_acertos(self):
        r = resultado_com_pai(0.9, 0, 0, 0, 0, 0, 0, 0, 37, 37, 37, 10, 10, 10) # 74% em cada prova PAI. Nota do PAI vai para 8.
        self.assertEqual(r, (2.5, 'RM'))

    def test_04h_media_pai_porcentagem_acertos(self):
        r = resultado_com_pai(0.9, 0, 0, 0, 0, 0, 0, 0, 38, 38, 38, 10, 10, 10) # 76% em cada prova PAI. Nota do PAI vai para 10.
        self.assertEqual(r, (3, 'RM'))

    def test_04i_media_pai_porcentagem_acertos(self):
        r = resultado_com_pai(0.9, 0, 0, 0, 0, 0, 0, 0, 50, 50, 50, 10, 10, 10) # 100% em cada prova PAI.
        self.assertEqual(r, (3, 'RM'))

    # Testes que verificam como se dá o ajuste das notas do PAI de acordo com os percentis de acertos.

    def test_05a_media_pai_percentis(self):
        r = resultado_com_pai(0.9, 0, 0, 0, 0, 0, 0, 0, 37, 37, 37, 1, 1, 7) # Nota do PAI seria 7.4, que é jogado para 8, mas como está acima do percentil80, vai para 10.
        self.assertEqual(r, (3, 'RM'))

    def test_05b_media_pai_percentis(self):
        r = resultado_com_pai(0.9, 0, 0, 0, 0, 0, 0, 0, 37, 37, 37, 1, 1, 8) # Nota do PAI seria 7.4, que é jogado para 8, mas como está igual ao percentil80, vai para 10.
        self.assertEqual(r, (3, 'RM'))

    def test_05c_media_pai_percentis(self):
        r = resultado_com_pai(0.9, 0, 0, 0, 0, 0, 0, 0, 20, 20, 20, 1, 2, 3) # Nota do PAI seria 4, mas como está acima do percentil80, vai para 10.
        self.assertEqual(r, (3, 'RM'))

    def test_05d_media_pai_percentis(self):
        r = resultado_com_pai(0.9, 0, 0, 0, 0, 0, 0, 0, 20, 20, 20, 1, 2, 4) # Nota do PAI seria 4, mas como está igual ao percentil80, vai para 10.
        self.assertEqual(r, (3, 'RM'))

    def test_05e_media_pai_percentis(self):
        r = resultado_com_pai(0.9, 0, 0, 0, 0, 0, 0, 0, 20, 20, 20, 1, 2, 9) # Nota do PAI seria 4, mas como está entre o percentil60 é o percentil80, vai para 8.
        self.assertEqual(r, (2.5, 'RM'))

    def test_05f_media_pai_percentis(self):
        r = resultado_com_pai(0.9, 0, 0, 0, 0, 0, 0, 0, 20, 20, 20, 1, 4, 9) # Nota do PAI seria 4, mas como é igual ao percentil60, vai para 8.
        self.assertEqual(r, (2.5, 'RM'))

    def test_05g_media_pai_percentis(self):
        r = resultado_com_pai(0.9, 0, 0, 0, 0, 0, 0, 0, 20, 20, 20, 1, 5, 9) # Nota do PAI seria 4, mas como está entre o percentil40 é o percentil60, vai para 6.
        self.assertEqual(r, (2, 'RM'))

    def test_05h_media_pai_percentis(self):
        r = resultado_com_pai(0.9, 0, 0, 0, 0, 0, 0, 0, 20, 20, 20, 4, 5, 9) # Nota do PAI seria 4, mas como é igual ao percentil40, vai para 6.
        self.assertEqual(r, (2, 'RM'))

    def test_05i_media_pai_percentis(self):
        r = resultado_com_pai(0.9, 0, 0, 0, 0, 0, 0, 0, 20, 20, 20, 5, 7, 9) # Nota do PAI é 4, que assim fica por ser menor que o percentil40.
        self.assertEqual(r, (1, 'RM'))

    def test_05j_media_pai_percentis(self):
        r = resultado_com_pai(0.9, 0, 0, 0, 0, 0, 0, 0, 37, 37, 37, 9, 9, 9) # Nota do PAI é 8, mesmo que esteja abaixo do percentil40, pois o percentil40 é bem alto.
        self.assertEqual(r, (2.5, 'RM'))

    # Testes que verificam como as faltas afetam o conceito.

    def test_06a_faltas(self):
        r = resultado_com_pai(0.9, 2, 2, 2, 2, 2, 2, 2, 10, 10, 10, 10, 10, 10)
        self.assertEqual(r, (2, 'RM'))

    def test_06b_faltas(self):
        r = resultado_com_pai(0.2, 2, 2, 2, 2, 2, 2, 2, 10, 10, 10, 10, 10, 10)
        self.assertEqual(r, (2, 'RMF'))

    def test_06c_faltas(self):
        r = resultado_com_pai(0.2, 10, 10, 10, 10, 10, 10, 10, 50, 50, 50, 1, 2, 3)
        self.assertEqual(r, (10, 'RF'))

    def test_06d_faltas(self):
        r = resultado_com_pai(0.9, 10, 10, 10, 10, 10, 10, 10, 50, 50, 50, 1, 2, 3)
        self.assertEqual(r, (10, 'AP'))

    # Testes que verificam como a nota é composta.

    def test_07a_composicao_das_notas(self):
        r = resultado_com_pai(0.9, 10, 10, 10, 10, 10, 0, 0, 0, 0, 0, 10, 10, 10)
        self.assertEqual(r, (3, 'RM'))

    def test_07b_composicao_das_notas(self):
        r = resultado_com_pai(0.9, 0, 0, 0, 0, 0, 10, 10, 0, 0, 0, 10, 10, 10)
        self.assertEqual(r, (4, 'RM'))

    def test_07c_composicao_das_notas(self):
        r = resultado_com_pai(0.9, 0, 0, 0, 0, 0, 0, 0, 10, 50, 50, 10, 10, 10)
        self.assertEqual(r, (3, 'RM'))

    def test_07d_composicao_das_notas(self):
        r = resultado_com_pai(0.9, 8, 8, 8, 8, 8, 0, 8, 12, 12, 12, 10, 10, 10)
        self.assertEqual(r, (6.5, 'AP'))

    # Testes que verificam a nota mínima para a aprovação.

    def test_08a_arredondamento_das_notas(self):
        r = resultado_com_pai(0.9, 10, 10, 10, 10, 10, 2.24 / 0.4, 0, 0, 0, 0, 10, 10, 10) # Média sem arredondamento é 5.24.
        self.assertEqual(r, (5, 'RM'))

    def test_08b_arredondamento_das_notas(self):
        r = resultado_com_pai(0.9, 10, 10, 10, 10, 10, 2.25 / 0.4, 0, 0, 0, 0, 10, 10, 10) # Média sem arredondamento é 5.25.
        self.assertEqual(r, (5.5, 'RM'))

    def test_08c_arredondamento_das_notas(self):
        r = resultado_com_pai(0.9, 10, 10, 10, 10, 10, 2.74 / 0.4, 0, 0, 0, 0, 10, 10, 10) # Média sem arredondamento é 5.74.
        self.assertEqual(r, (5.5, 'RM'))

    def test_08d_arredondamento_das_notas(self):
        r = resultado_com_pai(0.9, 10, 10, 10, 10, 10, 2.75 / 0.4, 0, 0, 0, 0, 10, 10, 10) # Média sem arredondamento é 5.75.
        self.assertEqual(r, (6, 'AP'))

def runTests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestNota)
    unittest.TextTestRunner(verbosity = 2, failfast = True).run(suite)

if __name__ == '__main__':
    runTests()
