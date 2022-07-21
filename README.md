# jogo-da-velha
Inteligência Artificial criada para jogar o "jogo da velha". Foi utilizado um algoritmo de busca competitiva, mais profundamente o algoritmo MinMaxAlfaBeta.

<p>Basicamente ela explora todas as possibilidades de jogadas(na sua respectiva vez de jogar), e vê a melhor posição. 
Para tornar o algoritmo mais eficiente foi utilizado o conceito de poda na busca(pruning the search on backtracking).
O algoritmo é de busca competitiva, isso em IA significa que em jogos mais comuns são aqueles de ambientes determinísticos, 
completamente observáveis em que existem dois agentes cujas ações se alternam e os valores de utilidade são iguais e simétricos.
Por exemplo, se um jogador ganha, recebe +1, o outro que perde recebe -1. </p>
<p> Com o algoritmo MinMaxAlfaBeta usamos a busca em que a cada turno um jogador faz sua ação(min ou max) sendo max tentando o maior valor possível para o grau da árvore,
e min tentando o menor possível.</p>
<p> Dessa forma criamos um jogador "mestre" do qual NÃO É POSSÍVEL VENCER, pois para um jogo pequeno como jogo da velha, ele sempre irá pegar a posição mais favorável no tabuleiro. Logo o melhor resultado que o adversário da IA irá conseguir é o empate</p>
<br>
  <img src="https://c.tenor.com/GX5odnI5fgkAAAAC/idea-genius.gif"/>
