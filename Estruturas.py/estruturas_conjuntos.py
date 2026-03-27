#Conjuntos armazenam valores únicos (sem repetição) é + usado para remover duplicidade
numeros = {1,2,3,3,4}
print(numeros) # resultado: {1,2,3,4} 1 dos nº 3 foi excluído.
#OU
print (set(numeros))


a = {1,2,3}
b = {3,4,5}
print(a.union(b))
print(a.intersection(b))

#Exercício
# 4) Conjunto
conjunto = {"maçã", "banana", "laranja"}
print("Conjunto:", conjunto)