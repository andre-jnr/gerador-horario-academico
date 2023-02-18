import modulo as md

nome_curso = str(input('Digite o nome do curso: ')).upper().strip()

while (nome_curso == '') or (nome_curso == ' '):
    print(' ')
    print('Por favor, digite algo.')
    nome_curso = str(input('Digite o nome do curso: ')).upper().strip()

materias = []
md.coletarMaterias(materias)

quantidade_materias = len(materias)
quantidade_turmas = md.leia_inteiro('Quantidade de turmas: ')

while quantidade_turmas > 5:
    print('Há muita turma pra pouca matéria!')
    quantidade_turmas = md.leia_inteiro('Quantidade de turmas: ')

turmas = md.nomearTurmas(nome_curso, quantidade_turmas)
horario_das_turmas = md.criarHorarios(materias, turmas)

validacao = md.validadarHorario(horario_das_turmas)

while validacao == False:
    horario_das_turmas = md.criarHorarios(materias, turmas)
    validacao = md.validadarHorario(horario_das_turmas)

md.CriarTabelas(horario_das_turmas)
