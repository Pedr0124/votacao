# import os
# from app import aluno

# class avaliacao:
#         notas = []

#     def __init__ (self, ):

#     def exibir_opcoes():
#                 print('1. Novo aluno')
#                 print('2. listar notas')
#                 print('3. Sair\n')

#     def encerrar():
#             os.system('cls')
#             print('Encerrando programa')

#     def avaliar():
#             os.system('cls')
#             nome_do_aluno = input('nome do aluno: ')
#             elegancia = float(input('Elegância: '))
#             desenvoltura = float(input('Desenvoltura: '))
#             simpatia = float(input('Simpatia: '))
#             reciclavel = float(input('Item reciclável: '))
#             dados_da_avaliacao = {'nome do aluno':nome_do_aluno,'elegancia':elegancia, 'desenvoltura':desenvoltura, 'simpatia':simpatia, 'reciclavel': reciclavel}
#             notas.append(dados_da_avaliacao)
#             input('Digite uma tecla para reiniciar: ')
#             main()

#     def listar_notas():
#             os.system('cls')
#             for nota in notas:
#                 elegancia = nota['elegancia']
#                 desenvoltura = nota['desenvoltura']
#                 simpatia = nota['simpatia']
#                 item_reciclavel = nota['item reciclavel']
#                 print(f' - {elegancia.ljust(15)} | {desenvoltura.ljust(15)} | {simpatia.ljust(15)} | {item_reciclavel.ljust(15)}' )
#                 input('Digite uma tecla para reiniciar: ')
#                 main()

#     def escolher_opcao():
#                 opcao_escolhida = int(input('Escolha uma opção: '))
#                 print(f'Você escolheu a opção: {opcao_escolhida}')

#     if opcao_escolhida == 1:
#             avaliar()
#     elif opcao_escolhida == 2:
#             listar_notas()
#     else:
#             encerrar()
            

#     def main():
#             exibir_opcoes()
#             escolher_opcao()
#             listar_notas()

#     if __name__ == '__main__':
#             main()

# from avaliacao_classes import ProgramaAvaliacao

# def main():
#     programa = ProgramaAvaliacao()
#     programa.executar()

# if __name__ == "__main__":
#     main()


# from modelo.jurados import Jurado
# from modelo.aluno import Aluno

# aluno = Aluno('Pedro', 'TI', 'mister')
# jurado = Jurado('fábio', 'master') 

# jurado.atribuir_nota()

from modelo.jurados import Jurado
from modelo.aluno import Aluno

caua = Aluno('caua', 'TI', 'Mister')
jurado = Jurado('Fábio', 'Educacional')

jurado.atribuir_nota(caua, 5, 5, 5, 5)
jurado.atribuir_nota(caua, 6, 6, 6, 6)

print(caua)