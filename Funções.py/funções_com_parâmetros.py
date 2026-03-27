#Função com Parâmetros
"""Parâmetros são valores que a função recebe para trabalhar
é como uma váriavel que está recebendo um valor"""

"""Exemplo com Parâmetro"""
def saudacao(nome):
 print("Olá", nome)

"""Chamando a função"""
saudacao("Maria")
saudacao("Carlos")

#Função com Dois Parâmetros:
"""Exemplo 1:"""
def soma(a, b):
 resultado = a + b
 print(a, "+", b, "=", resultado)

"""Chamando a função:"""
soma(5, 3)
soma(a=4, b=2) # pode pôr explicito qual o parametro
soma(b=3, a=7)
soma(5, 6)


"""Exemplo 2:"""
def soma(a=None, b=None):  # None significa "nada"
    if a != None and b != None:
        resultado = a + b
        print(resultado)
    else:
        print("Não consigo fazer soma com apenas um valor")

"""Chamando a função:"""
soma(a=2.5, b=5)
soma(5)


