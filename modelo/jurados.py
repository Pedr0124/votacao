# class Jurado:
#     notas = []

#     def __init__ (self, nome, curso, nota):
#         self.nome = nome
#         self.curso = curso
#         self.nota = []

   
#     def __str__(self):
#         return f'Jurado: {self.nome}, Curso: {self.curso}, Nota: {self.nota}'
    
#     def avaliacao_nota(self, aluno, elegancia, desenvoltura, simpatia, reciclagem):
#         avaliacao = nota(self, elegancia, desenvoltura, simpatia, reciclagem)
#         aluno.notas.append(avaliacao)

# import os
# class Jurado:
#     def __init__(self, nome, area):
#         self._nome = nome
#         self._area = area

#     def __str__ (self) -> str:
#         return f'nome: {self._nome} | Nome: {self._area}'
    
    # def avaliar_aluno(self, aluno):
    #     os.system('cls' if os.name == 'nt' else 'clear')
    #     print(f'Avaliação do aluno {aluno.nome} ({aluno.curso}) pelo jurado {self.nome}:\n')
        
    #     notas = {}
    #     for criterio in self.criterios:
    #         nota = float(input(f'Nota para {criterio}: '))
    #         notas[criterio] = nota
        
    #     aluno.adicionar_nota(self.nome, **notas)
        
    #     print(f'\nAvaliação concluída para o aluno {aluno.nome}. Notas atribuídas: {notas}\n')

import os
from modelo.nota import Nota

class Jurado:
    def  __init__(self, nome, area):
        self._nome = nome
        self._area = area
        
    def __str__(self) -> str:
        return f'Jurado: {self._nome} | Area: {self._area}'
    
    def atribuir_nota(self, aluno, elegancia, desenvoltura, simpatia, reciclagem):
        avaliacao = Nota(elegancia, desenvoltura, simpatia, reciclagem)
        aluno._notas.append(avaliacao)

    def cadastrar_jurado():
        os.system('cls')
        print('cadastrar jurado\n')
        nome= input('Digite o nome do jurado: ')
        area = input('Digite a área do jurado: ')
        dados_do_jurado = {'nome':nome, 'area': area}
        Jurado.jurado.append(dados_do_jurado)
            
        print("nome: ", nome, "área: ", area)

        input("digite uma tecla para reiniciar: ")
