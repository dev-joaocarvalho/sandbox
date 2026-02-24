//Trabalho de:
// João Marcos Santos e Carvalho

// biblioteca
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>

#define MAX_JOGADORES 6
#define clear system("clear")

#define BLK "\e[0;30m"
#define RED "\e[0;31m"
#define GRN "\e[0;32m"
#define YEL "\e[0;33m"
#define BLU "\e[0;34m"
#define MAG "\e[0;35m"
#define CYN "\e[0;36m"
#define WHT "\e[0;37m"
#define CRESET "\e[0m"

#define BWHT "\e[1;37m"

int main() {
  system("color 0F");
  // variaveis pro jogador
  typedef struct {
    char nome[50];
    float vitorias;
    float tentativas;
    float pontuacao;
    float acertos;
  } Jogador;

  Jogador jogadores[MAX_JOGADORES];


  for (int p = 1; p < MAX_JOGADORES; p++) {
    strcpy(jogadores[p].nome, "???\0");
    jogadores[p].vitorias = 0;
    jogadores[p].tentativas = 0;
    jogadores[p].pontuacao = 0;
    jogadores[p].acertos = 0;
  }

  srand(time(NULL));
  // variaveis
  int final;
  int dificuldade;
  int tentativas;

  clear;

  printf(YEL"｡☆✼★━━━━━━━━━━━━━━━━━━━━━━★✼☆｡\n"CRESET);
  printf(BLU"-Bem-Vindo ao Jogo Da Memória-\n\n"CRESET);
  printf("     ->ENTER para começar\n");
  printf(YEL"｡☆✼★━━━━━━━━━━━━━━━━━━━━━━★✼☆｡\n\n"CRESET);
  getchar();
  clear;

  for (int p = 1; p < MAX_JOGADORES; p++) {
    clear;
    int jogadas = 0;
    printf("Digite o nome do jogador %d: ", p);
    scanf("%s", jogadores[p].nome);
    getchar();
    clear;

    int v0 = 1; //validade
do{
  clear;

    // ESCOLHER DIFICULDADE
    printf(BWHT"%s"CRESET", escolha uma dificuldade de 1 a 3.\n\n", jogadores[p].nome);
    printf("1.Básico - 4x4\n\n");
    printf("2.Médio - 6x6\n\n");
    printf("3.Avançado - 8x8\n\n");
    printf("-> ");
    v0 = scanf("%1i", &dificuldade);
    getchar();

    if(v0==0){
      printf("Dificuldade "RED"invalida"CRESET"\n");
      printf("\nPressione ENTER\n");
      continue;
    }
    switch (dificuldade) {
    case 1:
      printf("Tabuleiro básico selecionado.\n");
      break;
    case 2:
      printf("Tabuleiro médio selecionado.\n");
      break;
    case 3:
      printf("Tabuleiro avançado selecionado.\n");
      break;
    default:
      printf("Dificuldade "RED"invalida"CRESET"\n");
      v0=0;
      printf("\nPressione ENTER\n");
      getchar();
      continue;
    }
}while(v0==0);

    printf("Pressione ENTER\n");
    getchar();


    clear;
    // CRIAR TABULEIRO
    // 65=A , 66=B, ..., 90=Z
    int tamanhoTab = 2 + 2 * dificuldade;
    char tabuleiro1[10][10];
    int k = 65;

    // CRIAR TABULEIRO ORGANIZADO
    for (int i = 0; i < tamanhoTab; i++) {
      for (int j = 0; j < tamanhoTab - 1; j += 2) {
        if (k == 91) {
          k = 97;
        }
        tabuleiro1[i][j] = k;
        tabuleiro1[i][j + 1] = k;

        // printf("%c ", tabuleiro1[i][j]);
        // printf("%c ", tabuleiro1[i][j + 1]);
        k++;
      }
      printf("\n");
    }
    // getchar();
    //  RANDOMIZAR
    printf("\n");
    for (int i = 0; i < 40; i++) {
      int l1 = (rand() % tamanhoTab + 0);
      int c1 = (rand() % tamanhoTab + 0);
      int l2 = (rand() % tamanhoTab + 0);
      int c2 = (rand() % tamanhoTab + 0);

      char tempr;
      char temp1 = tabuleiro1[l1][c1];
      char temp2 = tabuleiro1[l2][c2];
      tempr = temp1;
      temp1 = temp2;
      temp2 = tempr;

      tabuleiro1[l1][c1] = temp1;
      tabuleiro1[l2][c2] = temp2;
    }

    // IMPRIMIR
    // for (int i = 0; i < tamanhoTab; i++) {
    //   for (int j = 0; j < tamanhoTab; j++) {
    //     printf("%c ", tabuleiro1[i][j]);
    //   }
    //   printf("\n");
    // }

    //  CRIAR TABULEIRO DO JOGADOR
    char tabuleiroJogo[10][10] = {};
    for (int i = 0; i < tamanhoTab; i++) {
      for (int j = 0; j < tamanhoTab; j++) {
        tabuleiroJogo[i][j] = 63;
        printf("%c ", tabuleiroJogo[i][j]);
      }
      printf("\n");
    }
    printf("\n");

    int gameWin = 0;
    int tentativas = 0;
    clear;

    // JOGO-------------------------------------------------
    while (gameWin == 0) {

      // IMPRIMIR
      printf("    1");
      for (int i = 0; i < tamanhoTab - 1; i++) {
        printf(" %i", i + 2);
      }
      printf("\n\n");

      for (int i = 0; i < tamanhoTab; i++) {
        printf("%i   ", i + 1);
        for (int j = 0; j < tamanhoTab; j++) {
          printf("%c ", tabuleiroJogo[i][j]);
        }
        printf("\n");
      }
      printf("\n");

      // PEGAR COORDENADAS
      int coluna1;
      int linha1;
      printf("Digite as coordenadas da "BWHT"primeira"CRESET" carta.\n");
      printf("Linha:");
      int v1 = scanf("%i", &linha1);
      getchar();

      //CÓDIGO DE TRAPAÇA
      if (linha1 == 0) {
        gameWin = 1;
        clear;
        continue;
      }

      printf("Coluna:");
      int v2 = scanf("%i", &coluna1);
      getchar();
      printf("\n");

      int coluna2;
      int linha2;
      printf("Digite as coordenadas da "BWHT"segunda"CRESET" carta.\n");
      printf("Linha:");
      int v3 = scanf("%i", &linha2);
      getchar();
      printf("Coluna:");
      int v4 = scanf("%i", &coluna2);
      getchar();
      clear;

      //VERIFICAR VALIDADE
      if (v1==0||v2==0||v3==0||v4==0) {
        printf("Opções "RED"inválidas"CRESET".\n");
        printf("Pressione ENTER\n");
        getchar();
        clear;
        continue;
      }

      int validade = 1;

      // VERIFICAR SE AS CARTAS JÁ NÃO ESTÃO CERTAS
      if ((tabuleiroJogo[linha1 - 1][coluna1 - 1] != 63) || (tabuleiroJogo[linha2 - 1][coluna2 - 1] != 63)||(linha1==linha2 && coluna1==coluna2)) {
        if (linha1 == 0) {
          continue;
        }
        printf("Opções "RED"inválidas"CRESET".\n");
        printf("Pressione ENTER\n");
        getchar();
        clear;
        continue;
      }

      // TROCAR CARTAS
      tabuleiroJogo[linha1 - 1][coluna1 - 1] =
          tabuleiro1[linha1 - 1][coluna1 - 1];
      tabuleiroJogo[linha2 - 1][coluna2 - 1] =
          tabuleiro1[linha2 - 1][coluna2 - 1];

      // IMPRIMIR
      printf("    1");
      for (int i = 0; i < tamanhoTab - 1; i++) {
        printf(" %i", i + 2);
      }
      printf("\n\n");

      for (int i = 0; i < tamanhoTab; i++) {
        printf("%i   ", i + 1);
        for (int j = 0; j < tamanhoTab; j++) {
          printf("%c", tabuleiroJogo[i][j]);
          printf(" ");
        }
        printf("\n");
      }
      printf("\n");

      // VERIFICAR SE ESTÁ CORRETO
      if (tabuleiroJogo[linha1 - 1][coluna1 - 1] ==
          tabuleiroJogo[linha2 - 1][coluna2 - 1]) {
        printf("Você "GRN"acertou!\n"CRESET);
        jogadores[p].acertos++;
       //printf("Acertos: %.f\n", jogadores[p].acertos);
      } else {
        printf("Você "RED"errou!\n"CRESET);
        tabuleiroJogo[linha1 - 1][coluna1 - 1] = 63;
        tabuleiroJogo[linha2 - 1][coluna2 - 1] = 63;
      }
      jogadores[p].tentativas++;
      jogadas++;

      // VERIFICAR SE GANHOU
      if (jogadores[p].acertos == (2 + dificuldade * 2)*(2 + dificuldade * 2)/2) {
        gameWin = 1;
        printf("VOCÊ "BWHT"☆✼★GANHOU O JOGO★✼☆"CRESET"!!!\n");
      }

      printf("\nPressione ENTER\n");
      getchar();

      clear;
    }

    // PONTUAÇÃO
    jogadores[p].pontuacao =
        (jogadores[p].acertos / jogadores[p].tentativas) * 100 * dificuldade;
    printf("Sua pontuação: %.2f\n", jogadores[p].pontuacao);
    jogadores[p].vitorias++;
    printf("\nSelecione as opções:\n\n");

    // NOVO JOGO OU TERMINA
    printf("1.Novo Jogo\n\n");
    printf("0.Ranking\n\n");
    printf("-> ");
    scanf("%i", &final);
    getchar();
    clear;
    if (final == 0) {
      clear;
      break;
    }

  }

  // ORGANIZAR JOGADORES
  for (int j = 0; j < MAX_JOGADORES; j++) {
    for (int p = 1; p < MAX_JOGADORES - 1; p++) {
      if (jogadores[p].pontuacao < jogadores[p + 1].pontuacao) {
        Jogador temp = jogadores[p];
        jogadores[p] = jogadores[p + 1];
        jogadores[p + 1] = temp;
      }
    }
  }

  // RANKING
  printf("Jogos encerrados:\n");
  printf("-------------------------- "BWHT"RANKING"CRESET" --------------------------\n");
  for (int p = 1; p < MAX_JOGADORES; p++) {
    printf("%dº Lugar: %.10s - Pontuação: %.2f - Acertos: %.f - Tentativas: %.f\n",
           p, jogadores[p].nome, jogadores[p].pontuacao,
           jogadores[p].acertos, jogadores[p].tentativas);
  }
  printf("-------------------------------------------------------------\n");
  final++;
  getchar();
  getchar();
  clear;

  return 0;
}
