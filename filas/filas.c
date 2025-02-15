#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int itens[100];  // Tamanho máximo da fila
    int frente;
    int tras;
    int tamanho;
} Fila;

void inicializar(Fila *fila) {
    fila->frente = 0;
    fila->tras = -1;
    fila->tamanho = 0;
}

void enfileirar(Fila *fila, int item) {
    if (fila->tamanho < 100) { // Verifica se há espaço na fila
        fila->tras = (fila->tras + 1) % 100;
        fila->itens[fila->tras] = item;
        fila->tamanho++;
    } else {
        printf("Fila cheia!\n");
    }
}

int desenfileirar(Fila *fila) {
    if (fila->tamanho > 0) {
        int item = fila->itens[fila->frente];
        fila->frente = (fila->frente + 1) % 100;
        fila->tamanho--;
        return item;
    } else {
        printf("Fila vazia!\n");
        return -1; // Indica erro
    }
}

int tamanho(Fila *fila) {
    return fila->tamanho;
}

int main() {
    Fila fila;
    inicializar(&fila);

    enfileirar(&fila, 1);
    enfileirar(&fila, 2);
    enfileirar(&fila, 3);

    printf("Tamanho da fila: %d\n", tamanho(&fila));

    printf("Desenfileirado: %d\n", desenfileirar(&fila));
    printf("Desenfileirado: %d\n", desenfileirar(&fila));

    printf("Tamanho da fila: %d\n", tamanho(&fila));

    return 0;
}
