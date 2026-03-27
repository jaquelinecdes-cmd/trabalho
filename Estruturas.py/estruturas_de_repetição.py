#for, while, break e continue
# usadas quando queremos repetir uma ação sem precisar escrever o mesmo código várias vezes.

#FOR: já temos a quantidade de vezes haverá repetição
for valor in range(5):
 print(valor)
 #exemplo 1:
 for valor in range(5):
    if valor == 3:
        print(valor, "Chegou no 3")
    else:
        print(valor)

#Exemplo 2:
nomes = ["Ana", "Carlos", "João"]
for nome in nomes:
 print(nome)
 
# Atividade 1:
cores = ["azul", "verde", "vermelho", "rosa"]

for i in range(len(cores)):
    if cores[i] == "verde":
        cores[i] = "amarelo"
    
    print(cores[i])

print("Lista final:", cores)

#RANGE: uma sequência 
for valor in range(1, 6):
 print(valor)

 #Exemplo while:
contador = 1
while contador <= 5:
 print(contador)
contador += 1

 # atividade:
senha = ""
contador = 0
while senha != "python":
        if contador >=3:
            break
        senha = input ("Digite a senha: ")
        if senha =="python":
            print("Senha correta!")
        else:
            print ("Senha incorreta!")
            contador += 1

#BREAK:interrompe o loop imediatamente

 #Atividade:

for tentativa in range(3):
    senha = input("Digite a senha: ")
    
    if senha == "python":
        print("Senha correta!")
        break
    else:
        print("Senha incorreta!")
        
#CONTINUE: pula para a próxima repetição do loop

#1) Mostrar os números de 1 a 10 usando for
for números in range(1, 11):
    print(números)

#2) Pedir um número e mostrar a tabuada de 1 até 10 usando for
numero = int(input("Digite um número: "))

for i in range(1, 11):
     print(numero * i)

#3) Contar de 1 até 5 usando while
contador = 1
while contador <= 5:
    print(contador)
    contador += 1

#4)Pedir números ao usuário até ele digitar 0, usando break
while True:
    numero = int(input("Digite um número: "))
    if numero == 0:
        print("Programa encerrado!")
        break
    else:
     print("Você digitou: ", numero)

#5) Mostrar números de 1 a 10, mas ignorar o número 5 usando continue
for i in range(1, 11):
    if i == 5:
        continue  
    print(i)

 