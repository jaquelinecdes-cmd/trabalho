 # pode-se usar o string (texto) e float (número com casa decimais])
# dentro do "if" e do "elif" SEMPRE usar operadores de comparação 

# Exemplo 1:
idade = int (input ("Digite sua idade: "))
if idade >=18:
    print ("Pode dirigir")
else: 
    print ("Não pode dirigir")

# Exemplo 2:
    Nota = float (input("Digite a nota: "))
if Nota >= 7:
    print ("Aprovado")
elif Nota >=5:
    print ("Recuperação")
else: 
    print ("Reprovado")

    # Exemplo 3:
    idade = int (input ("Digite sua idade: "))
tem_carteira = True
if idade >=18 and tem_carteira:
    print ("Pode dirigir")
else: 
    print ("Não pode dirigir")

    # Exemplo 4:
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
if idade >= 1 and idade <= 12:
  print(nome, "é criança")
elif idade > 12 and idade < 18:
  print(nome, "é adolescente")
elif idade >= 18 and idade < 60:
  print(nome, "é adulto")
elif idade >=60:
  print(nome, "é idoso")
else:
   print ("Valor inválido")

   # Exemplo 4:
   numero1 = int (input("Digite o 1º Número: "))
numero2 = int (input("Digite o 2º Número: "))
if numero1 > numero2:
    print("O maior número é:", numero1)
elif numero2 > numero1:
    print("O maior número é:", numero2)

    #Exemplo 5:
    numero = int(input("Digite um número: "))
if numero % 2 == 0:
    print("O número é Par")
else:
    print("O número é Ímpar")
