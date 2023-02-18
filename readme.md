# Gerador de horarios academicos

Na volta as aulas, a minha faculdade estava com problemas em dividir a turma, então eu me desafiei a fazer um sistema parecido de separação de turmas.
Claro que esse sistema não seria usado em grande escala, mas queria desenvolver um script que realizasse as seguintes condições.

- Perguntaria o nome do curso
- Separaria as turmas pelo nome, se houver 2 turmas de **ads**, seria **ads 1** e **ads 2**.
- Perguntaria o nome das matérias
- geraria um horario único para cada turma

### Lembrando que

- Cada dia tem apenas uma matéria
- Suponhamos que cada matéria tem apenas um professor
- Mais de uma turma não pode conter a mesma matéria no mesmo dia
- A matéria não se repete na mesma semana, na mesma turma.
- Tem aula de segunda a sexta

# Implementação de tabelas usando biblioteca rich

![image](https://user-images.githubusercontent.com/99357762/219826572-3709e8dd-a543-4b50-a0a8-b2bd44b347d5.png)
