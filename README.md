# jogo-da-velha
Inteligência Artificial criada para jogar o "jogo da velha". Foi utilizado um algoritmo de busca competitiva, mais profundamente o algoritmo MinMaxAlfaBeta.

<p>Basicamente ela testa todas as possibilidades de jogadas(na sua respectiva vez de jogar), e vê a melhor posição. 
Para tornar o algoritmo mais eficiente foi utilizado o conceito de poda na busca(pruning the search on backtracking).
O algoritmo é de busca competitiva, isso em IA significa que em jogos mais comuns são aqueles de ambientes determinísticos, 
completamente observáveis em que existem dois agentes cujas ações se alternam e os valores de utilidade são iguais e simétricos.
Por exemplo, se um jogador ganha, recebe +1, o outro que perde recebe -1. </p>
<p> Com o algoritmo MinMaxAlfaBeta usamos a busca em que a cada turno um jogador faz sua ação(min ou max) sendo max tentando o maior valor possível para o grau da árvore,
e min tentando o menor possível.</p>
<p> Dessa forma criamos um jogador "master" do qual NÃO É POSSÍVEL VENCER, pois para um jogo pequeno como jogo da velha, ele sempre irá pegar a posição mais favorável no tabuleiro.</p>

<br>

  <center>
  
  <img src="https://media.giphy.com/media/Qq7XAPjyzW1mu8B7VH/giphy.gif" width="380" height="450" align="left"/> 
    </center>
