from statistics import mean
from time import sleep

nomes = ["Neymar", "Cleiton", "Guilherme", "Lebron"]
idades = [31,20,21,20]
pesos = [68,90,63,107]
alturas = [1.75,1.80,1.74,1.87]
imcs = [22,28,20,30]
def incluir():
    nome = input("Digite o nome do aluno: ")

    try:
        idade = int(input("Digite a idade do aluno: "))
        peso = float(input("Digite o peso do aluno: "))
        altura = float(input("Digite a altura do aluno: "))

        imc = peso/(altura**2)

        nomes.append(nome)
        idades.append(idade)
        alturas.append(altura)
        pesos.append(peso)
        imcs.append(imc)

        print("Aluno incluso!")

    except:
        print("Números, por favor.")

def listar():
    for i in range (len(nomes)):
        print(f"{nomes[i]}, {idades[i]} anos de idade, {pesos[i]} de peso, {alturas[i]} de altura, IMC={imcs[i]}")
        mediaimc=mean(imcs)

    print(f"a média do imc dos alunos é: {mediaimc}")

def listarum():
    nome=input("Digite o nome do aluno: ")
    try:
        i = nomes.index(nome)
        print(f"{nomes[i]}, {idades[i]} anos de idade, {pesos[i]} de peso, {alturas[i]} de altura, IMC = {imcs[i]}")
    except:
        print("Nenhum aluno com esse nome.")

def listarporidade():
    try:
        idade = int(input("Digite a idade dos alunos: "))
        alunosidade = [i for i in range(len(idades)) if idades[i]==idade]
        try:
            if alunosidade:
                for i in alunosidade:
                    print(f"{nomes[i]}, {idades[i]} anos de idade, {pesos[i]} de peso, {alturas[i]} de altura, IMC={imcs[i]}")
                    mediaimc= mean(imcs[i] for i in alunosidade)

            print(f"a média do IMC dos alunos com essa idade é: {mediaimc}")

        except:
            print("Nenhum aluno com essa idade.")

    except:
        print("NÚMEROS POR FAVOR")

def inicio():
    while True:
        try:
            menu=int(input("\nMENU\n\n1- Incluir Aluno \n2– Listar todos alunos e seus dados  \n\
3- Listar os dados de um aluno \n4– Listar dados dos alunos de uma determinada idade \n9- Fim\n\n"))
            
            if menu==1:
                incluir()

            elif menu==2:
                listar()

            elif menu==3:
                listarum()

            elif menu==4:
                listarporidade()

            elif menu==9:
                print("Encerrando.")
                sleep(0.5)
                print("Encerrando..")
                sleep(0.5)
                print("Encerrando...")
                break
            else:
                print("Essa não é uma das opções.")
        except:
            print("NÚMEROOOOOS")
inicio()