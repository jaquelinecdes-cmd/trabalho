#retorna todas as chaves
# keys() d.keys()

#retorna todos valores
#values() d.values()

#retorna chave e valor 
# items() d.items()

#acessa valor com segurança 
# get() d.get("nome")

#atualiza dicionário 
# update()  d.update({"idade":21})

#remove chave 
# pop() d.pop("idade")

#remove último item 
# popitem()  d.popitem()

#limpa dicionário 
# clear() d.clear()

#copia dicionário 
# copy() novo = d.copy()

#Exercício:
produto = {
    "nome": "Notebook",
    "preço": 3500,
    "estoque": 8
}
produto ["marca"] ="ACER" # adiciona valores na chave mesmo fora da chave

# 1) Mostrar todas as chaves
print("Chaves:", produto.keys())

# 2) Mostrar todos os valores
print("Valores:", produto.values())

# 3) Mostrar chave e valor
print("Chave e valor:", produto.items())

# 4) Pegar um valor pela chave
print("Valor da chave estoque:", produto.get("estoque"))

# 5) Atualizar uma informação
produto.update({"preço": 3900})
print("Após atualizar o preço:", produto)

# Remover um elemento específico
produto.pop("estoque")
print("Após remover o estoque:", produto)

# Remover o último elemento adicionado (Python 3.7+ mantém a ordem)
produto.popitem()
print("Após remover o último elemento:", produto)

#Exercício
# 3) Dicionário
aluno = {
    "nome": "Maria",
    "idade": 21,
    "curso": "Engenharia"
}
print("Informações do aluno:", aluno)
