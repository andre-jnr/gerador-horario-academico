def leia_inteiro(msg):
    while True:
        try:
            inteiro = int(input(msg))

        except (ValueError, TypeError):
            print('Você digitou um número inválido!')
            continue

        except KeyboardInterrupt:
            print('O usuário prefiriu não informar o solicitado')
            inteiro = 0
            return inteiro

        else:
            return inteiro


def coletarMaterias(lista):

    for i in range(1, 6):
        materia = ''
        while (materia == '') or (materia == ' '):
            materia = str(
                input(f'Digite o nome da {i}° Matéria: ')).strip().lower()

        if materia not in lista:
            lista.append(materia)

        else:
            while True:
                print(' ')
                print(f'Você já digitou {materia}!')
                materia = str(input(f'Digite o nome da {i}° Matéria: '))

                if materia not in lista:
                    lista.append(materia)
                    break


def nomearTurmas(nome_curso, quantidade_turmas):
    turmas = []

    for i in range(1, quantidade_turmas + 1):
        turma = f'{nome_curso} ' + str(i)
        turmas.append(turma)
    return turmas


def criarHorarios(materias, turmas):
    materias_de_segunda = []
    materias_de_terca = []
    materias_de_quarta = []
    materias_de_quinta = []
    materias_de_sexta = []
    horario_das_turmas = {}

    def criarHorario():
        for dia in dias_semana:  # Cria um horario único
            controle_de_loop = 0
            while True:
                materia = materias_da_turma[randint(
                    0, len(materias_da_turma) - 1)]

                if (materia not in horario.values()):

                    if (dia == 'segunda') and (materia not in materias_de_segunda):
                        horario[dia] = materia
                        materias_de_segunda.append(materia)
                        materias_da_turma.remove(materia)
                        break

                    if (dia == 'terça') and (materia not in materias_de_terca):
                        horario[dia] = materia
                        materias_de_terca.append(materia)
                        materias_da_turma.remove(materia)
                        break

                    if (dia == 'quarta') and (materia not in materias_de_quarta):
                        horario[dia] = materia
                        materias_de_quarta.append(materia)
                        materias_da_turma.remove(materia)
                        break

                    if (dia == 'quinta') and (materia not in materias_de_quinta):
                        horario[dia] = materia
                        materias_de_quinta.append(materia)
                        materias_da_turma.remove(materia)
                        break

                    if (dia == 'sexta') and (materia not in materias_de_sexta):
                        horario[dia] = materia
                        materias_de_sexta.append(materia)
                        materias_da_turma.remove(materia)
                        break

                    else:
                        controle_de_loop += 1
                        if controle_de_loop > 25:  # Evitar loop infinito
                            break

                elif len(horario.values()) == 5:
                    break
        horario_das_turmas[turmas[i]] = horario

    for i in range(len(turmas)):  # Criando chaves com o nome das turmas
        horario_das_turmas[turmas[i]] = ''

    for i in range(len(turmas)):
        from random import randint
        materias_da_turma = materias[:]
        dias_semana = ['segunda', 'terça', 'quarta', 'quinta', 'sexta']
        horario = {}  # onde vai ficar armazenado o horario da turma
        criarHorario()

    return horario_das_turmas


# Função antiga para criar a tabela dos horarios, deixei ela caso rich der falha.
def tabulacaoHorarios(horario_das_turmas, materias):
    tamanhos = []
    for materia in materias:
        tamanhos.append(len(materia))

    tabulacao = max(tamanhos)
    tabulacao_titulo = (tabulacao * 5) + 13

    for turma, horario in horario_das_turmas.items():
        print(f'{turma:^{tabulacao_titulo}}')
        print(f'{"DIA":^10}', end='|')

        for dia in horario.keys():

            if tabulacao < 8:
                print(f'{dia:^8}', end='|')

            else:
                print(f'{dia:^{tabulacao}}', end='|')
        print()

        print(f'{"DISCIPLINA":10}', end='|')

        for materia in horario.values():

            if tabulacao < 8:
                print(f'{materia:^8}', end='|')

            else:
                print(f'{materia:^{tabulacao}}', end='|')
        print('\n')


def CriarTabelas(horario_das_turmas):
    from rich.table import Table
    from rich.console import Console

    console = Console()

    for turma, horario in horario_das_turmas.items():
        tabela = Table(title=turma)
        tabela.add_column('DIA')

        for dia in horario.keys():
            tabela.add_column(dia)

        tabela.add_row('DISCIPLINA', horario['segunda'], horario['terça'], horario['quarta'],
                       horario['quinta'], horario['sexta'])

        console.print(tabela)


def validadarHorario(horario_das_turmas):
    validacao = True
    for horario in horario_das_turmas.values():
        quant_materias = len(horario.values())
        if (quant_materias < 5):
            validacao = False
            return validacao
    return validacao
