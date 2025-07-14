# PD_LeetCode_PA

**Número da Lista**: 5<br>
**Conteúdo da Disciplina**: Programação Dinâmica<br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 20/2015868  |  Alexandre Lema Xavier Júnior |
| 21/1039671  |  Pedro Lopes da Cunha |

## Sobre 
Resolução de questões do LeetCode (2 difíceis e 2 médias) pelos integrantes do grupo com o objetivo de demonstrar o conhecimento adquirido nesse módulo (PD) da disciplina.

|Questão | Dificuldade |
| -- | -- |
| [1255. Maximum Score Words Formed by Letters](https://leetcode.com/problems/maximum-score-words-formed-by-letters/description/)  | Difícil |
| [1140. Stone Game II](https://leetcode.com/problems/stone-game-ii/description/) | Média |
| [198. House Robber](https://leetcode.com/problems/house-robber/description/) | Média |
| [174. Dungeon Game](https://leetcode.com/problems/dungeon-game/description/?envType=problem-list-v2&envId=dynamic-programming) | Difícil |


## Screenshots

### [1255. Maximum Score Words Formed by Letters](https://leetcode.com/problems/maximum-score-words-formed-by-letters/description/) - Díficil

A questão "1255. Maximum Score Words Formed by Letters" busca encontrar a maior pontuação possível ao formar um conjunto de palavras válidas com letras disponíveis, onde cada letra tem um valor e só pode ser usada uma vez. O código resolve isso com programação dinâmica com memoização, usando uma função recursiva `backtrack` com `@lru_cache` para evitar recomputações. Em cada passo, ele decide se inclui ou não a palavra atual, verificando se há letras suficientes e atualizando a pontuação total. Com isso, o algoritmo explora todas as combinações possíveis de forma eficiente e retorna a pontuação máxima.

![Print resolução da questão 1255](/imgs/1255img.png)

### [1140. Stone Game II](https://leetcode.com/problems/stone-game-ii/description/) - Média

A questão "1140. Stone Game II" propõe um jogo entre Alice e Bob, que alternam turnos pegando pedras de pilhas dispostas em linha. Em cada turno, o jogador pode pegar de 1 até 2×M pilhas, onde M varia conforme as jogadas, e o objetivo é maximizar a quantidade de pedras coletadas. O código resolve esse problema utilizando programação dinâmica com memoização, armazenando em uma matriz `dp[i][M]` a pontuação máxima que o jogador atual pode obter ao começar na pilha `i` com valor `M`. A função `solve` percorre todas as escolhas possíveis de X pilhas, calcula a pontuação atual e considera o melhor cenário possível assumindo que o adversário também joga de forma ideal. Assim, o algoritmo explora recursivamente os subproblemas, evitando recalcular estados já resolvidos, e retorna o máximo de pedras que Alice pode conseguir.

![Print resolução da questão 1255](/imgs/1140img.png)

### [198. House Robber](https://leetcode.com/problems/house-robber/description/) - Média

A questão House Robber propõe encontrar o valor máximo que pode ser roubado de uma sequência de casas, com a restrição de que não é possível roubar duas casas adjacentes. A função recursiva dp(i) calcula o valor máximo a partir da casa i, escolhendo entre roubar a casa atual e pular a próxima ou pular a atual e considerar a seguinte. Com @lru_cache, evitamos recomputações, garantindo eficiência. O resultado final, dp(0), representa o valor máximo possível sem disparar o sistema de segurança. Utilizei PD na resolução dividindo o problema em subproblemas menores e armazenar os resultados parciais. Em vez de recalcular o valor máximo para cada posição, a função dp(i) guarda o melhor resultado a partir da casa i, evitando repetições e garantindo eficiência.
![Print resolução da questão 198](/imgs/198_img.jpg)

### [174. Dungeon Game](https://leetcode.com/problems/dungeon-game/description/?envType=problem-list-v2&envId=dynamic-programming) - Díficil

A questão Dungeon Game propõe calcular a quantidade mínima de vida que um cavaleiro precisa ter ao entrar em uma masmorra, de forma que ele consiga chegar até a princesa sem morrer. A masmorra é representada por uma grade 2D com valores negativos (que diminuem a vida), zeros e positivos. O cavaleiro começa no canto superior esquerdo e só pode se mover para a direita ou para baixo, com o objetivo de alcançar o canto inferior direito. Para resolver esse problema, a ideia é preencher uma matriz auxiliar a partir da posição final, onde está a princesa, até o início, calculando em cada célula o mínimo de vida que o cavaleiro deve ter ao entrar nela para sobreviver até o final. A cada passo, a vida necessária é o menor valor entre os caminhos possíveis, ajustado pelo valor da sala atual. A resposta final está na célula inicial, indicando a menor vida possível para completar o trajeto com segurança.
![Print resolução da questão 174](/imgs/174_img.jpg)


## Vídeo de explicação das Questões:

## Instalação 
**Linguagem**: Python <br>







