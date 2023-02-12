#  Gerador de horarios academicos

Na volta as aulas, a minha faculdade estava com problemas em dividir a turma, então eu me desafiei a fazer um sistema parecido de separação de turmas.
Claro que esse sistema não seria usado em grande escala, mas queria desenvolver um script que realizasse as seguintes condições.

- Pergunta o nome do curso
- Separa as turmas pelo nome, se houver 2 turmas de **ads**, seria **ads 1** e **ads 2**.
- Perguntaria o nome das matérias
- gerava um horario único para cada turma

### Lembrando que

- Cada dia tem apenas uma matéria
- Suponhamos que cada matéria tem apenas um prof
- Mais de uma turma não pode conter a mesma matéria no mesmo dia
- A matéria não se repete na mesma semana, na mesma turma.
- Tem aula de segunda a sexta

### Nota

O programa está com um bug, às vezes uma turma tem mais uma matéria para adicionar, mas essa matéria já está ocupada naquela semana, 
isso gera um loop infinito. Pensei em criar uma função separada para criar o loop e uma para gerar os horarios, assim poderia controlar
o loop, e toda vez que repetisse X vezes, eu geraria outro horario. Mas estou sem tempo para implementar. 
