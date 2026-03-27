#Atividade  Atividade 20 — Sistema Completo - DESAFIO FINAL SAÍDA:
alunos = {
    "nomes": ["Ana", "Beatriz", "Carlos", "Daniel", "Elis"],
    "notas": [6.5, 7.8, 10.0, 8.0, 5.4]
}
def mostrar_todos():
    for i in range(len(alunos["nomes"])):
        nome = alunos["nomes"][i]
        nota = alunos["notas"][i]

        if nota >= 7:
            status = "Aprovado"
        else:
            status = "Reprovado"

        print(nome, "-", nota, "-", status)

mostrar_todos()  