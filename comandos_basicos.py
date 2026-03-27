nome = input ("Digite o seu nome: ") # o input só recebe texto (string)
print ("Nome digitado:", nome)

numero1 = int(input("Digite o ano do seu nascimento: ")) # para o input receber diferente precisa informar o que quer
numero2 = int(input("Digite o ano atual: "))
resultado = numero2 - numero1
print("A sua idade é:", resultado)

# para contar o tamanho do texto, usa-se o "len"
palavra = "Programação"
print(len(palavra))

# Operadores de comparação (true or false): != (diferente de), < (menor que), < (maior que) , == (igual) ,  <= , >=
# sempre compara da esquerda para direita. 
# os operadores == e != pode ser usado para comparar textos, mas estes operadores são para números.