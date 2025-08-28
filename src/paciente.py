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

def buscar_paciente(lista_pacientes,campo_buscado,valor_buscado): 
    encontrado = False
    for paciente in lista_pacientes: 
        if getattr(paciente,campo_buscado) == valor_buscado: 
            print(f'Paciente encontrado:\nNome: {paciente.nome}\nIdade: {paciente.idade}\nTelefone: {paciente.telefone}')
            encontrado = True
    if encontrado == False: print('Paciente não encontrado.')

#só comentando essa parte, pois até eu me confundi enquanto fazia essa função. 
#basicamente a função acima ("buscar_paciente()" usando getattr) vai esperar como parametro a lista para a busca,
#o campo do objeto (literalmente o campo chamado nome)
#e o valor do campo (nesse caso o próprio nome, que será um parametro que vai vir na função)
#Tentei sinalizar bem tudo isso, nomeando detalhadamente. Mas mesmo assim, pode ser bem confuso.

def calculo_pacientes(lista_pacientes):
    idade_media = 0
    total_pacientes = len(lista_pacientes)
    for paciente in lista_pacientes:
        idade_media += paciente.idade
    if total_pacientes != 0:    
        idade_media = idade_media / total_pacientes
        print(f'Idade média dos pacientes cadastrados: {idade_media}')
    print(f'Pacientes cadastrados: {total_pacientes}')

calculo_pacientes(lista_pacientes)