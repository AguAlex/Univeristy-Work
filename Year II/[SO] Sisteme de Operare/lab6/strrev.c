#include <stdio.h>
#include <errno.h>
#include <string.h>
#include <pthread.h>

void *rev(void *str)
{
    char *s = (char*)str;
    int first = 0;
    int last = strlen(s) - 1;
    char aux;

    while(first < last)
    {
        aux = s[first];
        s[first] = s[last];
        s[last] = aux;

        first++;
        last--;
    }

    return s;
}

int main(int argc, char *argv[])
{
    if(argc != 2)
    {
        printf("Numar gresit de argumente\n");
        return 0;
    }
        
    pthread_t thr ;

    if (pthread_create(&thr, NULL, rev, argv[1]))
    {
        perror(NULL);
        return errno ;
    }

    char *rezultat;
    if (pthread_join(thr, &rezultat)) 
    {
        perror(NULL);
        return errno ;
    }
    printf("%s\n", rezultat);
    return 0;
}