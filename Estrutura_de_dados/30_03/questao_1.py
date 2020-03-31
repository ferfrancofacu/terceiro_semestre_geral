def funcao1(a,b):
    cont = 0
    for i in range(a):
        for j in range(b):
           cont = cont + 1 #marca!
    return cont

def funcao2(a,b):
    cont=0
    for i in range(a):
        for j in range(b):
            cont = cont+1 #marca!
    for i in range(a):
        for j in range(b):
            cont = cont+1 #marca!
    return cont

def funcao10(lista):
  i=0
  for e in lista:
      for k in [0,1,2,3,4,5,6,7,8,9]:
        i = i+1 #marca!
  return i


lista = [0,1,2,3,4,5,6,7,8,9]
print(funcao10(lista))

def procura_casal_22(lista):
   for i in lista:
       if 22-i in lista:
           return True
   return False

print(procura_casal_22(lista))