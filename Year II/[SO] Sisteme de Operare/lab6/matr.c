#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <errno.h>


int matrixA[20][20], matrixB[20][20], matrixC[20][20];

// Structura folosita la calculul fiecarui thread 
struct mat {
    int i, j, p;
};

void *produs(void *v) {
    struct mat *arg = (struct mat*)v;
    int sum = 0;
    for (int k = 0; k < arg->p; k++)
        sum += matrixA[arg->i][k] * matrixB[k][arg->j];
    matrixC[arg->i][arg->j] = sum;
    return NULL;
}

int main() {
    int n, m, k;
    struct mat args[20 * 20];  // Argumente pentru fiecare thread
    pthread_t thrd[20 * 20];  

    printf("Dimensiune matrice A:\n");
    scanf("%d %d", &n, &k);
    printf("Elementele matricei A:\n");
    for (int i = 0; i < n; i++)
        for (int j = 0; j < k; j++)
            scanf("%d", &matrixA[i][j]);

    printf("Dimensiune matrice B:\n");
    scanf("%d %d", &k, &m);
    printf("Elementele matricei B:\n");
    for (int i = 0; i < k; i++)
        for (int j = 0; j < m; j++)
            scanf("%d", &matrixB[i][j]);

    
    // Luam fiecare pereche linie - coloana
    int thrd_index = 0;
    for (int i = 0; i < n; i++){
        for (int j = 0; j < m; j++){
            // Pregatim argumentele pentru functia "produs"
            args[thrd_index].i = i;
            args[thrd_index].j = j;
            args[thrd_index].p = k;

            // Se creaza fiecare thread
            if (pthread_create(&thrd[thrd_index], NULL, produs, &args[thrd_index])){
                perror(NULL);
                return errno;
            }
            thrd_index++;
        }
    }

    // Se asteapta fiecare thread
    for (int i = 0; i < thrd_index; i++){
        if (pthread_join(thrd[i], NULL)){
            perror(NULL);
            return errno;
        }
    }

    printf("\nMatricea C:\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++)
            printf("%d ", matrixC[i][j]);
        printf("\n");
    }

    return 0;
}