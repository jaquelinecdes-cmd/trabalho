# Lista pode ter string, int, float
# Listas armazenam vários valores em uma única variável.
# Elas são definidas usando colchetes
#Exemplo 1:
frutas = ["maçã", "banana", "laranja"]
print (frutas [0])
print (frutas [1])
print (frutas [2])

#algumas funções e métodos:
notas = [4, 5, 7.8 , 9]
notas.append (10) #adiciona valor na lista
notas.insert (10) #adiciona em posição especifica
notas.remove (10) # remove valor especifico

alunos = ["Ana", "Carlos", "Maria", "João", "Ana", "Beatriz", "Davi"]

#1) adicionar um novo aluno
alunos.append("Ellen")
print(alunos)

#2) inserir aluno em posição específica
alunos.insert(4, "Mateus")
print("Após inserir Mateus na posição 4:", alunos)

#3) remover um aluno específico
alunos.remove("Carlos")
print("Após remover Carlos:", alunos)

#4) remover o último aluno
alunos.pop()
print("Após remover o último aluno:", alunos)

#5) verificar posição de um aluno
posicao = alunos.index("Maria")
print("Maria está na posição:", posicao)

#6) contar quantas vezes um nome aparece
quantidade = alunos.count("Ana")
print("Ana aparece ", quantidade, "vezes")

#7) ordenar a lista
ordenada = alunos.sort()
print("Lista em ordem alfabética:", alunos)

#8) inverter a ordem da lista
alunos.reverse()
print("Lista invertida:", alunos)

#9)limpar a lista
alunos.clear()
print("Lista após limpar:", alunos)

#Exercício:
# 1) Lista 
cores = ["vermelho", "azul", "verde", "amarelo", "rosa"]
print("Lista:", cores)