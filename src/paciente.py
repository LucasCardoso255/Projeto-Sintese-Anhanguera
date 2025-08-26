lista_pacientes = []

class Paciente:
    def __init__(self,nome,idade,telefone):
        self.nome = nome
        self.idade = int(idade)
        self.telefone = telefone

def listar_pacientes(lista_pacientes):
    if not lista_pacientes:
        print('Nenhum paciente cadastrado!')
    else:
        contador = 1
        for paciente in lista_pacientes:
            print(f'\n---------- Paciente {contador} ----------\n')
            print(f'Nome: {paciente.nome}')
            print(f'Idade: {paciente.idade}')
            print(f'Telefone: {paciente.telefone}')
            contador = contador + 1

def adicionar_paciente(instancia_paciente):
    lista_pacientes.append(instancia_paciente)
    print('Paciente adicionado com sucesso!')

listar_pacientes(lista_pacientes)