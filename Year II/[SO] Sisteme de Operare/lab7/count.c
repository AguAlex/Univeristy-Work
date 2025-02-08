#include <stdio.h>
#include <errno.h>
#include <pthread.h>
#include <stdlib.h>

#define MAX_RESOURCES 5

int available_resources = MAX_RESOURCES;
pthread_mutex_t mtx; // Mutex global pentru toate thread urile

int decrease_count(int count){
    pthread_mutex_lock(&mtx);

    if (available_resources < count) {
        pthread_mutex_unlock(&mtx);
        return -1;
    } else {
        available_resources -= count;
        printf("Got %d resources %d remaining\n", count, available_resources);
    }

    pthread_mutex_unlock(&mtx);
    return 0;
}

int increase_count(int count){
    pthread_mutex_lock(&mtx);

    available_resources += count;
    printf("Released %d resources %d remaining\n", count, available_resources);

    pthread_mutex_unlock(&mtx);
    return 0;
}

void *f(void *arg){ // Functie pentru thread uri
    int count = *((int*)arg); // Dereferentiere pentru a obtine valoarea int
    decrease_count(count);
    increase_count(count);

    free(arg);
    return NULL;
}

int main(){
    if (pthread_mutex_init(&mtx, NULL)){
        perror(NULL);
        return errno;
    }

    printf("MAX_RESOURCES = %d\n", available_resources);
    pthread_t thrds[5];

    for (int i = 0; i < 5; i++){
        int *count = malloc(sizeof(int));

        // Setam valoarea random 'count' pentru fiecare thread
        *count = rand() % (MAX_RESOURCES + 1);

        if (pthread_create(&thrds[i], NULL, f, count)){
            perror(NULL);
            return errno;
        }
    }

    // Se asteapta executia fiecarui thread
    for (int i = 0; i < 5; i++) {
        if (pthread_join(thrds[i], NULL)) {
            perror(NULL);
            return errno;
        }
    }

    pthread_mutex_destroy(&mtx);
    return 0;
}
