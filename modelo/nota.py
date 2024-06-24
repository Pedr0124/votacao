from aluno import Aluno
from jurados import Jurado
        
import os
class ProgramaAvaliacao:
    def __init__(self):
        self.alunos = []
        self.jurados = []

    def cadastrar_aluno(self):
        nome = input('Digite o nome do aluno: ')
        curso = input('Digite o curso do aluno: ')
        aluno = Aluno(nome, curso)
        self.alunos.append(aluno)
        print(f'Aluno {nome} cadastrado com sucesso!\n')

    def cadastrar_jurado(self):
        nome = input('Digite o nome do jurado: ')
        criterios = ['Elegância', 'Desenvoltura', 'Simpatia', 'Reciclável']
        jurado = Jurado(nome, criterios)
        self.jurados.append(jurado)
        print(f'Jurado {nome} cadastrado com sucesso!\n')

    def listar_alunos(self):
        if not self.alunos:
            print("Nenhum aluno cadastrado.\n")
            return
        
        for aluno in self.alunos:
            print(aluno)
        print()

    def avaliar_alunos(self):
        if not self.alunos or not self.jurados:
            print("É necessário cadastrar alunos e jurados antes de realizar as avaliações.\n")
            return
        
        for jurado in self.jurados:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f'Jurado {jurado.nome}, por favor, avalie os seguintes alunos:\n')
            for aluno in self.alunos:
                jurado.avaliar_aluno(aluno)
            input('Pressione Enter para continuar...')
    
    def mostrar_resultados(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n=== RESULTADOS DAS AVALIAÇÕES ===\n")
        for aluno in self.alunos:
            print(f'Aluno: {aluno.nome} ({aluno.curso})')
            print('Notas:')
            for jurado, notas in aluno.notas.items():
                print(f'  - Jurado: {jurado}, Notas: {notas}')
            print(f'Média das notas: {aluno.calcular_media()}\n')
    
    def executar(self):
        while True:
            print("\n=== MENU ===")
            print("1. Cadastrar aluno")
            print("2. Cadastrar jurado")
            print("3. Listar alunos")
            print("4. Avaliar alunos")
            print("5. Mostrar resultados")
            print("6. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                self.cadastrar_aluno()
            elif opcao == '2':
                self.cadastrar_jurado()
            elif opcao == '3':
                self.listar_alunos()
            elif opcao == '4':
                self.avaliar_alunos()
            elif opcao == '5':
                self.mostrar_resultados()
            elif opcao == '6':
                print("Encerrando o programa...")
                break
            else:
                print("Opção inválida. Tente novamente.")

# class Nota:
#     def __init__ (self, elegancia, desenvoltura, simpatia, reciclagem):
#         self._elegancia = elegancia
#         self._desenvoltura = desenvoltura
#         self._simpatia = simpatia
#         self._reciclagem = reciclagem

#     def calcular_media():

#     def __str__ (self)

class Nota:
    def __init__(self, elegancia, desenvoltura, simpatia, reciclagem):
        self._elegancia = elegancia
        self._desenvoltura = desenvoltura
        self._simpatia = simpatia
        self._reciclagem = reciclagem
        
    def calcular_media():
        pass
    
    def __str__(self) -> str:
        return f' Elegância: {self._elegancia} | Desenvoltura: {self._desenvoltura} | Simpatia: {self._simpatia} | Reciclagem: {self._reciclagem}'