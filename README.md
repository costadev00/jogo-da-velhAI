# jogo-da-velhAI
<h2>Jogo da Velha com Algoritmo Minimax</h2>

<p>Este projeto implementa o clássico jogo da velha (Tic-Tac-Toe) com uma inteligência artificial que utiliza o algoritmo Minimax para tomar decisões. O jogo é jogado no terminal entre um jogador humano e o computador.</p>

<p>Basicamente ela explora todas as possibilidades de jogadas(na sua respectiva vez de jogar), e vê a melhor posição. 
Para tornar o algoritmo mais eficiente foi utilizado o conceito de poda na busca(pruning the search on backtracking).
O algoritmo é de busca competitiva, isso em IA significa que em jogos mais comuns são aqueles de ambientes determinísticos, 
completamente observáveis em que existem dois agentes cujas ações se alternam e os valores de utilidade são iguais e simétricos.
Por exemplo, se um jogador ganha, recebe +1, o outro que perde recebe -1. </p>
<p> Com o algoritmo MinMaxAlfaBeta usamos a busca em que a cada turno um jogador faz sua ação(min ou max) sendo max tentando o maior valor possível para o grau da árvore,
e min tentando o menor possível.</p>
<p> Dessa forma criamos um jogador "mestre" do qual NÃO É POSSÍVEL VENCER, pois para um jogo pequeno como jogo da velha, ele sempre irá pegar a posição mais favorável no tabuleiro. Logo o melhor resultado que o adversário da IA irá conseguir é o empate</p>
<p> Segue abaixo o funcionamento do algoritmo minmax</p>
<img src="minimax.png" width="1002" height="256"/>
<br>
  <img src="https://c.tenor.com/GX5odnI5fgkAAAAC/idea-genius.gif" width="500" height="500">
