tupla1 = ('str1', 'str2')

print(tupla1)

v1, v2 = tupla1
v3 = tupla1
v4 = tupla1[0]
v5 = tupla1[1]

print(v1)
print(v2)
print(v3)
print(v4)
print(v5)

def nome_completo(inicial, meio, final):
  return inicial, meio, final

t1, t2, t3 = nome_completo('emilio', 'murta', 'resende')
print(t1)
print(t2)
print(t3)