import paciente
import os

def cls():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

loop = True

while loop == True:
    cls()
    print('=== SISTEMA CLÍNICA VIDA+ ===')
    print('1. Cadastrar paciente')
    print('2. Ver estatísticas')
    print('3. Buscar paciente')
    print('4. Listar todos os pacientes')
    print('5. Sair')
    i = input('Escolha uma opção: ')

    match i:
        case '1':
            cls()
            novo_paciente = paciente.Paciente( 
                nome=input('Insira o nome do paciente: '),
                idade=input('Insira a idade do paciente: '),
                telefone=input('Insira o telefone do paciente: ')                
            )
            paciente.adicionar_paciente(novo_paciente)
            input('\npressione para enter voltar')
        case '2':
            cls()
            paciente.calculo_pacientes(paciente.lista_pacientes)
            input('\npressione para enter voltar')
        case '3':
            cls()
            busca = input('Insira o nome do paciente a ser pesquisado: ')
            paciente.buscar_paciente(paciente.lista_pacientes,'nome',busca)
            input('\npressione para enter voltar')
        case '4':
            cls()
            paciente.listar_pacientes(paciente.lista_pacientes)
            input('\npressione para enter voltar')
        case '5':
            cls()
            print('Encerrado!')
            loop = False