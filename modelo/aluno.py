# class Aluno:
#     alunos = []

#     def __init__ (self, nome,curso, nota):
#         self.nome = nome
#         self.curso = curso
#         self.nota = []
#        

#     def cadastro_aluno():
#         nome = input('nome do aluno: ')
#         print(nome)
   
#     def __str__(self):
#         return f'aluno: {self.nome}, Curso: {self.curso}'
    
#     def avaliacao_nota(self, aluno, elegancia, desenvoltura, simpatia, reciclagem):
#         avaliacao = nota(self, elegancia, desenvoltura, simpatia, reciclagem)
#         aluno.notas.append(avaliacao)



# import os
# class Aluno:
      
#     alunos = []

#     def __init__(self, nome, curso, nota) -> None:
#           self._nome = nome
#           self._curso = curso
#           self.nota = nota

#     def exibir_cadastro():
#             print('CADASTRO ALUNO')

#     def exibir_opcao():
#             print("1. cadastrar aluno")
#             print("2. listar alunos")
#             print("3. sair\n")

#     def finalizar_app():
#             os.system('cls')
#             print("encerrando programa")

#     def cadastrar_aluno():
#         os.system('cls')
#         print('cadastrar aluno\n')
#         nome= input('Digite o nome do aluno: ')
#         curso = input('Digite o curso do aluno: ')
#         nota = float(input('Digite a nota do aluno: '))
#         dados_de_alunos = {'nome':nome, 'curso': curso, 'nota':nota}
#         Aluno.alunos.append(dados_de_alunos)
            
#         print("nome: ", nome, "curso: ", curso, "nota: ", nota)

#         input("digite uma tecla para reiniciar: ")
#         main()

#     def __str__(self):
#         return f'nome: {self.nome}, Curso: {self.curso}, Nota: {self.nota}'


#     def listar_alunos():
#             os.system('cls')
#             print('Lista de alunos\n')
#             for aluno in alunos:
#                 nome = aluno['nome']
#                 curso = aluno['curso']
#                 nota = aluno['nota']
#                 print(f' - {nome} | {curso} | {nota}\n')
#             input('Digite uma tecla para reiniciar')
#             main()

#     def escolher_opcao():
            
#             opcao_escolhida=int(input("escolha uma opção: "))
#             print("voce escolheu a opção: ", opcao_escolhida)

#     if opcao_escolhida==1:
#         cadastrar_aluno()
#     elif opcao_escolhida==2:
#         listar_alunos()
#     else:
#         finalizar_app()
                    
#     def main():
#         exibir_cadastro()
#         exibir_opcao()
#         escolher_opcao()

#     if __name__ == "__main__":
#         main()

# class Aluno:
#     def __init__(self, nome, categoria):
#         self.nome = nome
#         self.categoria = categoria
#         self.notas = {'Elegância': [], 'Desenvoltura': [], 'Simpatia': [], 'Item Reciclável': []}
#         self.jurados = []
 
#     def adicionar_notas(self, notas, jurado):
#         if jurado in self.jurados:
#             print(f"Jurado {jurado} já votou para {self.nome}.")
#         else:
#             for criterio, nota in notas.items():
#                 self.notas[criterio].append(nota)
#             self.jurados.append(jurado)
#             print(f"Notas {notas} adicionadas por {jurado}.")
 
#     def calcular_media(self):
#         medias = {criterio: sum(notas)/len(notas) if notas else 0 for criterio, notas in self.notas.items()}
#         return medias
 
#     def mostrar_resultado(self):
#         medias = self.calcular_media()
#         resultado = f'Aluno: {self.nome} ({self.categoria})\n'
#         for criterio, media in medias.items():
#             resultado += f'{criterio}: {media:.2f}\n'
#         resultado += f'Jurados: {", ".join(self.jurados)}\n'
#         print(resultado)

# import os

# class Aluno:
#     alunos = []

#     def __init__(self, nome, curso, nota):
#         self.nome = nome
#         self.curso = curso
#         self.nota = nota

#     def exibir_opcoes():
#         print("1. Cadastrar aluno")
#         print("2. Listar alunos")
#         print("3. Sair")

#     def cadastrar_aluno():
#         os.system('cls' if os.name == 'nt' else 'clear')
#         print('Cadastrar aluno\n')
#         nome = input('Digite o nome do aluno: ')
#         curso = input('Digite o curso do aluno: ')
#         nota = float(input('Digite a nota do aluno: '))
#         aluno = Aluno(nome, curso, nota)
#         Aluno.alunos.append(aluno)
#         print(f"Aluno cadastrado:\nNome: {aluno.nome}, Curso: {aluno.curso}, Nota: {aluno.nota}\n")

#     def listar_alunos():
#         os.system('cls' if os.name == 'nt' else 'clear')
#         print('Lista de alunos\n')
#         if Aluno.alunos:
#             for aluno in Aluno.alunos:
#                 print(f' - {aluno.nome} | {aluno.curso} | Nota: {aluno.nota}\n')
#         else:
#             print("Nenhum aluno cadastrado.\n")
    
#     def main():
#         while True:
#             Aluno.exibir_opcoes()
#             opcao = input("Escolha uma opção: ")
            
#             if opcao == '1':
#                 Aluno.cadastrar_aluno()
#             elif opcao == '2':
#                 Aluno.listar_alunos()
#             elif opcao == '3':
#                 os.system('cls' if os.name == 'nt' else 'clear')
#                 print("Encerrando programa.")
#                 break
#             else:
#                 os.system('cls' if os.name == 'nt' else 'clear')
#                 print("Opção inválida. Tente novamente.")

# if __name__ == "__main__":
#     Aluno.main()

# import os

# class Aluno:
#     def __init__(self,categoria, nome, curso):
#         self._categoria = categoria
#         self._nome = nome
#         self._curso = curso
#         self._notas = []

#     def __str__ (self) -> str:
#         notas_str = '\n'.join(str(nota) for nota)
#         return f'categoria: {self._categoria} | Nome: {self._nome} | Curso: {self._curso} | notas: {self._notas}'
   
    # def adicionar_sexo(self, miss, mister):
    #     self.miss = miss
    #     self.mister = mister

    
    # def adicionar_nota(self, jurado, elegancia, desenvoltura, simpatia, reciclavel):
    #     self.notas[jurado] = {'Elegância': elegancia, 'Desenvoltura': desenvoltura, 'Simpatia': simpatia, 'Reciclável': reciclavel}
    
    # def calcular_media(self):
    #     if self.notas:
    #         return sum(sum(j['Elegância'], j['Desenvoltura'], j['Simpatia'], j['Reciclável']) / 4 for j in self.notas.values()) / len(self.notas)
    #     else:
    #         return 0.0

    # def __str__(self):
    #     return f'Aluno: {self.nome}, Curso: {self.curso}, Notas: {self.notas}, Média: {self.calcular_media()}'


import os
class Aluno:
    def __init__(self, nome, turma, categoria):
        self._nome = nome
        self._turma = turma
        self._categoria = categoria
        self._notas = []
        
    def __str__(self) -> str:
        notas_str = '\n'.join(str(nota) for nota in self._notas)
        return f'Aluno: {self._nome} | Turma: {self._turma} | Categoria: {self._categoria} | Notas:\n{notas_str}'
    
    def cadastrar_aluno():
        os.system('cls')
        print('cadastrar aluno\n')
        nome= input('Digite o nome do aluno: ')
        turma = input('Digite a turma do aluno: ')
        categoria = (input('Digite a nota do aluno: '))
        dados_de_alunos = {'nome':nome, 'turma':turma, 'categoria':categoria}
        Aluno.alunos.append(dados_de_alunos)
            
        print("nome: ", nome, "turma: ", turma, "categoria: ", categoria)

        input("digite uma tecla para reiniciar: ")