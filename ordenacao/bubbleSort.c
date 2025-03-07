#include <stdio.h>

// Função Bubble Sort
void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) { // Percorre toda a lista
        for (int j = 0; j < n - i - 1; j++) { // Percorre até o último elemento não ordenado
            if (arr[j] > arr[j + 1]) { // Compara e troca se necessário
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

// Função principal para testar
int main() {
    int numeros[] = {5, 3, 8, 4, 2};
    int n = sizeof(numeros) / sizeof(numeros[0]); // Calcula o tamanho do array

    bubbleSort(numeros, n);

    // Imprime o array ordenado
    printf("Array ordenado: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", numeros[i]);
    }
    return 0;
}
