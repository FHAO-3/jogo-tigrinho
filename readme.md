# Máquina de Caça-Níquel

Este é um projeto inspirado pelo canal [Pythonando - RECRIANDO um CASSINO com PYTHON (Não apostem)](\\wsl.localhost\Ubuntu\home\fhao\youtube\pythonando), e me deu vontade de implementá-lo para aprender mais sobre Django e lógica de programação.

Como sabemos, o "Tigrinho" é conhecido como um jogo de apostas, e caça-níqueis são famosos em filmes de Las Vegas, sendo também jogos de aposta **(envolvendo dinheiro de verdade)**.

Neste projeto, vamos explorar conceitos como `lógica de programação`, `orientação a objetos`, `django` ,`geração de gráficos`, `matemática` e `estatística` para simular um cassino online.

### Funcionamento do Jogo
- 3 colunas
- 5 imagens distintas em cada coluna

### Regras
- Se as 3 colunas centrais pararem com imagens iguais, o dinheiro do usuário será multiplicado por 3.
- Se o jogador acertar apenas 2 colunas ou nenhuma, ele não ganha.

### Matemática
- Considerando que temos 5 imagens distintas em 3 colunas, a chance de obter 3 imagens iguais é `1/125`, ou seja, **a cada 125 tentativas, o jogador, em média, acerta uma vez**. Para equilibrar as probabilidades e garantir uma margem de 50% de perda e 50% de lucro, o cassino deve multiplicar o valor ganho por 125 em cada acerto.

