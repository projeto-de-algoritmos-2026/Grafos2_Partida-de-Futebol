# Partida de futebol

Número da Lista: 53<br>
Conteúdo da Disciplina: Grafos<br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 21/1063210  |  Maria Alice Bernardo da Costa Silva |
| 21/1062339  |  Milena Baruc Rodrigues Morais |

## Sobre 
O projeto tem como objetivo exibir o funcionamento do algoritmo **Dijkstra**, que realiza a busca do menor caminho em um grafo ponderado.

O cenário desenvolvido se baseia em uma formação tática de futebol. No sistema, cada jogador representa um **nó** e as possibilidades de passe são as **arestas**. Os pesos das arestas são calculados dinamicamente com base na distância euclidiana entre os jogadores no campo. O simulador permite que o usuário visualize como a bola percorreria o caminho mais eficiente (mais curto) entre dois atletas escolhidos.


## Screenshots
<!-- Adicione 3 ou mais screenshots do projeto em funcionamento. -->

## Video
<!-- [Apresentação]() -->

## Instalação 
Linguagem: Python 3<br>
Biblioteca Gráfica: Pygame

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# .\venv\Scripts\Activate.ps1 # Windows
pip install -r requirements.txt
```

### Pré-requisitos
- Ter o Python instalado

## Uso 
1. Execute o comando: `python main.py`
2. **Selecionar Origem**: Clique no jogador que está com a posse de bola.
3. **Selecionar Destino**: Clique no jogador para quem deseja realizar o passe final.
4. **Visualizar**: O sistema destacará o caminho de passes que minimiza a distância total percorrida pela bola.

## Outros 
<!-- Quaisquer outras informações sobre seu projeto podem ser descritas abaixo. -->