class Aluno:
    def __init__(self, nome, habilidade):
        self.nome = nome
        self.habilidade = habilidade

class Time:
    def __init__(self, id_time):
        self.id = id_time
        self.jogadores = []

    def adicionar(self, aluno):
        self.jogadores.append(aluno.nome)

    def imprimir(self):
        print(f"Time {self.id}")
        for nome in sorted(self.jogadores):
            print(nome)
        print()

class SelecaoTimes:
    def __init__(self, N, T):
        self.N = N
        self.T = T
        self.alunos = []
        self.times = [Time(i+1) for i in range(T)]

    def adicionar_aluno(self, nome, habilidade):
        self.alunos.append(Aluno(nome, habilidade))

    def distribuir(self):
        # Ordenar
        self.alunos.sort(key=lambda a: -a.habilidade)
        # Distribuir
        for i, aluno in enumerate(self.alunos):
            idx = i % self.T
            self.times[idx].adicionar(aluno)

    def imprimir_resultado(self):
        for time in self.times:
            time.imprimir()

def main():
    N, T = map(int, input().split())
    selecao = SelecaoTimes(N, T)

    for _ in range(N):
        nome, h = input().split()
        selecao.adicionar_aluno(nome, int(h))

    selecao.distribuir()
    selecao.imprimir_resultado()

    while True:
        print("\n--- MENU ---")
        print("1 - Adicionar aluno")
        print("2 - Distribuir alunos nos times")
        print("3 - Imprimir resultado")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            if len(selecao.alunos) < N:
                nome = input("Nome do aluno: ")
                habilidade = int(input("Habilidade do aluno: "))
                selecao.adicionar_aluno(nome, habilidade)
            else:
                print("Número máximo de alunos já foi atingido.")

        elif opcao == "2":
            selecao.distribuir()
            print("Alunos distribuídos com sucesso!")

        elif opcao == "3":
            selecao.imprimir_resultado()

        elif opcao == "0":
            print("Encerrando o programa...")
            break

        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
22