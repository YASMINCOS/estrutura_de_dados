#include <stdio.h>
#include <stdlib.h>

#define MAX 5  // Tamanho máximo da pilha

typedef struct {
    int topo;
    int itens[MAX];
} Stack;

// Inicializa a pilha
void init(Stack *s) {
    s->topo = -1;
}

// Verifica se a pilha está vazia
int isEmpty(Stack *s) {
    return s->topo == -1;
}

// Adiciona elemento na pilha
void push(Stack *s, int item) {
    if (s->topo == MAX - 1) {
        printf("A pilha está cheia!\n");
        return;
    }
    s->itens[++s->topo] = item;
}

// Remove elemento da pilha
int pop(Stack *s) {
    if (isEmpty(s)) {
        printf("A pilha está vazia!\n");
        return -1;
    }
    return s->itens[s->topo--];
}

// Mostra o topo da pilha
int peek(Stack *s) {
    if (isEmpty(s)) {
        return -1;
    }
    return s->itens[s->topo];
}

// Testando a pilha em C
int main() {
    Stack s;
    init(&s);

    push(&s, 10);
    push(&s, 20);
    push(&s, 30);

    printf("Topo: %d\n", peek(&s)); // Saída: 30
    printf("Removido: %d\n", pop(&s)); // Saída: 30
    printf("Topo: %d\n", peek(&s)); // Saída: 20

    return 0;
}
