# são usados para combinar condições (and,or, not) - valores booleanos (true e false)

# and:ambos valores precisa ser verdadeiros para ser True
idade = 20
tem_carteira = True
print("Tem carteira?", idade >= 18 and tem_carteira)

# or: ao menos um dos valores precisa ser verdadeiro para ser True
idade = 16
tem_autorizacao = True
print("Tem autorização para entrar?", idade >= 18 or tem_autorizacao)

# not: inverte o valor lógico (True vira False e vice-versa)
idade = 20
print(not (idade < 18))

# Exercicio 1:

senha = input("Digite aqui sua senha:  ")
usuario_ativo = True
senha_correta = "1234"   #tr
acesso_permitido = usuario_ativo and (senha == senha_correta)
print("Acesso permitido?", acesso_permitido)

# Exercício 2:

valor_compra = int(input("Digite o valor da compra: R$ "))
cliente_membro = True
tem_desconto = valor_compra >= 100 or cliente_membro
print("O cliente tem desconto?", tem_desconto)